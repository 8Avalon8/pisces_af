# -*- coding: utf-8 -*-

'''
username :
password :
'''
acts = ActionSet(tag=tag,desc=desc,mp=mp)
#action 1.1
arg = { "detectRegion": GetRegionFromGrid(15, 32)           ,"imagePattern"  :  "UserCenter.PNG",
        "loopWaitingTime": 120                               ,"failResponse" : "Fail",
        "loopTime":1                                       ,"loopType"      :  1}
act = DetectAction(tag = "1.1", desc = "FindLoginPage", **arg)
acts.addAction(act)
#action 1.12
arg = { "detectRegion": GetRegionFromGrid(102, 106)           ,"imagePattern"  :  "text_chooseserver.png",
        "loopWaitingTime": 50                               ,"failResponse" : "Fail",
        "loopTime":1                                       ,"loopType"      :  0}
act = DetectAction(tag = "1.12", desc = "Judge login success or not", **arg)
acts.addAction(act)
#action 1.13
arg = { "time": 2}
act = SleepAction(tag = "1.13", **arg)
acts.addAction(act)
#action 1.15
arg = { "detectRegion" : GetRegionFromGrid(15, 32),
        "imagePattern" : "UserCenter.PNG",
        "loopRegion": GetRegionFromGrid(89, 108),
        "loopPattern"  :"UserConfirm.PNG",
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 6,
        "loopType"     :  1}
act = ClickAction(tag = "1.14", desc = "FindUserLoginWindow", **arg)
acts.addAction(act)
#action 1.2
arg = { "detectRegion" : GetRegionFromGrid(53, 54),
        "imagePattern" : "UsernameFrame.PNG",
        "clk_region" : GetRegionFromGrid(53, 54),
        "clk_ptn" : Pattern("UsernameFrame.PNG").targetOffset(50, 0),
        "loopWaitingTime" : 10,
        "failResponse" : "Fail",
        "loopRegion": gl.R_Screen,
        "loopPattern": "input_done.png",
        "loopTime":5,
        "loopType":1}
act = ClickAction(tag = "1.2", desc = "FindUsernameFrame", **arg)
acts.addAction(act)
#action 1.3
arg = { "contents" : acts.getArg('username') }
act = PasteAction(tag = "1.3", desc = "InputUsername", **arg)
acts.addAction(act)
#action 1.305
arg = { "time" : 1.5 }
act = SleepAction(tag = "1.305", desc = "WaitForInputPassword", **arg)
acts.addAction(act)
#action 1.31
arg = { "detectRegion" : gl.R_Screen,    "imagePattern" : "input_done.png",
        "loopWaitingTime" : 6,                          "failResponse" : "Fail",
        "loopTime" : 5                                 ,"loopType"     :  0 }
act = ClickAction(tag = "1.31", desc = "ClickInputDone", **arg)
acts.addAction(act)
#action 1.4
arg = { "detectRegion" : GetRegionFromGrid(69, 70),
        "imagePattern" : "PasswordFrame.PNG",
        "clk_region" : GetRegionFromGrid(69, 70),
        "clk_ptn" : Pattern("PasswordFrame.PNG").targetOffset(50, 0),
        "loopWaitingTime" : 6,
        "failResponse" : "Fail",
        "loopRegion": gl.R_Screen,
        "loopPattern": "input_done.png",
        "loopTime":5,
        "loopType":1}
act = ClickAction(tag = "1.4", desc = "FindPasswordFrame", **arg)
acts.addAction(act)
#action 1.45
arg = { "time" : 0.5 }
act = SleepAction(tag = "1.45", desc = "WaitForInputPassword", **arg)
acts.addAction(act)
#action 1.5
arg = { "contents" : acts.getArg('password')}
act = PasteAction(tag = "1.5", desc = "InputPassword", **arg)
acts.addAction(act)
#action 1.505
arg = { "time" : 1.5 }
act = SleepAction(tag = "1.505", desc = "WaitForInputPassword", **arg)
acts.addAction(act)
#action 1.51
arg = { "detectRegion" : gl.R_Screen,    "imagePattern" : "input_done.png",
        "loopWaitingTime" : 6,                          "failResponse" : "Fail",
        "loopTime" : 5                                 ,"loopType"     :  0 }
