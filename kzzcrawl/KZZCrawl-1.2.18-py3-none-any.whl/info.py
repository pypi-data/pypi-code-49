#coding=utf-8

# 更新：
# 1、定向抓取可转债一览表,可转债比价,债券指数

loginParam={
    'com': {
        'pn': 1,
        'pz': 2000,
        'po': 1,
        'np': 1,
        'fltt': 2,
        'invt': 2,
        'fid': 'f243',
        'fs' :'b:MK0354',
        'fields' :'f1,f152,f2,f3,f12,f13,f14,f227,f228,f229,f230,f231,f232,f233,f234,f235,f236,f237,f238,f239,f240,f241,f242,f26,f243',     #无限延伸？
    },
    'kzz': {
        'p': 1,
        'ps': 2000,
        'sr': -1,
        'js': '{pages:(tp),data:(x),font:(font)}',
        'type': 'KZZ_LB2.0',
        'st': 'STARTDATE',
        'token': '70f12f2f4f091e459a279469fe49eca5',
    },
}

loginUrls =  {
    'proxyWeb': 'https://www.xicidaili.com/nn/',
    'proxies': {
        # "http": 'http://127.0.0.1:1080',
        "https": 'https://127.0.0.1:1080'
    },
    'url':'http://17.push2.eastmoney.com/api/qt/clist/get?',
    'kzz':'http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?',
}
loginHeaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
    'Host': '17.push2.eastmoney.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection':'keep-alive'
}
loginCookie=''

