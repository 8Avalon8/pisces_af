# coding=utf-8
from step import *
from utils import *
import logging
from timeout import *
import gl
from utils import *
class Task(object):
    """docstring for Task"""
    def __init__(self, tag, desc = None,pretask = []):
        super(Task, self).__init__()
        self.tag = tag
        self.description = desc
        self.cur_step = 0
        self.fail_handler = None
        self.steps    = []
        self.step_serial = []
        self.setup_actionsets = []
        self.teardown_actionsets = []
        self.pretask = pretask
    def addSetupActionSet(self,setname,tag="default",desc = "", mp={}):
        setpath = gl.project_path+"\\actionsets\\"+setname+".py"
        execfile(setpath)
        acts = locals()['acts']
        self.setup_actionsets.append(acts)
    def addTeardownActionSet(self,setname,tag="default",desc = "", mp={}):
        setpath = gl.project_path+"\\actionsets\\"+setname+".py"
        execfile(setpath)
        acts = locals()['acts']
        self.teardown_actionsets.append(acts)
    def addStep(self, step):
        if step.tag != 'Fail_Handler':
            self.steps.append(step)
            self.step_serial.append(step.tag)
        else:
            self.fail_handler = step
    @timeout(10800)
    def run(self):
        logging.info(u"Start excute Task:" + str(self.tag))
        logging.info(self.description)
        ret = self.setup()
        if ret == False:
            return self.tearDown(False)
        while True:
            if self.cur_step >= len(self.steps):
                logging.info(u"Task fisished")
                SaveImage(name =str(self.tag),saveimage = 'Debug')
                return self.tearDown(True)
            step = self.steps[self.cur_step]
            ret = self.runStep(step)
            logging.debug("runStep return:"+str(ret))
            if isinstance(ret,str):
                try:
                    if ret == "TaskFinish":
                        logging.info(u"Task finished as expected")
                        SaveImage(name =str(self.tag),saveimage = 'Debug')
                        return self.tearDown(True)
                    cur_step = self.step_serial.index(ret)
                except ValueError as e:
                    logging.critical(u"Can't find Step serial: "+ str(ret) +u" ,stop current task")
                    return self.tearDown(False)
                self.cur_step = cur_step
            elif isinstance(ret,bool):
                if ret == True:
                    self.cur_step += 1
                elif ret == False:
                    logging.info(u"Task fail")
                    tag = str(self.tag) + "_Fail"
                    SaveImage(name =tag,saveimage = 'Debug')
                    if self.fail_handler != None:
                        gl.AREA_ICON_LUAERROR.stopObserver()
                        self.runStep(self.fail_handler)
                    return self.tearDown(False)
    def loadTaskFromFile(self):
        pass
    def startTaskObserver(self):
        #register event : close_window detect network disconnection etc.
        #recieve region type:vanish/appear pattern
        
        #Test
        
        import gl
        def handler_neterror(event):
            logging.critical("Connetction Lost")
            logging.critical(event.getCount())
            SaveImage(name = "ConnectionLost",saveimage = 'Debug')
            cur_step = self.steps[self.cur_step] 
            cur_act  = cur_step.actions[cur_step.cur_act]
            e_info = u"Connection Lost\r\n"+cur_act.description
            if event.getCount()<2:
                if GetRegionFromGrid(88, 89).exists("neterror_confirm.png",1) != None:
                    click()
                else:
                    logging.critical(u"Can't find reconnect button")
                event.repeat()
                return

            else:
                SendEmail(e_info)
                print "aaa"
                gl.OBSERVER_FAIL = True
        
        #对于luaerror的检测不能移动游戏客户端的位置
        def handler_luaerror(event):
            logging.critical("LuaError Maybe Appeared")
            if gl.R_Screen.exists("close_piracy_win.png",0) != None:
                logging.critical("Find piracy win")
                click()
                event.repeat()
                return
            if gl.R_Screen.exists("luaerror_confirm.png",3) != None:
                logging.critical("LuaError")
                SaveImage(name = "LuaError",saveimage = 'Debug')
                SendEmail(u"Lua Error Happened")
                type(Key.ENTER)
                gl.OBSERVER_FAIL = True
                return

            SaveImage(name = "misinfomation",saveimage = 'Debug')
            sleep(2)
            event.repeat()

        def handler_lockerror(event):
            logging.critical("Game Locked!")
            #SendEmail(u"网络连接服务器断开")
            SaveImage(name = "Game Locked!",saveimage = 'Debug')
            gl.OBSERVER_FAIL = True

        if gl.AREA_ICON_DISCONNECTION.isObserving() == False:
            gl.AREA_ICON_DISCONNECTION.onAppear(Pattern("icon_disconnection.png").targetOffset(230,170), handler_neterror)
            gl.AREA_ICON_DISCONNECTION.observeInBackground(FOREVER)
        if gl.AREA_ICON_LUAERROR.isObserving() == False:
            gl.AREA_ICON_LUAERROR.onAppear(Pattern("luaerror.png").similar(1), handler_luaerror)
            gl.AREA_ICON_LUAERROR.observeInBackground(FOREVER)
        if gl.AREA_ICON_LOCK.isObserving() == False:
            gl.AREA_ICON_LOCK.onAppear("lock.png", handler_lockerror)
            gl.AREA_ICON_LOCK.observeInBackground(FOREVER)

        pass
    def stopTaskObserver(self):
        #Not proper Usage
        if gl.AREA_ICON_DISCONNECTION.isObserving() == True:
            gl.AREA_ICON_DISCONNECTION.stopObserver()
        if gl.AREA_ICON_LUAERROR.isObserving() == True:
            gl.AREA_ICON_LUAERROR.stopObserver()
        if gl.AREA_ICON_LOCK.isObserving() == True:
            gl.AREA_ICON_LOCK.stopObserver()
        pass
    def runStep(self,step):
        _step = step
        ret = _step.run()
        return ret
    def setup(self):
        #actionsets
        logging.info(u"Excute task's Setup Actionsets")
        for actset in self.setup_actionsets:
            ret = actset.run()
            if ret == False:
                logging.critical(u"Task Setup fail,task stop")
                return False
        logging.info(u"Task Setup finish")
        self.startTaskObserver()
        return True
    def tearDown(self,ret):
        self.stopTaskObserver()
        self.cur_step = 0
        logging.info(u"执行Task的TearDown Actionsets")
        for actset in self.teardown_actionsets:
            tret = actset.run()
            if tret == False:
                logging.critical(u"Task TearDown fail，task stop")
                return False
        logging.info(u"Task TearDown finish")
        return ret

