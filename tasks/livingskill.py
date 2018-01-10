# -*- coding: utf-8 -*-
task = Task("Livingskill", desc = u"生活技能")
#task.addSetupActionSet("RefreshGame",tag="pre1",desc="RefreshGame")
task.addTeardownActionSet("TypeCommand", tag = "0.6", desc = u"清除背包", mp={'command':'$dropall -1'})
tasksuit.addTask(task)

#Login
step = Step("step0.5", u"登陆")
step.addActionSet("InputNamePsd", tag = "login", desc = u"输入账号密码", mp={'username':'autotest0001', 'password':'123456'})
step.addActionSet("TypeCommand", tag = "0.6", desc = u"增加精力", mp={'command':'$full2'})
step.addActionSet("CLoseWindow", tag = "1.6", desc = u"关闭烦人的窗口")
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
arg = { "detectRegion" : GetRegionFromGrid(123, 140),
        "imagePattern" : Pattern("jineng.PNG"),
        "loopRegion" : GetRegionFromGrid(123, 140),
        "loopPattern" : Pattern("jineng.PNG"),
        "loopWaitingTime" : 30,
        "failResponse" : "Fail" }
act = ClickAction(tag = "2", desc = u"点击技能按钮", **arg)
step.addAction(act)
#action3
arg = { "detectRegion" : GetRegionFromGrid(110, 143),
        "imagePattern" : Pattern("shenghuo2.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopRegion" : GetRegionFromGrid(110, 143),
        "loopPattern" : Pattern("shenghuo.PNG"),
        "loopTime" : 3,
        "loopType" : 1 }
act = ClickAction(tag = "3", desc = u"点击生活按钮", **arg)
step.addAction(act)
#action4
arg = { "detectRegion" : GetRegionFromGrid(18, 35),
        "imagePattern" : Pattern("pengren.PNG"),
        "loopWaitingTime" : 1,
        "failResponse" : "Fail"}
act = ClickAction(tag = "4", desc = u"点击选择烹饪", **arg)
step.addAction(act)
#action5
arg = { "detectRegion" : GetRegionFromGrid(28, 46),
        "imagePattern" : Pattern("xuexi.PNG"),
        "loopWaitingTime" : 1,
        "failResponse" : "Fail"}
act = ClickAction(tag = "5", desc = u"点击学习", **arg)
step.addAction(act)
#action6
arg = { "detectRegion" : GetRegionFromGrid(124, 142),
        "imagePattern" : Pattern("pengrenzhizuo.PNG"),
        "loopWaitingTime" : 1,
        "failResponse" : "Fail"}
act = ClickAction(tag = "6", desc = u"点击制作", **arg)
step.addAction(act)
#action7
arg = { "detectRegion" : GetRegionFromGrid(34, 51),
        "imagePattern" : Pattern("lianyao.PNG"),
        "loopWaitingTime" : 1,
        "failResponse" : "Fail"}
act = ClickAction(tag = "7", desc = u"点击选择炼药", **arg)
step.addAction(act)
#action8
arg = { "detectRegion" : GetRegionFromGrid(28, 46),
        "imagePattern" : Pattern("xuexi.PNG"),
        "loopWaitingTime" : 1,
        "failResponse" : "Fail"}
act = ClickAction(tag = "8", desc = u"点击学习", **arg)
step.addAction(act)
#action9
arg = { "detectRegion" : GetRegionFromGrid(124, 142),
        "imagePattern" : Pattern("lianyaozhizuo.PNG"),
        "loopWaitingTime" : 1,
        "failResponse" : "Fail"}
act = ClickAction(tag = "9", desc = u"点击制作", **arg)
step.addAction(act)
#action10
arg = { "detectRegion" : GetRegionFromGrid(50, 67),
        "imagePattern" : Pattern("zhifu.PNG"),
        "loopWaitingTime" : 1,
        "failResponse" : "Fail"}
act = ClickAction(tag = "10", desc = u"点击选择制符", **arg)
step.addAction(act)
#action11
arg = { "detectRegion" : GetRegionFromGrid(28, 46),
        "imagePattern" : Pattern("xuexi.PNG"),
        "loopWaitingTime" : 1,
        "failResponse" : "Fail"}
act = ClickAction(tag = "11", desc = u"点击学习", **arg)
step.addAction(act)
#action12
arg = { "detectRegion" : GetRegionFromGrid(121, 138),
        "imagePattern" : Pattern("zhifuzhizuo.PNG"),
        "loopWaitingTime" : 1,
        "failResponse" : "Fail"}
act = ClickAction(tag = "12", desc = u"点击制作", **arg)
#action13
arg = { "detectRegion" : GetRegionFromGrid(13, 30),
        "imagePattern" : Pattern("btn_close_welfare_center.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "13", desc = u"关闭界面", **arg)
step.addAction(act)
#action模块结束等待
arg = { "time" : 5 }
act = SleepAction(tag = "end", desc = u"模块结束等待", **arg)
step.addAction(act)