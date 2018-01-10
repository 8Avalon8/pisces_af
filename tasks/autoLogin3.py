# -*- coding: utf-8 -*-
#Step
task = Task("Task1",desc = "Test Task")
task.addSetupActionSet("RefreshGame",tag="pre1",desc="RefreshGame")
#task.addTeardownActionSet("RefreshGame",tag="end1",desc="RefreshGame")
tasksuit.addTask(task)
step = Step("step1", "AutoLogin2")
task.addStep(step)
#setTemp 0.1
act = Exec(tag = "0.1", desc="SetInitialTemp", exp="Temp = 1")
step.addAction(act)
#action 0.5
act = Jump(tag = "0.51", desc = "JumpTologincount1", target = ["action","logincount1"], cond = "Temp == 1")
step.addAction(act)
act = Jump(tag = "0.52", desc = "JumpTologincount2", target = ["action","logincount2"], cond = "Temp == 2")
step.addAction(act)
act = Jump(tag = "0.53", desc = "JumpTologincount3", target = ["action","logincount3"], cond = "Temp == 3")
step.addAction(act)
act = Jump(tag = "0.54", desc = "JumpTologincount4", target = ["action","logincount4"], cond = "Temp == 4")
step.addAction(act)
act = Exec(tag = "0.55", desc = "ResetTemp", exp = "Temp = 1")
step.addAction(act)
act = Jump(tag = "0.56", desc = "JumpTologincount1", target = ["action","logincount1"])
step.addAction(act)
#actionset input name and password
step.addActionSet("InputNamePsd",tag = "logincount1",desc = "login input username and password", mp = {'username':'taoletest1','password':'taole123456'})
#action 1.1
act = Jump(tag = "1.1", desc = "JumpTo3.1", target = ["action","3.1"])
step.addAction(act)
#actionset input name and password
step.addActionSet("InputNamePsd",tag = "logincount2",desc = "login input username and password", mp = {'username':'taoletest2','password':'taole123456'})
#action 1.2
act = Jump(tag = "1.2", desc = "JumpTo3.1", target = ["action","3.1"])
step.addAction(act)
#actionset input name and password
step.addActionSet("InputNamePsd",tag = "logincount3",desc = "login input username and password", mp = {'username':'taoletest3','password':'taole123456'})
#action 1.3
act = Jump(tag = "1.3", desc = "JumpTo3.1", target = ["action","3.1"])
step.addAction(act)
#actionset input name and password
step.addActionSet("InputNamePsd",tag = "logincount4",desc = "login input username and password", mp = {'username':'taoletest4','password':'taole123456'})
#action 1.4
act = Jump(tag = "1.4", desc = "JumpTo3.1", target = ["action","3.1"])
step.addAction(act)
#action 3.1
arg =  {"time":5}
act = SleepAction(tag = "3.1", desc= "WaitForLoading", **arg)
step.addAction(act)
#action 4
arg = { "detectRegion" : GetRegionFromGrid(15, 16),
        "imagePattern" : "btn_skip_story.png",
        "loopWaitingTime" : 5,
        "failResponse" : "Ignore",
        "loopTime" : 0 }
act = ClickAction(tag = "4", desc="SkipAnimation", **arg)
step.addAction(act)
#action 5.1
arg = { "detectRegion" : gl.AREA_ICON_NEWS,
	"imagePattern" : "news.png",
        "clk_region" : gl.AREA_BTN_CLOSENEWS, 
        "clk_ptn" : "btn_close_news.png",
        "loopWaitingTime" : 3, 
        "failResponse" : "Ignore",
        "loopTime":0 }
act = ClickAction(tag = "5.1", desc="SkipTaohuaNews", **arg)
step.addAction(act)
#action 5.2
arg = { "detectRegion" : gl.AREA_ICON_WELFARECENTER,
 	"imagePattern" : "welfare_center.png",
        "clk_region" : gl.AREA_BTN_WELFARECENTER,
        "clk_ptn" : "btn_close_welfare_center.png",
        "loopWaitingTime" : 0,
        "failResponse" : "Ignore" }
act = ClickAction(tag = "5.2", desc = "Close WelfareCenter", **arg)
step.addAction(act)
#action 5.3
arg = { "detectRegion" : gl.AREA_BTN_GOACTIVITY,
 	"imagePattern" : "btn_close_activity.png",
        "loopWaitingTime": 0,
        "failResponse" : "Ignore" }
act = ClickAction(tag = "5.3", desc = "Close Go-Activity Window", **arg)
step.addAction(act)
#action 6
arg = { "detectRegion" : GetRegionFromGrid(126, 143),
 	"imagePattern" : "ZongheButton.PNG",
        "loopWaitingTime" : 3,
        "failResponse" : "Fail",
        "loopTime":0 }
act = ClickAction(tag = "6", desc = "ClickZongheButton", **arg)
step.addAction(act)
#action 7
arg = { "detectRegion" : GetRegionFromGrid(116, 134),
 	"imagePattern" : "QiehuanButton.PNG",
        "loopWaitingTime" : 3,
        "failResponse" : "Fail",
        "loopTime":0 }
act = ClickAction(tag = "7", desc = "ClickQiehuanButton", **arg)
step.addAction(act)
#action 7.5
arg = { "time": 1}
act = SleepAction(tag = "7.5", desc = "wait", **arg)
step.addAction(act)
#changeTemp 7.6
act = Exec(tag = "7.6", desc="ChangeTemp", exp="Temp+=1")
step.addAction(act)
#action 8
arg = { "detectRegion" : GetRegionFromGrid(100, 118),
	"imagePattern" : "QiehuanzhanghaoButton.PNG",
        "loopWaitingTime" : 3,
        "failResponse" : "Fail",
        "loopTime" : 0,
        "next" : ['action','0.51'] }
act = ClickAction(tag = "8", desc = "ClickQiehuanzhanghaoButton", **arg)
step.addAction(act)