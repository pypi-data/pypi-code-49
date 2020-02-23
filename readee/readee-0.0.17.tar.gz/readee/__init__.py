#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'readee'

from .article import getArticle

def _formaturl(url):
	if '://' not in url:
		return "https://" + url
	return url

def export(url, content=None, **args):
	article = getArticle(url, content, args)
	if not article.text or not article.text.strip():
		raise Exception('Can not find main content')
	return article