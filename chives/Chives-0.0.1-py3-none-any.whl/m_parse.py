#coding=utf-8

import re
from datetime import datetime


rootPath=r'./'


class MyParse():
    def __init__(self):
        self.urls = {}                      # 目标网页
        self.param = {}
        self.cachePool={}
        self.stamp = datetime.now().strftime('%Y%m%d')  # #北京时区时间戳转换为字符串

    #判断元素类型
    def typeofList(self, tList):
        if isinstance(tList, list):         #数组结构
            return 1
        elif isinstance(tList, dict):       #字典结构
            if tList['next'] != [] and tList['next'] is not None:       #有子节点
                return 2
            elif tList['next'] == [] or tList['next'] is None:          #叶子结点
                return 3
            else:
                return -1
        else:
            return -1
    #递归解析
    def parseList(self, tList):
        typl=self.typeofList(tList)
        if typl==1:         #数组并列
            for i in range(0, len(tList)):      #遍历数组
                self.parseList(tList[i])
        elif typl==2:        #1-N数据
            print(tList['title'])
            # print(tList['key'])
            # 带'-'的用上一级的key
            self.key = tList['href'].split('#')[-1]
            self.parseList(tList['next'])
        elif typl==3:           #base元素
            print(tList['title'])
            # print(tList['key'])
            self.key = tList['href'].split('#')[-1]
            # self.crawList(tList)
        else:
            print('err parseList')
            return typl

    def parse_fenshi(self,page):
        # 匹配分时数据
        pattern = re.compile(
            r'var url = "http://push2ex.eastmoney.com/getStockFenShi\?pagesize={0}&ut=(.*?)&dpt=(.*?)"'.format(144))
        match = pattern.search(page)
        if match:
            return(match.group(1),match.group(2))
            # ut = match.group(1)
            # dpt = match.group(2)
        else:
            return None

    def parse_param(self,key,page):
        # 匹配fs:case"gold_sh_spotgoods":new f(o.gold).Bankuai("#table_wrapper","m:118");break;
        pattern = re.compile(r'case"{0}":new f\(o.(.*?)\).Bankuai\("#table_wrapper","(.*?)"\);break;'.format(key))
        match = pattern.search(page)
        if match:
            return (match.group(1).split(',')[0],match.group(2))
            # print(match.group(1).split(',')[0])
            # fs = match.group(2)
        else:
            return None

    def parse_fid(self,type, page):
        # 匹配fid：gold:{order:"f3",orderDur:!1,type:"gold"},
        pattern = re.compile(r'{0}:.order:"(.*?)",orderDur:!1,type:"(.*?)".+?,'.format(type))
        match = pattern.search(page)
        if match:
            return (match.group(1),match.group(2))
            # fid = match.group(1)
        else:
            return None

    def parse_field(self,type, page):
        # 匹配fields：gold:{fields:"f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f28,f11,f62,f128,f136,f115,f152,f133,f124",
        pattern = re.compile(r'{0}:.fields:"(.*?)",'.format(type))
        match = pattern.search(page)
        if match:
            return match.group(1)
            # fields = match.group(1)
        else:
            return None

    def parse_fff(self,key,mainjs):
        # 港股市场特殊处理
        if '-' in key:
            # 'boards2-90.BK0713' -> 'b:BK0713'
            fs = key[0] + ':' + key.split('.')[-1]
            fid = 'f3'
            fields = 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f33,f22,f11,f62,f128,f136,f115,f152'
        else:
            # print('匹配param参数')
            # print(key)
            # 匹配fs:case"gold_sh_spotgoods":new f(o.gold).Bankuai("#table_wrapper","m:118");break;
            type, fs = self.parse_param(key, mainjs)
            # 匹配fid：gold:{order:"f3",orderDur:!1,type:"gold"},
            fid, type = self.parse_fid(type, mainjs)
            # 匹配fields：gold:{fields:"f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f28,f11,f62,f128,f136,f115,f152,f133,f124",
            fields = self.parse_field(type, mainjs)+',f26,f33'
        return(fs,fid,fields)

    def Imatate2(self):
        self.update_info()


# 主程序入口
if __name__ == '__main__':
    spider = MyParse()
    spider.Imatate()


    print('TS:'+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


