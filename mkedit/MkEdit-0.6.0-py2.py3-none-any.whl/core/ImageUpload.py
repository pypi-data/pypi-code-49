#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty
import typing
import os
import logging
import time
import rx
import requests
import shutil
from qiniu import Auth, put_file
from PIL import Image, ImageDraw
import sys
import json
from PySide2.QtCore import QMimeData
from PySide2.QtGui import QImage

import tinify


def fileNameGenerate(originName) -> str:
    suffix = os.path.splitext(originName)[-1]
    today = time.strftime("%Y%m%d%H%M%S", time.localtime())
    newFileName = "%s_%s" % (today, originName)
    print("new file name: %s" % newFileName)
    return newFileName


def getProjectPath():
    return os.path.dirname(sys.argv[0])


class Strategy(metaclass=ABCMeta):

    def __init__(self):
        self.supportSuffixs = None
        self.saveDirPath = "cacheTemp"
        self.defaultSupportSuffixs: typing.List = ['.jpg', '.png', '.jpeg', '.gif', '.svg', '.bmp', '.webp']
        self.textWatermark = None
        self.tinifyAppKey = None

    def save(self, imageSrc: str = None) -> typing.Any:
        if not os.path.isfile(imageSrc):
            printError("imageSrc must is image file")
            return None
        baseFileName = os.path.basename(imageSrc)
        suffix = os.path.splitext(baseFileName)[-1]
        if str(suffix).lower() not in self.supportSuffixs:
            printError("current setting is not support for image's type of suffix :%s " % suffix)
            return None
        newFileName = fileNameGenerate(baseFileName)
        savePath = os.path.join(self.saveDirPath, newFileName)
        shutil.copyfile(imageSrc, savePath)
        # 1、压缩处理
        if self.tinifyAppKey:
            savePath = self.processCompression(savePath)

        # 2、水印处理
        if self.textWatermark:
            savePath = self.processWatermark(savePath)
        # 3、开始上传
        result, error = self.startSave(savePath)
        os.remove(savePath)
        if result:
            return {'code': 'success', 'data': result}
        else:
            return {'code': 'error', 'msg': error}

    def processCompression(self, imgStr: str) -> str:
        tinify.key = self.tinifyAppKey
        source = tinify.from_file(imgStr)
        source.to_file(imgStr)
        return imgStr

    def processWatermark(self, imgStr: str) -> str:
        return self.addTextToImage(imgStr, self.textWatermark)

    def addTextToImage(self, imgSrc, text) -> str:
        # font = ImageFont.load("simsun.pil")
        # font = ImageFont.truetype("simsun.ttc", 40, encoding="unic")  # 设置字体
        type = ""
        type_value = None
        if str(os.path.splitext(imgSrc)[-1]).lower() in [".jpeg", '.jpg']:
            image = Image.open(imgSrc)
            print(os.path.splitext(imgSrc)[0])
            os.remove(imgSrc)
            imgSrc = imgSrc.replace(os.path.splitext(imgSrc)[-1], ".png")
            image.save(imgSrc)

        image = Image.open(imgSrc)

        type = "RGBA"
        type_value = (255, 255, 255, 0)

        rgba_image = image.convert(type)
        text_overlay = Image.new(type, rgba_image.size, type_value)
        image_draw = ImageDraw.Draw(text_overlay)

        text_size_x, text_size_y = image_draw.textsize(text)
        # 设置文本文字位置
        print(rgba_image)
        text_xy = (rgba_image.size[0] - text_size_x - 8, rgba_image.size[1] - text_size_y - 10)
        # 设置文本颜色和透明度
        image_draw.text(text_xy, text, fill=(76, 234, 124))

        image_with_text = Image.alpha_composite(rgba_image, text_overlay)
        image_with_text.save(imgSrc)
        return imgSrc

    @abstractmethod
    def startSave(self, imageSrc: str = None) -> typing.Any:
        pass

    @abstractmethod
    def initSetting(self, param: dict = None) -> typing.Any:
        if 'tempCache' in param.keys():
            self.saveDirPath = param["tempCache"]
        else:
            self.saveDirPath = os.path.join(getProjectPath(), self.saveDirPath)
        if not os.path.exists(self.saveDirPath):
            os.mkdir(self.saveDirPath)

        if 'supportSuffixs' in param.keys():
            self.supportSuffixs = param["supportSuffixs"]
        else:
            self.supportSuffixs = self.defaultSupportSuffixs

        if 'textWatermark' in param.keys():
            self.textWatermark = param['textWatermark']

        if 'tinifyAppKey' in param.keys():
            self.tinifyAppKey = param['tinifyAppKey']
        self.init = True


