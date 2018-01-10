# -*- coding: utf-8 -*-
#TypeCommand
#输入指令
'''
mp : variant dict in this actionsets
mp['command'] : '$setskill 2099 1'

'''
acts = ActionSet(tag=tag,desc=desc,mp=mp)
#step.addAction(acts)
#action1
arg = { "key": "`"}
act = TypeAction(tag = "1", **arg)
acts.addAction(act)
#action1.5
arg = { "time": 1}
act = SleepAction(tag = "1.5", **arg)
acts.addAction(act)
#action2
#contents = "$setskill 2099 1"
arg = { "contents": acts.getArg('command')}
act = PasteAction(tag = "2", **arg)
acts.addAction(act)
#action3
arg = { "key": Key.ENTER}
act = TypeAction(tag = "3", **arg)
acts.addAction(act)
#action4
arg = { "key": Key.ENTER}
act = TypeAction(tag = "4", **arg)
acts.addAction(act)
#action5
arg = { "time": 0.5}
act = SleepAction(tag = "5", **arg)
acts.addAction(act)
#action 6
arg = { "detectRegion" : gl.R_Screen,    "imagePattern" : "input_done.png",
        "loopWaitingTime" : 1,                          "failResponse" : "Fail",
        "loopTime" : 1                                 ,"loopType"     :  0 }
act = ClickAction(tag = "6", desc = "ClickInputDone", **arg)
#action7
arg = { "time": 0.5}
act = SleepAction(tag = "7", **arg)
acts.addAction(act)
