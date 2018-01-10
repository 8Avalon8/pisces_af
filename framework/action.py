# coding=utf-8
'''
Action:
Description: 
'''
import logging
from utils import *
import gl
class Action(object):
    """docstring for    Action



    """
    def __init__(self, tag, desc = None, **kw):
        #Identify of An Action
        self.tag = tag 
        self.description = desc
        self.loopTime = kw.get('loopTime',1)
        self.loopWaitingTime = kw.get('loopWaitingTime',Settings.WaitScanRate)
        self.loopRegion = kw.get('loopRegion',None)
        self.loopPattern = kw.get('loopPattern',None)
        self.loopSleepTime = kw.get('loopSleepTime',1)
        #loopType: 0: loopUntilVanish 1: loopUntilAppear
        self.loopType = kw.get('loopType',0)
        #next: ['Action','1.5'] or ['Step','3']
        self.nextAorS     = kw.get('next',None)
        self.detectRegion = kw.get('detectRegion',None)
        self.imagePattern = kw.get('imagePattern',None)
        self.failResponse = kw.get('failResponse','Fail')
        self.isEnd = kw.get('isEnd',False)
        #self.preHandler = None
        #self.endHandler = None
        self.returnStatus = []#not be used yet
        self.saveImage = kw.get('saveImage',gl.SCREENCAPTUREMODE)
    def function(self):
        pass
    def click(self):
        pass
    def action(self):
        pass
    def preHandler(self,actionset = None):
        if gl.OBSERVER_FAIL:
            return False
        if actionset == None:
            return True
        else:
            return actionset.run()

    #odd handler
    def endHandler(self,act_return, actionset = None):
        #need to modify action set
        if actionset != None:
            act_return = actionset.run(act_return)
        if act_return == True:
            if self.nextAorS != None:
                return self.nextAorS
            else:
                return act_return
        elif self.failResponse == 'Fail':
            return act_return
        elif self.failResponse == 'Ignore':
            #if self.nextAorS != None:
            #    return self.nextAorS
            #else:
            #    return True
            return True
            

    def loopActive(self):
        loopResult = False
        for lcount in xrange(0,self.loopTime):
            pH  = self.preHandler()
            if pH == True:
                act_ret = self.active()
            else:
                logging.error("preHandler False")
                return False
            eH  = self.endHandler(act_ret)
            if self.loopType == 0 and self.loopPattern != None:
                loopResult = self.loopRegion.waitVanish(self.loopPattern,self.loopWaitingTime)
            elif self.loopType == 1 and self.loopPattern != None:
                loopResult = self.loopRegion.exists(self.loopPattern,self.loopWaitingTime)
            if loopResult != None and loopResult != False:
                logging.debug(u"Find the Pattern, Action is finish")
                SaveImage(self.loopRegion,str(self.tag),saveimage = gl.SCREENCAPTUREMODE)
                #在满足条件但上次没找到的情况下应返回True
                if eH == False:
                    return True
                else:
                    return eH
            else:
                logging.debug(u"Can not find the Pattern, Action is continue")
                sleep(self.loopSleepTime)
                continue
        logging.debug(u"Can not find the Pattern, Action is finish")
        SaveImage(self.loopRegion,str(self.tag),saveimage = gl.SCREENCAPTUREMODE)
        return self.endHandler(False)

    def active(self):
        if self.preHandler() != None :
            pHresult = self.preHandler()

    def run(self):
        logging.debug(u"Start excute Action:" + str(self.tag))
        logging.debug(self.description)
        if self.loopTime > 1 :
            ret = self.loopActive()
            return ret
        else:
            pH  = self.preHandler()
            if pH == True:
                act_ret = self.active()
            else:
                logging.error("preHandler False")
                return False
            eH  = self.endHandler(act_ret)
            return eH

