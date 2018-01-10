# -*- coding: utf-8 -*-
task = Task("BugCommit",desc = u"BUG提交")
#task.addSetupActionSet("RefreshGame",tag="pre1",desc="RefreshGame")
tasksuit.addTask(task)

#Login
step = Step("step0.5", u"登陆")
#step.addActionSet("InputNamePsd", tag = "login", desc = "login input username and password", mp={'username':'test06001','password':'123456'})
task.addStep(step)
#PreCheck
#step = Step("step1", u"登陆预处理")
#act1.5
#step.addActionSet("FingerGuide", tag = "1.5", desc = u"处理新手指示手势")
#act1.6
#step.addActionSet("CLoseWindow", tag = "1.6", desc = u"关闭烦人的窗口")
#task.addStep(step)
#action2
arg = { "detectRegion" : GetRegionFromGrid(126, 143),
        "imagePattern" : Pattern("ZongheButton.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : GetRegionFromGrid(126, 143),
        "loopPattern" : Pattern("ZongheButton.PNG"),
        "loopType" : 0 }
act = ClickAction(tag = "2", desc = u"点击综合按钮", **arg)
step.addAction(act)
#action3
arg = { "detectRegion" : GetRegionFromGrid(123, 140),
        "imagePattern" : Pattern("fankui.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopRegion" : GetRegionFromGrid(123, 140),
        "loopPattern" : Pattern("fankui.PNG"),
        "loopTime" : 3,
        "loopType" : 0 }
act = ClickAction(tag = "3", desc = u"点击反馈按钮", **arg)
step.addAction(act)
#action4
arg = { "detectRegion" : GetRegionFromGrid(104, 121),
        "imagePattern" : Pattern("tijiao.PNG"),
        "clk_region" : GetRegionFromGrid(104, 121),
        "clk_ptn" : Pattern("tijiao.PNG").targetOffset(0, -100),
        "loopWaitingTime" : 2,
        "failResponse" : "Fail",
        "loopTime" : 0 }
act = ClickAction(tag = "4", desc = u"点击输入框", **arg)
step.addAction(act)
#action5-set contents
arg = { "contents": "I love TaoLe"}
act = PasteAction(tag = "5", **arg)
step.addAction(act)
#action6-confirm
arg = { "key": Key.ENTER}
act = TypeAction(tag = "6", **arg)
step.addAction(act)
#action7
arg = { "detectRegion" : GetRegionFromGrid(104, 121),
        "imagePattern" : Pattern("tijiao.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : GetRegionFromGrid(104, 121),
        "loopPattern" : Pattern("tijiao.PNG"),
        "loopType" : 0 }
act = ClickAction(tag = "7", desc = u"点击提交按钮", **arg)
step.addAction(act)
#action8
arg = { "detectRegion" : GetRegionFromGrid(14, 30),
        "imagePattern" : Pattern("btn_close_welfare_center.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : GetRegionFromGrid(14, 30),
        "loopPattern" : Pattern("btn_close_welfare_center.PNG"),
        "loopType" : 0 }
act = ClickAction(tag = "8", desc = u"点击关闭界面", **arg)
step.addAction(act)
