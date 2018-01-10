# -*- coding: utf-8 -*-
acts = ActionSet(tag = tag,desc = desc)
#action0.5
arg = { "time": 1}
act = SleepAction(tag = "0.5", **arg)
acts.addAction(act)
#action1
detectRegion = GetRealRegion(1185, 622,  88,  86)
arg = { "detectRegion": detectRegion , "imagePattern" : "test_cancelauto.png",
        "loopWaitingTime": 5         , "failResponse" : "Ignore",
        "successNext": ['action','2'], "failNext"     : ['action','5'],
        "loopType" : 1               , "loopSleepTime": 0.1}
act = DetectAction(tag = "1", desc = u"判断是否是自动战斗模式", **arg)
acts.addAction(act)
#action2
skillRegion = GetRealRegion(991,616,93,91)
arg = { "detectRegion": skillRegion , "imagePattern" : "test_wanjiebufu.png",
        "loopWaitingTime": 0        , "failResponse" : "Ignore",
        "successNext": ['action','6'],"failNext"     : ['action','4'],
        "loopType" : 1               , "loopSleepTime": 0.1}
act = DetectAction(tag = "2", desc = u"判断是否使用了万劫不复", **arg)
acts.addAction(act)

#action4如果否则选择万劫不复,操作成功is_end
detectRegion = GetRealRegion(1185, 622,  88,  86)
arg = { "detectRegion": detectRegion , "imagePattern" : Pattern("test_cancelauto.png").targetOffset(-200,0),
        "loopWaitingTime": 0.5       , "failResponse" : "Ignore",}
act = ClickAction(tag= "4", desc = u"点击选择技能", **arg)
acts.addAction(act)
#action4.5 选择万劫不复
skillPanelRegion = GetRealRegion(836,194,441,424)
arg = { "detectRegion": skillPanelRegion , "imagePattern" : "test_wanjiebufu1.png",
        "next" : ['action','6']     , "loopWaitingTime": 3, "failResponse" : "Ignore",}
act = ClickAction(tag= "4.5", desc = u"选择万劫不复", **arg)
acts.addAction(act)
#非自动战斗模式下点击进入自动战斗模式，再跳转至上述步骤
detectRegion = GetRealRegion(1185, 622,  88,  86)
arg = { "detectRegion" :detectRegion , "imagePattern" : "test_autobattle.png",
        "next" : ['action','2']     ,"loopWaitingTime": 0, "failResponse" : "Ignore",}
act = ClickAction(tag= "5", desc = u"点击自动战斗按钮", **arg)
acts.addAction(act)
#action6如果是则返回True，不用进行操作
arg = { "time" : 0 , "isEnd" : True}
act = SleepAction(tag= "6", desc = u"执行成功", **arg)
acts.addAction(act)