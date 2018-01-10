# -*- coding: utf-8 -*-
#Step
task = Task("TifuAutoLogin",desc = u"体服自动登录用例")
task.addSetupActionSet("RefreshGame",tag="pre1",desc="RefreshGame")
#task.addTeardownActionSet("RefreshGame",tag="end1",desc="RefreshGame")
tasksuit.addTask(task)
step = Step("step0.5", "pre")
task.addStep(step)
#action1
exp = """
import datetime
starttime = datetime.datetime.now()
"""
act = Exec(tag = "1", desc = u"清理任务计数器开始", exp = exp)
step.addAction(act)
step = Step("step1", "AutoLogin")
task.addStep(step)
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount2",desc = u"十里桃花", mp = {'username':'autologin2','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount3",desc = u"世外桃源", mp = {'username':'autologin3','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount4",desc = u"桃源盛世", mp = {'username':'autologin4','password':'123456'})
exp = """
endtime = datetime.datetime.now()
ftime = endtime - starttime
"""
act = Exec(tag = "2", desc = u"任务计数器加1", exp = exp)
step.addAction(act)
act = Jump(tag = "3", desc = u"判断是否满一小时", target = ["action","5"], cond = "ftime.seconds >= 3600")
step.addAction(act)
act = Jump(tag = "4", desc = u"一次循环完成", target = ["step","step1"])
step.addAction(act)
act = Exec(tag = "5", desc = u"什么都不干准备结束", exp = "cleartasktimer = 0")
step.addAction(act)