# -*- coding: utf-8 -*-
#Step0.5
task = Task("Task1",desc = "Test Task")
task.addSetupActionSet("RefreshGame",tag="pre1",desc="RefreshGame")
tasksuit.addTask(task)
step = Step("step0.5",u"Login")
task.addStep(step)
#step.addActionSet("InputNamePsd",tag = "login",desc = "login input username and password", mp={'username':'superlihai','password':'5221305'})
step.addActionSet("TypeCommand",tag = "0.4",desc = u"重置任务", mp={'command':'$cleartask'})
step.addActionSet("TypeCommand",tag = "0.5",desc = u"获得万劫不复技能", mp = {'command':'$setskill 2099 1'})
step.addActionSet("TypeCommand",tag = "0.6",desc = u"清理道具栏", mp = {'command':'$dropall -1'})
#Step1
step = Step("step1",u"找到狄仁杰")
task.addStep(step)
#action 1.1
arg = { "detectRegion": gl.AREA_ICON_NEWS           ,"imagePattern"  :  "news.png",
        "clk_region"  : gl.AREA_BTN_CLOSENEWS       ,"clk_ptn"       :  "btn_close_news.png",
        "loopWaitingTime": 0                        ,"failResponse"  :  "Ignore"            }
act = ClickAction(tag = "1.1",desc="Close News", **arg)
step.addAction(act)
#action 1.2
arg = { "detectRegion": gl.AREA_ICON_WELFARECENTER  ,"imagePattern"  :  "welfare_center.png",
        "clk_region"  : gl.AREA_BTN_WELFARECENTER   ,"clk_ptn"       :  "btn_close_welfare_center.png",
        "loopWaitingTime": 0                        ,"failResponse"  :  "Ignore"}
act = ClickAction(tag = "1.2",desc="Close WelfareCenter", **arg)
step.addAction(act)
#action 1.3
arg = { "detectRegion": gl.AREA_BTN_GOACTIVITY      ,"imagePattern"  :  "btn_close_activity.png",
        "loopWaitingTime": 0                        ,"failResponse"  :  "Ignore"}
act = ClickAction(tag = "1.3",desc="Close Go-Activity Window", **arg)
step.addAction(act)
#action 2
arg = { "detectRegion": gl.AREA_ICON_MAP           ,"imagePattern"  :  "icon_map.png",
        "failResponse"  :  "Fail"}
act = ClickAction(tag = "2",desc="Open Map", **arg)
step.addAction(act)
#action 3
arg = { "detectRegion": gl.AREA_MAP_LUOYANG         ,"imagePattern"  :  "map_luoyang.png",
        "failResponse"  :  "Fail"}
act = ClickAction(tag = "3",desc="Goto LuoYang", **arg)
step.addAction(act)
#action 4
arg = { "detectRegion": gl.AREA_MAP_FUBEN           ,"imagePattern"  :  "icon_map_fuben.png",
        "clk_region"  : gl.R_Screen                 ,"clk_ptn"       :  Location(gl.R_Screen.getX()+360, gl.R_Screen.getY()+240),
        "failResponse"  :  "Fail"}
act = ClickAction(tag = "4",desc="Goto Fuben Position", **arg)
step.addAction(act)
#action 4.5
arg = { "detectRegion": gl.AREA_MAP_FUBEN           ,"imagePattern"  :  "icon_map_fuben.png",
        "loopWaitingTime": 1                               ,"successNext"  :  ["action","5"],
        "failNext" : ["action","8"]                        ,"failResponse" : "Ignore",
        "loopTime":1                                       ,"loopType"      :  1}
act = DetectAction(tag = "4.5", desc = "Detect Whether In LuoYang or Not", **arg)
step.addAction(act)
#action 5
arg = { "detectRegion": gl.AREA_ICON_PLAYERINPOSITION      ,"imagePattern"  :  "player_position.png",
        "loopWaitingTime": 3                               ,"failResponse"  :  "Fail",
        "loopTime":10                                      ,"loopType"      :  1}
act = DetectAction(tag = "5", desc="Wait Player Go to Right Positison ", **arg)
step.addAction(act)
#action 6
arg = { "detectRegion": gl.AREA_BTN_CLOSEMAP         ,"imagePattern"  :  "btn_close_map.png",
        "failResponse"  :  "Fail"}
