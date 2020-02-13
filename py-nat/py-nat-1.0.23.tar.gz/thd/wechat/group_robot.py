#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/12
# @time: 11:20
# @doc: 企业微信群机器人
# Copyright © 2019 natloc. All rights reserved.
#
# 文档：https://work.weixin.qq.com/api/doc?notreplace=true&version=2.8.10.6069&platform=mac#90000/90136/91770
#


import nat.string
import nat.json
import nat.cmd
import nat.path
import nat.log
import nat.file
import nat.phone


# 基础消息
class __Message(object):

    __HTTP_HEADER_CONTENT_TYPE = "Content-Type: application/json"
    _ERROR_MSG_PREFIX = u"企业微信群机器人 * "

    # 机器人的地址
    __webHookUrl = ""


    def __init__(self, webHookUrl):
        self.__webHookUrl = nat.string.trim(webHookUrl)

        if "" == self.__webHookUrl:
            nat.log.error(u"%s实例化失败：机器人的 webhook 地址为空字符串" %(self._ERROR_MSG_PREFIX))


    # 发送消息
    # param: msgType :: string
    # param: jsonData :: json
    # return: bool
    def _send(self, msgType, jsonDict):
        argMsgType = nat.string.trim(msgType)

        if "" == self.__webHookUrl:
            nat.log.error(u"%s发送消息失败：机器人的 webhook 地址为空字符串" %(self._ERROR_MSG_PREFIX))
            return False

        elif "" == argMsgType:
            nat.log.error(u"%s发送消息失败：消息类型错误" %(self._ERROR_MSG_PREFIX))
            return False

        elif not isinstance(jsonDict, dict):
            nat.log.error(u"%s发送消息失败：消息内容类型错误" %(self._ERROR_MSG_PREFIX))
            return False

        else:
            msgJson = {}
            msgJson["msgtype"] = msgType
            msgJson[msgType] = jsonDict

            jsonStr = nat.json.json2str(msgJson)
            cmdStr = "curl %s -H '%s' -d '%s'" %(self.__webHookUrl, self.__HTTP_HEADER_CONTENT_TYPE, jsonStr)
            return nat.cmd.execute(cmdStr)



# text 消息
class TextMessage(__Message):

    __KEY_CONTENT = "content"
    __KEY_MENTIONED_LIST = "mentioned_list"
    __KEY_MENTIONED_MOBILE_LIST = "mentioned_mobile_list"

    # 消息数据
    __msgJson = {}


    # 设置消息内容
    def setContent(self, contentStr):
        self.__msgJson[self.__KEY_CONTENT] = nat.string.trim(contentStr)
        return self


    # 设置提醒所有人
    def setMentionedAll(self):
        self.__msgJson[self.__KEY_MENTIONED_LIST] = ["@all"]
        self.__msgJson[self.__KEY_MENTIONED_MOBILE_LIST] = []
        return self


    # 追加提醒人的 ID
    # param: userId :: string   # 如："lilei"
    # return: bool
    def appendMentionedUser(self, userId):
        argUserId = nat.string.trim(userId)
        if "" == argUserId:
            nat.log.error(u"%s添加提醒人的 ID 失败：用户 ID 为空字符串" %(self._ERROR_MSG_PREFIX))
            return self

        else:
            mentionedList = self.__msgJson.get(self.__KEY_MENTIONED_LIST, [])

            if 1 == len(mentionedList) and "@all" == mentionedList[0]:
                mentionedList = []

            for uid in mentionedList:
                if uid == argUserId:
                    return True

            mentionedList.append(argUserId)
            self.__msgJson[self.__KEY_MENTIONED_LIST] = mentionedList
            return self


    # 追加提醒人的 手机号
    # return: bool
    def appendMentionedPhone(self, phoneNumStr):
        argPhoneNumStr = nat.string.trim(phoneNumStr)
        if not nat.phone.isValid(argPhoneNumStr):
            nat.log.error(u"%s添加提醒人的 手机号 失败：手机号不合法 %s" %(self._ERROR_MSG_PREFIX, argPhoneNumStr))
            return self

        else:
            mentionedList = self.__msgJson.get(self.__KEY_MENTIONED_LIST, [])
            if 1 == len(mentionedList) and "@all" == mentionedList[0]:
                self.__msgJson[self.__KEY_MENTIONED_LIST] = []


            mentionedMobileList = self.__msgJson.get(self.__KEY_MENTIONED_MOBILE_LIST, [])
            for phone in mentionedMobileList:
                if phone == argPhoneNumStr:
                    return True

            mentionedMobileList.append(argPhoneNumStr)

            self.__msgJson[self.__KEY_MENTIONED_MOBILE_LIST] = mentionedMobileList

            return self


    # 发送消息
    # return: bool
    def send(self):
        contentStr = self.__msgJson.get(self.__KEY_CONTENT, "").strip()
        mentionedUserIdList = self.__msgJson.get(self.__KEY_MENTIONED_LIST, [])
        mentionedPhoneList = self.__msgJson.get(self.__KEY_MENTIONED_MOBILE_LIST, [])
        if "" == contentStr and [] == mentionedPhoneList and [] == mentionedUserIdList:
            nat.log.warn(u"%s发送消息失败：取消发送无意义的内容" %(self._ERROR_MSG_PREFIX))
            return

        else:
            return self._send("text", self.__msgJson)