class TaskSuit(object):
    """docstring for TaskSuit"""
    def __init__(self, tag, desc = None):
        super(TaskSuit, self).__init__()
        self.tag = tag
        self.description = desc
        self.cur_task = 0
        self.tasks    = []
        self.task_serial = []
        self.pass_task = []
        self.fail_task = []
    def addTask(self, task):
        self.tasks.append(task)
        self.task_serial.append(task)
    def run(self):
        logging.info(u"Start excute TaskSuit")
        info = u"All Task : " + str(len(self.tasks))
        logging.info(info)
        while True:
            if self.cur_task >= len(self.tasks):
                return self.stopTaskSuit(True)
            task = self.tasks[self.cur_task]
            #判断该任务是否前置任务出错，是则直接算作失败否则执行task
            ret = self.checkTask(task)
            if ret==True :
                try:
                    ret = task.run()
                except Timeout as e:
                    logging.critical(u"Time out !, task fail")
                    ret = False
                    #raise Timeout("Timeout")
                
            if isinstance(ret,bool):
                if ret == True:
                    self.pass_task.append(task.tag)

                    self.cur_task += 1
                elif ret == False:
                    self.fail_task.append(task.tag)
                    self.cur_task += 1


    def checkTask(self,task):
        fail_task_set = set(self.fail_task)
        pretask_set   = set(task.pretask)
        inter_set     = fail_task_set & pretask_set
        if len(inter_set) != 0:
            info = u"Task:(tag"+task.tag+u")pretask"+str(inter_set)+u"Fail,currnt task skipped and fail"
            logging.critical(info)
            return False
        else:
            return True
    def loadTasksFromFile(self):
        pass

    def stopTaskSuit(self, ret):
        import socket
        ####Find local IP address
        localIP = '192.168.1.1'
        ipList  = socket.gethostbyname_ex(socket.gethostname())
        localIP = ipList[0]

        info = str(len(self.pass_task)) + "/" + str(len(self.tasks)) + " passed"
        ##########Temp Usage, Should use Result Class to print
        mail = info+"\r\n"
        mail += u"================================================================\t\r\n"
        mail += u"Running Computer：" + str(socket.gethostname())+"\r\n"
        mail += info+"\r\n"
        mail += u"Fail Tasks:\r\n"
        mail += str(self.fail_task) + "\r\n"
        mail += u"Tasksuits finish\r\n"
        mail += u"================================================================\r\n"
        if gl.SCREENCAPTUREMODE == 'Fail' and (len(self.pass_task) < len(self.tasks)):
            SendEmail(mail,title=u"Automated Test Report")
        #############
        logging.info(u"================================================================")
        logging.info(info)
        logging.info(u"Fail Tasks:")
        logging.info(self.fail_task)
        logging.info(u"Tasksuits finished")
        arr = gl.TaskDir.split("\\")
        taskfolder = arr[len(arr)-1]
        textAddr = u"Log地址:" + "\\\\"+localIP+"\\log\\"+taskfolder
        logging.info(text)
        logging.info("================================================================")
        if len(self.fail_task)== 0 : return True
        else : return False
