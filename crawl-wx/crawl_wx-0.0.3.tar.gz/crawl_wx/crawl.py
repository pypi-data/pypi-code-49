# -*- coding: utf8 -*-

import logging
import asyncio
import requests
import tempfile
import uncurl

from copy import deepcopy

from bs4 import BeautifulSoup
from crawl_wx.util import UA

from urllib.parse import urlparse
from urllib.parse import parse_qsl


class WXCrawl(object):

    def __init__(self, curl_request: str, tick: int, output: str):
        """

        :param str curl_request: Curl command
        :param int tick: Sleep interval
        :param str output: Output directory
        """
        self.request_context = uncurl.parse_context(curl_request)
        self.cookie = self.request_context.cookies
        self.http_headers = self.request_context.headers
        self.query_param = None
        self.url = None
        self.tick = tick
        self.output = output
        self.__parse()

    async def __launch_browser(self):
        self.browser = await launch()

    def __parse(self):
        o = urlparse(self.request_context.url)
        query = parse_qsl(o.query)
        self.query_param = dict(query)
        self.url = f"{o.scheme}://{o.hostname}{o.path}"

    @staticmethod
    def extract_context(appmsg_info):
        for item in appmsg_info:
            if not item['is_deleted']:
                logging.info(f"get article: {item['title']}, content_url: {item['content_url']}")
                return item["title"], item["content_url"]
        return '', ''

    def __crawl_contents(self):
        params = deepcopy(self.query_param)
        params["begin"] = "0"
        current_count = 0
        while True:
            logging.info(f"crawl: {self.url}, params: {params}")
            resp = requests.get(
                self.url, headers=self.http_headers, cookies=self.cookie, params=params)
            data = resp.json()
            base_resp =  data["base_resp"]
            if base_resp["ret"] != 0:
                logging.info(f"crawl: {self.url} failed")
                return
            sent_list, total = data["sent_list"], data["total_count"]
            current_count += len(sent_list)
            for item in sent_list:
                yield self.extract_context(item['appmsg_info'])
            if current_count >= total:
                return
            with tempfile.TemporaryFile() as fp:
                fp.write(current_count)
            params["begin"] = current_count

    async def __extract_content(self, content_url):
        logging.info(f"extract content: {content_url}")
        resp = requests.get(content_url, headers={
            'User-Agent': UA
        })
        soup = BeautifulSoup(resp.text)
        tag = soup.find(id="js_content")
        if tag is not None:
            return str(a)
        else:
            tag = soup.find(id="img-content")
            if tag is not None:
                return str(a)
        return

    async def run(self):
        logging.info(f"start crawl {self.url}")
        for title, content_url in self.__crawl_contents():
            if content_url:
                task = asyncio.create_task(self.__extract_content(content_url))
                await task
                if task.exception():
                    logging.error(f"crawl {content_url} failed, exception {task.exception()}")
                else:
                    content = task.result()
                    if content:
                        with open(f"{self.output}/{title}.txt", "w") as f:
                            f.write(content)
                    else:
                        logging.warning(f"crawl {content_url} failed")
            await asyncio.sleep(self.tick)
        logging.info(f"end crawl {self.url}")
