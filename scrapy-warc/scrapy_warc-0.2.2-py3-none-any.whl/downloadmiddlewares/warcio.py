# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy_warc.warcio import ScrapyWarcIo,warc_date

class WarcioMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        return cls(crawler.settings)

    def __init__(self, settings):
        self.warcio = ScrapyWarcIo(settings)

    def process_request(self, request, spider):
        request.meta['WARC-Date'] = warc_date()
        return None

    def process_response(self, request, response, spider):
        self.warcio.write(response, request)
        return response