act = ClickAction(tag = "6", desc = "Close LuoYang Map", **arg)
step.addAction(act)
#action 7
#AREA_BTN_CLOSEMAP need to be modified, should be CLOSELUOYANGMAP
arg = { "detectRegion": gl.AREA_BTN_CLOSEMAP         ,"imagePattern"  :  "btn_close_map.png",
        "failResponse"  :  "Fail"                    ,"next"          :  ["action","9"]}
act = ClickAction(tag = "7", desc = "Close World Map", **arg)
step.addAction(act)
#action 8
arg = { "detectRegion": gl.AREA_ROLE_DIRENJIE      ,"imagePattern"  :  "name_direnjie.png",
        "loopWaitingTime": 3                       ,"failResponse"  :  "Fail",
        "loopTime":10                              ,"loopType"      : 1}
act = DetectAction(tag = "8", desc = "Wait Player Go to Right Position", **arg)
step.addAction(act)
#action 9
arg = { "detectRegion": gl.AREA_ROLE_DIRENJIE      ,"imagePattern"  :  "name_direnjie.png",
        "loopWaitingTime": 3                       ,"failResponse"  :  "Fail",
        "loopTime":10                              ,"loopType"      : 1 }
act = DetectAction(tag = "9", desc = "Find Direnjie", **arg)
step.addAction(act)




#Step2
step = Step("step2","Create Group")
task.addStep(step)
#action 1.1
arg = { "detectRegion": gl.AREA_ICON_NEWS           ,"imagePattern"  :  "news.png",
        "clk_region"  : gl.AREA_BTN_CLOSENEWS       ,"clk_ptn"       :  "btn_close_news.png",
        "loopWaitingTime": 1                        ,"failResponse"  :  "Ignore"            }
act = ClickAction(tag = "1.1",desc="Close News", **arg)
step.addAction(act)

#action 1.2
arg = { "detectRegion": gl.AREA_ICON_WELFARECENTER  ,"imagePattern"  :  "welfare_center.png",
        "clk_region"  : gl.AREA_BTN_WELFARECENTER   ,"clk_ptn"       :  "btn_close_welfare_center.png",
        "loopWaitingTime": 1                        ,"failResponse"  :  "Ignore"}
act = ClickAction(tag = "1.2",desc="Close WelfareCenter", **arg)
step.addAction(act)
#action 1.3
arg = { "detectRegion": gl.AREA_BTN_GOACTIVITY      ,"imagePattern"  :  "btn_close_activity.png",
        "loopWaitingTime": 1                        ,"failResponse"  :  "Ignore"}
act = ClickAction(tag = "1.3",desc="Close Go-Activity Window", **arg)
step.addAction(act)
#action 2
detectRegion = GetRealRegion(1118,  99, 130,  93)
arg = { "detectRegion": detectRegion                ,"imagePattern"  :  "test_zudui.png",
        "loopWaitingTime": 1                        ,"failResponse"  :  "Fail"            }
act = ClickAction(tag = "2",desc=u"点击组队", **arg)
step.addAction(act)

#action 3
detectRegion = GetRealRegion( 833, 598, 160,  67)
arg = { "detectRegion": detectRegion               ,"imagePattern"  :  "test_chuangdui.png",
        "loopWaitingTime": 3                       ,"successNext"  :  ["action","4"],
        "failNext" : ["action","5"]                        ,"failResponse" : "Ignore",
        "loopTime":1                                       ,"loopType"      :  1}
act = DetectAction(tag = "3", desc = u"检测是否已经组队", **arg)
step.addAction(act)

#action 4
detectRegion = GetRealRegion( 833, 598, 160,  67)
arg = { "detectRegion": detectRegion                ,"imagePattern"  :  "test_chuangdui.png",
        "loopWaitingTime": 2                        ,"failResponse"  :  "Ignore"            }
act = ClickAction(tag = "4",desc=u"点击创建队伍", **arg)
step.addAction(act)
#action 4.1
arg = { "detectRegion": GetRegionFromGrid(105,123)     ,"imagePattern"  :  "test_zudui_confirm.png",
        "loopWaitingTime": 1                        ,"failResponse"  :  "Ignore"            }
act = ClickAction(tag = "4.1",desc=u"点击确定如果出现创建窗口", **arg)
step.addAction(act)
#action 4.5
detectRegion = GetRealRegion(1107,  46,  74,  61)
arg = { "detectRegion": detectRegion                ,"imagePattern"  :  "btn_close_welfare_center.png",
        "loopWaitingTime": 1                        ,"failResponse"  :  "Fail"            }