class ClickAction(Action):
    """subclass of Action for click operation
        default: click if the pattern exists,normally waiting for click pattern vanish after click
    """
    def __init__(self, tag, desc = None, **kw):
        super(ClickAction, self).__init__(tag, desc=desc,**kw)
        self.clk_region = kw.get('clk_region',None)
        self.clk_ptn = kw.get('clk_ptn',None)
        if (self.loopTime >0) and (self.loopRegion == self.loopPattern == None) :
            self.loopRegion = self.detectRegion
            self.loopPattern = self.imagePattern
            #logging.debug(u"loopRegion和pattern未设定，将默认指向detectRegion与imagePattern")

    def active(self):
        detect_region = self.detectRegion
        image_pattern = self.imagePattern
        
        if detect_region.exists(image_pattern,self.loopWaitingTime):
            logging.debug(u"Find the Pattern")
            if self.clk_region == None:
                SaveImage(name =str(self.tag),saveimage = gl.SCREENCAPTUREMODE)
                clk_ret = detect_region.click()  #
                sleep(self.loopSleepTime) #
            else:
                #print self.clk_region
                #print self.tag
                #print self.clk_ptn
                SaveImage(name =str(self.tag),saveimage = gl.SCREENCAPTUREMODE)
                clk_ret = self.clk_region.click(self.clk_ptn)
                sleep(self.loopSleepTime)
            if clk_ret == 0:
                logging.critical(u"Click Failed!!!")
            else:
                SaveImage(name =str(self.tag),saveimage = self.saveImage)
                return True
        else : 
            SaveImage(detect_region,str(self.tag),saveimage = gl.SCREENCAPTUREMODE) #
            logging.debug(u"Can not find the Pattern")
            return False


class SwipeAction(Action):
    """Subclass of Action for swipe operation
        Not yet implemented
    """
    def __init__(self, tag, desc = None, **kw):
        super(SwipeAction, self).__init__(tag, desc=desc,**kw)
        self.destination = kw.get('destination',1)
    def run():
        pass
class SleepAction(Action):
    """docstring for SleepAction"""
    def __init__(self, tag, desc = None, **kw):
        super(SleepAction, self).__init__(tag, desc=desc,**kw)
        self.time = kw.get('time',1)
    def run(self):
        logging.debug(u"Waiting for "+str(self.time)+u"seconds")
        sleep(self.time)
        return True
        
class PasteAction(Action):
    """Subclass of Action for type text operation"""
    def __init__(self, tag, desc = None, **kw):
        super(PasteAction, self).__init__(tag, desc = desc,**kw)
        self.contents = kw.get('contents',None)
    def run(self):
        logging.debug(u"Paste the text"+self.contents)
        paste(self.contents)
        return True

class TypeAction(Action):
    """Subclass of Action for type text operation"""
    def __init__(self, tag, desc = None, **kw):
        super(TypeAction, self).__init__(tag, desc = desc,**kw)
        self.key = kw.get('key',None)
    def run(self):
        logging.debug(u"Type key"+self.key)
        type(self.key)
        return True
        
class DragAction(Action):
    """Subclass of Action for type text operation"""
    def __init__(self, tag, desc = None, **kw):
        super(DragAction, self).__init__(tag, desc = desc,**kw)
        self.start = kw.get('start',None)
        self.end   = kw.get('end',None)
    def run(self):
        #Settings.DelayBeforeMouseDown = 0.1
        #Settings.DelayBeforeDrag = 0.1
        #Settings.DelayBeforeDrop = 0.1
        Settings.MoveMouseDelay = 1
        if self.start != None and self.end != None:
            logging.debug(u"DragAction")
            dragDrop(self.start,self.end)
            return True
        else:
            logging.debug(u"DragAction could not be empty")
            return False
        
