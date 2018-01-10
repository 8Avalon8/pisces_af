# -*- coding: utf-8 -*-
task = Task("bagorganization",desc = u"背包整理")
#task.addSetupActionSet("RefreshGame",tag="pre1",desc="RefreshGame")
task.addTeardownActionSet("TypeCommand", tag = "12", desc = u"清除背包", mp={'command':'$dropall -1'})
tasksuit.addTask(task)

#Login
step = Step("step0.5", u"登陆")
#step.addActionSet("InputNamePsd", tag = "login", desc = u"输入账号密码", mp={'username':'test06001', 'password':'123456'})
step.addActionSet("TypeCommand", tag = "0.6", desc = u"清除背包", mp={'command':'$dropall -1'})
#物品准备
step.addActionSet("TypeCommand", tag = "0.61", desc = u"克隆宝石5", mp={'command':'$clone 60823'})
step.addActionSet("TypeCommand", tag = "0.615", desc = u"克隆藏宝图", mp={'command':'$clone 70031'})
step.addActionSet("TypeCommand", tag = "0.62", desc = u"克隆宝石3", mp={'command':'$clone 60821'})
step.addActionSet("TypeCommand", tag = "0.625", desc = u"克隆藏宝图", mp={'command':'$clone 70031'})
step.addActionSet("TypeCommand", tag = "0.63", desc = u"克隆宝石1", mp={'command':'$clone 60710'})
step.addActionSet("TypeCommand", tag = "0.635", desc = u"克隆藏宝图", mp={'command':'$clone 70031'})
step.addActionSet("TypeCommand", tag = "0.64", desc = u"克隆宝石x", mp={'command':'$clone 60720'})
step.addActionSet("TypeCommand", tag = "0.645", desc = u"克隆藏宝图", mp={'command':'$clone 70031'})
step.addActionSet("TypeCommand", tag = "0.65", desc = u"克隆宝石8", mp={'command':'$clone 60826'})
step.addActionSet("TypeCommand", tag = "0.655", desc = u"克隆藏宝图", mp={'command':'$clone 70031'})
step.addActionSet("TypeCommand", tag = "0.66", desc = u"克隆宝石4", mp={'command':'$clone 60822'})
step.addActionSet("TypeCommand", tag = "0.665", desc = u"克隆藏宝图", mp={'command':'$clone 70031'})
step.addActionSet("TypeCommand", tag = "0.67", desc = u"克隆宝石9", mp={'command':'$clone 60827'})
step.addActionSet("TypeCommand", tag = "0.675", desc = u"克隆藏宝图", mp={'command':'$clone 70031'})
step.addActionSet("TypeCommand", tag = "0.68", desc = u"克隆宝石7", mp={'command':'$clone 60825'})
step.addActionSet("TypeCommand", tag = "0.685", desc = u"克隆藏宝图", mp={'command':'$clone 70031'})
step.addActionSet("TypeCommand", tag = "0.69", desc = u"克隆宝石2", mp={'command':'$clone 60820'})
step.addActionSet("TypeCommand", tag = "0.695", desc = u"克隆藏宝图", mp={'command':'$clone 70031'})
step.addActionSet("TypeCommand", tag = "0.70", desc = u"克隆宝石6", mp={'command':'$clone 60824'})
step.addActionSet("TypeCommand", tag = "0.705", desc = u"克隆藏宝图", mp={'command':'$clone 70031'})
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
arg = { "detectRegion" : GetRegionFromGrid(111, 128),
        "imagePattern" : Pattern("wupin.PNG"),
        "loopRegion" : GetRegionFromGrid(111, 128),
        "loopPattern" : Pattern("wupin.PNG"),
        "loopWaitingTime" : 30,
        "failResponse" : "Fail" }
act = ClickAction(tag = "2", desc = u"点击物品按钮", **arg)
step.addAction(act)
#action3
arg = { "detectRegion" : GetRegionFromGrid(123, 141),
        "imagePattern" : Pattern("zhengli.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "3", desc = u"点击整理", **arg)
step.addAction(act)
#action4
arg = { "detectRegion" : GetRegionFromGrid(24, 41),
        "imagePattern" : Pattern("baoshi1.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "4", desc = u"点击选择宝石1", **arg)
step.addAction(act)
#action5
arg = { "detectRegion" : GetRegionFromGrid(82, 84),
        "imagePattern" : Pattern("shanghuichushou.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "5", desc = u"点击商会出售", **arg)
step.addAction(act)
#action6
arg = { "detectRegion" : GetRegionFromGrid(28, 45),
        "imagePattern" : Pattern("baoshi3.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "6", desc = u"点击选择宝石3", **arg)
step.addAction(act)
#action7
arg = { "detectRegion" : GetRegionFromGrid(82, 84),
        "imagePattern" : Pattern("shanghuichushou.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "7", desc = u"点击商会出售", **arg)
step.addAction(act)
#action8
arg = { "detectRegion" : GetRegionFromGrid(40, 57),
        "imagePattern" : Pattern("baoshi5.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "8", desc = u"点击选择宝石5", **arg)
step.addAction(act)
#action9
arg = { "detectRegion" : GetRegionFromGrid(82, 84),
        "imagePattern" : Pattern("shanghuichushou.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "9", desc = u"点击商会出售", **arg)
step.addAction(act)
#action10
arg = { "detectRegion" : GetRegionFromGrid(42, 60),
        "imagePattern" : Pattern("baoshi7.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "10", desc = u"点击选择宝石7", **arg)
step.addAction(act)
#action11
arg = { "detectRegion" : GetRegionFromGrid(82, 84),
        "imagePattern" : Pattern("shanghuichushou.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "11", desc = u"点击商会出售", **arg)
step.addAction(act)
#action12
arg = { "detectRegion" : GetRegionFromGrid(13, 30),
        "imagePattern" : Pattern("btn_close_welfare_center.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "12", desc = u"关闭界面", **arg)
step.addAction(act)
#action模块结束等待
arg = { "time" : 5 }
act = SleepAction(tag = "end", desc = u"模块结束等待", **arg)
step.addAction(act)