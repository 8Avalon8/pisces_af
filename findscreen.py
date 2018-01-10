#-*- coding: utf-8 -*-  ##设置编码方式

import win32api,win32gui,win32con
import sys,os
import time
#label = 'BlueStacks App Player' #蓝叠模拟器
label = 'Pisces' #pc客户端标题且无子句柄
#win32gui.GetClientRect(hld) #获取client的窗口大小
#win32gui.ClientToScreen(hld,(0,0))  #将client的(0,0)坐标转为屏幕坐标
hld = win32gui.FindWindow(None, label)

if hld > 0 and label == 'BlueStacks App Player':

    dlg = win32gui.FindWindowEx(hld, 0, None,'HOSTWND')#获取hld下第一个为edit控件的句柄
    dlg = win32gui.FindWindowEx(dlg, 0, None, None)#获取hld下第一个为edit控件的句柄
    dlg = win32gui.FindWindowEx(dlg, 0, None, None)
    position = win32gui.GetWindowRect(dlg)
    #print win32gui.GetWindowRect(dlg)
    
elif label == 'Pisces':
    if hld <= 0 :
        os.system("C:\\bin\\StartPisces.bat") #client's path
        time.sleep(5)
        hld = win32gui.FindWindow(None, label)
    win32gui.SetForegroundWindow(hld)
    dlg = win32gui.GetClientRect(hld) #获取client的窗口大小
    position = win32gui.ClientToScreen(hld,(0,0))  #将client的(0,0)坐标转为屏幕坐标


fp = open("E:\\pisces_af\\ScriptConfig.ini",'w')
fp.write(str(position))
fp.close()
sys.exit(0)
