# -*- coding: utf-8 -*-
task = Task("cangkufunction",desc = u"仓库功能")
#task.addSetupActionSet("RefreshGame",tag="pre1",desc="RefreshGame")
task.addTeardownActionSet("TypeCommand", tag = "12", desc = u"清除背包", mp={'command':'$dropall -1'})
tasksuit.addTask(task)

#Login
step = Step("step0.5", u"登陆")
#step.addActionSet("InputNamePsd", tag = "login", desc = u"输入账号密码", mp={'username':'test06001', 'password':'123456'})
step.addActionSet("TypeCommand", tag = "0.6", desc = u"清除背包", mp={'command':'$dropall -1'})
step.addActionSet("TypeCommand", tag = "0.61", desc = u"克隆宝石1", mp={'command':'$clone 60710'})
step.addActionSet("TypeCommand", tag = "0.62", desc = u"克隆宝石2", mp={'command':'$clone 60711'})
step.addActionSet("TypeCommand", tag = "0.63", desc = u"克隆宝石3", mp={'command':'$clone 60712'})
step.addActionSet("TypeCommand", tag = "0.64", desc = u"克隆宝石4", mp={'command':'$clone 60713'})
step.addActionSet("TypeCommand", tag = "0.65", desc = u"克隆宝石5", mp={'command':'$clone 60714'})
step.addActionSet("TypeCommand", tag = "0.66", desc = u"克隆宝石6", mp={'command':'$clone 60715'})
step.addActionSet("TypeCommand", tag = "0.67", desc = u"克隆宝石7", mp={'command':'$clone 60716'})
step.addActionSet("TypeCommand", tag = "0.68", desc = u"克隆宝石8", mp={'command':'$clone 60717'})
step.addActionSet("TypeCommand", tag = "0.69", desc = u"克隆宝石9", mp={'command':'$clone 60718'})
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
arg = { "detectRegion" : GetRegionFromGrid(121, 138),
        "imagePattern" : Pattern("cangku.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "3", desc = u"点击仓库", **arg)
step.addAction(act)

#存放
#action4
arg = { "detectRegion" : GetRegionFromGrid(24, 41),
        "imagePattern" : Pattern("cangkubaoshi1.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "4", desc = u"点击宝石1", **arg)
step.addAction(act)
#action5
arg = { "detectRegion" : GetRegionFromGrid(84, 102),
        "imagePattern" : Pattern("cunrucangku.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "5", desc = u"点击存入仓库", **arg)
step.addAction(act)

#action6
arg = { "detectRegion" : GetRegionFromGrid(25, 42),
        "imagePattern" : Pattern("cangkubaoshi2.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "6", desc = u"点击宝石2", **arg)
step.addAction(act)
#action7
arg = { "detectRegion" : GetRegionFromGrid(84, 102),
        "imagePattern" : Pattern("cunrucangku.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "7", desc = u"点击存入仓库", **arg)
step.addAction(act)

#action8
arg = { "detectRegion" : GetRegionFromGrid(26, 43),
        "imagePattern" : Pattern("cangkubaoshi3.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "8", desc = u"点击宝石3", **arg)
step.addAction(act)
#action9
arg = { "detectRegion" : GetRegionFromGrid(84, 102),
        "imagePattern" : Pattern("cunrucangku.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "9", desc = u"点击存入仓库", **arg)
step.addAction(act)

#action10
arg = { "detectRegion" : GetRegionFromGrid(28, 45),
        "imagePattern" : Pattern("cangkubaoshi4.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "10", desc = u"点击宝石4", **arg)
step.addAction(act)
#action11
arg = { "detectRegion" : GetRegionFromGrid(84, 102),
        "imagePattern" : Pattern("cunrucangku.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "11", desc = u"点击存入仓库", **arg)
step.addAction(act)

#action12
arg = { "detectRegion" : GetRegionFromGrid(29, 46),
        "imagePattern" : Pattern("cangkubaoshi5.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "12", desc = u"点击宝石5", **arg)
step.addAction(act)
#action13
arg = { "detectRegion" : GetRegionFromGrid(84, 102),
        "imagePattern" : Pattern("cunrucangku.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "13", desc = u"点击存入仓库", **arg)
step.addAction(act)

#action14
arg = { "detectRegion" : GetRegionFromGrid(40, 57),
        "imagePattern" : Pattern("cangkubaoshi6.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "14", desc = u"点击宝石6", **arg)
step.addAction(act)
#action15
arg = { "detectRegion" : GetRegionFromGrid(84, 102),
        "imagePattern" : Pattern("cunrucangku.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "15", desc = u"点击存入仓库", **arg)
step.addAction(act)

#action16
arg = { "detectRegion" : GetRegionFromGrid(41, 58),
        "imagePattern" : Pattern("cangkubaoshi7.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "16", desc = u"点击宝石7", **arg)
step.addAction(act)
#action17
arg = { "detectRegion" : GetRegionFromGrid(84, 102),
        "imagePattern" : Pattern("cunrucangku.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "17", desc = u"点击存入仓库", **arg)
step.addAction(act)

#action18
arg = { "detectRegion" : GetRegionFromGrid(42, 59),
        "imagePattern" : Pattern("cangkubaoshi8.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "18", desc = u"点击宝石8", **arg)
step.addAction(act)
#action19
arg = { "detectRegion" : GetRegionFromGrid(84, 102),
        "imagePattern" : Pattern("cunrucangku.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "19", desc = u"点击存入仓库", **arg)
step.addAction(act)

#action20
arg = { "detectRegion" : GetRegionFromGrid(44, 61),
        "imagePattern" : Pattern("cangkubaoshi9.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "18", desc = u"点击宝石9", **arg)
step.addAction(act)
#action21
arg = { "detectRegion" : GetRegionFromGrid(84, 102),
        "imagePattern" : Pattern("cunrucangku.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "19", desc = u"点击存入仓库", **arg)
step.addAction(act)

#取出
#action22   
arg = { "detectRegion" : GetRegionFromGrid(18, 35),
        "imagePattern" : Pattern("cangkubaoshi1.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "22", desc = u"点击宝石1", **arg)
step.addAction(act)
#action23
arg = { "detectRegion" : GetRegionFromGrid(90, 108),
        "imagePattern" : Pattern("quhuibaoguo.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "23", desc = u"点击取回包裹", **arg)
step.addAction(act)

#action24
arg = { "detectRegion" : GetRegionFromGrid(19, 36),
        "imagePattern" : Pattern("cangkubaoshi2.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "24", desc = u"点击宝石2", **arg)
step.addAction(act)
#action25
arg = { "detectRegion" : GetRegionFromGrid(90, 108),
        "imagePattern" : Pattern("quhuibaoguo.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "25", desc = u"点击取回包裹", **arg)
step.addAction(act)

#action26
arg = { "detectRegion" : GetRegionFromGrid(21, 37),
        "imagePattern" : Pattern("cangkubaoshi3.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "26", desc = u"点击宝石3", **arg)
step.addAction(act)
#action27
arg = { "detectRegion" : GetRegionFromGrid(90, 108),
        "imagePattern" : Pattern("quhuibaoguo.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "27", desc = u"点击取回包裹", **arg)
step.addAction(act)

#action28
arg = { "detectRegion" : GetRegionFromGrid(22, 39),
        "imagePattern" : Pattern("cangkubaoshi4.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "28", desc = u"点击宝石4", **arg)
step.addAction(act)
#action29
arg = { "detectRegion" : GetRegionFromGrid(90, 108),
        "imagePattern" : Pattern("quhuibaoguo.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "29", desc = u"点击取回包裹", **arg)
step.addAction(act)

#action30
arg = { "detectRegion" : GetRegionFromGrid(23, 40),
        "imagePattern" : Pattern("cangkubaoshi5.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "30", desc = u"点击宝石5", **arg)
step.addAction(act)
#action31
arg = { "detectRegion" : GetRegionFromGrid(90, 108),
        "imagePattern" : Pattern("quhuibaoguo.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "31", desc = u"点击取回包裹", **arg)
step.addAction(act)

#action32
arg = { "detectRegion" : GetRegionFromGrid(34, 51),
        "imagePattern" : Pattern("cangkubaoshi6.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "32", desc = u"点击宝石6", **arg)
step.addAction(act)
#action33
arg = { "detectRegion" : GetRegionFromGrid(90, 108),
        "imagePattern" : Pattern("quhuibaoguo.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "33", desc = u"点击取回包裹", **arg)
step.addAction(act)

#action34
arg = { "detectRegion" : GetRegionFromGrid(35, 52),
        "imagePattern" : Pattern("cangkubaoshi7.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "34", desc = u"点击宝石7", **arg)
step.addAction(act)
#action35
arg = { "detectRegion" : GetRegionFromGrid(90, 108),
        "imagePattern" : Pattern("quhuibaoguo.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "35", desc = u"点击取回包裹", **arg)
step.addAction(act)

#action36
arg = { "detectRegion" : GetRegionFromGrid(37, 53),
        "imagePattern" : Pattern("cangkubaoshi8.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "36", desc = u"点击宝石8", **arg)
step.addAction(act)
#action37
arg = { "detectRegion" : GetRegionFromGrid(90, 108),
        "imagePattern" : Pattern("quhuibaoguo.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "37", desc = u"点击取回包裹", **arg)
step.addAction(act)

#action38
arg = { "detectRegion" : GetRegionFromGrid(38, 55),
        "imagePattern" : Pattern("cangkubaoshi9.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "38", desc = u"点击宝石9", **arg)
step.addAction(act)
#action39
arg = { "detectRegion" : GetRegionFromGrid(90, 108),
        "imagePattern" : Pattern("quhuibaoguo.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "39", desc = u"点击取回包裹", **arg)
step.addAction(act)

#升级仓库
#action40
'''
arg = { "detectRegion" : GetRegionFromGrid(114, 132),
        "imagePattern" : Pattern("cangku1.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "40", desc = u"点击仓库1", **arg)
step.addAction(act)
#action41
arg = { "detectRegion" : GetRegionFromGrid(99, 116),
        "imagePattern" : Pattern("shengjicangku.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "41", desc = u"点击升级仓库", **arg)
step.addAction(act)
#action42
arg = { "detectRegion" : GetRegionFromGrid(104, 121),
        "imagePattern" : Pattern("shengjicangkuqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "42", desc = u"点击升级仓库确定", **arg)
step.addAction(act)
'''
#action43
arg = { "detectRegion" : GetRegionFromGrid(14, 30),
        "imagePattern" : Pattern("btn_close_welfare_center.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : GetRegionFromGrid(14, 30),
        "loopPattern" : Pattern("btn_close_welfare_center.PNG"),
        "loopType" : 0 }
act = ClickAction(tag = "43", desc = u"点击关闭界面", **arg)
step.addAction(act)
#action模块结束等待
arg = { "time" : 5 }
act = SleepAction(tag = "end", desc = u"模块结束等待", **arg)
step.addAction(act)