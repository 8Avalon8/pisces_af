# -*- coding: utf-8 -*-
from sikuli import *
from util import GetScreenPosition,GetRealRegion,GetRegionFromGrid
import os
project_path = "E:\\pisces_af"
log_path = project_path+"\\logs"
TaskDir = None
SCOPE = {}
OBSERVER_FAIL = False
#DEBUG
SCREENCAPTUREMODE = 'DEBUG' 
SCREEN_POSITION = GetScreenPosition() #a tuple like (x,y)
R_Simulator = GetRealRegion(0,0,1280,820)
R_Screen = GetRealRegion(0,0,1280,720)



#Old Method and Global Variable
AREA_BTN_UPDATECONFIRM   = GetRealRegion( 540, 570, 200,  80)
AREA_BTN_CHOOSESERVER    = GetRealRegion( 670, 480, 190,  70)
AREA_BTN_LOGINGAME       = GetRealRegion( 550, 590, 180,  50)
AREA_ICON_NEWS           = GetRealRegion( 630,  40,  80,  50)
AREA_BTN_CLOSENEWS       = GetRealRegion(1050,  40,  50,  60)
AREA_ICON_WELFARECENTER  = GetRealRegion( 635,  60,  70,  40)
AREA_BTN_WELFARECENTER   = GetRealRegion(1125,  65,  30,  25)
AREA_BTN_TRACESTORY      = GetRealRegion(1010, 180,  60, 140)
AREA_ICON_LEVELINFO      = GetRealRegion(1140,  65,  40,  25)
AREA_BTN_USEITEM         = GetRealRegion(1000, 530, 150,  65)
AREA_BTN_USEEQUIP        = GetRealRegion(1000, 530, 150,  65)
AREA_BTN_SKIPSTORY       = GetRealRegion(1200,   0,  45,  35)
AREA_BTN_GOACTIVITY      = GetRealRegion( 820, 215,  40,  40)
AREA_ICON_MAP            = GetRealRegion(   0,   0, 100, 100)
AREA_MAP_LUOYANG         = GetRealRegion( 580, 345, 110, 110)
AREA_MAP_FUBEN           = GetRealRegion( 290, 215,  65,  55)
AREA_BTN_CLOSEMAP        = GetRealRegion( 980,  40, 215, 190)
AREA_SCENE_LOCATION      = GetRealRegion(  90,  20, 115,  35)

#Test
#Error
AREA_ICON_DISCONNECTION  = GetRealRegion( 430, 230, 200,  80)
AREA_BTN_DISCONNECTION   = GetRealRegion( 660, 400, 180,  80)
AREA_ICON_LUAERROR       = GetRegionFromGrid(72)
AREA_ICON_LOCK           = GetRegionFromGrid(54,87)
AREA_ICON_PLAYERINPOSITION = GetRealRegion( 330, 180,  60,  80)
AREA_ROLE_DIRENJIE         = GetRealRegion( 140,  80, 430, 425)
