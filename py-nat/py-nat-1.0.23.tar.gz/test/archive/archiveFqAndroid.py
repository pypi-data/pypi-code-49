#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/22
# @time: 12:59
# @doc: 财商 * android 脚本
# Copyright © 2019 natloc. All rights reserved.
#


# --- 必选项

APP_NAME = u"小帮规划"
PROJECT_GIT_URL = "https://code.xiaobangtouzi.com/android/xiaobangguihuafq.git"

#QIYE_WECHAT_WEBHOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=309f173d-de7a-4f0a-ba3a-05f01ca7ea8a"  # 财商: 正式
QIYE_WECHAT_WEBHOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=49e78e2a-02a6-4f60-8949-45c026174d21"  # 测试：一个人的群

APK_SCRIPT_PATH = "/Users/xb/.jenkins/workspace/xb-android/buildtools/multi_package_build.sh"

# --- 可选项



















from nat_lib.global_ import nat_global
nat_global.set("APP_NAME", APP_NAME)
nat_global.set("PLATFORM", "android")
nat_global.set("GIT_BRANCH_MODE", "developer")
nat_global.set("PROJECT_GIT_URL", PROJECT_GIT_URL)
nat_global.set("QIYE_WECHAT_WEBHOOK", QIYE_WECHAT_WEBHOOK)
nat_global.set("POD_UPDATE_FQ_RESOURCE", True)
nat_global.set("APK_SCRIPT_PATH", APK_SCRIPT_PATH)


import archive