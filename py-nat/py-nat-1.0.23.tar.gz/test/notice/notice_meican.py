#!/usr/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc_developer
# @date: 2019/12/29
# @time: 21:42
# @doc: 美餐通知
# Copyright © 2019 natloc_developer. All rights reserved.
#


from thd.calendar.ics import ICS_XiaoBangGuiHua
import nat.datetime

if ICS_XiaoBangGuiHua().reqIcal().isEventDay():
	import thd.wechat.group_robot
	
	__WEB_HOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=eabcee36-cfc3-4661-b027-9de1e5f9de58"
	#__WEB_HOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=49e78e2a-02a6-4f60-8949-45c026174d21" # 测试
	__LOGIN_URL = "meican://home"
	__LOGO_URL = "https://www.meican.com/favicon.ico"


	newsMsg = thd.wechat.group_robot.NewsMessage(__WEB_HOOK)
	newsMsg.appendNews(u"美餐下单提示", "", __LOGIN_URL, "")
	#newsMsg.send()

	txtMsg = thd.wechat.group_robot.TextMessage(__WEB_HOOK)
	txtMsg.setContent(u"%s，你点了没？" %(u"午餐" if nat.datetime.now().hour <= 12 else u"晚餐"))
	txtMsg.setMentionedAll()
	txtMsg.send()
