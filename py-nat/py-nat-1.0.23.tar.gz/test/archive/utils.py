#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc_developer
# @date: 2020/1/2
# @time: 17:14
# @doc:
# Copyright © 2020 natloc_developer. All rights reserved.
#
# 研发面板：
#   11：-> START PROGRESS
#   31：-> TODO
#   71：-> START TEST
# BUG:
#   5：-> RESOVLED
#   3: -> REOPENED
#

from bs4 import BeautifulSoup

import nat.cmd
import nat.log
import nat.datetime
import nat.string


__ACCOUNT_USER = "luxiaolong"
__ACCOUNT_PASSWD = "654321qwerQ"


# 根据 issue code 获取标题
def reqJiraTitle(code):
    jiraUrl = u"http://jira.xiaobangtouzi.com/browse/FQ-%i" %(code)

    cmdStr = u"curl -u %s:%s %s" %(__ACCOUNT_USER, __ACCOUNT_PASSWD, jiraUrl)
    html = nat.cmd.executeRead(cmdStr).read()
    htmlBs = BeautifulSoup(html, "html.parser")
    titleNode = htmlBs.select_one("#summary-val")

    if None != titleNode:
        # 自动完成 issue
        issueId = htmlBs.select_one("#key-val").get("rel", [""])[0]
        
        cookieDict = __reqJiraRespSetCookieDict(code)
        atlToken = cookieDict.get("atlassian.xsrf.token", "")
        jsessionId = cookieDict.get("jsessionid", "")

        if "" != issueId and "" != atlToken and "" != jsessionId:
            __finishIssue(issueId, code, jsessionId, atlToken, __getIssueStatus(htmlBs))

        return titleNode.get_text()
    else:
        return u"FQ-%i" %(code)

# 请求 issue 响应的 Set-Cookie 的值字典
# return {}
def __reqJiraRespSetCookieDict(code):
    jiraUrl = u"http://jira.xiaobangtouzi.com/browse/FQ-%i" % (code)

    cmdStr = u"curl -u %s:%s %s -I" % (__ACCOUNT_USER, __ACCOUNT_PASSWD, jiraUrl)

    cookieDict = {}
    for cookie in nat.cmd.executeRead(cmdStr).readlines():
        splitArr = cookie.split(":")
        if 2 == len(splitArr) and "set-cookie" == splitArr[0].strip().lower():
            splitArr = splitArr[1].split(";")
            if len(splitArr) > 0:
                splitArr = splitArr[0].split("=")
                if 2 == len(splitArr):
                    key = splitArr[0].strip().lower()
                    value = splitArr[1].strip()
                    cookieDict[key] = value

    return cookieDict

# 获取 issue 的状态
# return: string   # 如："open" | "reopened" | "resolved" | "to do" | "in progress" | "in test" | "done"
def __getIssueStatus(htmlBeautifulSoup):
    for li in htmlBeautifulSoup.select_one("#issuedetails").find_all("li"):
        if "status:" == li.strong.get_text().lower():
            return li.select_one("#status-val").span.get_text().lower()

    return ""

# 完成 issue
# return: bool
def __finishIssue(issueId, code, jsessionId, atlToken, status):
    if "to do" == status:
        action = 11
    elif "in progress" == status:
        action = 71
    elif "open" == status or "reopened" == status:
        action = 5
    elif "resolved" == status or "in test" == status:
        return True
    else:
        nat.log.error(u"完成 jira issue 出错，当前状态不正确。issure 编号：%i, 状态: %s" %(code, status))
        return False


    jiraUrl = u"http://jira.xiaobangtouzi.com/secure/WorkflowUIDispatcher.jspa?id=%s&atl_token=%s&action=%i" %(issueId, atlToken, action)

    cmdStr = u"curl -u %s:%s \"%s\" -b \"JSESSIONID=%s; atlassian.xsrf.token=%s\"" %(__ACCOUNT_USER, __ACCOUNT_PASSWD, jiraUrl, jsessionId, atlToken)
    htmlRet = nat.cmd.executeRead(cmdStr).read()
    isSuccess = "" == nat.string.trim(htmlRet)

    if not isSuccess:
        nat.log.error(u"完成 issue 失败，issue 单号：%i" %(code))

    return isSuccess


# 输出耗时
def printArchiveDuration(startTi):
    __costSeconds = int(nat.datetime.getTi() - startTi)
    __costMinutes = __costSeconds / 60
    __costSeconds = __costSeconds % 60
    nat.log.warn(u"完成打包任务，共耗时：%i 分 %i 秒" % (__costMinutes, __costSeconds))


# 同步数据到 QA 集成平台
def syncQualityQA(appName, version, code, branchName, platform, commitId, mode, submitter, downloadUrl):
    __QUALITY_QA_URL = "https://quality-qa.xiaobangtouzi.com/treasure/api/v1/create"
    __QUALITY_QA_HEADER = "Content-Type:application/json"
    __QUALITY_QA_DATA = """{"name": "%s","version_name": "%s", "version": "%s", "branch": "%s", "platform": "%s", "commit_id": "%s", "type": "%s", "submitter": "%s", "created": "%s", "url": "%s"}"""

    quality_qa_data = __QUALITY_QA_DATA %(appName, version, code, branchName, platform, commitId, mode, submitter, nat.datetime.now(), downloadUrl)
    quality_qa_requrest = "curl '%s' -H '%s' -d '%s'" % (__QUALITY_QA_URL, __QUALITY_QA_HEADER, quality_qa_data)

    nat.cmd.execute(quality_qa_requrest)


# 补充完善更新日志行信息
# return string
def fillReleaseNotes(contentLineArr):
    content = u""

    for contentLine in contentLineArr:
        contentLine = contentLine.strip()

        if "" == contentLine:
            continue

        # info 类别：任务
        elif contentLine.startswith("+"):
            contentLine = contentLine[1:].strip()
            try:
                jiraCode = int(contentLine)
                jiraIssueTitle = reqJiraTitle(jiraCode)
                content += u"- **<font color=\"info\">[任务]</font>** [%s](http://jira.xiaobangtouzi.com/browse/FQ-%i)\n" %(jiraIssueTitle, jiraCode)
            except:
                contentLine = contentLine[1:].strip()
                content += u"- **<font color=\"info\">[任务]</font>** %s\n" %(contentLine)

        # warning 类别：bug
        elif contentLine.startswith("-"):
            contentLine = contentLine[1:].strip()
            try:
                jiraCode = int(contentLine)
                jiraIssueTitle = reqJiraTitle(jiraCode)
                content += u"- **<font color=\"warning\">[bug]</font>** [%s](http://jira.xiaobangtouzi.com/browse/FQ-%i)\n" %(jiraIssueTitle, jiraCode)
            except:
                nat.log.exit(u"- 类别必须填写 jira 的单号数字，当前内容错误：%s" %(contentLine))

        # comment 类别：
        elif contentLine.startswith("*"):
            contentLine = contentLine[1:].strip()
            content += u"- **<font color=\"comment\">[备注]</font>** %s\n" %(contentLine)

        # 引用 类别：
        elif contentLine.startswith(">"):
            content += u"%s\n" %(contentLine)

        else:
            content += u"- %s\n" %(contentLine)

    return content