act = ClickAction(tag = "1.51", desc = "ClickInputDone", **arg)
acts.addAction(act)
#action 1.6
arg = { "detectRegion" : GetRegionFromGrid(89, 108),    "imagePattern" : "UserConfirm.PNG",
        "loopWaitingTime" : 6,                          "failResponse" : "Fail",
        "loopRegion": GetRegionFromGrid(119, 138)      ,"loopPattern"  :"LoginGame.PNG",
        "loopTime" : 5                                 ,"loopType"     :  1}
act = ClickAction(tag = "1.6", desc = "ClickUserConfirm", **arg)
acts.addAction(act)
#action 1.7
arg = { "time" : 2 }
act = SleepAction(tag = "1.7", desc = "WaitForUserIdentify", **arg)
acts.addAction(act)
#action 3
arg = { "detectRegion" : GetRegionFromGrid(119, 138),   "imagePattern" : "LoginGame.PNG",
        "loopWaitingTime" : 6 ,                         "failResponse" : "Fail" ,
        "loopRegion": GetRegionFromGrid(119, 138)      ,"loopPattern"  :"LoginGame.PNG",
        "loopTime" : 5                                 ,"loopType"     :  0 }
act = ClickAction(tag = "3", desc = "LoginGame", **arg)
acts.addAction(act)

#action 5.1
arg = { "detectRegion" : gl.AREA_ICON_NEWS,
        "imagePattern" : "news.png",
        "clk_region" : gl.AREA_BTN_CLOSENEWS, 
        "clk_ptn" : "btn_close_news.png",
        "loopWaitingTime" : 15, 
        "failResponse" : "Ignore",
        "loopTime":0 }
act = ClickAction(tag = "5.1", desc="SkipTaohuaNews", **arg)
acts.addAction(act)
#action 5.2
arg = { "detectRegion": gl.AREA_ICON_WELFARECENTER  ,"imagePattern"  :  "welfare_center.png",
        "clk_region"  : gl.AREA_BTN_WELFARECENTER   ,"clk_ptn"       :  "btn_close_welfare_center.png",
        "loopWaitingTime": 0                        ,"failResponse"  :  "Ignore",
        "loopTime" : 1                              ,"loopType"      :  0}
act = ClickAction(tag = "5.2",desc="Close WelfareCenter", **arg)
acts.addAction(act)
#action 5.3
arg = { "detectRegion": gl.AREA_BTN_GOACTIVITY      ,"imagePattern"  :  "btn_close_activity.png",
        "loopWaitingTime": 0                        ,"failResponse"  :  "Ignore",
        "loopTime" : 1                              ,"loopType"      :  0}
act = ClickAction(tag = "5.3",desc="Close Go-Activity Window", **arg)
acts.addAction(act)
#action 6
arg = { "detectRegion" : GetRegionFromGrid(126, 143),
        "imagePattern" : "ZongheButton.PNG",
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 4  ,
        "loopType"     :  0 }
act = ClickAction(tag = "6", desc = "ClickZongheButton", **arg)
acts.addAction(act)
#action 7
arg = { "detectRegion" : GetRegionFromGrid(116, 134),
        "imagePattern" : "QiehuanButton.PNG",
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopRegion": GetRegionFromGrid(100, 118)      ,
        "loopPattern"  :"QiehuanzhanghaoButton.PNG",
        "loopTime" : 4  ,
        "loopType"     :  1}
act = ClickAction(tag = "7", desc = "ClickQiehuanButton", **arg)
acts.addAction(act)
#action 7.5
arg = { "time": 1}
act = SleepAction(tag = "7.5", desc = "wait", **arg)
acts.addAction(act)
#action 8
arg = { "detectRegion" : GetRegionFromGrid(100, 118),
        "imagePattern" : "QiehuanzhanghaoButton.PNG",
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 4  ,
        "loopType"     :  0}
act = ClickAction(tag = "8", desc = "ClickQiehuanzhanghaoButton", **arg)
acts.addAction(act)