# -*- coding:utf-8 -*- 

import os
import codecs

__version__ = codecs.open(os.path.join(os.path.dirname(__file__), 'VERSION.txt')).read()
__author__ = 'Iseuwei'

# from .m_crawl import MyCrawl
from .m_info import MyInfo
from .m_parse import MyParse
from .m_reque import MyReque
from .m_test import ChivesDemo