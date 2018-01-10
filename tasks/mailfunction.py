# -*- coding: utf-8 -*-
task = Task("mailfunction",desc = u"邮件功能")
#task.addSetupActionSet("RefreshGame",tag="pre1",desc="RefreshGame")
#task.addTeardownActionSet("TypeCommand", tag = "12", desc = u"清除背包", mp={'command':'$dropall -1'})
tasksuit.addTask(task)

#Login
step = Step("step0.5", u"登陆")
#step.addActionSet("InputNamePsd", tag = "login", desc = u"输入账号密码", mp={'username':'test06001', 'password':'123456'})
#发送邮件
step.addActionSet("TypeCommand", tag = "0.61", desc = u"发送邮件1", mp={'command':u'$mailitem 1350007 60710 1 邮件测试1'})
step.addActionSet("TypeCommand", tag = "0.62", desc = u"发送邮件2", mp={'command':u'$mailitem 1350007 60711 1 邮件测试2'})
step.addActionSet("TypeCommand", tag = "0.63", desc = u"发送邮件3", mp={'command':u'$mailitem 1350007 60712 1 邮件测试3'})
step.addActionSet("TypeCommand", tag = "0.64", desc = u"发送邮件4", mp={'command':u'$mailitem 1350007 60713 1 邮件测试4'})
step.addActionSet("TypeCommand", tag = "0.65", desc = u"发送邮件5", mp={'command':u'$mailitem 1350007 60714 1 邮件测试5'})
step.addActionSet("TypeCommand", tag = "0.66", desc = u"发送邮件6", mp={'command':u'$mailitem 1350007 60715 1 邮件测试6'})
step.addActionSet("TypeCommand", tag = "0.67", desc = u"发送邮件7", mp={'command':u'$mailitem 1350007 60716 1 邮件测试7'})
step.addActionSet("TypeCommand", tag = "0.68", desc = u"发送邮件8", mp={'command':u'$mailitem 1350007 60717 1 邮件测试8'})
step.addActionSet("TypeCommand", tag = "0.69", desc = u"发送邮件9", mp={'command':u'$mailitem 1350007 60718 1 邮件测试9'})
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
arg = { "detectRegion" : GetRegionFromGrid(97, 113),
        "imagePattern" : Pattern("haoyoutubiao.PNG"),
        "loopRegion" : GetRegionFromGrid(97, 113),
        "loopPattern" : Pattern("haoyoutubiao.PNG"),
        "loopWaitingTime" : 30,
        "failResponse" : "Fail" }
act = ClickAction(tag = "2", desc = u"点击好友图标", **arg)
step.addAction(act)
#action3
arg = { "detectRegion" : GetRegionFromGrid(17, 18),
        "imagePattern" : Pattern("youxiang.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "3", desc = u"点击邮箱", **arg)
step.addAction(act)
#action4
arg = { "detectRegion" : GetRegionFromGrid(18, 35),
        "imagePattern" : Pattern("xitongyoujian.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "4", desc = u"点击系统邮件", **arg)
step.addAction(act)
#action5
arg = { "detectRegion" : GetRegionFromGrid(2, 4),
        "imagePattern" : Pattern("yijianlingqu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "5", desc = u"点击一键领取", **arg)
step.addAction(act)
#action6
arg = { "detectRegion" : GetRegionFromGrid(5, 7),
        "imagePattern" : Pattern("yijianshanchu.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "6", desc = u"点击一键删除", **arg)
step.addAction(act)
#action7
arg = { "detectRegion" : GetRegionFromGrid(89, 91),
        "imagePattern" : Pattern("youjianshanchuqueding.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "7", desc = u"点击确定", **arg)
step.addAction(act)
#action8
arg = { "detectRegion" : GetRegionFromGrid(8, 9),
        "imagePattern" : Pattern("guanbishejiaojiemian.PNG"),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail"}
act = ClickAction(tag = "8", desc = u"点击关闭社交界面", **arg)
step.addAction(act)
#action模块结束等待
arg = { "time" : 5 }
act = SleepAction(tag = "end", desc = u"模块结束等待", **arg)
step.addAction(act)