#!/usr/local/bin/python3
# -*- coding: utf8 -*-
#
# @author: natloc
# @date: 2019/10/12
# @time: 13:45
# @doc:
# Copyright © 2019 natloc. All rights reserved.
#

import base64
import hashlib


import nat.path


# 获取文件的 base64
# return: string
def getBase64(path):
    if nat.path.isFile(path):
        fp = open(nat.path.getAbsPath(path), "rb")
        base64Str = base64.b64encode(fp.read()).decode("utf8")
        fp.close()
        return base64Str

    else:
        return ""


# 获取文件的 md5
# return: string
def getMd5(path):
    if nat.path.isFile(path):
        hash = hashlib.md5()
        fp = open(nat.path.getAbsPath(path), "rb")

        while True:
            b = fp.read(8096)
            if not b:
                break
            hash.update(b)

        fp.close()
        return hash.hexdigest()

    else:
        return ""


# 读取文件内容
# return: string
def read(path):
    if nat.path.isFile(path):
        fp = open(nat.path.getAbsPath(path), "r")
        content = fp.read()
        fp.close()
        return content

    else:
        return ""

# 创建空文件
# return: bool
def createEmptyFile(file, contentStr = ""):
    if nat.path.isValidFilePath(file) and not nat.path.isFile(file):
        fp = open(file, "w")
        fp.write(contentStr)
        fp.close()
        return True
    else:
        return False

# 写数据到文件；若文件不存在则新建
# return: bool
def write(dir, filename, contentStr = ""):
    if not nat.path.isDir(dir):
        return False

    elif not nat.path.isValidFilePath(nat.path.join(dir, filename)):
        return False

    else:
        path = nat.path.join(dir, filename)
        fp = open(path, "w")
        fp.write(contentStr)
        fp.close()
        return True
