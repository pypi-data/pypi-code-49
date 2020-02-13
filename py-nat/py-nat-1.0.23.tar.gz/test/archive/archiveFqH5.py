#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/22
# @time: 12:59
# @doc: 财商 * h5 脚本
# Copyright © 2019 natloc. All rights reserved.
#

import utils

# --- 必选项

APP_NAME = u"小帮规划"


#QIYE_WECHAT_WEBHOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=309f173d-de7a-4f0a-ba3a-05f01ca7ea8a"  # 财商: 正式
QIYE_WECHAT_WEBHOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=49e78e2a-02a6-4f60-8949-45c026174d21"  # 测试：一个人的群

MODE_URL_DICT = {
    "qa": "https://app-qa.xiaobangguihua.com/course",
    "staging": "https://app-staging.xiaobangguihua.com/course",
    "production": "https://app.xiaobangguihua.com/course"
}



import nat.cmdOpt
import nat.string
import thd.wechat.group_robot
import nat.log

__parser = nat.cmdOpt.createParser()
__parser.add_argument("--releaseNote", help=u"更新日志", type=str, required=True)
__parser.add_argument("--mode", help=u"模式：qa | staging | production", type=str, required=True)
__args = nat.cmdOpt.genArgs(__parser)

# --- 更新日志内容
__releaseNoteStr = nat.string.trim(__args.releaseNote)
__releaseNote = utils.fillReleaseNotes(__releaseNoteStr.split("\n"))

# --- 模式
__mode = nat.string.trim(__args.mode)
__modeUrl = MODE_URL_DICT.get(__mode, "")
if "" == __modeUrl:
    __mode = "qa"
    __modeUrl = MODE_URL_DICT[__mode]

# --- 发送到微信群
msgMd = thd.wechat.group_robot.MarkdownMessage(QIYE_WECHAT_WEBHOOK)
__modeName = __mode.upper() if "qa" == __mode else __mode.capitalize()
msgMd.append("【提测-H5-%s】" %(__modeName), fragmentCount=3, shouldAppendNewLine=True)
msgMd.append(__releaseNote)
msgMd.append(u"\n👉 %s" %(msgMd.mkLink(u"提测链接", __modeUrl)))
msgMd.send()

msgText = thd.wechat.group_robot.TextMessage(QIYE_WECHAT_WEBHOOK)
msgText.setMentionedAll()
msgText.send()

# --- 完成
nat.log.warn("H5 提测完成")