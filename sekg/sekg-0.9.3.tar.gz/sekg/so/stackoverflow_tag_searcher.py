# # -*-coding:utf-8-*-
import os
import urllib
from urllib.parse import quote
import time
import gensim
import requests
from bs4 import BeautifulSoup
import zipfile
from xml.etree.ElementTree import parse
from sekg.util.annotation import catch_exception
from pathlib import Path
from sekg.so.SOTagItem import SOTagItem
from sekg.so.SOTagItemCollection import SOTagItemCollection


class SOTagSearcher():
    maxTryNum = 5
    user_agent = {"user-agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322)"}

    def __init__(self, so_tag_item_collection_path=None):
        self.int_tags = self.__int_tags()
        self.synonyms_data = {}
        self.init_all_synonyms()
        if so_tag_item_collection_path:
            self.so_tag_item_collection: SOTagItemCollection = SOTagItemCollection.load(so_tag_item_collection_path)
        else:
            self.so_tag_item_collection = SOTagItemCollection()

    @catch_exception
    def __int_tags(self):
        so_path = os.path.dirname(os.path.abspath(__file__))
        tag_path = str(Path(so_path) / "stackoverflow.com-Tags.zip")
        if os.path.exists(tag_path):
            with zipfile.ZipFile(tag_path, 'r') as z:
                f = z.open('Tags.xml')
            doc = parse(f)
            root = doc.getroot()
            tag_data = []
            for child in root:
                tag_data.append(child.attrib)
            tag_dic = {}
            for item in tag_data:
                tag_dic[item["TagName"].lower()] = item
            return tag_dic
        else:
            return {}

    def parse_synonyms(self, html):
        if html:
            soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
            div = soup.find('div', class_="mainbar")
            syn_set = set()
            if div:
                a_list = div.find_all('a', class_="post-tag")
                for item in a_list:
                    syn_set.add(item.text)
            return syn_set
        else:
            return set()

    def parse_tag_info(self, html):
        short_text = ""
        long_text = ""
        info_html = ""
        if html:
            soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
            text_div = soup.find('div', class_='post-text')
            short_div = text_div.find('div', class_="welovestackoverflow")
            if short_div:
                p = short_div.find('p')
                short_text = p.text
                info_html += str(short_div)
            long_text = ""
            while True:
                item = short_div.find_next_sibling()
                item_current = str(item)
                if item_current.startswith("<p>"):
                    long_text += item.text + "\n"
                    info_html += str(item)
                    short_div = item
                else:
                    break
            return short_text, long_text, info_html
        else:
            return short_text, long_text, info_html

    def download_html(self, url):
        try:
            html = requests.get(url, headers=self.user_agent).content
            if html:
                return html
            else:
                return ""
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
            time.sleep(5)
            return ""

    def __fetch_synonyms_for_one_tag(self, tag):
        try:
            url = 'https://stackoverflow.com/tags/' + quote(tag) + "/synonyms"
            # print("url now: ", url)
            for tries in range(self.maxTryNum):
                html = self.download_html(url)
                if not html:
                    print("Dear Host,I can not find the web page for tag", tag)
                else:
                    parse_result = self.parse_synonyms(html)
                    if parse_result:
                        synonyms = parse_result - {tag}
                        return synonyms
            return {}
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
            time.sleep(5)
            return {}
        except Exception as e:
            print("exception:" + str(e))
            time.sleep(5)
            return {}

    def __fetch_tag_info_for_one_tag(self, tag):
        try:
            url = 'https://stackoverflow.com/tags/' + quote(tag) + "/info"
            # print("url now: ", url)
            for tries in range(self.maxTryNum):
                html = self.download_html(url)
                if not html:
                    print("Dear Host,I can not find the web page for tag", tag)
                else:
                    short_text, long_text, info_html = self.parse_tag_info(html)
                    if short_text or long_text:
                        return short_text, long_text, info_html
            return "", "", ""
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
            time.sleep(5)
            return "", "", ""
        except Exception as e:
            print("exception:" + str(e))
            time.sleep(5)
            return "", "", ""

    def get_tag_item_for_one_tag(self, tag):
        tag = tag.lower()
        if tag in self.so_tag_item_collection.get_all_tag_name():
            so_tag_item: SOTagItem = self.so_tag_item_collection.get_so_tag_item(tag)
            if so_tag_item.is_valid():
                print("info of {} is completed".format(tag))
                return so_tag_item
            else:
                if not so_tag_item.get_long_description() and not so_tag_item.get_short_description():
                    short_text, long_text, info_html = self.__fetch_tag_info_for_one_tag(tag)
                    so_tag_item.update_short_description(short_text)
                    so_tag_item.update_long_description(long_text)
                    so_tag_item.update_info_html(info_html)
                if not so_tag_item.get_tag_synonyms():
                    # synonyms = self.__fetch_synonyms_for_one_tag(tag)
                    # so_tag_item.update_tag_synonyms(synonyms)
                    # if tag not self.synonyms_data, it maybe no synonyms originally
                    if tag in self.synonyms_data:
                        so_tag_item.update_tag_synonyms(self.synonyms_data[tag])
                self.so_tag_item_collection.add_so_tag_item(so_tag_item)
                return so_tag_item
        elif tag in self.int_tags.keys():
            short_text, long_text, info_html = self.__fetch_tag_info_for_one_tag(tag)
            synonyms = self.__fetch_synonyms_for_one_tag(tag)
            item = self.int_tags[tag]
            so_tag_item = SOTagItem(tag_info_dic=item)
            so_tag_item.update_short_description(short_text)
            so_tag_item.update_long_description(long_text)
            so_tag_item.update_info_html(info_html)
            so_tag_item.update_tag_synonyms(synonyms)
            self.so_tag_item_collection.add_so_tag_item(so_tag_item)
            return so_tag_item
        else:
            return None

    def get_tag_item(self, tags):
        so_tag_collection = SOTagItemCollection()
        for tag in tags:
            tag = tag.lower()
            tag_item = self.get_tag_item_for_one_tag(tag)
            if tag_item:
                so_tag_collection.add_so_tag_item(tag_item)
        return so_tag_collection

    def init_all_synonyms(self):
        try:
            page = 1
            while True:
                url_tag = "http://api.stackexchange.com/2.2/tags/synonyms?page={}&pagesize=100&order=desc&sort=creation&site=stackoverflow".format(
                    str(page))
                response = requests.get(url_tag, headers=self.user_agent).json()
                if response["items"]:
                    for item in response["items"]:
                        tag_from = item["from_tag"]
                        tag_to = item["to_tag"]
                        if tag_to not in self.synonyms_data.keys():
                            self.synonyms_data[tag_to] = {tag_from}
                        else:
                            self.synonyms_data[tag_to].add(tag_from)
                else:
                    break
                page += 1
        except Exception as e:
            print("exception:" + str(e))
            time.sleep(30)

    def run(self):
        # for tag_name in self.int_tags:
        #     self.get_tag_item_for_one_tag(tag_name)
        # return self.so_tag_item_collection

        # we can use api get all synonyms, and the number of tags which have synonyms is about 2500, use api is more faster
        self.init_all_synonyms()
        valid_tag = set()
        for tag, so_tag_item in self.so_tag_item_collection.name2sotag:
            if tag in self.synonyms_data.keys():
                so_tag_item.update_tag_synonyms()
                self.so_tag_item_collection.add_so_tag_item(so_tag_item)
            if so_tag_item.get_long_description or so_tag_item.get_short_description:
                valid_tag.add(tag)

        need_tag = set(self.int_tags.keys()) - valid_tag
        for tag in need_tag:
            short_text, long_text, info_html = self.__fetch_tag_info_for_one_tag(tag)
            item = self.int_tags[tag]
            so_tag_item = SOTagItem(tag_info_dic=item)
            so_tag_item.update_short_description(short_text)
            so_tag_item.update_long_description(long_text)
            so_tag_item.update_info_html(info_html)
            if tag in self.synonyms_data:
                so_tag_item.update_tag_synonyms(self.synonyms_data[tag])
            self.so_tag_item_collection.add_so_tag_item(so_tag_item)

    def get_tag_info_cache(self):
        return self.so_tag_item_collection

    def save(self, path):
        self.so_tag_item_collection.save(path)

    def init(self, path):
        if path and os.path.exists(path):
            self.so_tag_item_collection: SOTagItemCollection = SOTagItemCollection.load(path)

    def __repr__(self):
        return "<AsyncWikiSearcher tags_count=%r>" % (len(self.so_tag_item_collection.size()))


if __name__ == '__main__':
    searcher = SOTagSearcher()
    print(len(searcher.synonyms_data))
