#coding=utf-8


from spdex import info
import json
import time
import requests
from tqdm import tqdm
from urllib import parse
from datetime import datetime
from datetime import timedelta
from pymongo import MongoClient



rootPath=r'./'


class IOSCrawl():
    def __init__(self):
        self.urls = {}                      # 目标网页
        self.headers = {}                   # Get/Post请求头
        self.param = {}
        self.stamp = self.utc2local(self.local2utc(datetime.now())).strftime('%Y%m%d')  # #北京时区时间戳转换为字符串
        self.client = MongoClient("localhost", 27017)
        self.db=self.client['spdex']
        self._matches = self.db['matches']
        self._records = self.db['records']
    #析构函数
    def __del__(self):
        self.client.close()
    # 从配置文件中更新登录链接信息
    def update_info(self):
        self.urls = info.loginUrls                                                  #http地址
        self.headers = info.loginHeaders
        self.param = info.loginParam

    # 发送Get请求
    def requests_get(self, url, data=None):
        try:
            url = url if data is None else url+parse.urlencode(data)
            # print(url)
            response = requests.get(url, timeout=5)
            response.encoding = 'utf-8'
            return response if response.status_code == requests.codes.ok else None
        except:
            return None
    # 保存htmlPage
    def write_html_page(self, path, page):
        f=open(path, 'w')
        f.write(page.encode('utf-8'))
        f.close()
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
    # 匹配相对应的链接编号
    def get_mid(self, match):
        for each in self.links:
            if (match['HomeTeam'] == each['h_cn']) and (match['AwayTeam'] == each['a_cn']):
                return each['id']
        return match['mid']
    # 获取比分
    def get_score(self, mid):
        try:
            page=requests.get('https://i.sporttery.cn/api/fb_match_info/get_pool_rs/&mid='+mid).json()
            return page['result']['pool_rs']['crs']['prs_name']
        except:
            return ''
    # 爬取数据并保存
    def crawl_match(self,sp_json):
        # 遍历每一场比赛
        for sp in sp_json:
            self.param['sr']['keyword'] = sp['EventId']
            sr_json = self.requests_get(self.urls['sr'], self.param['sr']).json()
            if(sr_json is None):
                continue
            # 交易信息更新
            item=[sp['MaxUpdateTime'],sr_json['BaseInfo']['BfOddsHome'],sr_json['BaseInfo']['BfOddsDraw'],sr_json['BaseInfo']['BfOddsAway'],sr_json['BaseInfo']['UoOddsOver'],sr_json['BaseInfo']['UoOddsUnder'],sr_json['BaseInfo']['BfAmountHome'],sr_json['BaseInfo']['BfAmountDraw'],sr_json['BaseInfo']['BfAmountAway'],sr_json['BaseInfo']['UoAmountOver'],sr_json['BaseInfo']['UoAmountUnder']]
            # 比赛内容
            match=self._matches.find_one({'EventId':sp['EventId']})
            flag= (match is None)
            # 标题行
            if flag:
                match={}
                match['mid'] = ''
                match['Score'] = ''
                match['EventId'] = sp['EventId']
                match['SortName']=sp['SortName']
                # match['Team']=sp['HomeTeam']+'VS'+sp['AwayTeam']
                match['HomeTeam'] = sp['HomeTeam']
                match['AwayTeam'] = sp['AwayTeam']
                match['MatchTime']=sp['MatchTime']
                match['MaxUpdateTime'] = sp['MaxUpdateTime']
                match['Comp'] = json.dumps(item)
                match['Detail']=[]
                match['Times'] = []
                match['Data']={}
                # match['Detail']=[['MaxUpdateTime','BfOddsHome','BfOddsDraw','BfOddsAway','UoOddsOver','UoOddsUnder','BfAmountHome','BfAmountDraw','BfAmountAway','UoAmountOver','UoAmountUnder']]
            # 记录更新的交易信息
            if ((not flag) and (not(match['Comp']==json.dumps(item)))) or flag:
                print('->')
                match['MaxUpdateTime'] = sp['MaxUpdateTime']
                match['Comp'] = json.dumps(item)
                item[0]=self.utc2local(self.local2utc(datetime.now())).strftime('%Y-%m-%d %H:%M:%S')
                match['Detail'].append(item)
                match['Times'].append(sr_json)
                # 记录-1h的时间段信息(没必要)
                # mt_time = datetime.strptime(sp['MatchTime'], '%Y-%m-%dT%H:%M:%S')  # 字符串转换成日期
                # mut_time = datetime.strptime(sp['MaxUpdateTime'], '%Y-%m-%dT%H:%M:%S')
                # delta = (mt_time - mut_time).seconds  # 起止时间间隔（分钟）
                # if(delta<3600):
                #     match['Times'].append(item)
            #分时数据
            self.param['cs']['id'] = sp['EventId']
            cs_json = self.requests_get(self.urls['cs'], self.param['cs']).json()
            if(cs_json is None):
                continue
            for cs in cs_json:
                match['Data'][str(cs['PcId'])]=cs
            if flag:
                self._matches.insert_one(match)
            else:
                self._matches.update_one({'EventId': sp['EventId']},{"$set": match})


    # 爬取数据并保存
    def Imatate(self):
        try:
            # 同步配置参数
            self.update_info()
            lg_json = self.requests_get(self.urls['url']).json()
            for i in tqdm(range(0,len(lg_json))):
                league=lg_json[i]
                self.param['sp']['league']=league['Id']
                sp_json = self.requests_get(self.urls['sp'], self.param['sp']).json()
                league['next']=sp_json
                # 每一个联赛
                self.crawl_match(sp_json)
            self._records.update_one({'date': self.stamp}, {"$set": {"events": lg_json}}, True)
        except:
            pass

    #清除30天前数据
    def delete(self,nday=30):
        now = spider.utc2local(spider.local2utc(datetime.now()))
        if (now.day % 3) == 1 and (now.hour == 9):
            print('clear:'+str(now))
            try:
                past3 = datetime.now() - timedelta(days=nday)
                # 获取全部联赛信息
                self._matches.delete_many({'MatchTime': {'$lt': past3.strftime('%Y-%m-%d')}})
                self._records.delete_many({'date': {'$lt': past3.strftime('%Y%m%d')}})
            except:
                pass
# 主程序入口
if __name__ == '__main__':
    spider = IOSCrawl()
    spider.Imatate()
    spider.delete()

    print('TS:'+spider.utc2local(spider.local2utc(datetime.now())).strftime('%Y-%m-%d %H:%M:%S'))



