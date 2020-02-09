# -*- coding: utf8 -*-

import logging
import asyncio
import requests
import time
import uncurl

from copy import deepcopy

from pyppeteer import launch

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
        self.browser = None
        self.tick = tick
        self.event_loop = asyncio.get_event_loop()
        self.output = output
        self.__parse()
        self.event_loop.run_until_complete(self.__launch_browser())

    async def __launch_browser(self):
        self.browser = await launch(headless=True)

    def __parse(self):
        o = urlparse(self.request_context.url)
        query = parse_qsl(o.query)
        self.query_param = dict(query)
        self.url = f"{o.scheme}://{o.hostname}{o.path}"

    @staticmethod
    def extract_context(appmsg_info):
        for item in appmsg_info:
            if not item['is_deleted']:
                logging.debug(f"extract title: {item['title']}, content_url: {item['content_url']}")
                return item["title"], item["content_url"]
        return '', ''

    def __crawl_contents(self):
        params = deepcopy(self.query_param)
        params["begin"] = "0"
        current_count = 0
        while True:
            logging.debug(f"crawl: {self.url}, params: {params}")
            resp = requests.get(
                self.url, headers=self.http_headers, cookies=self.cookie, params=params)
            data = resp.json()
            base_resp, sent_list, total = data["base_resp"], data["sent_list"], data["total_count"]
            current_count += len(sent_list)
            for item in sent_list:
                yield self.extract_context(item['appmsg_info'])
            if current_count >= total:
                return
            params["begin"] = current_count
            time.sleep(self.tick)

    async def __extract_content(self, content_url):
        page = await self.browser.newPage()
        await page.goto(content_url)
        element = await page.querySelector("#img-content")
        content = await page.evaluate('(element) => element.innerHTML', element)
        return content

    async def run(self):
        logging.info(f"start crawl {self.url}")
        for title, content_url in self.__crawl_contents():
            if content_url:
                content = await self.__extract_content(content_url)
                with open(f"{self.output}/{title}.txt", "w") as f:
                    f.write(content)
        await self.browser.close()
        logging.info(f"end crawl {self.url}")
