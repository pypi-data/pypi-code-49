"""Utilities to scrape search results from Google Images."""
import asyncio
import json
import logging
import re
from typing import List

import aiohttp
import bs4

from . import utils


GOOGLE_SEARCH_ENDPOINT = "https://www.google.com/search"
LOG = logging.getLogger(__name__)


async def search_worker(
    index: int,
    session: aiohttp.ClientSession,
    search_queue: asyncio.Queue,
    download_queue: asyncio.Queue,
) -> None:
    worker_name = ".".join([__name__, "search_worker", str(index)])
    logger = logging.getLogger(worker_name)
    while True:
        query = await search_queue.get()
        logger.debug(f"read query '{query.query}'")
        params = (
            ("as_st", "y"),
            ("tbm", "isch"),
            ("hl", "en"),
            ("as_q", query.query),
            ("as_epq", ""),
            ("as_oq", ""),
            ("as_eq", ""),
            ("cr", ""),
            ("as_sitesearch", ""),
            ("safe", "images"),
            ("tbs", "itp:face" if query.face else "itp:photo"),
        )
        try:
            logger.debug(f"querying google for '{query.query}'")
            async with session.get(
                GOOGLE_SEARCH_ENDPOINT, params=params
            ) as response:
                logger.debug("fetched url %s", response.url)
                response_text = await response.text()
        except (aiohttp.ClientError, asyncio.TimeoutError) as err:
            logger.error(
                "could not query google images for %s (%s)",
                query.query,
                str(err),
            )
            response_text = ""
        logger.debug(f"done querying google for '{query}', parsing")
        found_images = parse_google_images_results(response_text, query)
        logger.info("found %d images querying for %s", len(found_images), query)
        for image_metadata in found_images:
            # logger.debug("putting %s onto download queue", result.url)
            await download_queue.put(image_metadata)
        logger.debug(f"done parsing results for query '{query}'")
        search_queue.task_done()


def parse_google_images_results(
    html: str, query: utils.GoogleImagesQuery
) -> List[utils.ImageMetadata]:
    LOG.debug("parsing Google Images results")
    dom = bs4.BeautifulSoup(html, "html.parser")
    for parser in [parse_results_type_a, parse_results_type_b]:
        results = parser(dom, query)
        if results:
            return results
    return []


def parse_results_type_a(
    dom: bs4.BeautifulSoup, query: utils.GoogleImagesQuery
) -> List[utils.ImageMetadata]:
    """Parse the prominent Google Images page data format as of 20200101."""
    results = []
    for result_div in dom.select("div.rg_meta.notranslate"):
        metadata = json.loads(result_div.text)
        results.append(
            utils.ImageMetadata(
                url=metadata["ou"],
                image_format=metadata["ity"],
                description=metadata["pt"],
                height=metadata["oh"],
                width=metadata["ow"],
                host=metadata["rh"],
                source=metadata["ru"],
                query=query,
            )
        )
    return results


def parse_results_type_b(
    dom: bs4.BeautifulSoup, query: utils.GoogleImagesQuery
) -> List[utils.ImageMetadata]:
    """Parse the prominent Google Images page data format as of 20200201."""
    results = []
    for script in dom.select("script"):
        script_text = script.get_text()
        script_text = script_text.replace("\n", " ")
        match = re.search(
            r"AF_initDataCallback\((.*?)return(.*)}}\);", script_text
        )  # reliable? looks like a huge blob of callback args
        data = None
        if match:
            data = json.loads(match.group(2))
            if len(data) < 2:
                continue
        else:
            continue
        for i, d in enumerate(data[31][0][12][2]):  # reliable? seems to work.
            try:
                url, height, width = d[1][3]
                results.append(
                    utils.ImageMetadata(
                        url=url,
                        image_format=None,
                        description=None,
                        height=height,
                        width=width,
                        host=None,
                        source=None,
                        query=query,
                    )
                )
            except TypeError:
                continue
    return results

