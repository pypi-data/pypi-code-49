#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019-10-18
# @time: 22:50
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import nat.log
import nat.cmd


cmdPillow = "Pillow"
if not nat.cmd.hasInstalledPipDep(cmdPillow) and not nat.cmd.installPipDep(cmdPillow, True):
    nat.log.error(u"安装 %s 失败" %(cmdPillow))


from PIL import Image
import nat.path
import nat.string


class NatImage:

    __img = None
    __imgFile = ""

    def __init__(self, imgFile):
        imgFile = nat.path.getAbsPath(imgFile)
        if nat.path.isFile(imgFile):
            self.__img = Image.open(imgFile)

        self.__imgFile = imgFile
        if None == self.__img:
            nat.log.error(u"加载图片文件失败: %s" %(imgFile))


    # 判断是否有效的图片
    def isAvail(self):
        return None != self.__img

    # 获取图像
    def getImg(self):
        return self.__img



    # MARK:- 宽高

    # 获取宽度
    # return: int
    def getWidth(self):
        return self.__img.size[0]

    # 获取高度
    # return: int
    def getHeight(self):
        return self.__img.size[1]


    # 设置宽度
    # return: bool
    def setWidth(self, widthInt, isAspect = False):
        if widthInt <= 0:
            return False

        elif self.getWidth() == widthInt:
            if isAspect:
                return self.setHeight(widthInt)
            else:
                return True

        else:
            heightInt = self.getHeight()
            self.__img = self.__img.resize((widthInt, heightInt), Image.ANTIALIAS)

            if isAspect:
                return self.setHeight(widthInt)
            else:
                return True

    # 设置高度
    # return: bool
    def setHeight(self, heightInt, isAspect = False):
        if heightInt <= 0:
            return False

        elif self.getHeight() == heightInt:
            if isAspect:
                return self.setWidth(heightInt)
            else:
                return True

        else:
            widthInt = self.getWidth()
            self.__img = self.__img.resize((widthInt, heightInt), Image.ANTIALIAS)

            if isAspect:
                return self.setWidth(heightInt)
            else:
                return True




    # 开启颜色模式
    def setRGBA(self):
        if None != self.__img:
            self.__img = self.__img.convert("RGBA")

        return self


    # 在当前图片上粘贴另一张图片
    def pasteImg(self, aboveImg, offsetX = 0, offsetY = 0):
        if None != aboveImg and aboveImg.isAvail() and self.isAvail():
            self.__img.paste(aboveImg.getImg(), (offsetX, offsetY))

        return self



    # MARK:- 保存

    # 保存图片：覆盖自身
    # return: bool
    def save(self):
        filename = nat.path.getFilename(self.__imgFile)
        return self.saveWithNewName(filename)

    # 保存图片：新图片所在的路径与源图片相同
    # return: bool
    def saveWithNewName(self, newFilename):
        newFilename = nat.string.trim(newFilename)
        if "" == newFilename:
            return False

        dir = nat.path.getDirPath(self.__imgFile)
        newPath = nat.path.join(dir, newFilename)
        return self.saveWithNewPath(newPath)

    # 保存图片到新目录
    # return: bool
    def saveWithNewDir(self, newDir):
        newDir = nat.string.trim(newDir)
        if not nat.path.isDir(newDir) and not nat.path.mkDirRecursive(newDir):
            return False

        filename = nat.path.getFilename(self.__imgFile)
        newPath = nat.path.join(newDir, filename)
        return self.saveWithNewPath(newPath)

    # 保存图片到新路径
    # return: bool
    def saveWithNewPath(self, newPath):
        newPath = nat.string.trim(newPath)
        if not nat.path.isValidFilePath(newPath):
            return False
        else:
            self.__img.save(newPath)
            return True












