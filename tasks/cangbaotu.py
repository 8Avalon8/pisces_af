# -*- coding: utf-8 -*-
task = Task("cangbaotu",desc = u"藏宝图")
#task.addSetupActionSet("RefreshGame",tag="pre1",desc="RefreshGame")
task.addTeardownActionSet("TypeCommand", tag = "37", desc = u"清除任务标记", mp={'command':'$cleartask 1'})
task.addTeardownActionSet("TypeCommand", tag = "37", desc = u"清除任务标记", mp={'command':'$dropall -1'})
tasksuit.addTask(task)

#Login
step = Step("step0.5", u"登陆")
#step.addActionSet("InputNamePsd", tag = "login", desc = u"输入账号密码", mp={'username':'test06001', 'password':'123456'})
step.addActionSet("TypeCommand", tag = "0.6", desc = u"清除任务标记", mp={'command':'$cleartask 1'})
# $task 90016为藏宝图的推荐任务 
step.addActionSet("TypeCommand", tag = "0.7", desc = u"添加藏宝图任务", mp={'command':'$task 90016'})
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

#购买藏宝图
'''
#action2
arg = { "detectRegion" : GetRegionFromGrid(5, 6),
        "imagePattern" : Pattern("richang.PNG"),
        "loopRegion" : GetRegionFromGrid(5, 6),
        "loopPattern" : Pattern("richang.PNG"),
        "loopWaitingTime" : 15,
        "failResponse" : "Fail" }
act = ClickAction(tag = "2", desc = u"点击日常", **arg)
step.addAction(act)
#action3
arg = { "start":GetRegionFromGrid(121),"end":GetRegionFromGrid(25)}
act = DragAction(tag = "3",desc=u"日常指引向上滑动翻一页", **arg)
step.addAction(act)
#action4
arg = { "detectRegion" : GetRegionFromGrid(21, 134),
        "imagePattern" : Pattern("cangbaotu.PNG"),
        "clk_region" : GetRegionFromGrid(21, 134),
        "clk_ptn" : Pattern("cangbaotu.PNG").targetOffset(200, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "4", desc = u"点击藏宝图", **arg)
step.addAction(act)
'''
step = Step("1", u"模块任务开始")
task.addStep(step)
#action2.1
arg = { "detectRegion" : GetRegionFromGrid(45, 96),
        "imagePattern" : Pattern("cangbaoturenwu.PNG"),
        "loopRegion" : GetRegionFromGrid(45, 96),
        "loopPattern" : Pattern("cangbaoturenwu.PNG"),
        "loopWaitingTime" : 30,
        "failResponse" : "Fail" }
act = ClickAction(tag = "2.1", desc = u"点击藏宝图任务", **arg)
step.addAction(act)
#action5
arg = { "detectRegion" : GetRegionFromGrid(61, 80),
        "imagePattern" : Pattern("goumaicangbaotu.PNG"),
        "loopWaitingTime" : 30,
        "failResponse" : "Fail" }
