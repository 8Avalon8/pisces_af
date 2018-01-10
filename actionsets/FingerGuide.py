# -*- coding: utf-8 -*-
'''
username :
password :
'''

acts = ActionSet(tag=tag,desc=desc,mp=mp)
#act1
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("6.png").similar(0.90).targetOffset(0,-69),
        "loopWaitingTime": 0,
        "failResponse" : "Ignore",
        "loopTime": 0,
        "saveImage" :True }
act = ClickAction(tag = "1",desc=u"上箭头", **arg)
acts.addAction(act)
#act2
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("7.png").similar(0.90).targetOffset(0,70),
        "loopWaitingTime": 0,
        "failResponse" : "Ignore",
        "loopTime": 0,
        "saveImage" :True }
act = ClickAction(tag = "2",desc=u"下箭头", **arg)
acts.addAction(act)
#act3
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("8.png").similar(0.90).targetOffset(-80,-1),
        "loopWaitingTime": 0,
        "failResponse" : "Ignore",
        "loopTime": 0,
        "saveImage" :True }
act = ClickAction(tag = "3",desc=u"左箭头", **arg)
acts.addAction(act)
#act4
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("9.png").similar(0.90).targetOffset(74,0),
        "loopWaitingTime": 0,
        "failResponse" : "Ignore",
        "loopTime": 0,
        "saveImage" :True }
act = ClickAction(tag = "4",desc=u"右箭头", **arg)
acts.addAction(act)