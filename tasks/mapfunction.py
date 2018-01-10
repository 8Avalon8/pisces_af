# -*- coding: utf-8 -*-
task = Task("mapfunction",desc = u"地图功能")
#task.addSetupActionSet("RefreshGame",tag="pre1",desc="RefreshGame")
#task.addTeardownActionSet("TypeCommand", tag = "12", desc = u"清除背包", mp={'command':'$dropall -1'})
tasksuit.addTask(task)

#Login
step = Step("step0.5", u"登陆")
#step.addActionSet("InputNamePsd", tag = "login", desc = u"输入账号密码", mp={'username':'test06001', 'password':'123456'})
#step.addActionSet("TypeCommand", tag = "0.6", desc = u"清除背包", mp={'command':'$dropall -1'})
task.addStep(step)
#Fail_Handler
step = Step("Fail_Handler", u"模块失败处理")
step.addActionSet("RefreshGame",tag = "pre1", desc = u"刷新游戏客户端")
step.addActionSet("QuickLogin", tag = "quicklogin", desc = u"快速登录")
task.addStep(step)
#PreCheck
#step = Step("step1", u"登陆预处理")
#act1.5
#step.addActionSet("FingerGuide", tag = "1.5", desc = u"处理新手指示手势")
#act1.6
#step.addActionSet("CLoseWindow", tag = "1.6", desc = u"关闭烦人的窗口")
#task.addStep(step)
step = Step("1", u"模块任务开始")
task.addStep(step)
#碧波潭
#action2
arg = { "detectRegion" : GetRegionFromGrid(1, 18),
        "imagePattern" : Pattern("icon_map.PNG"),
        "loopRegion" : gl.AREA_MAP_LUOYANG,
        "loopPattern" : "map_luoyang.png",
        "loopWaitingTime" : 30,
        "failResponse" : "Fail" }
