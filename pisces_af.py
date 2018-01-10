# -*- coding: utf-8 -*-
import traceback
import logging
import os
import time
import sys
from ConfigParser import ConfigParser
import socket

#import gl
project_path = "E:\\pisces_af.sikuli"
addImportPath(project_path)
addImagePath(project_path+"\\img")

sys.path.append(project_path+"\\config")
sys.path.append(project_path+"\\utils")
sys.path.append(project_path+"\\tasks")
sys.path.append(project_path+"\\actionsets")
from utils import *
from framework import *
import gl

#--------Loading Config File
CONFIGFILE = project_path+"\\config\\config.ini"
config = ConfigParser()
config.read(CONFIGFILE)
####Find local IP address
ipList  = socket.gethostbyname_ex(socket.gethostname())
comName = ipList[0]
config.options(comName)


print getBundlePath()
MakeDir()

#--------logging Settings
#
logger = logging.getLogger()  
logger.setLevel(logging.DEBUG)    #
  
#  
logfile = os.path.join(gl.TaskDir,"logger.txt")
fh = logging.FileHandler(logfile, mode='w')  
fh.setLevel(logging.DEBUG)   # 
  
# 
ch = logging.StreamHandler()  
ch.setLevel(logging.INFO)   # 
  
#
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")  
fh.setFormatter(formatter)  
ch.setFormatter(formatter)  
  
#
logger.addHandler(fh)  
logger.addHandler(ch)  
  
#test
#logger.debug('Debug info')  
#logger.info('this is a logger info message')  
#logger.warning('this is a logger warning message')  
#logger.error('this is a logger error message')  
#logger.critical('this is a logger critical message')  

#--------SikuliX Settings
setShowActions(True)
Settings.WaitScanRate = config.getint(comName,"WaitScanRate")
Settings.ObserveScanRate = config.getint(comName,"ObserveScanRate")
Settings.ActionLogs = False
#Settings.InfoLogs = True
Settings.MoveMouseDelay = config.getfloat(comName,"MoveMouseDelay")
#Settings.WaitScanRate(10)
Settings.ActionLogs = True
Settings.InfoLogs = True
Settings.DebugLogs = True
Settings.LogTime = False
Debug.setLogFile(gl.TaskDir+"\\runerrorlog.txt")
Debug.on(3)

#--------PiscesAF Settings
#Debug: Default argument ; Save every image before each action(click and detect) 
#Fail : Only save screencapture when task fail
gl.SCREENCAPTUREMODE = config.get(comName,"ScreenCaptureMode")
print "ScreenCaptureMode : "
print gl.SCREENCAPTUREMODE
#Test 
#type(Key.ENTER)
if exists(Pattern("teamview.png").targetOffset(92,-1)):
    click()

#
tasksuit = TaskSuit("TaskSuit",desc = "Test TaskSuit")

#execfile(project_path+"\\tasks\\mainstory.py")
try:
    tasksuit_section = comName+"_Tasksuit"
    for task in config.options(tasksuit_section):
        if config.getint(tasksuit_section,task) != 1:
            continue
        print task
        execfile(project_path+"\\tasks\\"+task+".py")
except Exception as e:
    logging.critical("Error when loading script")
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
    raise Exception
else:
    pass
finally:
    pass


ret = tasksuit.run()
print "Killing Game Client"
os.system('TASKKILL /F /IM piscesD.exe /t')

if ret == False: sys.exit(-1)