act = ClickAction(tag = "5", desc = u"点击购买藏宝图", **arg)
step.addAction(act)
#action6
arg = { "detectRegion" : GetRegionFromGrid(71, 87),
        "imagePattern" : Pattern("cangbaotujianhao.PNG"),
        "clk_region" : GetRegionFromGrid(71, 87),
        "clk_ptn" : Pattern("cangbaotujianhao.PNG").targetOffset(50, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "6", desc = u"点击小键盘", **arg)
step.addAction(act)

#小键盘测试
#小键盘1
#action7
arg = { "detectRegion" : GetRegionFromGrid(24, 41),
        "imagePattern" : Pattern("xiaojianpan1.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "7", desc = u"点击小键盘1", **arg)
step.addAction(act)
#action8
arg = { "detectRegion" : GetRegionFromGrid(56, 73),
        "imagePattern" : Pattern("xiaojianpanshanchu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "8", desc = u"点击删除", **arg)
step.addAction(act)

#小键盘2
#action9
arg = { "detectRegion" : GetRegionFromGrid(25, 42),
        "imagePattern" : Pattern("xiaojianpan2.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "9", desc = u"点击小键盘2", **arg)
step.addAction(act)
#action10
arg = { "detectRegion" : GetRegionFromGrid(56, 73),
        "imagePattern" : Pattern("xiaojianpanshanchu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "10", desc = u"点击删除", **arg)
step.addAction(act)

#小键盘3
#action11
arg = { "detectRegion" : GetRegionFromGrid(27, 44),
        "imagePattern" : Pattern("xiaojianpan3.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "11", desc = u"点击小键盘3", **arg)
step.addAction(act)
#action12
arg = { "detectRegion" : GetRegionFromGrid(56, 73),
        "imagePattern" : Pattern("xiaojianpanshanchu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "12", desc = u"点击删除", **arg)
step.addAction(act)

#小键盘4
#action13
arg = { "detectRegion" : GetRegionFromGrid(40, 57),
        "imagePattern" : Pattern("xiaojianpan4.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "13", desc = u"点击小键盘4", **arg)
step.addAction(act)
#action14
arg = { "detectRegion" : GetRegionFromGrid(56, 73),
        "imagePattern" : Pattern("xiaojianpanshanchu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "14", desc = u"点击删除", **arg)
step.addAction(act)

#小键盘5
#action15
arg = { "detectRegion" : GetRegionFromGrid(41, 58),
        "imagePattern" : Pattern("xiaojianpan5.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "15", desc = u"点击小键盘5", **arg)
step.addAction(act)
#action16
arg = { "detectRegion" : GetRegionFromGrid(56, 73),
        "imagePattern" : Pattern("xiaojianpanshanchu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "16", desc = u"点击删除", **arg)
step.addAction(act)

#小键盘6
#action17
arg = { "detectRegion" : GetRegionFromGrid(43, 60),
        "imagePattern" : Pattern("xiaojianpan6.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "17", desc = u"点击小键盘6", **arg)
step.addAction(act)
#action18
arg = { "detectRegion" : GetRegionFromGrid(56, 73),
        "imagePattern" : Pattern("xiaojianpanshanchu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "18", desc = u"点击删除", **arg)
step.addAction(act)

#小键盘7
#action19
arg = { "detectRegion" : GetRegionFromGrid(56, 57),
        "imagePattern" : Pattern("xiaojianpan7.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "19", desc = u"点击小键盘7", **arg)
step.addAction(act)
#action20
arg = { "detectRegion" : GetRegionFromGrid(56, 73),
        "imagePattern" : Pattern("xiaojianpanshanchu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "20", desc = u"点击删除", **arg)
step.addAction(act)

#小键盘8
#action21
arg = { "detectRegion" : GetRegionFromGrid(57, 58),
        "imagePattern" : Pattern("xiaojianpan8.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "21", desc = u"点击小键盘8", **arg)
step.addAction(act)
#action22
arg = { "detectRegion" : GetRegionFromGrid(56, 73),
        "imagePattern" : Pattern("xiaojianpanshanchu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "22", desc = u"点击删除", **arg)
step.addAction(act)

#小键盘9
#action23
arg = { "detectRegion" : GetRegionFromGrid(59, 60),
        "imagePattern" : Pattern("xiaojianpan9.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "23", desc = u"点击小键盘9", **arg)
step.addAction(act)
#action24
arg = { "detectRegion" : GetRegionFromGrid(56, 73),
        "imagePattern" : Pattern("xiaojianpanshanchu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "24", desc = u"点击删除", **arg)
step.addAction(act)

#小键盘0
#action25
arg = { "detectRegion" : GetRegionFromGrid(57, 74),
        "imagePattern" : Pattern("xiaojianpan0.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "25", desc = u"点击小键盘0", **arg)
step.addAction(act)
#action26
arg = { "detectRegion" : GetRegionFromGrid(59, 76),
        "imagePattern" : Pattern("xiaojianpanqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "26", desc = u"点击确定", **arg)
step.addAction(act)
#action27
arg = { "detectRegion" : GetRegionFromGrid(89, 107),
        "imagePattern" : Pattern("goumaicangbaotuqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "27", desc = u"点击购买藏宝图确定", **arg)
step.addAction(act)
'''
#action27.5
arg = { "contents": "$cleartask 1"}
act = PasteAction(tag = "27.5", **arg)
step.addAction(act)
#action27.6
arg = { "key": Key.ENTER}
act = TypeAction(tag = "27.6", **arg)
step.addAction(act)
'''

#兑换妖龙宝图
'''
#action28
arg = { "detectRegion" : GetRegionFromGrid(5, 6),
        "imagePattern" : Pattern("richang.PNG"),
        "loopRegion" : GetRegionFromGrid(5, 6),
        "loopPattern" : Pattern("richang.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "28", desc = u"点击日常", **arg)
step.addAction(act)
#action29
arg = { "start":GetRegionFromGrid(121),"end":GetRegionFromGrid(25)}
act = DragAction(tag = "29",desc=u"日常指引向上滑动翻一页", **arg)
step.addAction(act)
#action30
arg = { "detectRegion" : GetRegionFromGrid(21, 134),
        "imagePattern" : Pattern("cangbaotu.PNG"),
        "clk_region" : GetRegionFromGrid(21, 134),
        "clk_ptn" : Pattern("cangbaotu.PNG").targetOffset(200, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "30", desc = u"点击藏宝图", **arg)
step.addAction(act)
'''
#action30.1
arg = { "detectRegion" : GetRegionFromGrid(45, 96),
        "imagePattern" : Pattern("cangbaoturenwu.PNG"),
        "loopRegion" : GetRegionFromGrid(45, 96),
        "loopPattern" : Pattern("cangbaoturenwu.PNG"),
        "loopWaitingTime" : 15,
        "failResponse" : "Fail" }
act = ClickAction(tag = "30.1", desc = u"点击藏宝图任务", **arg)
step.addAction(act)
#action31
arg = { "detectRegion" : GetRegionFromGrid(61, 96),
        "imagePattern" : Pattern("duihuanyaolongbaotu.PNG"),
        "loopRegion" : GetRegionFromGrid(61, 96),
        "loopPattern" : Pattern("duihuanyaolongbaotu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopType" : 0 }
act = ClickAction(tag = "31", desc = u"点击兑换妖龙宝图", **arg)
step.addAction(act)
#action32
arg = { "detectRegion" : GetRegionFromGrid(89, 91),
        "imagePattern" : Pattern("yaolongbaotuqueding.PNG"),
        "loopRegion" : GetRegionFromGrid(89, 96),
        "loopPattern" : Pattern("yaolongbaotuqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "32", desc = u"点击兑换妖龙宝图确定", **arg)
step.addAction(act)
'''
#action32.5
arg = { "contents": "$cleartask 1"}
act = PasteAction(tag = "32.5", **arg)
step.addAction(act)
#action32.6
arg = { "key": Key.ENTER}
act = TypeAction(tag = "32.6", **arg)
step.addAction(act)
'''
#打听藏宝图
'''
#action33
arg = { "detectRegion" : GetRegionFromGrid(5, 6),
        "imagePattern" : Pattern("richang.PNG"),
        "loopRegion" : GetRegionFromGrid(5, 6),
        "loopPattern" : Pattern("richang.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "33", desc = u"点击日常", **arg)
step.addAction(act)
#action34
arg = { "start":GetRegionFromGrid(121),"end":GetRegionFromGrid(25)}
act = DragAction(tag = "34",desc=u"日常指引向上滑动翻一页", **arg)
step.addAction(act)
#action35
arg = { "detectRegion" : GetRegionFromGrid(21, 134),
        "imagePattern" : Pattern("cangbaotu.PNG"),
        "clk_region" : GetRegionFromGrid(21, 134),
        "clk_ptn" : Pattern("cangbaotu.PNG").targetOffset(200, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "35", desc = u"点击藏宝图", **arg)
step.addAction(act)
'''
#action35.1
arg = { "detectRegion" : GetRegionFromGrid(45, 96),
        "imagePattern" : Pattern("cangbaoturenwu.PNG"),
        "loopRegion" : GetRegionFromGrid(45, 96),
        "loopPattern" : Pattern("cangbaoturenwu.PNG"),
        "loopWaitingTime" : 15,
        "failResponse" : "Fail" }
act = ClickAction(tag = "35.1", desc = u"点击藏宝图任务", **arg)
step.addAction(act)
#action36
arg = { "detectRegion" : GetRegionFromGrid(45, 96),
        "imagePattern" : Pattern("datingcangbaotu.PNG"),
        "loopRegion" : GetRegionFromGrid(45, 96),
        "loopPattern" : Pattern("datingcangbaotu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "36", desc = u"点击打听藏宝图", **arg)
step.addAction(act)
#action模块结束等待
arg = { "time" : 5 }
act = SleepAction(tag = "end", desc = u"模块结束等待", **arg)
step.addAction(act)