act = ClickAction(tag = "2", desc = u"点击大地图", **arg)
step.addAction(act)
#action3
arg = { "detectRegion" : GetRegionFromGrid(28, 44),
        "imagePattern" : Pattern("bibotan.PNG"),
        "clk_region" : GetRegionFromGrid(28, 44),
        "clk_ptn" : Pattern("bibotan.PNG").targetOffset(-80, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "3", desc = u"点击小地图碧波潭", **arg)
step.addAction(act)
#action4
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("shijieditutubiao.PNG"),
        "clk_region" : gl.R_Screen,
        "clk_ptn" : Pattern("shijieditutubiao.PNG").targetOffset(-150, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "4", desc = u"点击小地图固定位置", **arg)
step.addAction(act)

#黑火深渊
#action5
arg = { "detectRegion" : GetRegionFromGrid(1, 18),
        "imagePattern" : Pattern("icon_map.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : gl.AREA_MAP_LUOYANG,
        "loopPattern" : "map_luoyang.png",
        "loopType" : 1 }
act = ClickAction(tag = "5", desc = u"点击大地图", **arg)
step.addAction(act)
#action6
arg = { "detectRegion" : GetRegionFromGrid(19, 35),
        "imagePattern" : Pattern("heihuoshenyuan.PNG"),
        "clk_region" : GetRegionFromGrid(19, 35),
        "clk_ptn" : Pattern("heihuoshenyuan.PNG").targetOffset(60, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "6", desc = u"点击小地图黑火深渊", **arg)
step.addAction(act)
#action7
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("shijieditutubiao.PNG"),
        "clk_region" : gl.R_Screen,
        "clk_ptn" : Pattern("shijieditutubiao.PNG").targetOffset(-150, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "7", desc = u"点击小地图固定位置", **arg)
step.addAction(act)

#神木林
#action8
arg = { "detectRegion" : GetRegionFromGrid(1, 18),
        "imagePattern" : Pattern("icon_map.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : gl.AREA_MAP_LUOYANG,
        "loopPattern" : "map_luoyang.png",
        "loopType" : 1 }
act = ClickAction(tag = "8", desc = u"点击大地图", **arg)
step.addAction(act)
#action9
arg = { "detectRegion" : GetRegionFromGrid(25, 42),
        "imagePattern" : Pattern("shenmulin.PNG"),
        "clk_region" : GetRegionFromGrid(25, 42),
        "clk_ptn" : Pattern("shenmulin.PNG").targetOffset(-60, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "9", desc = u"点击小地图神木林", **arg)
step.addAction(act)
#action10
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("shijieditutubiao.PNG"),
        "clk_region" : gl.R_Screen,
        "clk_ptn" : Pattern("shijieditutubiao.PNG").targetOffset(-150, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "10", desc = u"点击小地图固定位置", **arg)
step.addAction(act)

#江宁
#action11
arg = { "detectRegion" : GetRegionFromGrid(1, 18),
        "imagePattern" : Pattern("icon_map.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : gl.AREA_MAP_LUOYANG,
        "loopPattern" : "map_luoyang.png",
        "loopType" : 1 }
act = ClickAction(tag = "11", desc = u"点击大地图", **arg)
step.addAction(act)
#action12
arg = { "detectRegion" : GetRegionFromGrid(54, 70),
        "imagePattern" : Pattern("jiangning.PNG"),
        "clk_region" : GetRegionFromGrid(54, 70),
        "clk_ptn" : Pattern("jiangning.PNG").targetOffset(60, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "12", desc = u"点击小地图江宁", **arg)
step.addAction(act)
#action13
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("shijieditutubiao.PNG"),
        "clk_region" : gl.R_Screen,
        "clk_ptn" : Pattern("shijieditutubiao.PNG").targetOffset(-150, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "13", desc = u"点击小地图固定位置", **arg)
step.addAction(act)

#镜湖山
#action14
arg = { "detectRegion" : GetRegionFromGrid(1, 18),
        "imagePattern" : Pattern("icon_map.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : gl.AREA_MAP_LUOYANG,
        "loopPattern" : "map_luoyang.png",
        "loopType" : 1 }
act = ClickAction(tag = "14", desc = u"点击大地图", **arg)
step.addAction(act)
#action15
arg = { "detectRegion" : GetRegionFromGrid(59, 75),
        "imagePattern" : Pattern("jinghushan.PNG"),
        "clk_region" : GetRegionFromGrid(59, 75),
        "clk_ptn" : Pattern("jinghushan.PNG").targetOffset(60, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "15", desc = u"点击小地图镜湖山", **arg)
step.addAction(act)
#action16
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("shijieditutubiao.PNG"),
        "clk_region" : gl.R_Screen,
        "clk_ptn" : Pattern("shijieditutubiao.PNG").targetOffset(-150, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "16", desc = u"点击小地图固定位置", **arg)
step.addAction(act)

#红莲岛
#action17
arg = { "detectRegion" : GetRegionFromGrid(1, 18),
        "imagePattern" : Pattern("icon_map.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : gl.AREA_MAP_LUOYANG,
        "loopPattern" : "map_luoyang.png",
        "loopType" : 1 }
act = ClickAction(tag = "17", desc = u"点击大地图", **arg)
step.addAction(act)
#action18
arg = { "detectRegion" : GetRegionFromGrid(53, 69),
        "imagePattern" : Pattern("hongliandao.PNG"),
        "clk_region" : GetRegionFromGrid(53, 69),
        "clk_ptn" : Pattern("hongliandao.PNG").targetOffset(-60, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "18", desc = u"点击小地图红莲岛", **arg)
step.addAction(act)
#action19
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("shijieditutubiao.PNG"),
        "clk_region" : gl.R_Screen,
        "clk_ptn" : Pattern("shijieditutubiao.PNG").targetOffset(-150, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "19", desc = u"点击小地图固定位置", **arg)
step.addAction(act)

#洛阳
#action20
arg = { "detectRegion" : GetRegionFromGrid(1, 18),
        "imagePattern" : Pattern("icon_map.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : gl.AREA_MAP_LUOYANG,
        "loopPattern" : "map_luoyang.png",
        "loopType" : 1 }
act = ClickAction(tag = "20", desc = u"点击大地图", **arg)
step.addAction(act)
#action21
arg = { "detectRegion" : GetRegionFromGrid(72, 89),
        "imagePattern" : Pattern("luoyang.PNG"),
        "clk_region" : GetRegionFromGrid(72, 89),
        "clk_ptn" : Pattern("luoyang.PNG").targetOffset(60, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "21", desc = u"点击小地图洛阳", **arg)
step.addAction(act)
#action22
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("shijieditutubiao.PNG"),
        "clk_region" : gl.R_Screen,
        "clk_ptn" : Pattern("shijieditutubiao.PNG").targetOffset(-150, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "22", desc = u"点击小地图固定位置", **arg)
step.addAction(act)

#燕子坞
#action23
arg = { "detectRegion" : GetRegionFromGrid(1, 18),
        "imagePattern" : Pattern("icon_map.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : gl.AREA_MAP_LUOYANG,
        "loopPattern" : "map_luoyang.png",
        "loopType" : 1 }
act = ClickAction(tag = "23", desc = u"点击大地图", **arg)
step.addAction(act)
#action24
arg = { "detectRegion" : GetRegionFromGrid(92, 109),
        "imagePattern" : Pattern("yanziwu.PNG"),
        "clk_region" : GetRegionFromGrid(92, 109),
        "clk_ptn" : Pattern("yanziwu.PNG").targetOffset(-60, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "24", desc = u"点击小地图燕子坞", **arg)
step.addAction(act)
#action25
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("shijieditutubiao.PNG"),
        "clk_region" : gl.R_Screen,
        "clk_ptn" : Pattern("shijieditutubiao.PNG").targetOffset(-150, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "25", desc = u"点击小地图固定位置", **arg)
step.addAction(act)

#剑门关
#action26
arg = { "detectRegion" : GetRegionFromGrid(1, 18),
        "imagePattern" : Pattern("icon_map.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : gl.AREA_MAP_LUOYANG,
        "loopPattern" : "map_luoyang.png",
        "loopType" : 1 }
act = ClickAction(tag = "26", desc = u"点击大地图", **arg)
step.addAction(act)
#action27
arg = { "detectRegion" : GetRegionFromGrid(86, 103),
        "imagePattern" : Pattern("jianmenguan.PNG"),
        "clk_region" : GetRegionFromGrid(86, 103),
        "clk_ptn" : Pattern("jianmenguan.PNG").targetOffset(-60, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "27", desc = u"点击小地图剑门关", **arg)
step.addAction(act)
#action28
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("shijieditutubiao.PNG"),
        "clk_region" : gl.R_Screen,
        "clk_ptn" : Pattern("shijieditutubiao.PNG").targetOffset(-150, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "28", desc = u"点击小地图固定位置", **arg)
step.addAction(act)

#轩辕古墓
#action29
arg = { "detectRegion" : GetRegionFromGrid(1, 18),
        "imagePattern" : Pattern("icon_map.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : gl.AREA_MAP_LUOYANG,
        "loopPattern" : "map_luoyang.png",
        "loopType" : 1 }
act = ClickAction(tag = "29", desc = u"点击大地图", **arg)
step.addAction(act)
#action30
arg = { "detectRegion" : GetRegionFromGrid(99, 115),
        "imagePattern" : Pattern("xuanyuangumu.PNG"),
        "clk_region" : GetRegionFromGrid(99, 115),
        "clk_ptn" : Pattern("xuanyuangumu.PNG").targetOffset(60, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "30", desc = u"点击小地图轩辕古墓", **arg)
step.addAction(act)
#action31
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("shijieditutubiao.PNG"),
        "clk_region" : gl.R_Screen,
        "clk_ptn" : Pattern("shijieditutubiao.PNG").targetOffset(-150, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "31", desc = u"点击小地图固定位置", **arg)
step.addAction(act)

#蜀南竹海
#action32
arg = { "detectRegion" : GetRegionFromGrid(1, 18),
        "imagePattern" : Pattern("icon_map.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : gl.AREA_MAP_LUOYANG,
        "loopPattern" : "map_luoyang.png",
        "loopType" : 1 }
act = ClickAction(tag = "32", desc = u"点击大地图", **arg)
step.addAction(act)
#action33
arg = { "detectRegion" : GetRegionFromGrid(105, 121),
        "imagePattern" : Pattern("shunanzhuhai.PNG"),
        "clk_region" : GetRegionFromGrid(105, 121),
        "clk_ptn" : Pattern("shunanzhuhai.PNG").targetOffset(-60, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "33", desc = u"点击小地图蜀南竹海", **arg)
step.addAction(act)
#action34
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("shijieditutubiao.PNG"),
        "clk_region" : gl.R_Screen,
        "clk_ptn" : Pattern("shijieditutubiao.PNG").targetOffset(-150, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "34", desc = u"点击小地图固定位置", **arg)
step.addAction(act)

#青云村
#action35
arg = { "detectRegion" : GetRegionFromGrid(1, 18),
        "imagePattern" : Pattern("icon_map.PNG"),
        "loopWaitingTime" : 5,
        "failResponse" : "Fail",
        "loopTime" : 3,
        "loopRegion" : gl.AREA_MAP_LUOYANG,
        "loopPattern" : "map_luoyang.png",
        "loopType" : 1 }
act = ClickAction(tag = "35", desc = u"点击大地图", **arg)
step.addAction(act)
#action36
arg = { "detectRegion" : GetRegionFromGrid(106, 123),
        "imagePattern" : Pattern("qingyuncun.PNG"),
        "clk_region" : GetRegionFromGrid(106, 123),
        "clk_ptn" : Pattern("qingyuncun.PNG").targetOffset(60, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "36", desc = u"点击小地图青云村", **arg)
step.addAction(act)
#action37
arg = { "detectRegion" : gl.R_Screen,
        "imagePattern" : Pattern("shijieditutubiao.PNG"),
        "clk_region" : gl.R_Screen,
        "clk_ptn" : Pattern("shijieditutubiao.PNG").targetOffset(-150, 0),
        "loopWaitingTime" : 3,
        "failResponse" : "Fail" }
act = ClickAction(tag = "37", desc = u"点击小地图固定位置", **arg)
step.addAction(act)
#action模块结束等待
arg = { "time" : 5 }
act = SleepAction(tag = "end", desc = u"模块结束等待", **arg)
step.addAction(act)