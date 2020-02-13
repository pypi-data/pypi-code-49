#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/22
# @time: 12:59
# @doc: 财商 * iOS 脚本
# Copyright © 2019 natloc. All rights reserved.
#


# --- 必选项

APP_NAME = u"小帮保险"
PROJECT_GIT_URL = "https://code.xiaobangtouzi.com/ios/XiaoBangInsuranceProject.git"

TEAM_ID = "PWA4SBB7ND"
BUNDLE_ID = "com.xiaobang.insurance"

CERTIFICATE_INFO_ADHOC = ("Apple Distribution", "service_addHoc")   # 保险：正式

#QIYE_WECHAT_WEBHOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a40ffd66-aef9-491f-a338-091764b9edbb"  # 保险: 正式
QIYE_WECHAT_WEBHOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=49e78e2a-02a6-4f60-8949-45c026174d21"  # 测试：一个人的群



# --- 可选项

# 可选：发布到 appstore 时必须设置
ITC_API_KEY = ""
ITC_ISSUER_ID = ""

# 可选：发布到 appstore 时必须设置
CERTIFICATE_INFO_APPSTORE = ("Apple Distribution", "service_appStore")   # 保险：正式

# 可选：生成的二维码的背景图
QRCODE_BG_PNG_PATH = "/Users/xb/Documents/ios/fq/qrcode-bg.png"
QRCODE_BG_STANDBY_PNG_PATH = "/Users/xb/Documents/ios/fq/qrcode-bg-standby.png"


















from nat_lib.global_ import nat_global
nat_global.set("APP_NAME", APP_NAME)
nat_global.set("PLATFORM", "ios")
nat_global.set("GIT_BRANCH_MODE", "develop")
nat_global.set("PROJECT_GIT_URL", PROJECT_GIT_URL)
nat_global.set("TEAM_ID", TEAM_ID)
nat_global.set("BUNDLE_ID", BUNDLE_ID)
nat_global.set("ITC_API_KEY", ITC_API_KEY)
nat_global.set("ITC_ISSUER_ID", ITC_ISSUER_ID)
nat_global.set("CERTIFICATE_INFO_ADHOC", CERTIFICATE_INFO_ADHOC)
nat_global.set("CERTIFICATE_INFO_APPSTORE", CERTIFICATE_INFO_APPSTORE)
nat_global.set("QIYE_WECHAT_WEBHOOK", QIYE_WECHAT_WEBHOOK)
nat_global.set("QRCODE_BG_PNG_PATH", QRCODE_BG_PNG_PATH)
nat_global.set("QRCODE_BG_STANDBY_PNG_PATH", QRCODE_BG_STANDBY_PNG_PATH)


import archive