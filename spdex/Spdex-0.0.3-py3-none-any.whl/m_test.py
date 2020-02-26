#coding=utf-8

from spdex import crawl
from spdex import spider
import pandas as pb

rootPath=r'./'


class SpdexIOS():
    def __init__(self):
        self.cachePool={}
        self.cw = crawl.IOSCrawl()
        self.sp=spider.IOSdown()
        self.flag=0
    #在线更新数据库
    def update(self):
        self.cw.Imatate()
    #导出联赛列表
    def export(self):
        df=self.sp.export()
        return df
    #显示联赛列表
    def leagues(self):
        df=self.sp.leagues()
        return df
    #查询联赛信息
    def events(self, key):
        df=self.sp.events(key)
        return df
    #查询赛事信息
    def markets(self, eventid, key):
        df=self.sp.markets(eventid, key)
        return df
    #格式转换
    def pb2csv(self, df, path):
        df.to_csv(path, header=True, index=False, encoding='utf_8_sig')  # 写入
    def csv2pb(self, path):
        df=pb.read_csv(path, header=True, index=False, encoding='utf_8_sig')  # 读取
        return df

# 主程序入口
if __name__ == '__main__':
    mt=SpdexIOS()
    mt.update()




