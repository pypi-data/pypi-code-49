#coding=utf-8

import os
import sys
import random
import json
import time
import datetime
import requests
import pandas as pd
from urllib import parse
from bs4 import BeautifulSoup
from datetime import datetime
from sqlalchemy import create_engine
from chives import MyParse
from chives import MyReque
from chives import info



rootPath=r'./'


class ChoiceStock():
    def __init__(self):
        self.urls = {}                      # 目标网页
        self.headers = {}                   # Get/Post请求头
        self.param = {}
        self.cachePool={}
        self.ip_pool = []
        self.flag=0
        self.key = ''
        self.keyValue={}
        self.key2=''
        self.value2=None
        self.stamp = datetime.now().strftime('%Y%m%d')  # #北京时区时间戳转换为字符串
        # self.client = MongoClient("localhost", 27017)
        # self.db=self.client['choicestock']
        # self.cookie=requests.cookies.RequestsCookieJar()
        # self.session = requests.session()

        self.parse=MyParse()
        self.reque=MyReque()
        self.reque.update_info()

        #15162q1k54.imwork.net:58744#mt29353962.wicp.vip:43541#127.0.0.1:3306
        self.sqlUrl = 'mysql+pymysql://peppa:111111@mt29353962.wicp.vip:43541/eastmoney'
        self.engine = create_engine(self.sqlUrl, encoding='utf-8', echo=True)

    # 从配置文件中更新登录链接信息
    def update_info(self):
        self.urls = info.loginUrls                                                  #http地址
        self.headers = info.loginHeaders
        self.param = info.loginParam
        # self.cookie.set("cookie", info.loginCookie)
        # self.session.cookies.update(self.cookie)

    # 发送Get请求
    def requests_get(self, url, data=None):
        try:
            url = url if data is None else url+parse.urlencode(data)
            # url = url.replace('%2C', ',').replace('%3A', ':').replace('%2B', '+')
            if url in self.cachePool.keys():
                print('url cache:')
                return self.cachePool[url]
            time.sleep(random.random() * 0 + 0.3)  # 0-1区间随机数
            #没有缓存就开始抓取
            # print('proxies->'+self.urls['proxies'])
            # response = requests.get(url, timeout=10)

            response = requests.get(url, proxies=self.urls['proxies'], timeout=3)
            # self.session.keep_alive = False
            # response = self.session.get(url, proxies=self.urls['proxies'], timeout=10)
            # response.encoding = 'utf-8'
            value = response if response.status_code == requests.codes.ok else None
        except Exception as e:
            print(e)
            value = None
        finally:
            return value

    # 获取代理ip
    def get_iplist(self,url):
        # print(url)
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
    # 更新IP代理池
    def update_ip_pool(self):
        print('更新IP代理池')
        result=[]
        pgs=random.sample(range(2, 3600), 3)
        for pg in pgs:
            url=self.urls['proxyWeb']+str(pg)
            result.extend(self.get_iplist(url))
        # self.check_ip_avai(result)
        self.ip_pool=result
    # 检查IP有效性
    def check_ip_avai(self, result):
        print('检查IP可用性：')
        for ipport in result:
            print('ip_pool:sum : {}:{}'.format(len(self.ip_pool),len(result)))
            try:
                proxies = {
                    'http': 'http://'+ipport,
                    'https': 'https://'+ipport,
                }
                # print(proxies)
                response = requests.get('http://httpbin.org/get', proxies=proxies, timeout=1)
                flag = True if response.status_code == requests.codes.ok else False
                if flag:
                    self.ip_pool.append(ipport)
            except Exception as e:
                result.remove(ipport)
                print(e)
                continue

    # 切换ip代理
    def switchProxy(self):
        if len(self.ip_pool)<2:
            self.update_ip_pool()
            random.shuffle(self.ip_pool)
        proxy_ip=self.ip_pool.pop()
        self.urls['proxies']['http']='http://' + proxy_ip
        self.urls['proxies']['https'] = 'https://' + proxy_ip
        return proxy_ip

    def switchDB(self,pw,url,db):
        self.sqlUrl = 'mysql+pymysql://{}@{}/{}'.format(pw,url,db)
        self.engine = create_engine(self.sqlUrl, encoding='utf-8', echo=True)
        return self.sqlUrl

    def getStamp(self):
        return self.reque.utc2local(self.reque.local2utc(datetime.now())).strftime('%Y%m%d')

    #递归解析
    def parseList(self, tList):
        typl=self.parse.typeofList(tList)
        if typl==1:         #数组并列
            for i in range(0, len(tList)):      #遍历数组
                self.parseList(tList[i])
        elif typl==2:        #1-N数据
            # print(tList['title'])
            # print(tList['key'])
            # 带'-'的用上一级的key
            self.key = tList['href'].split('#')[-1]
            self.parseList(tList['next'])
        elif typl==3:           #base元素
            # print(tList['title'])
            # print(tList['key'])
            self.key = tList['href'].split('#')[-1]
            self.crawList(tList)
        else:
            print('err parseList')
            return typl

    def getdbmysql(self, key, mode=0):
        try:
            conn = self.engine.connect()
            # print(df)
            # 将新建的DataFrame储存为MySQL中的数据表，不储存index列 , con=con, if_exists='append',
            sql_cmd ='select * from {}'.format(self.keyValue[key] if mode==0 else key)
            df = pd.read_sql(sql=sql_cmd, con=conn)
            return df
        except Exception  as e:
            print(e)
        finally:
            conn.close()
    # 抓取记录并加入字典'data'字段
    def crawList(self, tList):
        # print(self.key, tList['title'])
        # return
        if self.flag==0:
            #当前可查询的板块列表
            self.keyValue[tList['title']]=self.key
            return
        elif self.flag==1:
            #实时抓取板块数据
            if self.key==self.keyValue[self.key2]:
                fs, fid, fields = self.parse.parse_fff(self.key, self.mainjs)
                mk_json = self.reque.get_boardpage(fs, fid, fields)
                tList['data']=mk_json
                df=self.parseHisData(tList)
                # self.save2mysqldb(df, self.key)
                # df=self.getdbmysql(self.key2)
                self.value2=df
            return
        elif self.flag == 2:
            #数据库下载当天板块数据
            if self.key==self.keyValue[self.key2]:
                df = self.getdbmysql(self.key2)
                self.value2=df
            return
        elif self.flag == 3:
            #实时抓取板块数据并导入数据库
            if self.key == self.keyValue[self.key2]:
                fs, fid, fields = self.parse.parse_fff(self.key, self.mainjs)
                mk_json = self.reque.get_boardpage(fs, fid, fields)
                tList['data'] = mk_json
                df = self.parseHisData(tList)
                self.save2mysqldb(df, self.key)
                self.value2 = df
            return
        # #这一步必须公用
        # fs, fid, fields = self.parse.parse_fff(self.key, self.mainjs)
        # mk_json = self.reque.get_boardpage(fs, fid, fields)
        # tList['data'] = mk_json

        #避免耗时重复
        if self.value2!=None:
            return
        else:
            return
            if self.key == 'hs_a_board':
                result={}
                lineFlag=False  #导出dfUrl的开关
                for i in range(0, len(mk_json['data']['diff'])):
                    mk = mk_json['data']['diff'][i]
                    code = mk['f12']
                    secid = str(mk['f13']) + '.' + code
                    line = [code, mk['f14'], secid]     #记录url
                    #遍历匹配个股ID
                    if (self.key2==secid) or (self.key2==mk['f14']) or lineFlag:
                        print(mk['f14'])  # 名称
                        if self.flag == 4 or lineFlag:
                            # 下载个股当天分时数据
                            ut, dpt = self.parse.parse_fenshi(self.timejs)
                            fs_json = self.reque.get_fenshi(line, code, mk['f13'], ut, dpt)  # 分时成交详情；暂时停用
                            df=self.parseFSData(fs_json)
                            # self.save2mysqldb(df, secid)
                            self.value2 = df
                        if self.flag == 5 or lineFlag:
                            #抓取当天个股评论
                            guba = self.reque.get_guba(line, code)
                            self.value2 = guba
                        if self.flag == 6 or lineFlag:
                            #历史5分钟K线
                            his5 = self.reque.get_kline(line, secid, 5)
                            df=self.parseMinData(his5,'klines')
                            self.value2 = df
                        if self.flag == 7 or lineFlag:
                            # 历史日K
                            his_w = self.reque.get_kline(line, secid, 101)
                            df=self.parseMinData(his_w,'klines')
                            self.value2 = df
                        if self.flag == 8 or lineFlag:
                            # 1分钟资金流向线？
                            fflow1 = self.reque.get_fflow(line, secid, 1, 0)
                            df=self.parseMinData(fflow1,'klines')
                            self.value2 = df
                        if self.flag == 9 or lineFlag:
                            # 盘前趋势线
                            trends0 = self.reque.get_trends(line, secid, 1, 1)
                            df = self.parseMinData(trends0,'trends')
                            self.value2 = df
                        if self.flag == 10 or lineFlag:
                            # 最近3天趋势线
                            trends3 = self.reque.get_trends(line, secid, 3, 0)
                            df = self.parseMinData(trends3,'trends')
                            self.value2 = df
                        if self.flag == 11 or lineFlag:
                            # 当天日K
                            daykline = self.reque.get_fflow(line, secid, 101, 100)
                            df = self.parseMinData(daykline,'klines')
                            self.value2 = df
                        if self.flag == 12 or lineFlag:
                            # 基本信息
                            info = self.reque.get_stockinfo(line, secid)
                            df = self.parseInfoData(info)
                            self.value2 = df
                        else:
                            pass
                    result[secid]=line
                print(result)
                with open('urls.json','w') as f:
                    json.dump(result,f)
                # df=pd.DataFrame(data=result)
                df=pd.DataFrame(data=[x for x in result.values()], columns=['代码', '名称', '编号', '分时', '股吧', '5分钟K', '日K', '1分钟K', '3天趋势', '盘前', '一天','基本信息'])
                self.save2mysqldb(df,'hs_a_url')
                print(df)
            return
        return


        # return
        for i in range(0,len(mk_json['data']['diff'])):
            mk=mk_json['data']['diff'][i]
            code=mk['f12']
            secid = str(mk['f13']) + '.' + code
            print(mk['f14'])        #名称
            ut, dpt = self.parse.parse_fenshi(self.timejs)
            mk['fs'] = self.reque.get_fenshi(code,mk['f13'], ut, dpt)      # 分时成交详情；暂时停用
            mk['info'] = self.reque.get_stockinfo(secid)          # 个股基本信息；暂时关闭
            mk['guba'] = self.reque.get_guba(code)                # 股吧评论
            mk['his5'] =self.reque.get_kline(secid,5)             # 历史5分钟K线
            mk['his_w'] = self.reque.get_kline(secid,101)         # 历史日K
            mk['fflow1'] = self.reque.get_fflow(secid,1,0)        # 1分钟K线
            mk['daykline'] = self.reque.get_fflow(secid,101,100)  # 当天日K
            mk['trends3'] = self.reque.get_trends(secid,3,0)      # 最近3天
            mk['trends0'] = self.reque.get_trends(secid,1,1)      # 盘前


    def save2mysqldb(self, df, table):
        try:
            conn = self.engine.connect()
            # print(df)
            # 将新建的DataFrame储存为MySQL中的数据表，不储存index列 , con=con, if_exists='append',
            df.to_sql(table, con=conn, if_exists='replace', index=False)
            print('Read from and write to Mysql table successfully!')
        except Exception  as e:
            print(e)
        finally:
            conn.close()
    '''
    
    def save2mongodb(self, tList):
        mk_json=tList['data']
        for i in range(0,len(mk_json['data']['diff'])):
            mk=mk_json['data']['diff'][i]
            code=mk['f12']
            secid = str(mk['f13']) + '.' + code
            print(mk['f14'])        #名称

            if Flag:    #逐条操作数据库比较耗时；暂时关闭
                #更新数据库
                match = self._matches.find_one({'symbol': mk['f12']})       #代码
                flag = (match is None)
                # 标题行
                if flag:
                    match = {}
                    match['Label'] = mk['f14']
                    match['symbol'] = mk['f12']
                    match['from'] = self.getStamp()
                    match['Comp'] = json.dumps(mk)
                    match['Detail'] = []
                # 记录更新的交易信息
                if ((not flag) and (not (match['Comp'] == json.dumps(mk)))) or flag:
                    print('->')
                    match['Comp'] = json.dumps(mk)
                    match['Detail'].append(mk)
                    match['to'] = self.getStamp()
                if False:
                    self._matches.insert_one(match)
                else:
                    self._matches.update_one({'symbol': match['symbol']}, {"$set": match}, True)
        self._records.update_one({'date': self.stamp}, {"$addToSet": {"events": tList}}, True)
    '''

    # 更新离线解析文件
    def update_files(self):
        self.menu=requests.get('http://quote.eastmoney.com/config/sidemenu.json').text
        self.mainjs = requests.get('http://quote.eastmoney.com/center/js/gridlist3.min.js?').text
        self.timejs = requests.get('http://quote.eastmoney.com/f1static/js/timetrade.js').text
        # self.reque.write_html_page('chives/sidemenu.json', page.text)
        # self.reque.write_html_page('chives/gridlist3.min.js', self.mainjs)
        # self.reque.write_html_page('chives/timetrade.js',self.timejs)
        self.mainjs = self.reque.read_html_page('gridlist3.min.js')
        self.timejs = self.reque.read_html_page('timetrade.js')
        self.menu = self.reque.read_html_page('sidemenu.json')

    # 爬取数据并保存
    def Imatate(self):
        try:
            # 同步配置参数
            self.update_info()
            # self.update_files()
            # self.switchProxy()
            # 获取全部联赛信息
            # self._matches = self.db['matches']
            # self._records = self.db['records']
            self.mainjs=info.mainjs
            self.timejs = info.timejs
            # self.menu = info.menu
            sidemenu=json.loads(info.menu)
            # [1,4,5,6,7,8,9,10,12,14,15,16,17,18]    #全部跑完一个小时
            for i in range(1,len(sidemenu)):
                if i not in [1,4,5,6,7,8,9,10,12,14,15,16,17,18]:
                    continue
                try:
                    board = sidemenu[i]
                    # print(board['title'])
                    self.parseList(board)
                    board['trick'] = datetime.now()  # 添加时间戳到记录里
                    # print(board)
                    # self._records.update_one({'date': self.stamp}, {"$addToSet": {"events": board}}, True)
                except:
                    continue
        finally:
            pass
            # self.client.close()

    def exportInfo(self, date=None):
        key='info' if date is None else 'info_'+date
        df=self.getdbmysql(key,1)
        return df

    def testMysql(self, table, filename):
        try:
            conn = self.engine.connect()
            df = self.parseHisData(filename)
            # print(df)
            # 将新建的DataFrame储存为MySQL中的数据表，不储存index列 , con=con, if_exists='append',
            df.to_sql(table, con=conn, if_exists='fail', index=True)
            print('Read from and write to Mysql table successfully!')
        except Exception  as e:
            print(e)
        finally:
            conn.close()

    #从服务器查询个股url
    def getUrlfromDB(self, secid, type='编号'):
        sqlStr = "SELECT * FROM hs_a_url WHERE {} = \"{}\"".format(type, secid)
        with self.engine.raw_connection().cursor() as raw_cursor:
            query_count = raw_cursor.execute(sqlStr)
            # 若存在则跳过
            if query_count > 0:
                return raw_cursor.fetchall()[0]
            else:
                return None
    def getRowby(self,secid, mode=12):
        line=self.getUrlfromDB(secid)
        if mode == 4:
            # 下载个股当天分时数据
            fs_json = self.requests_get(line[4]).json()
            df = self.parseFSData(fs_json)
        elif mode == 5 :
            # 抓取当天个股评论
            df = self.requests_get(line[5]).json()
        elif mode == 6 :
            # 历史5分钟K线
            his5 = self.requests_get(line[6]).json()
            df = self.parseMinData(his5, 'klines')
        elif mode == 7 :
            # 历史日K
            his_w = self.requests_get(line[7]).json()
            df = self.parseMinData(his_w, 'klines')
        elif mode == 8 :
            # 1分钟资金流向线？
            fflow1 = self.requests_get(line[8]).json()
            df = self.parseMinData(fflow1, 'klines')
        elif mode == 9 :
            # 盘前趋势线
            trends0 = self.requests_get(line[9]).json()
            df = self.parseMinData(trends0, 'trends')
        elif mode == 10 :
            # 最近3天趋势线
            trends3 = self.requests_get(line[10]).json()
            df = self.parseMinData(trends3, 'trends')
        elif mode == 11 :
            # 当天日K
            daykline = self.requests_get(line[11]).json()
            df = self.parseMinData(daykline, 'klines')
        elif mode == 12 :
            # 基本信息
            info = self.requests_get(line[12]).json()
            df = self.parseInfoData(info)
        else:
            return None
        return df


    # 解析板块数据
    def parseHisData(self, tList):
        try:
            result = []
            mk_json = tList['data']
            for i in range(0, len(mk_json['data']['diff'])):
                mk = mk_json['data']['diff'][i]
                # 这里强制转换会报错，因为有的字段为'-'
                line = (
                mk['f12'], mk['f14'], mk['f2'], mk['f3'], mk['f4'], mk['f5'], mk['f6'], mk['f7'], mk['f15'], mk['f16'],
                mk['f17'], mk['f18'], mk['f10'], mk['f8'], mk['f9'], mk['f23'], mk['f26'], mk['f33'], mk['f20'], mk['f21'],
                mk['f24'], mk['f25'], mk['f22'], mk['f11'])
                result.append(line)
            df = pd.DataFrame(data=result,
                              columns=['代码', '名称', '最新价', '涨跌幅', '涨跌额', '成交量(手)', '成交额', '振幅', '最高', '最低', '今开', '昨收',
                                       '量比', '换手率', '市盈率(动态)', '市净率', '上市时间', '委比', '总市值', '流通市值', '60日涨跌幅', '年初至今涨跌幅', '涨速',
                                       '5分钟涨跌'])
            return df
        except Exception as e:
            print(e)
            return None
    # 解析分时数据
    def parseFSData(self, tList):
        try:
            result = []
            mk_json = tList['data']
            for i in range(0, len(mk_json['data'])):
                mk = mk_json['data'][i]
                # 这里强制转换会报错，因为有的字段为'-'
                line = ( mk['t'], mk['p'], mk['v'], mk['bs'])
                result.append(line)
            df = pd.DataFrame(data=result, columns=['时间', '成交价', '手数', '买卖'])
            return df
        except Exception as e:
            print(e)
            return None
    # 解析K线数据
    def parseMinData(self, tList, key):
        try:
            # print(tList)
            result = []
            klines = tList['data'][key]
            for i in range(0, len(klines)):
                line = klines[i].split(',')
                result.append(line)
            df = pd.DataFrame(data=result)
            # df = pd.DataFrame(data=result, columns=['时间', '今开', '最高', '最低', '昨收', '成交量', '成交额', '量比'])
            return df
        except Exception as e:
            print(e)
            return None

    # 解析K线数据
    def parseGuba(self, tList, key):
        try:
            # print(tList)
            result = []
            klines = tList['data'][key]
            for i in range(0, len(klines)):
                line = klines[i].split(',')
                result.append(line)
            df = pd.DataFrame(data=result)
            # df = pd.DataFrame(data=result, columns=['时间', '今开', '最高', '最低', '昨收', '成交量', '成交额', '量比'])
            return df
        except Exception as e:
            print(e)
            return None

    # 解析K线数据
    def parseUrlData(self, result):
        try:
            # print(tList)
            result = []
            df = pd.DataFrame(data=result)
            # df = pd.DataFrame(data=result, columns=['时间', '今开', '最高', '最低', '昨收', '成交量', '成交额', '量比'])
            return df
        except Exception as e:
            print(e)
            return None

    # 解析基本信息数据
    def parseInfoData(self, nf_json):
        try:
            result = []
            # print(nf_json['svr'])
            nf = nf_json['data']
            line = (
            nf['f43'], nf['f57'], nf['f58'], nf['f169'], nf['f170'], nf['f46'], nf['f44'], nf['f51'],
            nf['f168'], nf['f47'], nf['f164'], nf['f163'], nf['f116'], nf['f60'], nf['f45'], nf['f52'],
            nf['f50'], nf['f48'], nf['f167'], nf['f117'], nf['f71'], nf['f161'], nf['f49'],  nf['f135'],
            nf['f136'], nf['f137'], nf['f138'], nf['f139'], nf['f141'], nf['f142'], nf['f144'], nf['f145'],
            nf['f147'], nf['f148'], nf['f140'], nf['f143'], nf['f146'], nf['f149'], nf['f55'], nf['f62'],
            nf['f162'], nf['f92'], nf['f173'], nf['f104'], nf['f105'], nf['f84'], nf['f85'], nf['f183'],
            nf['f184'], nf['f185'], nf['f186'], nf['f187'], nf['f188'], nf['f189'], nf['f190'], nf['f191'],
            nf['f192'], nf['f107'], nf['f111'], nf['f86'], nf['f177'], nf['f78'], nf['f110'], nf['f262'],
            nf['f263'], nf['f264'], nf['f267'], nf['f268'], nf['f250'], nf['f251'], nf['f252'], nf['f253'],
            nf['f254'], nf['f255'], nf['f256'], nf['f257'], nf['f258'], nf['f266'], nf['f269'], nf['f270'],
            nf['f271'], nf['f273'], nf['f274'], nf['f275'], nf['f127'], nf['f199'], nf['f128'], nf['f198'],
            nf['f259'], nf['f260'], nf['f261'], nf['f171'], nf['f277'], nf['f278'], nf['f279'], nf['f288'])
            result.append(line)     #剔除'f530'字段
        except Exception as e:
            print(e)
        df = pd.DataFrame(data=result, columns=['f43', 'f57', 'f58', 'f169', 'f170', 'f46', 'f44', 'f51', 'f168', 'f47', 'f164', 'f163', 'f116', 'f60', 'f45', 'f52', 'f50', 'f48', 'f167', 'f117', 'f71', 'f161', 'f49', 'f135', 'f136', 'f137', 'f138', 'f139', 'f141', 'f142', 'f144', 'f145', 'f147', 'f148', 'f140', 'f143', 'f146', 'f149', 'f55', 'f62', 'f162', 'f92', 'f173', 'f104', 'f105', 'f84', 'f85', 'f183', 'f184', 'f185', 'f186', 'f187', 'f188', 'f189', 'f190', 'f191', 'f192', 'f107', 'f111', 'f86', 'f177', 'f78', 'f110', 'f262', 'f263', 'f264', 'f267', 'f268', 'f250', 'f251', 'f252', 'f253', 'f254', 'f255', 'f256', 'f257', 'f258', 'f266', 'f269', 'f270', 'f271', 'f273', 'f274', 'f275', 'f127', 'f199', 'f128', 'f198', 'f259', 'f260', 'f261', 'f171', 'f277', 'f278', 'f279', 'f288'])
        return df

# 主程序入口
if __name__ == '__main__':
    spider = ChoiceStock()
    spider.Imatate()


    print('TS:'+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


