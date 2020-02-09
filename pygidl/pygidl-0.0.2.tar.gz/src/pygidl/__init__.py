import asyncio
import logging
import os
from timeit import default_timer as timer
from typing import List

from tqdm import tqdm

from . import download_images
from . import google_images
from . import utils
from .version import __version__
from .version import __version_info__


PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
PACKAGE_NAME = os.path.basename(PACKAGE_DIR)
LOG = logging.getLogger(PACKAGE_NAME)


async def scrape_google_images(
    base_query: str,
    prefixes: List[str],
    suffixes: List[str],
    group: str,
    output_dir: str,
    *,
    face: bool = False,
    num_search_tasks: int = 3,
    num_download_tasks: int = 100,
) -> List[str]:
    """Run queries through google images and download the results."""
    search_queue = asyncio.Queue()
    download_queue = asyncio.Queue()
    google_session = utils.create_default_session()
    http_session = utils.create_default_session()

    LOG.info("Starting Google Images searches")
    queries = utils.generate_queries(
        base_query, prefixes, suffixes, group, face
    )
    for query in queries:
        LOG.info(f"putting '{query.query}' onto search queue")
        await search_queue.put(query)
    search_time_start = timer()
    search_tasks = []
    for i in range(num_search_tasks):
        search_task = asyncio.create_task(
            google_images.search_worker(
                i, google_session, search_queue, download_queue
            )
        )
        search_tasks.append(search_task)
    LOG.debug("Waiting for all searches to finish")
    await search_queue.join()
    LOG.debug("Searches done, ending search tasks")
    for search_task in search_tasks:
        search_task.cancel()
    await asyncio.gather(*search_tasks, return_exceptions=True)
    LOG.debug("Search tasks ended, closing google session")
    await google_session.close()
    LOG.debug("Google session closed")
    search_time = timer() - search_time_start
    LOG.info("Done with Google Images searches, %.2fs", search_time)

    # The following block that starts download tasks could be moved
    # above the joining of the search queue to start downloading images
    # while more searches continue. This ordering was chosen in order
    # to have a synchronization point where the total number of expected
    # downloads could be read from the download queue -- see
    # https://github.com/tqdm/tqdm/wiki/How-to-make-a-great-Progress-Bar
    LOG.info("Starting image downloads")
    download_time_start = timer()
    progress_bar = tqdm(total=download_queue.qsize(), unit="images")
    seen_urls = set()
    downloaded_images = []
    download_tasks = []
    for i in range(num_download_tasks):
        download_task = asyncio.create_task(
            download_images.download_worker(
                i,
                http_session,
                download_queue,
                output_dir,
                progress_bar,
                seen_urls,
                downloaded_images,
            )
        )
        download_tasks.append(download_task)

    LOG.debug("Waiting for all downloads to finish")
    await download_queue.join()
    LOG.debug("Downloads done, ending downloads tasks")
    for download_task in download_tasks:
        download_task.cancel()
    await asyncio.gather(*download_tasks, return_exceptions=True)
    LOG.debug("Download tasks ended, closing http session")
    await http_session.close()
    LOG.debug("http session closed")
    download_time = timer() - download_time_start
    LOG.info("Done with image downloads, %.2fs", download_time)
    return downloaded_images
