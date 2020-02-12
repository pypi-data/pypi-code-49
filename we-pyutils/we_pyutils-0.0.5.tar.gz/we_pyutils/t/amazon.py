#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : amazon.py
@Time    : 2020-02-09 8:53
@Author  : ZENKR
@Email   : zenkr@qq.com
@Software: PyCharm
@Desc    :
@license : Copyright (c) 2020 WingEase Technology Co.,Ltd. All Rights Reserved.
"""
import re
from decimal import Decimal, getcontext


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance


# 参考：http://docs.developer.amazonservices.com/en_US/dev_guide/DG_Endpoints.html
MARKETPLACES = {
    # North America
    'BR': 'www.amazon.com.br',
    'CA': 'www.amazon.ca',
    'MX': 'www.amazon.com.mx',
    'US': 'www.amazon.com',
    # Europe region
    'AE': 'www.amazon.ae',
    'DE': 'www.amazon.de',
    'ES': 'www.amazon.es',
    'FR': 'www.amazon.fr',
    'UK': 'www.amazon.co.uk',  # GB
    'GB': 'www.amazon.co.uk',
    'IN': 'www.amazon.in',
    'IT': 'www.amazon.it',
    'TR': 'www.amazon.com.tr',
    # Far East region
    'SG': 'www.amazon.sg',
    'AU': 'www.amazon.com.au',
    'JP': 'www.amazon.co.jp',
    # China
    'CN': 'www.amazon.cn',
    # Others
    'NL': 'www.amazon.nl',
}

MARKETPLACE_IDS = {
    # North America
    'BR': 'A2Q3Y263D00KWC',
    'CA': 'A2EUQ1WTGCTBG2',
    'MX': 'A1AM78C64UM0Y8',
    'US': 'ATVPDKIKX0DER',
    # Europe region
    'AE': 'A2VIGQ35RCS4UG',
    'DE': 'A1PA6795UKMFR9',
    'ES': 'A1RKKUPIHCS9HS',
    'FR': 'A13V1IB3VIYZZH',
    'UK': 'A1F83G8C2ARO7P',  # GB
    'GB': 'A1F83G8C2ARO7P',
    'IN': 'A21TJRUUN4KGV',
    'IT': 'APJ6JRA9NG5V4',
    'TR': 'A33AVAJ2PDY3EV',
    # Far East region
    'SG': 'A19VAU5U5O7RUS',
    'AU': 'A39IBJ37TRP1C6',
    'JP': 'A1VC38T7YXB528',
    # China
    'CN': 'AAHKV2X7AFYLW',
    # Others
    'NL': '',
}

MWS_ENDPOINTS = {
    # North America
    'BR': 'https://mws.amazonservices.com',
    'CA': 'https://mws.amazonservices.ca',
    'MX': 'https://mws.amazonservices.com.mx',
    'US': 'https://mws.amazonservices.com',
    # Europe region
    'AE': 'https://mws.amazonservices.ae',
    'DE': 'https://mws-eu.amazonservices.com',
    'ES': 'https://mws-eu.amazonservices.com',
    'FR': 'https://mws-eu.amazonservices.com',
    'UK': 'https://mws-eu.amazonservices.com',  # GB
    'GB': 'https://mws-eu.amazonservices.com',
    'IN': 'https://mws.amazonservices.in',
    'IT': 'https://mws-eu.amazonservices.com',
    'TR': 'https://mws-eu.amazonservices.com',
    # Far East region
    'SG': 'https://mws-fe.amazonservices.com',
    'AU': 'https://mws.amazonservices.com.au',
    'JP': 'https://mws.amazonservices.jp',
    # China
    'CN': 'https://mws.amazonservices.com.cn',
    # Others
    'NL': '',
}


class MarketPlaces(Singleton):
    # North America
    BR = None
    CA = None
    MX = None
    US = None
    # Europe region
    AE = None
    DE = None
    ES = None
    FR = None
    UK = None  # GB
    GB = None
    IN = None
    IT = None
    TR = None
    # Far East region
    SG = None
    AU = None
    JP = None
    # China
    CN = None
    # Others
    NL = None

    def __init__(self):
        for country_code, domain in MARKETPLACES.items():
            setattr(self, country_code, domain)

    @staticmethod
    def all():
        return MARKETPLACES

    @staticmethod
    def domains():
        return list(MARKETPLACES.values())

    @staticmethod
    def ids():
        return list(MARKETPLACE_IDS.values())

    @staticmethod
    def endpoints():
        return list(MWS_ENDPOINTS.values())


def extract_star(star):
    if star:
        tmp = str.replace(star, ',', '.')
        tmp = re.findall(r'(\d+[,.]*\d*)', tmp)
        tmp = float(min(tmp))
        return tmp
    return None


def extract_review_count(review):
    tmp = re.findall('([\d,.]+)', review)
    if len(tmp) > 0:
        tmp = tmp[0]
        tmp = str.replace(tmp, ',', '')
        tmp = str.replace(tmp, '.', '')
        tmp = int(tmp)
        return tmp
    return None


def extract_price(price, thousands_symbol=',', decimal_symbol='.', precision=2):
    tmp = re.findall('([\d,.]+)', price)
    if len(tmp) > 0:
        tmp = tmp[0]
        tmp = str.replace(tmp, thousands_symbol, '')
        tmp = str.replace(tmp, decimal_symbol, '.')
        getcontext().prec = precision
        tmp = Decimal(tmp)
        return tmp
    return None


if __name__ == '__main__':
    e = extract_star('4.6 of 5')
    # e = extract_price('1,199.88')
    print(e)
