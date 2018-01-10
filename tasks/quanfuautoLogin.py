# -*- coding: utf-8 -*-
#Step
task = Task("QuanfuAutoLogin",desc = u"自动登录用例")
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
step.addActionSet("LogInOut",tag = "logincount1",desc = u"缘定三生", mp = {'username':'autologin1','password':'123456'})
#actionset input name and password
#step.addActionSet("LogInOut",tag = "logincount2",desc = u"十里桃花", mp = {'username':'autologin2','password':'123456'})
#actionset input name and password
#step.addActionSet("LogInOut",tag = "logincount3",desc = u"世外桃源", mp = {'username':'autologin3','password':'123456'})
#actionset input name and password
#step.addActionSet("LogInOut",tag = "logincount4",desc = u"桃源盛世", mp = {'username':'autologin4','password':'123456'})
#actionset input name and password
#step.addActionSet("LogInOut",tag = "logincount5",desc = u"御剑江湖", mp = {'username':'autologin5','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount6",desc = u"海阔天空", mp = {'username':'autologin6','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount7",desc = u"国色天香", mp = {'username':'autologin7','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount8",desc = u"紫气东来", mp = {'username':'autologin8','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount9",desc = u"一战成名", mp = {'username':'autologin9','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount10",desc = u"群英荟萃", mp = {'username':'autologin10','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount11",desc = u"金玉满堂", mp = {'username':'autologin11','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount12",desc = u"斗转星移", mp = {'username':'autologin12','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount13",desc = u"天马行空", mp = {'username':'autologin13','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount14",desc = u"高山流水", mp = {'username':'autologin14','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount15",desc = u"旗开得胜", mp = {'username':'autologin15','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount16",desc = u"金桂飘香", mp = {'username':'autologin16','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount17",desc = u"铁骨铮铮", mp = {'username':'autologin17','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount18",desc = u"金风玉露", mp = {'username':'autologin18','password':'123456'})
#actionset input name and password
step.addActionSet("LogInOut",tag = "logincount19",desc = u"桃源盛世", mp = {'username':'autologin19','password':'123456'})
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