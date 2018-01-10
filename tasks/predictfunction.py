# -*- coding: utf-8 -*-
task = Task("predictfunction",desc = u"算卦")
#task.addSetupActionSet("RefreshGame",tag="pre1",desc="RefreshGame")
task.addTeardownActionSet("TypeCommand", tag = "17", desc = u"清除任务标记", mp={'command':'$cleartask 1'})
tasksuit.addTask(task)

#Login
step = Step("step0.5", u"登陆")
#step.addActionSet("InputNamePsd", tag = "login", desc = u"输入账号密码", mp={'username':'test06001', 'password':'123456'})
step.addActionSet("TypeCommand", tag = "0.6", desc = u"清除任务标记", mp={'command':'$cleartask -1'})
step.addActionSet("TypeCommand", tag = "0.6", desc = u"清除任务标记", mp={'command':'$addactivity 0'})
step.addActionSet("TypeCommand", tag = "0.7", desc = u"去往袁证道处", mp={'command':'$goto 1002 108 26'})
task.addStep(step)
#Fail_Handler
step = Step("Fail_Handler", u"模块失败处理")
step.addActionSet("RefreshGame",tag = "pre1", desc = u"刷新游戏客户端")
step.addActionSet("QuickLogin", tag = "quicklogin", desc = u"快速登录")
task.addStep(step)
#PreCheck
#step = Step("step1", u"登陆预处理")
#act1.5
#step.addActionSet("FingerGuide", tag = "1.5", desc = u"处理新手指示手势")
#act1.6
#step.addActionSet("CLoseWindow", tag = "1.6", desc = u"关闭烦人的窗口")
#task.addStep(step)
step = Step("1", u"模块任务开始")
task.addStep(step)
#action2
arg = { "detectRegion" : GetRegionFromGrid(73, 91),
        "imagePattern" : Pattern("yuanzhengdao.PNG"),
        "clk_region" : GetRegionFromGrid(73, 91),
        "clk_ptn" : Pattern("yuanzhengdao.PNG").similar(0.80).targetOffset(0, -50),
        "loopWaitingTime" : 30,
        "failResponse" : "Fail" }
act = ClickAction(tag = "2", desc = u"点击袁证道", **arg)
step.addAction(act)
#action3
arg = { "detectRegion" : GetRegionFromGrid(93, 96),
        "imagePattern" : Pattern("woyaosuangua.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "3", desc = u"点击我要算卦", **arg)
step.addAction(act)
#action4
arg = { "detectRegion" : GetRegionFromGrid(124, 142),
        "imagePattern" : Pattern("kaishisuangua.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "4", desc = u"点击开始算卦", **arg)
step.addAction(act)

#再算一次1
#action5
arg = { "detectRegion" : GetRegionFromGrid(122, 140),
        "imagePattern" : Pattern("zaisuanyici.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail"}
act = ClickAction(tag = "5", desc = u"点击再算一次1", **arg)
step.addAction(act)
#action6
arg = { "detectRegion" : GetRegionFromGrid(89, 91),
        "imagePattern" : Pattern("suanguaqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "6", desc = u"点击算卦确定", **arg)
step.addAction(act)
#action6.5
arg = { "time" : 7 }
act = SleepAction(tag = "6.5", desc = u"等待算卦结果", **arg)
step.addAction(act)

#再算一次2
#action7
arg = { "detectRegion" : GetRegionFromGrid(122, 140),
        "imagePattern" : Pattern("zaisuanyici.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail"}
act = ClickAction(tag = "7", desc = u"点击再算一次2", **arg)
step.addAction(act)
#action8
arg = { "detectRegion" : GetRegionFromGrid(89, 91),
        "imagePattern" : Pattern("suanguaqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "8", desc = u"点击算卦确定", **arg)
step.addAction(act)
#action8.5
arg = { "time" : 7 }
act = SleepAction(tag = "8.5", desc = u"等待算卦结果", **arg)
step.addAction(act)

#再算一次3
#action9
arg = { "detectRegion" : GetRegionFromGrid(122, 140),
        "loopWaitingTime" : 5,
        "imagePattern" : Pattern("zaisuanyici.PNG"),
        "failResponse" : "Fail"}
act = ClickAction(tag = "9", desc = u"点击再算一次3", **arg)
step.addAction(act)
#action10
arg = { "detectRegion" : GetRegionFromGrid(89, 91),
        "imagePattern" : Pattern("suanguaqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "10", desc = u"点击算卦确定", **arg)
step.addAction(act)
#action10.5
arg = { "time" : 7 }
act = SleepAction(tag = "10.5", desc = u"等待算卦结果", **arg)
step.addAction(act)

#再算一次4
#action11
arg = { "detectRegion" : GetRegionFromGrid(122, 140),
        "loopWaitingTime" : 5,
        "imagePattern" : Pattern("zaisuanyici.PNG"),
        "failResponse" : "Fail"}
act = ClickAction(tag = "11", desc = u"点击再算一次4", **arg)
step.addAction(act)
#action12
arg = { "detectRegion" : GetRegionFromGrid(89, 91),
        "imagePattern" : Pattern("suanguaqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "12", desc = u"点击算卦确定", **arg)
step.addAction(act)
#action12.5
arg = { "time" : 7 }
act = SleepAction(tag = "12.5", desc = u"等待算卦结果", **arg)
step.addAction(act)

#再算一次5
#action13
arg = { "detectRegion" : GetRegionFromGrid(122, 140),
        "imagePattern" : Pattern("zaisuanyici.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail"}
act = ClickAction(tag = "13", desc = u"点击再算一次5", **arg)
step.addAction(act)
#action14
arg = { "detectRegion" : GetRegionFromGrid(89, 91),
        "imagePattern" : Pattern("suanguaqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "14", desc = u"点击算卦确定", **arg)
step.addAction(act)
#action14.5
arg = { "time" : 7 }
act = SleepAction(tag = "14.5", desc = u"等待算卦结果", **arg)
step.addAction(act)

#接受卦象
#action15
arg = { "detectRegion" : GetRegionFromGrid(125, 143),
        "imagePattern" : Pattern("jieshouguaxiang.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "15", desc = u"点击接受卦象", **arg)
step.addAction(act)

#检查日常
#action16
arg = { "detectRegion" : GetRegionFromGrid(5, 6),
        "imagePattern" : Pattern("richang.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : GetRegionFromGrid(5, 6),
        "loopPattern" : Pattern("richang.PNG"),
        "loopType" : 0 }
act = ClickAction(tag = "15", desc = u"点击日常", **arg)
step.addAction(act)
#action17
arg = { "detectRegion" : GetRegionFromGrid(14, 30),
        "imagePattern" : Pattern("btn_close_welfare_center.PNG"),
        "loopRegion" : GetRegionFromGrid(14, 30),
        "loopPattern" : Pattern("btn_close_welfare_center.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail" }
act = ClickAction(tag = "17", desc = u"点击关闭界面", **arg)
step.addAction(act)
#action模块结束等待
arg = { "time" : 5 }
act = SleepAction(tag = "end", desc = u"模块结束等待", **arg)
step.addAction(act)