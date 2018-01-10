# -*- coding: utf-8 -*-

'''
username :
password :
'''
acts = ActionSet(tag=tag,desc=desc,mp=mp)
#action 0.5
arg = { "detectRegion" : GetRegionFromGrid(7, 25),
        "imagePattern" : "GameNotice.PNG",
        "clk_region" : GetRegionFromGrid(119, 122),
        "clk_ptn" : "ConfirmGameNotice.PNG",
        "loopWaitingTime": 10,
        "failResponse" : "Ignore",
        "loopTime": 0 }
act = ClickAction(tag = "0.5",desc="ConfirmGameNotice", **arg)
acts.addAction(act)
#action 0.6
arg =  { "time" : 3 }
act = SleepAction(tag = "0.6", desc= "JustForWaitingInfo", **arg)
acts.addAction(act)
#action 1.1
arg = { "detectRegion" : GetRegionFromGrid(15, 32),
        "imagePattern" : "UserCenter.PNG",
        "loopWaitingTime" : 10,
        "failResponse" : "Fail",
        "loopTime" : 0 }
act = ClickAction(tag = "1.1", desc = "FindUserLoginWindow", **arg)
acts.addAction(act)
#action 1.2
arg = { "detectRegion" : GetRegionFromGrid(53, 54),
        "imagePattern" : "UsernameFrame.PNG",
        "clk_region" : GetRegionFromGrid(53, 54),
        "clk_ptn" : Pattern("UsernameFrame.PNG").targetOffset(50, 0),
        "loopWaitingTime" : 10,
        "failResponse" : "Fail",
        "loopTime" : 0 }
act = ClickAction(tag = "1.2", desc = "FindUsernameFrame", **arg)
acts.addAction(act)
#action 1.3
arg = { "contents" : acts.getArg('username') }
act = PasteAction(tag = "1.3", desc = "InputUsername", **arg)
acts.addAction(act)
#action 1.305
arg = { "time" : 0.5 }
act = SleepAction(tag = "1.305", desc = "WaitForInputPassword", **arg)
acts.addAction(act)
#action 1.31
arg = { "key" : Key.ENTER }
act = TypeAction(tag = "1.31", **arg)
acts.addAction(act)
#action 1.4
arg = { "detectRegion" : GetRegionFromGrid(69, 70),
        "imagePattern" : "PasswordFrame.PNG",
        "clk_region" : GetRegionFromGrid(69, 70),
        "clk_ptn" : Pattern("PasswordFrame.PNG").targetOffset(50, 0),
        "loopWaitingTime" : 2,
        "failResponse" : "Fail",
        "loopTime" : 0 }
act = ClickAction(tag = "1.4", desc = "FindPasswordFrame", **arg)
acts.addAction(act)
#action 1.5
arg = { "contents" : acts.getArg('password')}
act = PasteAction(tag = "1.5", desc = "InputPassword", **arg)
acts.addAction(act)
#action 1.505
arg = { "time" : 0.5 }
act = SleepAction(tag = "1.505", desc = "WaitForInputPassword", **arg)
acts.addAction(act)
#action 1.51
arg = { "key" : Key.ENTER }
act = TypeAction(tag = "1.51", **arg)
acts.addAction(act)
#action 1.6
arg = { "detectRegion" : GetRegionFromGrid(89, 108),    "imagePattern" : "UserConfirm.PNG",
        "loopWaitingTime" : 5,                          "failResponse" : "Fail",
        "loopRegion": GetRegionFromGrid(119, 138)      ,"loopPattern"  :"LoginGame.PNG",
        "loopTime" : 5                                 ,"loopType"     :  1 }
act = ClickAction(tag = "1.6", desc = "ClickUserConfirm", **arg)
acts.addAction(act)
#action 1.7
arg = { "time" : 2 }
act = SleepAction(tag = "1.7", desc = "WaitForUserIdentify", **arg)
acts.addAction(act)
#action 3
arg = { "detectRegion" : GetRegionFromGrid(119, 138),   "imagePattern" : "LoginGame.PNG",
        "loopWaitingTime" : 5 ,                         "failResponse" : "Fail" ,
        "loopRegion": GetRegionFromGrid(119, 138)      ,"loopPattern"  :"LoginGame.PNG",
        "loopTime" : 5                                 ,"loopType"     :  0 }
act = ClickAction(tag = "3", desc = "LoginGame", **arg)
acts.addAction(act)
#action 4
arg = { "time" : 10 }
act = SleepAction(tag = "4", desc = "WaitForUserIdentify", **arg)
acts.addAction(act)