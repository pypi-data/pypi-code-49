import time
import hashlib
import logging

from dateutil import parser as date_parser
from lxml.html import etree
from bs4 import BeautifulSoup
from redis import StrictRedis

from .config import config

logging.basicConfig(level=logging.INFO, format='[%(asctime)s %(levelname)s] %(name)s >> %(message)s')
redis = StrictRedis(host=config.host, port=config.port, db=config.db, password=config.password)


def get_logger(name):
    return logging.getLogger(name)


def user_agent(browser='chrome'):
    browsers = {
        'chrome': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'iphone': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    }
    assert browser in browsers, ValueError(f'no such browser: {browser}')
    return browsers[browser]


def xpath_selector(html):
    return etree.HTML(html)


def bs4_selector(html):
    return BeautifulSoup(html, 'lxml')


def format_date(ts=None, ft='%Y-%m-%d %H:%M:%S'):
    time_array = time.localtime(ts if ts else int(time.time()))
    return time.strftime(ft, time_array)


def parse_date(date, ft='%Y-%m-%d %H:%M:%S'):
    return date_parser.parse(date).strftime(ft)


def md5(msg):
    return hashlib.md5(msg.encode()).hexdigest()


def sha1(msg):
    return hashlib.sha1(msg.encode()).hexdigest()


def splist(target, step):
    return [target[i:i + step] for i in range(len(target)) if i % step == 0]
