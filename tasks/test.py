# -*- coding: utf-8 -*-
task = Task("MainStory",desc = u"test")
tasksuit.addTask(task)
step = Step("step0.5",u"teststep")
task.addStep(step)
#act1.7
arg = { "start":GetRegionFromGrid(136),"end":GetRegionFromGrid(24)}
act = DragAction(tag = "1",desc=u"日常指引向上滑动翻一页", **arg)
step.addAction(act)
