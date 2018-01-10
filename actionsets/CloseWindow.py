# -*- coding: utf-8 -*-

acts = ActionSet(tag = tag,desc = desc)
#step.addAction(acts)
#action 1.1
arg = { "detectRegion": gl.AREA_ICON_NEWS           ,"imagePattern"  :  "news.png",
        "clk_region"  : gl.AREA_BTN_CLOSENEWS       ,"clk_ptn"       :  "btn_close_news.png",
        "loopWaitingTime": 0                        ,"failResponse"  :  "Ignore"            ,
        "loopTime" : 2                              ,"loopType"      :  0}
act = ClickAction(tag = "1.1",desc="Close News", **arg)
acts.addAction(act)

#action 1.2
arg = { "detectRegion": gl.AREA_ICON_WELFARECENTER  ,"imagePattern"  :  "welfare_center.png",
        "clk_region"  : gl.AREA_BTN_WELFARECENTER   ,"clk_ptn"       :  "btn_close_welfare_center.png",
        "loopWaitingTime": 0                        ,"failResponse"  :  "Ignore",
        "loopTime" : 2                              ,"loopType"      :  0}
act = ClickAction(tag = "1.2",desc="Close WelfareCenter", **arg)
acts.addAction(act)
#action 1.3
arg = { "detectRegion": gl.AREA_BTN_GOACTIVITY      ,"imagePattern"  :  "btn_close_activity.png",
        "loopWaitingTime": 0                        ,"failResponse"  :  "Ignore",
        "loopTime" : 2                              ,"loopType"      :  0}
act = ClickAction(tag = "1.3",desc="Close Go-Activity Window", **arg)
acts.addAction(act)