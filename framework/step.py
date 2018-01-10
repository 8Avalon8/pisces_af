# coding=utf-8
'''
Step:
Description: 
'''
from action import *
from actionset import *
from utils import *
import logging
import traceback
class Step(object):
    """docstring for Step"""
    def __init__(self, tag, desc = None, nextStep = None ,isEnd = False):
        super(Step, self).__init__()
        self.tag = tag #Identify of An Action
        self.description = desc
        self.preHandler = None
        self.endHandler = None
        self.actions    = []
        self.actions_serial = []
        self.cur_act    = 0
        self.nextStep = nextStep
        self.isEnd = isEnd
    def addActionSet(self,setname,tag="default",desc = "", mp={}):
        setpath = gl.project_path+"\\actionsets\\"+setname+".py"
        try:
            execfile(setpath)
        except  Exception as e:
            print e.message
            logging.error(u"Error occurs when loading" + setpath)
            logging.error(u"Please check keywords and sysmbols")
            print 'traceback.format_exc():\n%s' % traceback.format_exc()
            raise Exception
        
        acts = locals()['acts']
        #acts variable from execfile
        self.actions.append(acts)
        self.actions_serial.append(acts.tag)
    def addAction(self,action):
        self.actions.append(action)
        self.actions_serial.append(action.tag)
    def loadActionsFromFile(self,file):
        pass
    def run(self):
        logging.info(u"Start excute step:" + str(self.tag))
        logging.info(self.description)
        self.startStep()
        while True:
            if self.cur_act >= len(self.actions):
                logging.info(u"Step finished")
                return self.stopStep(True)
            act = self.actions[self.cur_act]
            ret = self.runAction(act)
            if isinstance(ret,list):
                try:
                    if ret[0] == "action":
                        cur_act = self.actions_serial.index(ret[1])
                    elif ret[0] == "step":
                        logging.info(u"Current step excute as expected，ready to excute next step")
                        return self.stopStep(ret[1])
                except ValueError as e:
                    logging.critical(u"Can't find Action，Serial: "+ str(ret))
                    logging.critical(u"Stop current Task")
                    return self.stopStep(False)
                self.cur_act = cur_act
            elif isinstance(ret,bool):
                if gl.OBSERVER_FAIL:
                    logging.info("observer fail")
                    return self.stopStep(False)
                if ret == True:
                    self.cur_act += 1
                elif ret == False:
                    logging.info("Step run fail")
                    return self.stopStep(False)

    def startStepObserver(self):
        #register event : close_window detect network disconnection etc.
        #recieve region type:vanish/appear pattern
        
        #Test
        
        import gl
        pass
    def stopStepObserver(self):
        pass
    def runAction(self,act):
        action = act
        ret = action.run()
        logging.debug("action return" + str(ret))
        return ret
    def getNextAction(self):
        pass

    def startStep(self):
        #self.startStepObserver()
        pass

    def stopStep(self,ret):
        #self.stopStepObserver()
        self.cur_act = 0
        self.observerFail = False
        if self.isEnd and isinstance(ret,bool):
            if ret == True:
                return "TaskFinish" #bad method
        return ret