# -*- coding: utf-8 -*-
task = Task("MainStory",desc = u"自动主线")
task.addSetupActionSet("RefreshGame",tag="pre1",desc="RefreshGame")
tasksuit.addTask(task)
step = Step("step0.5",u"Login")
task.addStep(step)
step.addActionSet("InputNamePsd",tag = "login",desc = "login input username and password", mp={'username':'autotest3','password':'123456'})
step.addActionSet("TypeCommand",tag = "0.5",desc = u"获得万劫不复技能", mp = {'command':'$setskill 2099 1'})
step.addActionSet("TypeCommand",tag = "0.6",desc = u"清理道具栏", mp = {'command':'$dropall -1'})
step.addActionSet("TypeCommand",tag = "0.7",desc = u"清理宠物栏", mp = {'command':'$dropsummon'})
step.addActionSet("TypeCommand",tag= "0.8",desc = u"清除所有任务",mp = {'command':'$cleartask 1'})
step.addActionSet("TypeCommand",tag= "0.9",desc = u"重置等级为1级",mp ={'command':'$r who.Base.m_Grade = 1;who.Base.m_Exp=0;who.CalculateProp();who.SendPropChange();'})
step.addActionSet("TypeCommand",tag= "1.0",desc = u"添加主线任务",mp = {'command':'$task 10000'})
#step1
step = Step("step1",u"主循环")
task.addStep(step)
#act1.5
step.addActionSet("FingerGuide",tag = "1.5",desc = u"处理新手指示手势")
#act1.6
step.addActionSet("CLoseWindow",tag = "1.6",desc = u"关闭烦人的窗口")
#act1.7
arg = { "detectRegion": GetRegionFromGrid(13,30)           ,"imagePattern"  :  Pattern("btn_close_welfare_center.png").similar(0.80),
        "failResponse"  :  "Ignore"                        ,"loopWaitingTime": 0   }
act = ClickAction(tag = "1.7",desc=u"关闭人物信息（防止误操作）", **arg)
step.addAction(act)
#act2
arg = { "detectRegion": gl.AREA_BTN_USEITEM           ,"imagePattern"  :  "btn_equip.png",
        "loopWaitingTime": 0                               ,"successNext"  :  ["step","step2"],
        "failResponse" : "Ignore"                          ,"loopSleepTime" : 0.1,
        "loopTime":1                                       ,"loopType"      :  1}
act = DetectAction(tag = "2", desc = u"是否有装备窗口", **arg)
step.addAction(act)
#act3
arg = { "detectRegion": gl.AREA_BTN_USEITEM           ,"imagePattern"  :  "btn_useitem.png",
        "loopWaitingTime": 0                               ,"successNext"  :  ["step","step2"],
        "failResponse" : "Ignore","loopSleepTime" : 0.1,
        "loopTime":1                                       ,"loopType"      :  1}
act = DetectAction(tag = "3", desc = u"是否有使用道具窗口", **arg)
step.addAction(act)
#act4
arg = { "detectRegion": gl.AREA_BTN_SKIPSTORY           ,"imagePattern"  :  Pattern("btn_skip_story.png").similar(0.60),
        "loopWaitingTime": 0                               ,"successNext"  :  ["step","step3"],
        "failResponse" : "Ignore","loopSleepTime" : 0.1,
        "loopTime":1                                       ,"loopType"      :  1}
act = DetectAction(tag = "4", desc = u"是否在剧情或对话中", **arg)
step.addAction(act)
#act4
arg = { "detectRegion": GetRegionFromGrid(45, 128)           ,"imagePattern"  :  Pattern("main_story.png").similar(0.60),
        "loopWaitingTime": 0                               ,"successNext"  :  ["step","step4"],
        "failResponse" : "Ignore","loopSleepTime" : 0.1,"failNext"     :  ["step","step1"],
        "loopTime":1                                       ,"loopType"      :  1}
act = DetectAction(tag = "5", desc = u"任务栏是否有主线", **arg)
step.addAction(act)


#Step2
step = Step("step2",u"处理道具装备")
task.addStep(step)
#action1
arg = { "detectRegion" : gl.AREA_BTN_USEITEM,   "imagePattern" : "btn_useitem.PNG",
        "loopWaitingTime" : 0 ,                         "failResponse" : "Ignore" ,
        "loopRegion": gl.AREA_BTN_USEITEM      ,"loopPattern"  :"btn_useitem.PNG",
        "loopTime" : 5                                 ,"loopType"     :  0 ,
        "loopSleepTime" : 0.1                          ,"saveImage" : True}
act = ClickAction(tag = "1", desc = u"使用道具", **arg)
step.addAction(act)
#action2
arg = { "detectRegion" : gl.AREA_BTN_USEITEM,   "imagePattern" : "btn_equip.PNG",
        "loopWaitingTime" : 0 ,                         "failResponse" : "Ignore" ,
        "loopRegion": gl.AREA_BTN_USEITEM      ,"loopPattern"  :"btn_equip.PNG",
        "loopSleepTime" : 0.1                          ,"saveImage" : True,
        "loopTime" : 5                                 ,"loopType"     :  0 }
