#coding=utf-8

from chives import m_crawl

rootPath=r'./'


class ChivesDemo():
    def __init__(self):
        self.cachePool={}
        self.cw = m_crawl.ChoiceStock()
        self.flag=0
        self.cw.Imatate()
        self.keys=self.cw.keyValue.keys()
    #执行板块查询
    def board(self,key,mode=2):
        self.cw.flag=mode
        self.cw.key2=key
        self.cw.value2=None
        self.cw.Imatate()
        return self.cw.value2
    #公用http代理接口
    def get(self, url, data=None):
        result=self.cw.requests_get(url,data)
        return result
    #导出基本信息
    def base(self, date=None):
        df=self.cw.exportInfo(date)
        return df
    #从服务器查询个股url
    def url(self, secid, type='编号'):
        line=self.cw.getUrlfromDB(secid, type)
        return line
    #获取个股信息
    def does(self, secid, mode=12):
        df=self.cw.getRowby(secid, mode)
        return df
    #切换数据库
    def switchDB(self, pw, url, db):
        sqlUrl=self.cw.switchDB(pw, url, db)
        return sqlUrl
    #切换IP代理
    def switchIP(self, url):
        url=self.cw.switchProxy()
        return url

# 主程序入口
if __name__ == '__main__':
    mt=ChivesDemo()
    mt.do('沪深A股',0)




