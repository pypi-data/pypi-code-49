#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019-10-12
# @time: 00:22
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import nat.cmd
import nat.log
import nat.path
import nat.string


class Generator:
    __CMD_MYQR = "myqr"
    __DEFAULT_SUFFIX = "png"
    __ITMS_SERVICES_PREFIX = "itms-services://?action=download-manifest&url="



    # 生成的二维码图片的存放地址；为 空字符串 则表示使用执行脚本所在的目录
    __destDirPath = ""

    # 生成的二维码图片的 basename
    __destBasename = ""

    # 生成的二维码图片的后缀，默认是 png
    __destSuffix = "png"

    # 用于生成二维码的链接
    __url = ""

    # 用于背景图片的文件路径
    __bgImgPath = ""



    # 设置二维码图片的生成目录路径
    def setDestDirPath(self, path):
        self.__destDirPath = path.strip()

    # 设置二维码图片的 basename
    def setDestBasename(self, basename):
        self.__destBasename = basename.strip()

    # 设置二维码图片的后缀；默认是：png
    def setDestSuffix(self, suffix):
        if None == suffix or "" == suffix.strip():
            self.__destSuffix = self.__DEFAULT_SUFFIX
        else:
            self.__destSuffix = suffix.strip()

    # 设置的下载链接地址
    # param: url   # 若是 itmsServices 下载，则需填写 manifest.plist 的下载地址
    def setUrl(self, url, isItmsServices = False):
        self.__url = url.strip()

        if isItmsServices and "" != self.__url:
            self.__url = "%s%s" %(self.__ITMS_SERVICES_PREFIX, self.__url)

    # 设置背景图片
    def setBgImgPath(self, imgPath):
        imgPath = nat.string.trim(imgPath)
        if nat.path.isFile(imgPath):
            self.__bgImgPath = nat.path.getAbsPath(imgPath)

    # 获取二维码图片的路径
    # return: string
    def getQrPath(self):
        dirPath = nat.path.getAbsPath(self.__destDirPath)
        filename = "%s.%s" %(self.__destBasename, self.__destSuffix)
        return nat.path.join(dirPath, filename)


    # 生成二维码图片
    # return bool
    def generate(self):
        if not nat.cmd.installPipDep(self.__CMD_MYQR):
            return False

        elif not nat.path.isDir(self.__destDirPath):
            nat.log.error(u"生成二维码图片失败，目录不存在：%s" %(self.__destDirPath))
            return False

        elif "" == self.__destBasename:
            nat.log.error(u"生成二维码图片失败，文件名不合法：%s" %(self.__destBasename))
            return False

        elif "" == self.__url:
            nat.log.error(u"生成二维码图片失败，url 不合法：%s" %(self.__url))
            return False

        else:
            dirPath = nat.path.getAbsPath(self.__destDirPath)
            filename = "%s.%s" %(self.__destBasename, self.__destSuffix)

            bgImgOpts = ""
            if "" != self.__bgImgPath:
                bgImgOpts = " -p %s -c " %(self.__bgImgPath)

            cmdStr = "myqr -d %s -n %s %s \"%s\"" %(dirPath, filename, bgImgOpts, self.__url)
            nat.log.warn(u"生成二维码的地址：%s" %(self.__url))

            return nat.cmd.execute(cmdStr) and nat.path.isFile(self.getQrPath())