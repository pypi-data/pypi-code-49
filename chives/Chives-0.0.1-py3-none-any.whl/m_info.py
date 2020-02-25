#coding=utf-8


class MyInfo():
    def __init__(self):
        self.urls = {}                      # 目标网页
        self.headers = {}                   # Get/Post请求头
        self.param = {}
        self.cachePool={}
    def doMy(self):
        print('myInfo')