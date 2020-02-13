#!/usr/bin/python
# -*- coding: utf8 -*-
#
# @author: natloc_developer
# @date: 2019/12/29
# @time: 21:32
# @doc: 通知更新迭代信息
# Copyright © 2019 natloc_developer. All rights reserved.
#
#
# 更新日期：
#   迭代第2周的周五

from thd.calendar.ics import ICS_XiaoBangGuiHua

if ICS_XiaoBangGuiHua().reqIcal().isEventLastDay():
	import thd.wechat.group_robot

	__WEB_HOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=309f173d-de7a-4f0a-ba3a-05f01ca7ea8a"  # 财商: 正式
	# __WEB_HOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=49e78e2a-02a6-4f60-8949-45c026174d21" # 测试

	robot = thd.wechat.group_robot.TextMessage(__WEB_HOOK)
	robot.setContent("请将本迭代的更新内容、截图到迭代文档的评论区")
	robot.appendMentionedUser("lijing")
	robot.send()
