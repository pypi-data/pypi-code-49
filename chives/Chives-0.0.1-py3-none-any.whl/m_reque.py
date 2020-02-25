#coding=utf-8

import math
import random
import json
import time
import requests
from bs4 import BeautifulSoup
from urllib import parse
from datetime import datetime
from datetime import timedelta
from chives import  info


rootPath=r'./'


class MyReque():
    def __init__(self):
        self.urls = {}                      # 目标网页
        self.headers = {}                   # Get/Post请求头
        self.param = {}
        self.cachePool={}
        self.stamp = self.utc2local(self.local2utc(datetime.now())).strftime('%Y%m%d')  # #北京时区时间戳转换为字符串
        self.cookie=requests.cookies.RequestsCookieJar()
        self.session = requests.session()

    # 从配置文件中更新登录链接信息
    def update_info(self):
        self.urls = info.loginUrls                                                  #http地址
        self.headers = info.loginHeaders
        self.param = info.loginParam
        self.cookie.set("cookie", info.loginCookie)
        self.session.cookies.update(self.cookie)

    def requests_url(self, url, data=None):
        url = url if data is None else url+parse.urlencode(data)
        url = url.replace('%2C', ',').replace('%3A', ':').replace('%2B', '+')
        return url
    # 发送Get请求
    def requests_get(self, url, data=None):
        try:
            url = url if data is None else url+parse.urlencode(data)
            # url = url.replace('%2C', ',').replace('%3A', ':').replace('%2B', '+')
            if url in self.cachePool.keys():
                print('cache:')
                return self.cachePool[url]
            time.sleep(random.random() * 0 + 0.1)  # 0-1区间随机数
            #没有缓存就开始抓取
            # print(self.urls['proxies']['https'] + ' --> ' + url)
            response = requests.get(url, timeout=10)
            # response = requests.get(url, proxies=self.urls['proxies'], timeout=10)
            # self.session.keep_alive = False
            # response = self.session.get(url, proxies=self.urls['proxies'], timeout=10)
            # response.encoding = 'utf-8'
            value = response if response.status_code == requests.codes.ok else None
        except:
            value = None
        finally:
            return value
    # 保存htmlPage
    def write_html_page(self, path, page):
        f=open(path, 'w')
        f.write(page.encode('utf-8').decode('utf-8'))
        f.close()
    # 读取htmlPage
    def read_html_page(self, path):
        f = open(path, 'r')
        page=f.read().encode('utf-8').decode('utf-8')
        f.close()
        return page
    # UTC转本地（北京）
    def utc2local(self, utc_st):
        offset = timedelta(hours=8)
        local_st = utc_st + offset
        return local_st
    # 本地转UTC
    def local2utc(self, local_st):
        time_struct = time.mktime(local_st.timetuple())
        utc_st = datetime.utcfromtimestamp(time_struct)
        return utc_st
    # 字符串转换成datetime
    def strptime(self, str):
        return datetime.strptime(str, '%Y-%m-%d')
    # datetime转换为字符串
    def strftime(self, time):
        return time.strftime('%Y%m%d')

    # 获取代理ip
    def get_iplist(self,url):
        headers={
            'User-Agent':info.loginHeaders['User-Agent']
        }
        page=requests.get(url, headers=headers)
        soup=BeautifulSoup(page.text,'lxml')
        trs=soup.find_all('tr')
        ip_list = []
        for tr in trs[1:]:
            tds=tr.find_all('td')
            ip_list.append(tds[1].text+':'+tds[2].text)
        return ip_list
    # 切换ip代理
    def switchProxy(self):
        proxy_ip=random.choice(self.get_iplist(self.urls['proxyWeb']))
        # self.urls['proxies']['http']='http://' + proxy_ip
        self.urls['proxies']['https'] = 'https://' + proxy_ip

    def getStamp(self):
        return self.utc2local(self.local2utc(datetime.now())).strftime('%Y%m%d')


    def get_fenshi(self,line,code, market, ut, dpt):
        # 匹配分时数据
        # ut, dpt = self.parse.parse_fenshi(self.timejs)
        self.param['fs']['code'] =code
        self.param['fs']['market'] = market
        self.param['fs']['ut'] = ut
        self.param['fs']['dpt'] = dpt
        self.param['fs']['pageindex'] = 0
        # 每条记录都要get一下太慢了
        # url = self.requests_url(self.urls['fs'], self.param['fs'])
        # line.append(url)
        page = self.requests_get(self.urls['fs'], self.param['fs'])
        if page is None:
            return None
        fs_json = json.loads(page.text)
        # print(fs_json['data']['tc'])
        if fs_json['data'] is not None:
            # print(len(fs_json['data']['data']))
            numNode = fs_json['data']['tc']  # 记录总数
            numPage = math.ceil(numNode / self.param['fs']['pagesize'])  # 页码数
            # print(numPage)
            for i in range(1, numPage):  # 跳过第一页
                # break                           #可配置（开启的话太慢了）
                try:
                    self.param['fs']['pageindex'] = i + 1
                    page = self.requests_get(self.urls['fs'], self.param['fs'])
                    fs_json['data']['data'].extend(json.loads(page.text)['data']['data'])
                except:
                    continue
            # 返回结果
            # mk['fs'] = fs_json
        return fs_json

    def get_kline(self,line,secid,klt):
        # 获取历史k线
        self.param['kline']['secid'] = secid
        self.param['kline']['klt'] = klt
        # url=self.requests_url(self.urls['kline'], self.param['kline'])
        # line.append(url)
        page=self.requests_get(self.urls['kline'], self.param['kline'])
        his_json = json.loads(page.text)
        # mk['his5'] = his_json  # 历史5分钟K线
        return his_json

    def get_fflow(self,line,secid,klt,lmt):
        # 获取当天K线
        self.param['fflow']['secid'] = secid
        self.param['fflow']['klt'] = klt
        self.param['fflow']['lmt'] = lmt
        # url=self.requests_url(self.urls['fflow'], self.param['fflow'])
        # line.append(url)
        page = self.requests_get(self.urls['fflow'], self.param['fflow'])
        if page is None:
            return None
        his_json = json.loads(page.text)
        # mk['fflow1'] = his_json  # 1分钟K线
        return his_json
    def get_trends(self,line,secid,ndays,iscr):
        # 获取近期趋势线
        self.param['trends2']['secid'] = secid
        self.param['trends2']['ndays'] = ndays
        self.param['trends2']['iscr'] = iscr
        # url=self.requests_url(self.urls['trends2'],self.param['trends2'])
        # line.append(url)
        page=self.requests_get(self.urls['trends2'],self.param['trends2'])
        if page is None:
            return None
        his_json = json.loads(page.text)
        # mk['trends3'] = his_json    #最近3天
        return his_json

    def get_stockinfo(self,line,secid):
        # 获取个股基本信息
        self.param['info']['secid'] = secid
        # url=self.requests_url(self.urls['info'],self.param['info'])
        # line.append(url)
        page=self.requests_get(self.urls['info'],self.param['info'])
        if page is None:
            return None
        his_json=json.loads(page.text)
        # mk['info'] = his_json
        return his_json

    def get_guba(self,line,code):
        # 获取股吧聊天记录
        self.param['guba']['code'] = code
        # url=self.requests_url(self.urls['guba'],self.param['guba'])
        # line.append(url)
        page=self.requests_get(self.urls['guba'],self.param['guba'])
        if page is None:
            return None
        his_json=json.loads(page.text)
        # mk['guba'] = his_json
        return his_json

    def get_boardpage(self,fs,fid,fields):
        # 获取板块所有页码的内容
        self.param['com']['pn'] = 1  # 重新置为1
        self.param['com']['fs'] = fs
        self.param['com']['fid'] = fid
        self.param['com']['fields'] = fields  # 可配置

        page=self.requests_get(self.urls['url'], self.param['com'])
        if page is None:
            return
        mk_json=json.loads(page.text)
        # print(mk_json)
        #查询剩余分页并追加到字典
        numNode = mk_json['data']['total']      #记录总数
        numPage = math.ceil(numNode / self.param['com']['pz'])      #页码数
        # print(numPage)
        for i in range(1, numPage):   #跳过第一页
            # break                           #可配置，只查询第一页
            try:
                self.param['com']['pn'] = i + 1
                page = self.requests_get(self.urls['url'], self.param['com'])
                if page is None:
                    continue
                mk_json['data']['diff'].extend(json.loads(page.text)['data']['diff'])
            except:
                continue
        #返回结果
        # tList['data']=mk_json
        return mk_json


    def Imatate(self):
        self.update_info()

        page=self.requests_get('http://35.push2his.eastmoney.com/api/qt/stock/kline/get?secid=1.600789&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58&klt=101&fqt=0&end=20500101&lmt=90')
        kl_json=json.loads(page.text)
        print(kl_json)
        print(len(kl_json['data']['klines']))




# 主程序入口
if __name__ == '__main__':
    spider = MyReque()
    spider.Imatate()


    print('TS:'+spider.utc2local(spider.local2utc(datetime.now())).strftime('%Y-%m-%d %H:%M:%S'))