act = ClickAction(tag = "4.5",desc=u"关闭队伍界面", **arg)
step.addAction(act)
#action 5
arg = { "detectRegion": gl.AREA_ROLE_DIRENJIE      ,"imagePattern"  :  Pattern("name_direnjie.png").targetOffset(0,-50),
        "loopWaitingTime": 1                       ,"failResponse"  :  "Fail"             }
act = ClickAction(tag = "5", desc = u"点击狄仁杰", **arg)
step.addAction(act)
#action 6
detectRegion = GetRealRegion( 939, 109, 336, 377)
arg = { "detectRegion": detectRegion               ,"imagePattern"  :  "test_cikeliezhuan.png",
        "loopWaitingTime": 2                       ,"failResponse"  :  "Ignore",
        "next":["action","7"]             }
act = ClickAction(tag = "6", desc = u"如果有则选择刺客列传", **arg)
step.addAction(act)
#action 6.2
detectRegion = GetRealRegion( 939, 109, 336, 377)
arg = { "detectRegion": detectRegion               ,"imagePattern"  :  "test_jianwumen.png",
        "loopWaitingTime": 2                       ,"failResponse"  :  "Fail",
        "next":["action","7"]             }
act = ClickAction(tag = "6.2", desc = u"如果有则选择剑舞门", **arg)
step.addAction(act)
#action 7
detectRegion = GetRealRegion( 239, 504, 120,  54)
arg = { "detectRegion": detectRegion               ,"imagePattern"  :  "test_btn_tiaozhan.png",
        "loopWaitingTime": 3                       ,"failResponse"  :  "Fail"             }
act = ClickAction(tag = "7", desc = u"挑战普通难度", **arg)
step.addAction(act)
#action 8
detectRegion = GetRealRegion( 833, 598, 160,  67)
arg = { "detectRegion": gl.AREA_BTN_TRACESTORY      ,"imagePattern"  :  "test_icon_fuben.png",
        "loopWaitingTime": 1                       ,"failResponse"  :  "Fail",
        "loopTime":10                              ,"loopType"      : 1 }
act = DetectAction(tag = "8", desc = u"确认是否进入副本", **arg)
step.addAction(act)

##########
#Step 3
##########

step = Step("step3","LoopFuben")
task.addStep(step)
#action0.5
arg =  {"time":1}
act = SleepAction(tag = "0.5", desc= "sleep", **arg)
step.addAction(act)
#action1
detectRegion = GetRealRegion( 989, 164, 148, 352)
arg = { "detectRegion": detectRegion                ,"imagePattern"  :  "test_icon_fuben.png",
        "loopWaitingTime": 0                        ,"failResponse"  :  "Ignore"            ,
        "loopRegion": gl.AREA_BTN_SKIPSTORY         ,"loopPattern"   :  "btn_skip_story.png",
        "loopTime": 50                              ,"loopType"      :  1                   }
act = ClickAction(tag = "1",desc=u"循环点击副本", **arg)
step.addAction(act)

#action2
detectRegion = GetRealRegion( 931, 99, 210, 373)
arg = { "detectRegion": gl.AREA_BTN_SKIPSTORY       ,"imagePattern"  :  "btn_skip_story.png",
        "loopWaitingTime": 0                        ,"failResponse"  :  "Ignore"            ,
        "loopRegion": detectRegion         ,"loopPattern"   :  "test_choose.png",
        "loopTime": 50                              ,"loopType"      :  1                   }
act = ClickAction(tag = "2",desc=u"循环点击跳过剧情", **arg)
step.addAction(act)
#action 3
detectRegion = GetRealRegion( 944, 172, 320, 302)
arg = { "detectRegion": detectRegion               ,"imagePattern"  :  "test_btn_zhandou.png",
        "loopWaitingTime": 1                               ,"successNext"  :  ["action","4"],
        "failNext" : ["action","5"]                        ,"failResponse" : "Ignore",
        "loopTime": 1                                       ,"loopType"      :  1}
act = DetectAction(tag = "3", desc = u"检测是否可以开始战斗", **arg)
step.addAction(act)
#action4
detectRegion = GetRealRegion( 944, 172, 320, 302)
arg = { "detectRegion": detectRegion               ,"imagePattern"  :  "test_btn_zhandou.png",
        "loopWaitingTime": 1                       ,"failResponse"  :  "Ignore"              ,
        "next"          :  ["step","step4"]}
