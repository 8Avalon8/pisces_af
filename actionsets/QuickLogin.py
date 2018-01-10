# -*- coding: utf-8 -*-
#QuickLogin
#快速登录
'''

'''
acts = ActionSet(tag=tag,desc=desc,mp=mp)
#step.addAction(acts)
#action1
arg = { "detectRegion" : GetRegionFromGrid(119, 138),
        "imagePattern" : "LoginGame.PNG",
        "loopWaitingTime" : 5,                         
        "failResponse" : "Fail",
        "loopRegion" : GetRegionFromGrid(119, 138),
        "loopPattern" : "LoginGame.PNG",
        "loopTime" : 3,
        "loopType" : 0 }
act = ClickAction(tag = "1", desc = "LoginGame", **arg)
acts.addAction(act)
#action2
arg = { "time" : 5 }
act = SleepAction(tag = "end", desc = u"登录后等待", **arg)
acts.addAction(act)