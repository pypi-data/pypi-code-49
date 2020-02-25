"""Universal breadth first search graph traversal crawler module.

  Typical usage example:

  crawler = UniversalBfsCrawler(seeds=["http://example.com"])
  crawler.crawl()
"""
import asyncio
import os
import queue
from http import HTTPStatus
from pathlib import Path
from typing import Any, List

import aiohttp
import matplotlib.pyplot as plt
import networkx as nx
from bs4 import BeautifulSoup

from ekrhizoc.bot.base_crawler import BaseCrawler
from ekrhizoc.bot.helpers import url_utils
from ekrhizoc.logging import logger
from ekrhizoc.settings import BIN_DIR, MAX_URLS, URL_REQUEST_TIMER


class UniversalBfsCrawler(BaseCrawler):
    """
    Initialise crawler bot.
    """

    def __init__(self, seeds: List = [], output: str = ""):
        super(UniversalBfsCrawler, self).__init__()
        self.name = "universal-bfs"
        self.seeds = seeds
        self.visited_urls = set()
        self.to_visit_urls = queue.Queue()
        self.output = output
        self._graph = nx.DiGraph()

    async def _fetch_page(self, session: Any = None, url: str = "") -> bytes:
        """Asynchronous implementation.

        For every fetch call, the function will sleep for
        URL_REQUEST_TIMER seconds.
        Handles exception raised for when retrieval of page fails.

        Returns:
            The page contents in bytes.
        """
        if not url:
            return None
        await asyncio.sleep(~URL_REQUEST_TIMER)
        try:
            async with session.get(url) as response:
                if response.status == HTTPStatus.OK.value:
                    return await response.read()
                return None
        except Exception as e:
            logger.error(e)
            return None

    async def _scrape_links(self, raw_html: bytes = b"") -> List:
        """Asynchronous implementation.

        Use of an htlm parser library to pick up hyperlinks by
        searching for HTML anchor tags <a>.
        """
        extracted_links = []
        if not raw_html:
            return extracted_links

        parser = BeautifulSoup(raw_html, "html.parser")
        extracted_links = parser.find_all("a")
        return extracted_links

    async def _is_valid_url(self, url: str = "", domain: str = "") -> bool:
        """Asynchronous helper function.

        Check urls against the below rules.
            * URL is valid:
                - non-empty
                - matches a valid url pattern
                - does not exceed the MAX_URL_LENGTH length in characters
                - possible to convert a relative urls to a full url
            * URL is not visited before
            * URL is not part of an ignored file type
            * URL has the same domain as the seed url
            * URL is not restricted by the robots.txt file
        """
        if not url:
            logger.debug("Invalid url: skipping...")
            return False

        if url in self.visited_urls:
            logger.debug(f"Visited already: skipping url {url}")
            return False

        _, file_type = os.path.splitext(url)
        if file_type in self.ignore_filetypes:
            logger.debug(f"Ignore url with file type: {file_type} (full url: {url})")
            return False

        if domain and not url_utils.is_same_subdomain(url, domain):
            logger.debug(f"Different domain: skipping url {url}")
            return False

        if domain and url_utils.is_robots_restricted(url):
            logger.debug(f"Restricted by robots.txt: skipping url {url}")
            return False

        return True

    async def _fetch_links(self, session: Any = None, url: str = "") -> None:
        """Asynchronous implementation.

        Checks if urls are valid, if request returned any data and searches
        for any valid links. Valid links are then added in a FIFO queue.
        A graph is also constructed with nodes, edges.
        """
        valid_url = await self._is_valid_url(url)
        if not valid_url:
            return

        logger.info(f"Fetching {url}")

        page_content = await self._fetch_page(session, url)
        if not page_content:
            logger.debug(f"No content found for {url}")
            return

        self.visited_urls.add(url)

        links = await self._scrape_links(page_content)
        if not links:
            logger.debug(f"No links found for {url}")
            return

        for domain in self.domains:
            for link in links:
                link_href = link.get("href", "")
                canonical_link = url_utils.get_full_url(link_href, url)
                valid_link = await self._is_valid_url(canonical_link, domain)
                if not valid_link:
                    continue

                self.to_visit_urls.put(canonical_link)
                self._graph.add_node(canonical_link)
                self._graph.add_edge(url, canonical_link)

    async def _crawl(self):
        """Asynchronous implementation.

        Assign seeds as the root nodes of the graph.
        """
        tasks = []
        for seed in self.seeds:
            logger.debug(f"Add seed {seed}")
            self.to_visit_urls.put(seed)
            self._graph.add_node(seed)

        logger.debug("Start async requests...")
        async with aiohttp.ClientSession() as session:
            while not self.to_visit_urls.empty() and len(self.visited_urls) < ~MAX_URLS:
                if len(self.to_visit_urls.queue) % 100 == 0:
                    logger.debug(f"Queued urls: {len(self.to_visit_urls.queue)}")
                url = self.to_visit_urls.get()
                task = asyncio.ensure_future(self._fetch_links(session, url))
                tasks.append(task)
                _ = await asyncio.gather(*tasks)

    def crawl(self):
        """Entrypoint.

        Implement an asynchronous fetching of urls.
        Once all tasks finish, return.
        """
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self._crawl())
        loop.run_until_complete(future)
        loop.close()
        logger.debug(
            f"Unfetched (queued) urls ({len(self.to_visit_urls.queue)}): {list(self.to_visit_urls.queue)}"
        )
        logger.debug(f"Fetched urls: {list(self.visited_urls)}")
        logger.info(f"URL pages fetched: {len(self.visited_urls)}")

    def write_output(self):
        """Write the structure of a graph to the output file as yaml."""
        filepath = Path(~BIN_DIR) / (self.output + ".yaml")
        nx.write_yaml(self._graph, filepath)
        logger.info(f"Graph structure output can be found here: {filepath}")

    def draw_output(self):
        """Write the graph image of a graph to the output file as png."""
        filepath = Path(~BIN_DIR) / (self.output + ".png")
        nx.draw(self._graph)
        plt.savefig(filepath)
        logger.info(f"Graph image output can be found here: {filepath}")