act = ClickAction(tag = "4",desc=u"点击开始战斗", **arg)
step.addAction(act)
#action5
detectRegion = GetRealRegion( 931, 99, 210, 373)
arg = { "detectRegion": detectRegion               ,"imagePattern"  :  Pattern("test_choose.png").targetOffset(0,50),
        "loopWaitingTime": 1                       ,"failResponse"  :  "Fail"             ,
        "next"          :  ["action","0.5"]}
act = ClickAction(tag = "5",desc=u"点击继续剧情", **arg)
step.addAction(act)



##########
#Step 4
##########
step = Step("step4",u"开始战斗")
task.addStep(step)

#action0.5
arg =  {"time":3}
act = SleepAction(tag = "0.5", desc= "sleep", **arg)
step.addAction(act)
#action1
arg = { "detectRegion": gl.AREA_ICON_MAP           ,"imagePattern"  :  "icon_map.png",
        "loopWaitingTime": 3                       ,"failResponse"  :  "Fail",
        "loopTime":20                              ,"loopType"      : 1 }
act = DetectAction(tag = "1", desc = u"确认战斗是否结束", **arg)
step.addAction(act)
#action1.5
detectRegion = GetRealRegion( 645, 359, 200, 117)
arg = { "detectRegion": detectRegion               ,"imagePattern"  :  Pattern("test_baoxiang.png").similar(0.80),
        "loopWaitingTime": 3                               ,"successNext"  :  ["action","1.6"],
        "failNext" : ["action","1.9"]                        ,"failResponse" : "Ignore",
        "loopTime":1                                       ,"loopType"      :  1}
act = DetectAction(tag = "1.5", desc = u"检测是否有宝箱", **arg)
step.addAction(act)
#action1.6
detectRegion = GetRealRegion( 645, 359, 200, 117)
arg = { "detectRegion": detectRegion               ,"imagePattern"  :  "test_baoxiang.png",
        "loopWaitingTime": 3                       ,"saveImage":"True"}
act = ClickAction(tag = "1.6",desc=u"点击第三个宝箱", **arg)
step.addAction(act)
#action1.7
arg = { "detectRegion": gl.AREA_BTN_USEITEM               ,"imagePattern"  :  "btn_useitem.png",
        "loopWaitingTime": 3                              ,"successNext"  :  ["action","1.8"],
        "failNext" : ["action","1.9"]                     ,"failResponse" : "Ignore",
        "loopTime":1                                      ,"loopType"      :  1}
act = DetectAction(tag = "1.7", desc = u"检测是否有道具使用提示", **arg)
step.addAction(act)

#action1.8
detectRegion = GetRealRegion(1129, 346,  38,  34)
arg = { "detectRegion": detectRegion                ,"imagePattern"  :  "test_close_item.png",
        "loopWaitingTime": 0                        ,"failResponse"  :  "Ignore"            ,
        "loopRegion": gl.AREA_BTN_USEITEM           ,"loopPattern"   :  "btn_useitem.png",
        "loopTime": 50                              ,"loopType"      :  0                   }
act = ClickAction(tag = "1.8",desc=u"关闭提示使用道具窗口直到窗口消失（并非使用）", **arg)
step.addAction(act)

'''
#action1.9
arg = { "detectRegion": gl.AREA_BTN_SKIPSTORY       ,"imagePattern"  :  "btn_skip_story.png",
        "loopWaitingTime": 1                        ,"failResponse"  :  "Ignore"            ,
        "successNext"  :  ["step","step3"]          ,"failNext"      :  ["action","2"],
        "loopTime": 0                               ,"loopType"      : 1 }
act = DetectAction(tag = "1.9", desc = u"确认副本是否结束(是否直接战斗后进入剧情)", **arg)
step.addAction(act)
'''
#action1.9
detectRegion = GetRealRegion( 989, 164, 148, 352)
arg = { "detectRegion": detectRegion               ,"imagePattern"  :  "test_icon_fuben.png",
        "loopWaitingTime": 3                       ,"failResponse"  :  "Ignore",
        "successNext"  :  ["step","step3"]             ,
        "loopTime":0                               ,"loopType"      : 1 }
act = DetectAction(tag = "1.9", desc = u"确认副本是否结束", **arg)
step.addAction(act)

