"""Download images from Google Images search results."""
import asyncio
import argparse
from datetime import datetime
import logging
import os
import sys
from timeit import default_timer as timer
from typing import Optional

import pygidl

LOG = logging.getLogger(pygidl.PACKAGE_NAME)


def main(args: Optional[argparse.Namespace] = None) -> None:
    """
    1. Parse command line args and configs.
    2. Create google images queries
    3. Use google images results to create images queue
    4. Process images queue to download all files
    """
    if not args:
        parser = build_parser()
        args = parser.parse_args()
    configure_logging(args.verbose)
    LOG.debug(args)
    downloaded_images = asyncio.run(
        pygidl.scrape_google_images(
            base_query=args.query,
            prefixes=args.prefix,
            suffixes=args.suffix,
            group=args.group,
            output_dir=args.output_dir,
            face=args.face,
            num_search_tasks=args.num_search_tasks,
            num_download_tasks=args.num_download_tasks,
        )
    )
    LOG.info("Downloaded %d images", len(downloaded_images))


def configure_logging(verbosity: int = 0) -> None:
    """Configure logging to standard error."""
    log_level = logging.WARNING
    if verbosity == 1:
        log_level = logging.INFO
    elif verbosity >= 2:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)


def build_parser() -> argparse.ArgumentParser:
    """Create a command-line argument parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-d",
        "--num-download-tasks",
        type=int,
        default=100,
        help="number of concurrent image url downloaders",
    )
    parser.add_argument(
        "-f",
        "--face",
        action="store_true",
        help="search for face images",
    )
    parser.add_argument(
        "-g",
        "--group",
        default=datetime.now().strftime("%Y-%m-%d--%H-%M-%S"),
        help="group to save query results under (defaults to timestamp)",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default=os.getcwd(),
        help="base directory to save outputs",
    )
    parser.add_argument(
        "-p",
        "--prefix",
        default=[],
        action="append",
        help="prefixes to re-run the main queries with",
    )
    parser.add_argument(
        "-s",
        "--suffix",
        default=[],
        action="append",
        help="suffixes to re-run the main queries with",
    )
    parser.add_argument(
        "-t",
        "--num-search-tasks",
        type=int,
        default=3,
        help="number of concurrent google image scrapers",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="increase output verbosity",
    )
    parser.add_argument("query", help="query term")
    return parser


if __name__ == "__main__":
    main()
