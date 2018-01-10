# -*- coding: utf-8 -*-
task = Task("namechange",desc = u"角色改名")
#task.addSetupActionSet("RefreshGame",tag="pre1",desc="RefreshGame")
#task.addTeardownActionSet("TypeCommand", tag = "12", desc = u"清除背包", mp={'command':'$dropall -1'})
tasksuit.addTask(task)

#Login
step = Step("step0.5", u"登陆")
#step.addActionSet("InputNamePsd", tag = "login", desc = u"输入账号密码", mp={'username':'test06001', 'password':'123456'})
#step.addActionSet("TypeCommand", tag = "0.6", desc = u"增加金钱", mp={'command': '$addgold 99999999 99999999'})
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
arg = { "detectRegion" : GetRegionFromGrid(15, 32),
        "imagePattern" : Pattern("renwutouxiang.PNG"),
        "loopRegion" : GetRegionFromGrid(15, 32),
        "loopPattern" : Pattern("renwutouxiang.PNG"),
        "loopWaitingTime" : 30,
        "failResponse" : "Fail" }
act = ClickAction(tag = "2", desc = u"点击人物头像", **arg) 
step.addAction(act)
#action3
arg = { "detectRegion" : GetRegionFromGrid(22, 23),
        "imagePattern" : Pattern("gaiminganniu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "3", desc = u"点击改名按钮", **arg)
step.addAction(act)
#action4
arg = { "detectRegion" : GetRegionFromGrid(70, 87),
        "imagePattern" : Pattern("xinjueseming.PNG"),
        "clk_region" : GetRegionFromGrid(70, 87),
        "clk_ptn" : Pattern("xinjueseming.PNG").targetOffset(100, 0),
        "loopWaitingTime" : 10,
        "failResponse" : "Fail" }
act = ClickAction(tag = "4", desc = u"点击改名框", **arg)
step.addAction(act)
#action4.5
arg = { "contents" : u"改名测试" }
act = PasteAction(tag = "4.5", desc = u"改名1", **arg)
step.addAction(act)
#action4.6
arg = { "key" : Key.ENTER }
act = TypeAction(tag = "4.6", **arg)
step.addAction(act)
#action5
arg = { "detectRegion" : GetRegionFromGrid(89, 107),
        "imagePattern" : Pattern("gaimingqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "3", desc = u"点击改名确定", **arg)
step.addAction(act)
#action5.1
arg = { "detectRegion" : GetRegionFromGrid(89, 91),
        "imagePattern" : Pattern("gaimingqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "5.1", desc = u"点击改名二次确定", **arg)
step.addAction(act)

#改名重名测试
'''
#action6
arg = { "detectRegion" : GetRegionFromGrid(15, 32),
        "imagePattern" : Pattern("renwutouxiang.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : GetRegionFromGrid(15, 32),
        "loopPattern" : Pattern("renwutouxiang.PNG"),
        "loopType" : 0 }
act = ClickAction(tag = "6", desc = u"点击人物头像", **arg)
step.addAction(act)
'''
#action7
arg = { "detectRegion" : GetRegionFromGrid(22, 23),
        "imagePattern" : Pattern("gaiminganniu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "7", desc = u"点击改名按钮", **arg)
step.addAction(act)
#action8
arg = { "detectRegion" : GetRegionFromGrid(70, 87),
        "imagePattern" : Pattern("xinjueseming.PNG"),
        "clk_region" : GetRegionFromGrid(70, 87),
        "clk_ptn" : Pattern("xinjueseming.PNG").targetOffset(100, 0),
        "loopWaitingTime" : 10,
        "failResponse" : "Fail" }
act = ClickAction(tag = "8", desc = u"点击改名框", **arg)
step.addAction(act)
#action8.5
arg = { "contents" : u"改名测试" }
act = PasteAction(tag = "8.5", desc = u"改名1", **arg)
step.addAction(act)
#action8.6
arg = { "key" : Key.ENTER }
act = TypeAction(tag = "8.6", **arg)
step.addAction(act)
#action9
arg = { "detectRegion" : GetRegionFromGrid(89, 107),
        "imagePattern" : Pattern("gaimingqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "9", desc = u"点击改名确定", **arg)
step.addAction(act)
#action9.1
arg = { "detectRegion" : GetRegionFromGrid(89, 91),
        "imagePattern" : Pattern("gaimingqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "9.1", desc = u"点击改名二次确定", **arg)
step.addAction(act)

#返回改名
'''
#action10
arg = { "detectRegion" : GetRegionFromGrid(15, 32),
        "imagePattern" : Pattern("renwutouxiang.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : GetRegionFromGrid(15, 32),
        "loopPattern" : Pattern("renwutouxiang.PNG"),
        "loopType" : 0 }
act = ClickAction(tag = "10", desc = u"点击人物头像", **arg)
step.addAction(act)
'''
#action11
arg = { "detectRegion" : GetRegionFromGrid(22, 23),
        "imagePattern" : Pattern("gaiminganniu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "11", desc = u"点击改名按钮", **arg)
step.addAction(act)
#action12
arg = { "detectRegion" : GetRegionFromGrid(70, 87),
        "imagePattern" : Pattern("xinjueseming.PNG"),
        "clk_region" : GetRegionFromGrid(70, 87),
        "clk_ptn" : Pattern("xinjueseming.PNG").targetOffset(100, 0),
        "loopWaitingTime" : 10,
        "failResponse" : "Fail" }
act = ClickAction(tag = "12", desc = u"点击改名框", **arg)
step.addAction(act)
#action12.5
arg = { "contents" : u"萧0001" }
act = PasteAction(tag = "12.5", desc = u"改名1", **arg)
step.addAction(act)
#action12.6
arg = { "key" : Key.ENTER }
act = TypeAction(tag = "12.6", **arg)
step.addAction(act)
#action13
arg = { "detectRegion" : GetRegionFromGrid(89, 107),
        "imagePattern" : Pattern("gaimingqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "13", desc = u"点击改名确定", **arg)
step.addAction(act)
#action13.1
arg = { "detectRegion" : GetRegionFromGrid(89, 91),
        "imagePattern" : Pattern("gaimingqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "13.1", desc = u"点击改名二次确定", **arg)
step.addAction(act)
#action14
arg = { "detectRegion" : GetRegionFromGrid(13, 30),
        "imagePattern" : Pattern("btn_close_welfare_center.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "14", desc = u"关闭界面", **arg)
step.addAction(act)
#action模块结束等待
arg = { "time" : 5 }
act = SleepAction(tag = "end", desc = u"模块结束等待", **arg)
step.addAction(act)