# markdown 消息
class MarkdownMessage(__Message):

    __KEY_CONTENT = "content"
    __DEFAULT_HEAD_SIZE = 3

    # 消息数据
    __msgJson = {}

    # 内容文本
    __content = ""



    # 设置链接
    def mkLink(self, contentStr, urlStr):
        argContentStr = nat.string.trim(contentStr)
        argUrlStr = nat.string.trim(urlStr)

        if "" == argContentStr:
            return ""

        elif "" == argUrlStr:
            return contentStr

        else:
            return u"[%s](%s)" %(argContentStr, argUrlStr)




    # 添加绿色文本
    # return: string
    def mkColorGreen(self, contentStr):
        return self.__mkTextColor("info", contentStr)

    # 添加橙色文本
    # return: string
    def mkColorOrange(self, contentStr):
        return self.__mkTextColor("warning", contentStr)

    # 添加灰色文本
    # return: string
    def mkColorGray(self, contentStr):
        return self.__mkTextColor("comment", contentStr)

    # return: string
    def __mkTextColor(self, typeStr, contentStr):
        if "" == contentStr:
            return ""
        else:
            return u"<font color=\"%s\">%s</font>" %(typeStr, contentStr)



    # 追加字符串
    def append(self, contentStr, isBold = False, isQuote = False, fragmentCount = 0, shouldAppendNewLine = False):
        if nat.string.isNotEmpty(contentStr):

            # 粗体
            if isBold:
                contentStr = "**%s**" %(contentStr)

            # 引用
            if isQuote:
                contentStr = "> %s" %(contentStr)

            # 标题
            fragmentCount = min(6, max(0, fragmentCount))
            fragPrefix = ""
            for _ in range(0, fragmentCount):
                fragPrefix += "#"
            if "" != fragPrefix:
                contentStr = "%s %s" %(fragPrefix, contentStr)

            # 换行
            if shouldAppendNewLine:
                contentStr = "%s\n" %(contentStr)

            self.__content += contentStr

        return self



    # 发送消息
    # return: bool
    def send(self):
        contentStr = nat.string.trim(self.__content)
        if "" == contentStr:
            nat.log.warn(u"%s发送 md 消息失败：取消发送无意义的内容" %(self._ERROR_MSG_PREFIX))
            return

        else:
            self.__msgJson[self.__KEY_CONTENT] = contentStr
            return self._send("markdown", self.__msgJson)



# image 消息
class ImageMessage(__Message):

    __KEY_BASE_64 = "base64"
    __KEY_MD_5 = "md5"

    # 消息数据
    __msgJson = {}

    # 要发送的图片地址
    __imgPath = ""


    # 设置图片；仅支持 png | jpg 格式，且 <= 2M
    # return: bool
    def setImg(self, path):
        if not nat.path.isFile(path):
            nat.log.error(u"%s设置图片失败：文件不存在：%s" %(self._ERROR_MSG_PREFIX, path))
            return False

        suffixWithDot = nat.path.getFileSuffixWithDot(path)
        if ".png" != suffixWithDot and ".jpg" != suffixWithDot and ".jpeg" != suffixWithDot:
            nat.log.error(u"%s设置图片失败：不支持的图片格式：%s" %(self._ERROR_MSG_PREFIX, suffixWithDot))
            return False

        self.__imgPath = nat.path.getAbsPath(path)
        return True


    # 发送消息
    # return: bool
    def send(self):
        if not nat.path.isFile(self.__imgPath):
            nat.log.warn(u"%s发送消息失败：未设置要发送的图片" %(self._ERROR_MSG_PREFIX))
            return False


        base64Str = nat.file.getBase64(self.__imgPath)
        md5Str = nat.file.getMd5(self.__imgPath)
        if "" == base64Str or "" == md5Str:
            nat.log.warn(u"%s发送消息失败：图片解析失败" %(self._ERROR_MSG_PREFIX))
            return

        else:
            self.__msgJson[self.__KEY_BASE_64] = base64Str
            self.__msgJson[self.__KEY_MD_5] = md5Str
            return self._send("image", self.__msgJson)



# news 消息
class NewsMessage(__Message):

    __KEY_ARTICLES = "articles"
    __KEY_TITLE = "title"
    __KEY_DESC = "description"
    __KEY_URL = "url"
    __KEY_PIC_URL = "picurl"


    # 消息数据
    __msgJson = {}

    __MAX_NEWS_COUNT = 8


    # 添加一条新闻
    def appendNews(self, title, desc, url, picUrl):
        newsList = self.__msgJson.get(self.__KEY_ARTICLES, [])

        if len(newsList) >= self.__MAX_NEWS_COUNT:
            nat.log.error(u"%s添加新闻消息失败：已达最大新闻数量" %(self._ERROR_MSG_PREFIX))
            return False

        argTitle = nat.string.trim(title)
        argDesc = nat.string.trim(desc)
        argUrl = nat.string.trim(url)
        argPicUrl = nat.string.trim(picUrl)

        if "" == argTitle:
            nat.log.error(u"%s添加新闻消息失败：标题为空，链接：%s" %(self._ERROR_MSG_PREFIX, argUrl))
            return False
        elif "" == argUrl:
            nat.log.error(u"%s添加新闻消息失败：链接为空，标题：%s" %(self._ERROR_MSG_PREFIX, argTitle))
            return False
        else:
            news = {}
            news[self.__KEY_TITLE] = argTitle
            news[self.__KEY_DESC] = argDesc
            news[self.__KEY_URL] = argUrl
            news[self.__KEY_PIC_URL] = argPicUrl

            newsList.append(news)
            self.__msgJson[self.__KEY_ARTICLES] = newsList
            return True


    # 发送消息
    # return: bool
    def send(self):
        if 0 == len(self.__msgJson.get(self.__KEY_ARTICLES, [])):
            nat.log.warn(u"%s发送 md 消息失败：取消发送无意义的内容" %(self._ERROR_MSG_PREFIX))
            return

        else:
            return self._send("news", self.__msgJson)












