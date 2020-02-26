#coding=utf-8

import sys
import logging
# reload(sys)
# sys.setdefaultencoding('utf8')
# logging.basicConfig(filename='logging.log',
#                     format='%(asctime)s %(message)s',
#                     filemode="w", level=logging.DEBUG)

# 更新：
# 1、更新了定时抓取spdex数据，并写入数据库
# 2、特定时间段的记录保存
# 3、mongodb的导出Excel功能
# 4、数据更新的比较字段改成整条记录
# 5、datetime的时区转换问题
# 6、加入更新比赛结果的功能

loginParam={
    'cs': {
        'id': 29131354,
        'min': 0,
        'app': 'z',
        'version' :'i3.11',
    },
    'sp': {
        'class': -1,
        'hot': 1,
        'app': 'z',
        'version': 'i3.11',
    },
    'lg': {
        'league': 151,
        'app': 'z',
        'version': 'i3.11',
    },
    'sr': {
        'keyword': 29131354,
        'min': 0,
        'product_id': 0,
        'user_id': 215840,
        'tutorial': 0,
        'app': 'z',
        'version': 'i3.11',
    },
    'jc': {
        'rt': 3,
        'eid': 29112827,
        'f': 6,
        't': 0,
        'app': 'z',
        'version': 'i3.11',
    },
}

loginUrls =  {
    'url':'http://api.spdex.com/spdex/leagues?app=z&version=a3.11',
    'cs':'http://api.spdex.com/data/cs?',
    'sr':'http://api.spdex.com/data/search?',
    'sp':'http://api.spdex.com/spdex/match_data/sports?',
    'jc':'http://c.spdex.com/api/Json_Chart_App.aspx?',
}

loginHeaders = {
    'User-Agent': 'spdex_zhishu_v2.0/3.11 (iPhone; iOS 12.1.4; Scale/3.00)',
    'Host': 'api.spdex.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-Hans-CN;q=1',
    'Connection':'keep-alive'
}

loginCookie='''Cookie: ASP.NET_SessionId=bm2u3howy5jbo0kw3sveb20h'''