act = ClickAction(tag = "2", desc = u"使用装备", **arg)
step.addAction(act)
#action3
act = Jump(tag = "3", desc = u"返回主循环", target = ["step","step1"])
step.addAction(act)

#Step3
step = Step("step3", desc = u"处理剧情中")
task.addStep(step)
#action1
arg = { "detectRegion": gl.AREA_BTN_SKIPSTORY           ,"imagePattern"  :  Pattern("btn_skip_story.png").similar(0.60),
        "loopWaitingTime": 0                               ,"failNext"  :  ["step","step1"],
        "failResponse" : "Ignore","loopSleepTime" : 0.1,
        "loopTime":1                                       ,"loopType"      :  1}
act = DetectAction(tag = "1", desc = u"是否在剧情或对话中，不在则返回主循环Step1", **arg)
step.addAction(act)
#action2
arg = { "detectRegion": GetRegionFromGrid(76, 112)           ,"imagePattern"  :  "enterbattle.png",
        "loopWaitingTime": 0                               ,"next"  :  ["step","step6"],
        "failResponse" : "Ignore","loopSleepTime" : 0.1                          ,"saveImage" : True,
        "loopTime":1                                       ,"loopType"      :  1}
act = DetectAction(tag = "2", desc = u"如果有开始战斗则点击直到消失，并进入战斗Step", **arg)
step.addAction(act)
#action3
arg = { "detectRegion": GetRegionFromGrid(45, 128)           ,"imagePattern"  :  Pattern("main_story.png").similar(0.60),
        "loopWaitingTime": 0                               ,"next"  :  ["step","step4"],
        "failResponse" : "Ignore","loopSleepTime" : 0.1                          ,"saveImage" : True,
        "loopTime":1                                       ,"loopType"      :  1}
act = DetectAction(tag = "3", desc = u"如果有主线则点主线", **arg)
step.addAction(act)
#action 4
arg = { "detectRegion" : gl.AREA_BTN_SKIPSTORY,   "imagePattern" : Pattern("btn_skip_story.png").similar(0.60),
        "loopWaitingTime" : 0 ,                         "failResponse" : "Ignore" ,
        "loopSleepTime" : 0.3,                          "saveImage" : False,
        "loopRegion": gl.AREA_BTN_SKIPSTORY      ,"loopPattern"  :Pattern("btn_skip_story.png").similar(0.60),
        "loopTime" : 8                                 ,"loopType"     :  0 }
act = ClickAction(tag = "4",desc=u"点击跳过", **arg)
step.addAction(act)
#action 5
arg = { "time":1}
act = SleepAction(tag = "5",desc=u"sleep 1s", **arg)
step.addAction(act)
#action 6
act = Jump(tag = "6", desc = u"返回继续处理剧情", target = ["action","1"])
step.addAction(act)

#Step4
step = Step("step4",u"处理剧情追踪")
task.addStep(step)
#act0.5
arg = { "detectRegion": GetRegionFromGrid(45, 128)           ,"imagePattern"  :  Pattern("main_story.png").similar(0.60),
        "loopWaitingTime": 0                                 ,"saveImage" : True  ,
        "failNext" : ["step","step3"]                       ,"failResponse" : "Ignore",
        "loopTime":1                                      ,"loopType"      :  1}
act = DetectAction(tag = "0.5", desc = u"任务栏是否有主线", **arg)
step.addAction(act)
#act1
arg = { "detectRegion": GetRegionFromGrid(45, 128)           ,"imagePattern"  :  Pattern("yiwailaixin.png").similar(0.70),
        "loopWaitingTime": 0                               ,"successNext"  :  ["step","step7"],
        "failResponse" : "Ignore","loopSleepTime" : 0.1,
        "loopTime":1                                       ,"loopType"      :  1}
act = DetectAction(tag = "1", desc = u"是否达到15级下一个任务是意外来信", **arg)



step.addAction(act)
#action2
arg = { "detectRegion" : GetRegionFromGrid(45, 128),   "imagePattern" : Pattern("main_story.png").similar(0.60),
        "loopWaitingTime" : 1 ,                         "failResponse" : "Ignore" ,
        "loopSleepTime" : 0.1,                          "saveImage" : False,
        "loopRegion": GetRegionFromGrid(45, 128)      ,"loopPattern"  :Pattern("main_story.png").similar(0.60),
        "loopTime" : 5                                 ,"loopType"     :  0 }
act = ClickAction(tag = "2", desc = u"循环点击主线直到消失", **arg)
step.addAction(act)
#action3
act = Jump(tag = "3", desc = u"jump to step4 action1",target=["action","0.5"])
step.addAction(act)
#Step6
step = Step("step6",u"自动战斗")
task.addStep(step)
step.addActionSet("AutoBattle",tag = "1",desc = u"自动战斗actionset", mp = {})
#Step7
step = Step("step7",u"结束Task")
task.addStep(step)
arg = {'time':1}
act = SleepAction(tag="end sleep",desc = u"准备结束该任务",**arg)
step.addAction(act)
