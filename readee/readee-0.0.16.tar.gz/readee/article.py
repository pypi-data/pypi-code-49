#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from readability import Document
from .content import _findMain
import hashlib
import sys
import os

TO_REMOVE = [
	'跳到导航', 
	'跳到搜索', 
	'Skip to main content'
]

def _findUrl(url, soup):
	if 'telegra.ph' not in url:
		return
	address = soup.find('address')
	if not address:
		return
	link = address.find('a')
	return link and link.get('href')

def _trimWebpage(raw):
	for to_remove in TO_REMOVE:
		raw = raw.replace(to_remove, '')
	anchor = '<!-- detail_toolbox -->'
	index = raw.find(anchor)
	if index != -1:
		return raw[:index]
	return raw

def _getUrlContent(url):
	headers = {
		'method': 'GET',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
	}
	return requests.get(url, headers=headers).text

def _cachedContent(url):
	os.system('mkdir tmp > /dev/null 2>&1')
	cache = 'tmp/' + hashlib.sha224(url.encode('utf-8')).hexdigest()[:10] + '.html'
	try:
		with open(cache) as f:
			return f.read()
	except:
		content = _getUrlContent(url)
		with open(cache, 'w') as f:
			f.write(content)
		return content

def getArticle(url, content, args = {}):
	if not content:
		if 'test' in str(sys.argv):
			content = _cachedContent(url)
		else:
			content = _getUrlContent(url)
	soup = BeautifulSoup(_trimWebpage(content), 'html.parser')
	article_url = _findUrl(url, soup) # may need to use
	doc = Document(content)
	return _findMain(soup, doc, url, args)