def printError(msg: str = ""):
    logging.error("%s | %s " % ("ImageLocalSaveStrategy", msg))


class ImageQiniuSaveStrategy(Strategy):

    def __init__(self):
        Strategy.__init__(self)
        self.access_key = ""
        self.secret_key = ""
        self.bucket_name = ""
        self.host_image = ""

    def startSave(self, imageSrc: str = None) -> typing.Any:
        q = Auth(self.access_key, self.secret_key)
        token = q.upload_token(self.bucket_name, os.path.basename(imageSrc), 3600)

        ret, info = put_file(token, os.path.basename(imageSrc), imageSrc)
        print(info)
        print(ret)
        if info.status_code == 200:
            return ("%s/%s" % (self.host_image, ret['key']), None)
        return (None, "上传失败")

    def initSetting(self, param: dict = None) -> typing.Any:
        Strategy.initSetting(self, param)
        if 'access_key' in param.keys():
            self.access_key = param["access_key"]
        if 'secret_key' in param.keys():
            self.secret_key = param["secret_key"]
        if 'bucket_name' in param.keys():
            self.bucket_name = param["bucket_name"]

        if 'host_image' in param.keys():
            self.host_image = param["host_image"]


class ImageSMMSSaveStrategy(Strategy):

    def __init__(self):
        Strategy.__init__(self)
        self.appk = ""
        self.username = ""
        self.password = ""
        self.getTokenUrl = 'https://sm.ms/api/v2/token'
        self.uploadUrl = 'https://sm.ms/api/v2/upload'

    def startSave(self, imageSrc: str = None) -> typing.Any:
        return self.upload(imageSrc)

    def getToken(self):
        payload = {'username': self.username, 'password': self.password}
        response = requests.post(url=self.getTokenUrl, data=payload)
        rsp = response.text
        result = json.loads(rsp)
        if result['code'] == 'success':
            return result['data']['token']
        return None

    def upload(self, filePath):
        token = self.getToken()
        headers = {}
        if token:
            headers = {"Authorization": "Basic %s" % token}
            print(headers)
        files = {'smfile': open(filePath, 'rb')}

        response = requests.post(url=self.uploadUrl, headers=headers, files=files)
        rsp = response.text
        print(rsp)
        result = json.loads(rsp)
        if result['code'] == 'success':
            return (result['data']['url'], None)
        elif result['code'] == 'image_repeated':
            return (result['images'], None)
        else:
            return (None, result['message'])

    def initSetting(self, param: dict = None) -> typing.Any:
        Strategy.initSetting(self, param)
        if 'appk' in param.keys():
            self.appk = param["appk"]

        if 'username' in param.keys():
            self.username = param["username"]

        if 'password' in param.keys():
            self.password = param["password"]


class ImageUploadHelper:
    _instance = None

    def __init__(self):
        self.strategy: Strategy = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ImageUploadHelper, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    def init(self, strategy: Strategy = None):
        self.strategy = strategy

    def saveImage(self, imageSrcList: list = None) -> rx.Observable:

        _imageSrcList = imageSrcList

        def _createObserver(observable, scheduler):
            try:
                for img in _imageSrcList:
                    if self.strategy:
                        result = self.strategy.save(img)
                        if result["code"] == 'success':
                            observable.on_next(result['data'])
                        else:
                            observable.on_error(result["msg"])
                    else:
                        observable.on_error("未设置图片上传插件")
            except Exception as e:
                observable.on_error(e)

        return rx.create(_createObserver)

    def saveImageForQMineImage(self, data: QMimeData) -> rx.Observable:
        _data = data

        def _createObserver(observable, scheduler):
            tempFileName = None
            try:
                image = QImage(data.imageData())
                tempFileName = os.path.join(getProjectPath(), fileNameGenerate('%s.png' % time.time()))
                image.save(tempFileName)
                result = None
                if self.strategy:
                    result = self.strategy.save(tempFileName)
                    if result["code"] == 'success':
                        observable.on_next(result['data'])
                    else:
                        observable.on_error(result["msg"])
                else:
                    observable.on_error("未设置图片上传插件")
            except Exception as e:
                observable.on_error(e)
            finally:
                if tempFileName:
                    os.remove(tempFileName)

        return rx.create(_createObserver)


imageUploadManager = ImageUploadHelper()
