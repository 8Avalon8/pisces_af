# coding=utf-8
import logging
from utils import *
class ActionSet(object):
    """docstring for ActionSet"""
    def __init__(self, tag = "temp", desc = "actionset", isEnd = False,mp = {}):
        super(ActionSet, self).__init__()
        self.tag = tag
        self.description = desc
        self.preHandler = None
        self.endHandler = None
        self.actions    = []
        self.actions_serial = []
        self.cur_act    = 0
        self.isEnd = isEnd
        self.mp = mp

    def setArg(self,arg,value):
        self.mp[arg] = value
        return True
    def getArg(self,arg):
        if arg in self.mp:
            return self.mp[arg]
        else:
            logging.debug(u"no such argument in actionsets!")
            sys.exit(1)
    def addAction(self,action):
        self.actions.append(action)
        self.actions_serial.append(action.tag)
    def run(self):
        logging.info(u"Start excute ActionSet:" + str(self.tag))
        logging.info(self.description)
        self.startStep()
        while True:
            if self.cur_act >= len(self.actions):
                logging.info(u"ActionSet is finish")
                return self.stopStep(True)
            act = self.actions[self.cur_act]
            ret = self.runAction(act)
            if isinstance(ret,list):
                try:
                    if ret[0] == "action":
                        cur_act = self.actions_serial.index(ret[1])
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
                    logging.info("ActionSet run fail")
                    return self.stopStep(False)

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
    def check(self):
        pass
    def loadFromPyFile(self):
        #execfile(".\\actionsets\\autobattle.py")]
        pass

