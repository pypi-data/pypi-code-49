# -*- coding:utf-8 -*- 

import os
import codecs

__version__ = codecs.open(os.path.join(os.path.dirname(__file__), 'VERSION.txt')).read()
__author__ = 'Iseuwei'

# from .m_crawl import MyCrawl
from .crawl import IOSCrawl
from .spider import IOSdown
from .m_test import SpdexIOS