class DetectAction(Action):
    """Subclass of Action for Detect behavior"""
    def __init__(self, tag, desc = None, **kw):
        super(DetectAction, self).__init__(tag, desc=desc,**kw)
        self.detectSuccess = kw.get('detectSuccess',None) #not used
        self.detectFail    = kw.get('detectFail',None) #not used
        self.detectRegion = kw.get('detectRegion',None)
        self.loopRegion = self.detectRegion
        self.imagePattern = kw.get('imagePattern',None)
        self.loopPattern = self.imagePattern
        self.loopTime = kw.get('loopTime',1)
        self.suc_next = kw.get('successNext',None)
        self.nextAorS = self.suc_next
        self.fail_next = kw.get('failNext',None)
    def active(self):
        return True

    #odd handler
    def endHandler(self,act_return, actionset = None):
        if actionset != None:
            act_return = actionset.run(act_return)
        if act_return == True:
            logging.debug(u"Detect success")
            if self.nextAorS != None:
                logging.debug(u"Jump to " + str(self.nextAorS))
                return self.nextAorS
            else:
                logging.debug(u"Jump to next Action")
                return act_return
        elif self.failResponse == 'Fail':
            logging.debug(u"Detect Failed")
            return act_return
        elif self.failResponse == 'Ignore':
            logging.debug(u"Detect Failed")
            if self.fail_next != None:
                #logging.debug("Jump to " + str(self.fail_next))
                return self.fail_next
            else:
                #logging.debug("Jump to next action")
                return True


    def loopActive(self):
        loopResult = False
        for lcount in xrange(0,self.loopTime):
            pH  = self.preHandler()
            if pH == False:
                logging.error("DetectAction preHandler False")
                return False
            if self.loopType == 0 and self.loopPattern != None:
                SaveImage(self.loopRegion,str(self.tag),saveimage = gl.SCREENCAPTUREMODE)
                loopResult = self.loopRegion.waitVanish(self.loopPattern,self.loopWaitingTime)
            elif self.loopType == 1 and self.loopPattern != None:
                SaveImage(self.loopRegion,str(self.tag),saveimage = gl.SCREENCAPTUREMODE)
                #Type of loopResult:  Pattern of None 
                loopResult = self.loopRegion.exists(self.loopPattern,self.loopWaitingTime)
            if loopResult != None:
                logging.debug(u"Find the Pattern, DetectAction is finish")
                SaveImage(self.loopRegion,str(self.tag),saveimage = self.saveImage)
                eH  = self.endHandler(True)
                return eH
            else:
                eH  = self.endHandler(True)
                #the waiting time after one loop
                sleep(self.loopSleepTime)
                continue
        logging.debug(u"Can not find the Pattern, DetectAction is finish")
        SaveImage(name = str(self.tag),saveimage = gl.SCREENCAPTUREMODE)
        return self.endHandler(False)

    def run(self):
        logging.debug(u"Start execute Action:" + str(self.tag))
        logging.debug(self.description)
        ret = self.loopActive()
        return ret


class Exec(object):
    """docstring for Eval"""
    def __init__(self,tag,desc = None,exp=None):
        #super(Exec, self).__init__()
        self.tag = tag
        self.description = desc
        self.exp = exp
    def run(self):
        try:
            logging.debug(u"Start execute ExecAction:" + str(self.tag))
            logging.debug(self.description)
            exec(self.exp,gl.SCOPE)
        except:
            logging.critical(u"ExecAction Failed")
            return False
        return True

        
class Jump(object):
    """docstring for Jump"""
    def __init__(self, tag, desc = None,target=None,cond="True"):
        #super(Jump, self).__init__()
        self.cond = cond
        self.tag = tag
        self.description = desc
        self.target = target
    def run(self):
        logging.debug(u"Start excute JumpAction:" + str(self.tag))
        logging.debug(self.description)
        try:
            ret = eval(self.cond,gl.SCOPE)
            #print ret
        except:
            logging.critical(u"Jump Condition Error")
            return True
        if ret:
            logging.debug(u"Jump to "+str(self.target))
            return self.target
        else:
            return True