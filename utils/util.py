# -*- coding: utf-8 -*-
import os
from sikuli import *
import gl
import time
import shutil
import logging
def GetScreenPosition():
    #rootpath = os.path.dirname(os.getcwd())
    path = gl.project_path+"\\ScriptConfig.ini"
    fp = open(path,'r')
    screenPostion = fp.readline()
    screenPostion = eval(screenPostion)
    x = screenPostion[0]
    y = screenPostion[1]
    print screenPostion
    fp.close()
    return (x,y)

def GetRegionFromGrid(regionS,regionE = None):
    if not isinstance(regionS,int):
        logging.ERROR("Wrong region serial"+str(regionS))
        return False
    x1 = ((regionS-1) % 16 ) * 80 #left top
    y1 = ((regionS-1) / 16 ) * 80
    if regionE != None:
        x2 = ((regionE-1) % 16 +1) * 80 #right bottom
        y2 = ((regionE-1) / 16 +1) * 80
        h  = y2 - y1
        w  = x2 - x1
        if h > 0 and w > 0 :
            return GetRealRegion(x1,y1,w,h)
        else:
            print str(regionE)
            print h
            logging.ERROR("Wrong region serial"+ str(regionE))
            return False
    return GetRealRegion(x1,y1,80,80)


def GetRealRegion(x,y,w,h):
    if gl.SCREEN_POSITION == None:
        gl.SCREEN_POSITION = GetScreenPosition()
    else:
        screenPostion = gl.SCREEN_POSITION
    x = x+screenPostion[0]
    y = y+screenPostion[1]
    return Region(x,y,w,h)

def MakeDir():
    dirname = "task_%s" % time.strftime("%Y-%m-%d_%H-%M")
    if os.path.isdir(gl.log_path) == False:
        os.mkdir(gl.log_path)
    dirname = os.path.join(gl.log_path,dirname)
    if os.path.isdir(dirname) == False:
        os.mkdir(dirname)
    print dirname
    gl.TaskDir = dirname

def SaveImage(region = None,name = None,saveimage = 'False'):
    screenshotsDir = gl.TaskDir
    if saveimage == 'Debug':
        saveimage = 'True'
    elif saveimage == 'Fail':
        saveimage = 'False'
    if saveimage == 'False' or saveimage == False:
        return True
    if name == None:
        filename = "%s.png" % (time.strftime("%Y-%m-%d_%H-%M-%S"))
    else:
        logging.debug(u"Save screenshot"+str(name))
        filename = "%s" % (time.strftime("%Y-%m-%d_%H-%M-%S"))
        filename += "_"
        filename += str(name)
        filename += ".png"
    if region == None:
        img = capture(gl.R_Screen)
    else: 
        #print region
        img = capture(region)
    shutil.move(img, os.path.join(screenshotsDir, filename))

