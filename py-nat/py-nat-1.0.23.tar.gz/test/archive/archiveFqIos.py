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

APP_NAME = u"小帮规划"
PROJECT_GIT_URL = "https://code.xiaobangtouzi.com/ios/fq.git"

TEAM_ID = "HZHJKZ6BK5"
BUNDLE_ID = "com.xiaobang.fq"

CERTIFICATE_INFO_ADHOC = ("Apple Distribution", u"fq - 发布证书 - AdHoc")   # 财商：正式
EXTRA_ADHOC_BUNDLEID_PROVISION_LIST = [("com.xiaobang.fq.FQServiceExtension", u"fq - 推送扩展 - AdHoc")]

QIYE_WECHAT_WEBHOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=309f173d-de7a-4f0a-ba3a-05f01ca7ea8a"  # 财商: 正式
#QIYE_WECHAT_WEBHOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=49e78e2a-02a6-4f60-8949-45c026174d21"  # 测试：一个人的群



# --- 可选项

# 可选：发布到 appstore 时必须设置
ITC_API_KEY = "7J4N7BQFCM"
ITC_ISSUER_ID = "811e5f14-7529-4416-98ce-2355e3f0b9e1"

# 可选：发布到 appstore 时必须设置
CERTIFICATE_INFO_APPSTORE = ("Apple Distribution", u"fq - 发布证书 - AppStore")   # 财商：正式
EXTRA_APPSTORE_BUNDLEID_PROVISION_LIST = [("com.xiaobang.fq.FQServiceExtension", u"fq - 推送扩展 - AppStore")]

# 可选：生成的二维码的背景图
QRCODE_BG_PNG_PATH = "/Users/xb/Documents/ios/fq/qrcode-bg.png"
QRCODE_BG_STANDBY_PNG_PATH = "/Users/xb/Documents/ios/fq/qrcode-bg-standby.png"
APP_LOGO_FILE = "/Users/xb/Documents/ios/fq/qrcode-logo.png"


















import nat.global_
nat.global_.set("APP_NAME", APP_NAME)
nat.global_.set("APP_LOGO_FILE", APP_LOGO_FILE)
nat.global_.set("PLATFORM", "ios")
nat.global_.set("PROJECT_GIT_URL", PROJECT_GIT_URL)
nat.global_.set("TEAM_ID", TEAM_ID)
nat.global_.set("BUNDLE_ID", BUNDLE_ID)
nat.global_.set("ITC_API_KEY", ITC_API_KEY)
nat.global_.set("ITC_ISSUER_ID", ITC_ISSUER_ID)
nat.global_.set("CERTIFICATE_INFO_ADHOC", CERTIFICATE_INFO_ADHOC)
nat.global_.set("EXTRA_ADHOC_BUNDLEID_PROVISION_LIST", EXTRA_ADHOC_BUNDLEID_PROVISION_LIST)
nat.global_.set("CERTIFICATE_INFO_APPSTORE", CERTIFICATE_INFO_APPSTORE)
nat.global_.set("EXTRA_APPSTORE_BUNDLEID_PROVISION_LIST", EXTRA_APPSTORE_BUNDLEID_PROVISION_LIST)
nat.global_.set("QIYE_WECHAT_WEBHOOK", QIYE_WECHAT_WEBHOOK)
nat.global_.set("QRCODE_BG_PNG_PATH", QRCODE_BG_PNG_PATH)
nat.global_.set("QRCODE_BG_STANDBY_PNG_PATH", QRCODE_BG_STANDBY_PNG_PATH)
nat.global_.set("POD_UPDATE_FQ_RESOURCE", True)


import archive