"""Define workers and helper functions for downloading a list of image urls."""
import asyncio
import hashlib
import imghdr
import logging
import os
import shutil
from typing import List, Optional, Set

import aiohttp
from tqdm import tqdm

from . import utils


ALLOWED_FORMATS = set(["png", "jpg", "jpeg", "webp"])
LOG = logging.getLogger(__name__)


async def download_image(
    session: aiohttp.ClientSession,
    output_dir: str,
    image_metadata: utils.ImageMetadata,
) -> Optional[str]:
    """Download an image file from a given url to the filesystem."""
    save_dir = os.path.join(
        output_dir,
        image_metadata.query.group_slug,
        image_metadata.query.query_slug,
    )
    os.makedirs(save_dir, exist_ok=True)
    url_hash = utils.sha256_string(image_metadata.url)
    save_filename = f"{url_hash}.{image_metadata.image_format}"
    save_path = os.path.join(save_dir, save_filename)
    sha256 = await download_file(session, image_metadata.url, save_path)
    if not sha256:
        return None
    try:
        if not os.path.exists(save_path):
            LOG.warning("Some filesystem problem! Sleeping...")
            await asyncio.sleep(0.5)
        image_format = imghdr.what(save_path)
        if not image_format:
            if image_metadata.image_format:
                image_format = image_metadata.image_format.lower()
            else:
                image_format = None
        if image_format not in ALLOWED_FORMATS:
            LOG.warning("Bad file type, skipping %s", image_metadata.url)
            os.unlink(save_path)
            return None
        final_filename = f"{sha256}.{image_format}"
        final_path = os.path.join(save_dir, final_filename)
        shutil.move(save_path, final_path)
    except FileNotFoundError:
        LOG.error("%s, %s", image_metadata, sha256)
        final_path = None
    return final_path


async def download_file(
    session: aiohttp.ClientSession,
    url: str,
    path: str,
    chunk_size: int = 2 ** 14,
    timeout: int = 10,
) -> bool:
    """Fetch a file from a given url and download it to the filesystem."""
    sha256 = hashlib.sha256()
    try:
        async with session.get(url, timeout=timeout) as response:
            response.raise_for_status()
            with open(path, "wb") as save_file:
                while True:
                    chunk = await response.content.read(chunk_size)
                    if not chunk:
                        break
                    sha256.update(chunk)
                    save_file.write(chunk)
    except aiohttp.ClientResponseError as err:
        LOG.warning("Could not fetch %s [%d %s]", url, err.status, err.message)
        return None
    except aiohttp.ClientError as err:
        LOG.warning("Could not fetch %s [%s]", url, type(err).__name__)
        return None
    except asyncio.TimeoutError as err:
        LOG.warning("Could not fetch %s: %s", url, "timed out")
        return None
    return sha256.hexdigest()


async def download_worker(
    index: int,
    session: aiohttp.ClientSession,
    download_queue: asyncio.Queue,
    output_dir: str,
    progress_bar: tqdm,
    seen_urls: Set[str],
    downloaded_images: List[str],
) -> None:
    """Loop that pulls urls off of a queue and downloads them."""
    worker_name = ".".join([__name__, "download_worker", str(index)])
    logger = logging.getLogger(worker_name)
    while True:
        image_metadata = await download_queue.get()
        if image_metadata.url in seen_urls:
            logger.debug("skipping %s, already seen", image_metadata.url)
        else:
            seen_urls.add(image_metadata.url)
            logger.debug("downloading %s", image_metadata.url)
            image_path = await download_image(
                session, output_dir, image_metadata
            )
            if image_path:
                downloaded_images.append(image_path)
        download_queue.task_done()
        progress_bar.update()

