# -*- coding: utf-8 -*-
#ExitAccount
#切换账号
'''

'''
acts = ActionSet(tag=tag,desc=desc,mp=mp)
#action 1
arg = { "detectRegion" : GetRegionFromGrid(126, 143),
    "imagePattern" : "ZongheButton.PNG",
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopType"     :  0 }
act = ClickAction(tag = "1", desc = "ClickZongheButton", **arg)
acts.addAction(act)
#action 2
arg = { "detectRegion" : GetRegionFromGrid(116, 134),
    "imagePattern" : "QiehuanButton.PNG",
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime":0,
        "loopType":0 }
act = ClickAction(tag = "2", desc = "ClickQiehuanButton", **arg)
acts.addAction(act)

#action 3
arg = { "detectRegion" : GetRegionFromGrid(100, 118),
    "imagePattern" : "QiehuanzhanghaoButton.PNG",
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopType":  0
        }
act = ClickAction(tag = "3", desc = "ClickQiehuanzhanghaoButton", **arg)
acts.addAction(act)
#action 4
arg = { "time": 5}
act = SleepAction(tag = "4", desc = "wait", **arg)
acts.addAction(act)