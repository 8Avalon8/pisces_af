# -*- coding: utf-8 -*-
#RefreshGame
#按F5刷新游戏
'''

'''
acts = ActionSet(tag=tag,desc=desc,mp=mp)
#step.addAction(acts)
#action1
arg = { "key": Key.F5}
act = TypeAction(tag = "1", **arg)
acts.addAction(act)
#action2
arg = {"time":15}
act = SleepAction(tag = "2", **arg)
acts.addAction(act)