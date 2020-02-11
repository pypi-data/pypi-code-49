# -*- coding: utf8 -*-

import argparse
import asyncio
import logging

from crawl_wx.crawl import WXCrawl


def cmd():
    parser = argparse.ArgumentParser(description="crawl wx")
    parser.add_argument("--curl_file", required=True, dest="curl_request")
    parser.add_argument("--output", required=True, dest="output_dir")
    parser.add_argument("--log_level", default="INFO", dest="log_level")
    args = parser.parse_args()
    log_level = getattr(logging, args.log_level, "INFO")
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    with open(args.curl_request) as f:
        curl_request = f.read()
    spider = WXCrawl(curl_request=curl_request, output=args.output_dir, tick=5)
    asyncio.get_event_loop().run_until_complete(spider.run())
