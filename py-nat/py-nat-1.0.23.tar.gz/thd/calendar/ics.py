#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc_developer
# @date: 2020/1/5
# @time: 10:21
# @doc: 处理 ics 日历文件
# Copyright © 2020 natloc_developer. All rights reserved.
#

import nat.cmd
import nat.net
import nat.string
import nat.log
import nat.datetime

import icalendar


# MARK:- 类
class ICS:
    # MARK:- 私有属性
    __CALENDAR_URL = "https://p12-caldav.icloud.com/published/2"

    __calendarID = ""
    __ical = ""
    __calendar = None


    # MARK:- 初始化

    def __init__(self, calendarID):
        self.__calendarID = nat.string.trim(calendarID)
        if "" == self.__calendarID:
            nat.log.error(u"日历ID为空字符串")



    # MARK:- 成员函数

    # 请求网络日历数据
    def reqIcal(self):
        urlStr = "%s/%s" % (self.__CALENDAR_URL, self.__calendarID)

        try:
            self.__ical = nat.net.reqUrl(urlStr)
            if "" == self.__ical:
                nat.log.error(u"无法请求日历数据")
            else:
                self.__calendar = icalendar.Calendar.from_ical(self.__ical)
        except Exception as err:
            nat.log.error(f"请求日历数据失败：{err}")

        return self



    # 获取所有事件列表
    # return: [Event]
    def getEventList(self):
        eventList = []

        if None != self.__calendar:
            for component in self.__calendar.subcomponents:
                if 'VEVENT' == component.name:
                    eventList.append(component)

        return eventList

    # 获取指定日期的事件列表
    # return: [Event]
    def getEventListByDatetime(self, datetimeObj = nat.datetime.now()):
        eventList = []
        summary = self.getEventSummary(datetimeObj)

        if "" != summary:
            for event in self.getEventList():
                if nat.string.trim(event['summary']) == summary:
                    eventList.append(event)

        return eventList



    # 获取事件的概要
    # return: string
    def getEventSummary(self, datetimeObj = nat.datetime.now()):
        dateInt = nat.datetime.getDateInt(datetimeObj)
        if dateInt > 0:
            for event in self.getEventList():
                startDateInt = nat.datetime.getDateInt(icalendar.vDDDTypes.from_ical(event['dtstart']))
                endDateInt = nat.datetime.getDateInt(icalendar.vDDDTypes.from_ical(event['dtend']))

                if startDateInt <= dateInt and dateInt <= endDateInt:
                    return nat.string.trim(event['summary'])

        return ""



    # 判断是否事件日；只考虑起始和结束的日期，不考虑时间
    # return: bool
    def isEventDay(self, datetimeObj = nat.datetime.now()):
        return "" != self.getEventSummary(datetimeObj)

    # 是否事件的第一天；只考虑起始和结束的日期，不考虑时间
    # return: bool
    def isEventFirstDay(self, datetimeObj = nat.datetime.now()):
        dateInt = nat.datetime.getDateInt(datetimeObj)
        if dateInt > 0:
            lastDayInt = 99999999
            for event in self.getEventListByDatetime(datetimeObj):
                lastDayInt = min(lastDayInt, nat.datetime.getDateInt(icalendar.vDDDTypes.from_ical(event['dtstart'])))

            return dateInt == lastDayInt

        else:
            return False

    # 是否事件的最后一天；只考虑起始和结束的日期，不考虑时间
    # return: bool
    def isEventLastDay(self, datetimeObj = nat.datetime.now()):
        dateInt = nat.datetime.getDateInt(datetimeObj)
        if dateInt > 0:
            lastDayInt = 0
            for event in self.getEventListByDatetime(datetimeObj):
                lastDayInt = max(lastDayInt, nat.datetime.getDateInt(icalendar.vDDDTypes.from_ical(event['dtend'])))

            return dateInt == lastDayInt

        else:
            return False




# MARK:- 小帮规划
class ICS_XiaoBangGuiHua(ICS):
    # MARK:- 私有属性
    __XiaoBangGuiHua_CALENDAR_ID = "MTk1NTE5NTI3NzE5NTUxOZf-83pNOHq6gqW6ycF5AeDNvGxRdUYC-Z5oE7CRAisq"

    def __init__(self):
        super().__init__(self.__XiaoBangGuiHua_CALENDAR_ID)