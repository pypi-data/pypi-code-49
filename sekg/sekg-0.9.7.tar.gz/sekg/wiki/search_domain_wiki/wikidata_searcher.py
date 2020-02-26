#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fetch wikadata and wikipedia item with api
"""

import asyncio
import pickle
import traceback
from pathlib import Path

import aiohttp
import async_timeout

from sekg.util.annotation import catch_exception
from sekg.util.url_util import URLUtil
from sekg.wiki.WikiDataItem import WikiDataItem


# if sys.platform == 'win32':
#     loop = asyncio.ProactorEventLoop()
#     asyncio.set_event_loop(loop)

# import wikipedia


class AsyncWikiSearcher:
    API_URL = 'https://www.wikidata.org/w/api.php'
    WIKI_PEDIA_URL = 'https://en.wikipedia.org/w/api.php'
    TYPE_ALL = 0
    TYPE_TITLE = 1
    TYPE_ITEM = 2
    TYPE_WIKIPEDIA = 3

    def __init__(self, proxy_server=None, pool_size=63, stride=60):
        self.proxy_server = proxy_server
        self.semaphore = asyncio.Semaphore(pool_size)
        self.title_cache = {}
        self.item_cache = {}
        self.wikipedia_content_cache = {}
        self.wikidata_wikipedia_cache = {}
        self.wikipedia_content_html_cache = {}

        self.stride = stride
        self.wiki_pedia_none_list = []
        self.wikidata_id_2_wikipedia_title_dic = {}
        self.wikipedia_title_2_wikidata_id_dic = {}

    def init_id_to_title(self):
        if self.item_cache:
            for id, item in self.item_cache.items():
                if id not in self.wikidata_id_2_wikipedia_title_dic.keys():
                    title = self.get_title_from_wikidata_item(item)
                    self.wikidata_id_2_wikipedia_title_dic[id] = title
                    if title not in self.wikipedia_title_2_wikidata_id_dic.keys():
                        self.wikipedia_title_2_wikidata_id_dic[title] = {id}
                    else:
                        self.wikipedia_title_2_wikidata_id_dic[title].add(id)

    async def __fetch_titles(self, query, limit=5):
        if query in self.title_cache:
            return self.title_cache[query]
        params = {
            'action': 'query',
            'format': 'json',
            'list': 'search',
            'srprop': 'snippet',
            'srlimit': limit,
            'srsearch': query
        }
        try:
            async with self.semaphore:
                async with aiohttp.ClientSession() as session:
                    with async_timeout.timeout(10):
                        async with session.get(self.API_URL, params=params, proxy=self.proxy_server) as response:
                            json_data = await response.json()
                            result = [
                                {"pageid": item["pageid"], "title": item["title"], "snippet": item.get("snippet", "")}
                                for item in json_data["query"]["search"]]
                            if result:
                                self.title_cache[query] = result
                                self.title_cache[query.lower()] = result
                            else:
                                print(query, ", no search result")
                            return result
        except Exception:
            print("[Failed] query: {}".format(query))
            traceback.print_exc()
            return []

    async def __fetch_entity(self, id):
        if id in self.item_cache:
            return self.item_cache[id]
        params = {
            'ids': id,
            'format': 'json',
            'action': 'wbgetentities'
        }
        try:
            async with self.semaphore:
                async with aiohttp.ClientSession() as session:
                    with async_timeout.timeout(10):
                        async with session.get(self.API_URL, params=params, proxy=self.proxy_server) as response:
                            json_data = await response.json()
                            wikidata_item = WikiDataItem(id, init_at_once=False).init_wikidata_item_from_json(
                                json_data)
                            self.item_cache[id] = wikidata_item
                            wikidata_title = self.get_title_from_wikidata_item(wikidata_item)
                            self.wikidata_id_2_wikipedia_title_dic[id] = wikidata_title
                            # print("[Done] title: {}".format(id))
                            return json_data
        except Exception:
            print("[Failed] title: {}".format(id))
            traceback.print_exc()
            return {}

    async def __fetch_wikipedia_content(self, title):
        if title in self.wiki_pedia_none_list:
            return {}
        if title in self.wikipedia_content_cache:
            return self.wikipedia_content_cache[title]
        params = {
            'titles': title,
            'format': 'json',
            'action': 'query',
            'prop': 'extracts',
            'exintro': '',
            'explaintext': '',
            'redirects': 1
        }
        try:
            async with self.semaphore:
                async with aiohttp.ClientSession() as session:
                    with async_timeout.timeout(10):
                        async with session.get(self.WIKI_PEDIA_URL, params=params, proxy=self.proxy_server) as response:
                            json_data = await response.json()
                            result = [
                                {"pageid": item["pageid"], "title": item["title"], "context": item.get("extract", ""),
                                 }
                                for index, item in json_data["query"]["pages"].items()]
                            if result:
                                self.wikipedia_content_cache[title] = result
                            else:
                                self.wiki_pedia_none_list.append(title)
                                print(title, ", no wikipedia context")
                            # print("[Done] title: {}".format(title))
                            return result
        except Exception:
            print("[Failed] title: {}".format(title))
            traceback.print_exc()
            return {}

    async def __fetch_wikipedia_context_html(self, title):
        if title in self.wiki_pedia_none_list:
            return {}
        if title in self.wikipedia_content_cache:
            return self.wikipedia_content_cache[title]
        params = {
            'titles': title,
            'format': 'json',
            'action': 'query',
            'prop': 'extracts',
            'exintro': '',
            'redirects': 1
        }
        try:
            async with self.semaphore:
                async with aiohttp.ClientSession() as session:
                    with async_timeout.timeout(10):
                        async with session.get(self.WIKI_PEDIA_URL, params=params, proxy=self.proxy_server) as response:
                            json_data = await response.json()
                            result = [
                                {"pageid": item["pageid"], "title": item["title"], "context": item.get("extract", ""),
                                 }
                                for index, item in json_data["query"]["pages"].items()]
                            if result:
                                self.wikipedia_content_html_cache[title] = result
                            else:
                                self.wiki_pedia_none_list.append(title)
                                print(title, ", no wikipedia context html")
                            # print("[Done] title: {}".format(title))
                            return result
        except Exception:
            print("[Failed] title: {}".format(title))
            traceback.print_exc()
            return {}

    async def __fetch_wikidata_id_by_wikipedia_title(self, title):
        if title in self.wikipedia_title_2_wikidata_id_dic.keys():
            return self.wikipedia_title_2_wikidata_id_dic[title]
        params = {
            'titles': title,
            'format': 'json',
            'action': 'query',
            'prop': 'pageprops',
            "ppprop": "wikibase_item",
            "redirects": 1
        }
        try:
            async with self.semaphore:
                async with aiohttp.ClientSession() as session:
                    with async_timeout.timeout(10):
                        async with session.get(self.WIKI_PEDIA_URL, params=params, proxy=self.proxy_server) as response:
                            json_data = await response.json()
                            result = set()
                            for key, item in json_data["query"]["pages"].items():
                                if "pageprops" in item.keys():
                                    wikidata_id = item["pageprops"].get("wikibase_item", "")
                                    result.add(wikidata_id)
                            if result:
                                self.wikipedia_title_2_wikidata_id_dic[title] = result
                            else:
                                print(title, ", no corresponding wikidata")

                            # print("[Done] title: {}".format(title))
                            return result
        except Exception:
            print("[Failed] title: {}".format(title))
            traceback.print_exc()
            return {}

    def __fet_wikipedia_content_by_wikidata_id(self, id):
        if id in self.wikidata_wikipedia_cache.keys():
            return self.wikidata_wikipedia_cache[id]
        wikipedia_title = self.get_wikipedia_title_by_wikidata_id(id)
        if wikipedia_title and wikipedia_title in self.wikipedia_content_cache.keys():
            wikipedia_context = self.wikipedia_content_cache[wikipedia_title]
            self.wikidata_wikipedia_cache[id] = wikipedia_context
            return wikipedia_context
        return {}

    def save(self, title_save_path=None, item_save_path=None, wikipedia_content_save_path=None,
             wikipedia_html_save_path=None, wikipedia_title_2_wikidata_id_path=None):
        print("Save...")
        if title_save_path is not None:
            with Path(title_save_path).open("wb") as f:
                pickle.dump(self.title_cache, f)
        if item_save_path is not None:
            with Path(item_save_path).open("wb") as f:
                pickle.dump(self.item_cache, f)
        if wikipedia_content_save_path is not None:
            with Path(wikipedia_content_save_path).open("wb") as f:
                pickle.dump(self.wikipedia_content_cache, f)
        if wikipedia_html_save_path is not None:
            with Path(wikipedia_html_save_path).open("wb") as f:
                pickle.dump(self.wikipedia_content_cache, f)
        if wikipedia_title_2_wikidata_id_path is not None:
            with Path(wikipedia_title_2_wikidata_id_path).open("wb") as f:
                pickle.dump(self.wikipedia_title_2_wikidata_id_dic, f)

    def save_by_type(self, save_path, type=0):
        if save_path:
            print("save....")
            if type == self.TYPE_ALL:
                save_data = {"title_cache": self.title_cache,
                             "item_cache": self.item_cache,
                             "wikipedia_context": self.wikipedia_content_cache
                             }
                with Path(save_path).open("wb") as f:
                    pickle.dump(save_data, f)
            elif type == self.TYPE_TITLE:
                with Path(save_path).open("wb") as f:
                    pickle.dump(self.title_cache, f)
            elif type == self.TYPE_ITEM:
                with Path(save_path).open("wb") as f:
                    pickle.dump(self.item_cache, f)
            elif type == self.TYPE_WIKIPEDIA:
                with Path(save_path).open("wb") as f:
                    pickle.dump(self.wikipedia_content_cache, f)
            else:
                pass

    def clear(self):
        del self.wikipedia_content_cache
        del self.item_cache
        del self.title_cache
        del self.wikidata_wikipedia_cache
        del self.wikipedia_content_html_cache

        self.item_cache = {}
        self.title_cache = {}
        self.wikipedia_content_cache = {}
        self.wikidata_wikipedia_cache = {}
        self.wikipedia_content_html_cache = {}

    def search_title(self, queries):
        loop = asyncio.get_event_loop()
        tasks = [self.__fetch_titles(q) for q in queries]
        loop.run_until_complete(asyncio.gather(*tasks))
        return self.title_cache

    def fetch_item_for_cache_title_search(self):
        """
        fetch given items by network with all Wikidata item id in the title search cache.
        :return:
        """
        ids = set([])
        for title, search_results in self.title_cache.items():
            if not search_results:
                continue
            for search_result in search_results:
                ids.add(search_result["title"])
        return self.fetch_item(ids)

    def fetch_item(self, ids):
        """
        fetch given items by network with given ids.
        :param ids:
        :return:
        """
        loop = asyncio.get_event_loop()
        if not ids:
            return {}
        else:
            tasks = [self.__fetch_entity(_id) for _id in ids]
            loop.run_until_complete(asyncio.gather(*tasks))
        return self.item_cache

    def fetch_item_neighbor(self, ids=None):
        neighbor_ids = set()
        self.fetch_item(ids)
        if ids is None:
            for _id, item in self.item_cache.items():
                neighbor_ids.update(item.get_neighbor_ids())
        else:
            for id in ids:
                if id in self.item_cache.keys():
                    item = self.item_cache[id]
                    neighbor_ids.update(item.get_neighbor_ids())
        self.fetch_item(neighbor_ids)
        return self.item_cache

    def fetch_wikipedia_context_for_wikidata(self, wikidata_ids):
        self.fetch_item(wikidata_ids)
        titles = [_title for _title in self.wikidata_id_2_wikipedia_title_dic.values() if _title]
        self.fetch_wikipedia_context(titles)
        for _id in wikidata_ids:
            self.__fet_wikipedia_content_by_wikidata_id(_id)
        return self.wikidata_wikipedia_cache

    def fetch_wikipedia_context(self, titles):
        loop = asyncio.get_event_loop()
        tasks = [self.__fetch_wikipedia_content(_title) for _title in titles]
        loop.run_until_complete(asyncio.gather(*tasks))
        return self.item_cache

    def fetch_wikipedia_context_html(self, titles):
        loop = asyncio.get_event_loop()
        tasks = [self.__fetch_wikipedia_context_html(_title) for _title in titles]
        loop.run_until_complete(asyncio.gather(*tasks))
        return self.item_cache

    def fetch_wikidata_id_by_wikipedia_title(self, titles):
        loop = asyncio.get_event_loop()
        tasks = [self.__fetch_wikidata_id_by_wikipedia_title(_title) for _title in titles]
        loop.run_until_complete(asyncio.gather(*tasks))
        return self.item_cache

    def fetch_wikidata_item_by_wikipedia_title(self, titles):
        self.fetch_wikidata_id_by_wikipedia_title(titles)
        print(self.wikipedia_title_2_wikidata_id_dic)
        wikidata_ids = set()
        for value in self.wikipedia_title_2_wikidata_id_dic.values():
            wikidata_ids.update(set(value))
        self.fetch_item(wikidata_ids)

    def get_title_from_wikidata_item(self, wikidata_item: WikiDataItem):
        url = wikidata_item.data_dict.get("site:enwiki", "")
        if url:
            wikidata_title = URLUtil.parse_url_to_title(url)
            return wikidata_title
        return ""

    def get_wikipedia_title_by_wikidata_id(self, id):
        if id in self.wikidata_id_2_wikipedia_title_dic:
            return self.wikidata_id_2_wikipedia_title_dic[id]
        return ""

    def update(self, cache_path, type=0):
        if cache_path is not None:
            if type == self.TYPE_ALL:
                self.init_from_cache_by_type(cache_path, type=type)
                self.save_by_type(cache_path, self.TYPE_ALL)
            elif type == self.TYPE_TITLE:
                self.init_from_cache(title_save_path=cache_path)
                self.save_by_type(cache_path, self.TYPE_TITLE)
            elif type == self.TYPE_ITEM:
                self.init_from_cache(item_save_path=cache_path)
                self.save_by_type(cache_path, self.TYPE_ITEM)
            elif type == self.TYPE_WIKIPEDIA:
                self.init_from_cache(wikipedia_save_path=cache_path)
                self.save_by_type(cache_path, self.TYPE_WIKIPEDIA)
            else:
                pass

    @catch_exception
    def init_from_cache_by_type(self, cache_path, type=0):
        if cache_path:
            print("Init from cache...")
            if type == self.TYPE_ALL:
                with Path(cache_path).open("rb") as f:
                    data = pickle.load(f)
                    self.title_cache = dict(self.title_cache, **data["title_cache"])
                    self.item_cache = dict(self.item_cache, **data["item_cache"])
                    self.wikipedia_content_cache = dict(self.wikipedia_content_cache, **data["wikipedia_context"])
                    self.init_id_to_title()
            elif type == self.TYPE_TITLE:
                self.init_from_cache(title_save_path=cache_path)
            elif type == self.TYPE_ITEM:
                self.init_from_cache(item_save_path=cache_path)
                self.init_id_to_title()
            elif type == self.TYPE_WIKIPEDIA:
                self.init_from_cache(wikipedia_save_path=cache_path)
            else:
                pass

    @catch_exception
    def init_from_cache(self, title_save_path=None, item_save_path=None, wikipedia_save_path=None,
                        wikidata_wikidedia_save_path=None, wikipedia_html_save_path=None,
                        wikipedia_title_2_wikidata_id_path=None):
        print("Init from cache...")
        if title_save_path is not None and Path(title_save_path).exists():
            with Path(title_save_path).open("rb") as f:
                title_cache = pickle.load(f)
                self.title_cache = dict(self.title_cache, **title_cache)
                for title in self.title_cache.keys():
                    self.title_cache[title.lower()] = self.title_cache[title]

        if item_save_path is not None and Path(item_save_path).exists():
            with Path(item_save_path).open("rb") as f:
                item_cache = pickle.load(f)
                self.item_cache = dict(self.item_cache, **item_cache)
                self.init_id_to_title()
        if wikipedia_save_path is not None and Path(wikipedia_save_path).exists():
            with Path(wikipedia_save_path).open("rb") as f:
                wikipedia_cache = pickle.load(f)
                self.wikipedia_content_cache = dict(self.wikipedia_content_cache, **wikipedia_cache)
        if wikidata_wikidedia_save_path is not None and Path(wikidata_wikidedia_save_path).exists():
            with Path(wikidata_wikidedia_save_path).open("rb") as f:
                wikidata_wikipedia_cache = pickle.load(f)
                self.wikidata_wikipedia_cache = dict(self.wikidata_wikipedia_cache, **wikidata_wikipedia_cache)
        if wikipedia_html_save_path is not None and Path(wikipedia_html_save_path).exists():
            with Path(wikipedia_html_save_path).open("rb") as f:
                wikipedia_html_cache = pickle.load(f)
                self.wikipedia_content_html_cache = dict(self.wikipedia_content_html_cache, **wikipedia_html_cache)
        if wikipedia_title_2_wikidata_id_path is not None and Path(wikipedia_title_2_wikidata_id_path).exists():
            with Path(wikipedia_title_2_wikidata_id_path).open("rb") as f:
                wikipedia_title_2_wikidata_id_dic = pickle.load(f)
                self.wikipedia_title_2_wikidata_id_dic = dict(self.wikipedia_title_2_wikidata_id_dic,
                                                              **wikipedia_title_2_wikidata_id_dic)

    def item_cache_size(self):
        return len(self.item_cache)

    def title_cache_size(self):
        return len(self.title_cache)

    def wikipedia_cache_size(self):
        return len(self.wikipedia_content_cache)

    def wikidata_wikipedia_context_cache_size(self):
        return len(self.wikidata_wikipedia_cache)

    def wikidedia_context_html_cache(self):
        return len(self.wikipedia_content_html_cache)

    def id_to_title_cache_size(self):
        return len(self.wikidata_id_2_wikipedia_title_dic)

    def get_item_cache(self):
        return self.item_cache

    def get_title_cache(self):
        return self.title_cache

    def get_wikipedia_cache(self):
        return self.wikipedia_content_cache

    def get_wikidata_wikipedia_context_cache(self):
        return self.wikidata_wikipedia_cache

    def get_wikipedia_content_html(self):
        return self.wikipedia_content_html_cache

    def get_id_to_title_cache(self):
        return self.wikidata_id_2_wikipedia_title_dic

    def __repr__(self):
        return "<AsyncWikiSearcher title=%r item=%r wikipedia=%r>" % (
            self.title_cache_size(), self.item_cache_size(), self.wikipedia_cache_size())

    def get_wikidata_items_by_ids(self, wd_ids):
        """
        get list of WikidataItem by given id list
        :param wd_ids: a list of wikidata ids
        :return:
        """
        items = []
        for id in wd_ids:
            item = self.get_wikidata_item_by_item_id(id)
            if item is None:
                continue
            items.append(item)
        return items

    def get_wikidata_item_by_item_id(self, item_id):
        """
        get the wikidata item by given item_id
        :param item_id: a str, e.g.,"Q21"
        :return: None or WikiDataItem object
        """
        item = self.item_cache.get(item_id, None)
        return item

    def get_all_neighbour_ids_by_item_id(self, item_id):
        """
        get all wikidata item ids having direct relations with the given item_id
        :param item_id: a str, e.g.,"Q21"
        :return: [] or list of str. e.g., ["Q12","Q23"]
        """

        neighbours = set()
        item = self.item_cache.get(item_id, None)
        if item == None:
            return set()
        return item.get_neighbor_ids()

    def get_neighbour_ids_by_item_id_for_relation(self, item_id, property_wd_id):
        """
        get all wikidata item ids having direct relations with the given item_id
        :param item_id: a str, e.g.,"Q21"
        :param property_wd_id, a str starting with "P", e.g., "P279", standing "subclass of" relation
        :return: [] or set of ids.
        """
        item = self.item_cache.get(item_id, None)
        if item == None:
            return set()
        neighbours = item.get_neighbor_ids_by_relation(property_wd_id)
        return neighbours

    def get_all_neighbour_items_by_item_id(self, item_id):
        """
        get all wikidata item having direct relations with the given item_id
        :param item_id: a str, e.g.,"Q21"
        :return: [] or list of WikiDataItem. e.g., ["Q12","Q23"]
        """
        wd_ids = self.get_all_neighbour_ids_by_item_id(item_id)
        return self.get_wikidata_items_by_ids(wd_ids)

    def search_wd_ids_by_keywords(self, keywords: str):
        """
        get wikidata id list from the cache in this class instance by searching with the given str
        :param keywords: a str. e.g., "Java","JVM","java virtual machine"
        :return: a list of wikidata item id related to the keywords, e.g., ["Q212","Q3444"]       """
        ids = []
        titles = self.get_title_cache().get(keywords, None)
        if titles == None:
            return []

        for title in titles:
            ids.append(title["title"])
        return ids

    def search_wikidata_items_by_keywords(self, keywords: str):
        """
        get WikiDataItem list from the cache in this class instance by searching with the given str
        :param keywords: a str. e.g., "Java","JVM","java virtual machine"
        :return: a list of WikiDataItem related to the keywords
        """
        wd_ids = self.search_wd_ids_by_keywords(keywords)
        return self.get_wikidata_items_by_ids(wd_ids)
