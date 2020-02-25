"""Crawl module for CLI.

  Typical usage example:

  crawl_command = CrawlCommand()
  crawl_command.run()
"""
import time
from argparse import ArgumentParser, Namespace
from timeit import default_timer

from ekrhizoc.bot.crawlers import UniversalBfsCrawler
from ekrhizoc.bot.helpers import url_utils
from ekrhizoc.cli.base_command import BaseCommand
from ekrhizoc.logging import logger


class CrawlCommand(BaseCommand):
    """Initialise crawl command.

    Example:
        ekrhizoc crawl -s "http://example.com"
    """

    def __init__(self):
        super(CrawlCommand, self).__init__()
        self.name = "crawl"

    def add_args(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "-s",
            "--seed",
            required=True,
            help="The seed URL (root, initial url to crawl from)",
        )

        parser.add_argument(
            "-f",
            "--filename",
            required=False,
            default=time.strftime("%Y%m%d-%H%M%S"),
            help="The filename to use as the output file",
        )

    def validate_args(self, args: Namespace) -> None:
        """Check command given argument, seed.

        Requires a non-empty seed.

        Raises:
            Exception: If seed url is not valid.
        """
        if url_utils.get_full_url(args.seed) == "":
            raise Exception(f'The given seed "{args.seed}" is an invalid url.')

    def execute(self, args: Namespace) -> None:
        start_time = default_timer()
        self.crawl(args.seed, args.filename)
        elapsed_time = default_timer() - start_time
        logger.debug(f'Command "{self.name}" took {elapsed_time:.2f} seconds.')

    def crawl(self, seed: str = "", filename: str = "") -> None:
        """Calls the crawl bot with the provided seed url.

        Execute crawl, write output structure and graph image.

        Args:
            seed: The given argument of the command.
            filename: The file name for the output of the command.
        """
        crawler = UniversalBfsCrawler(seeds=[seed], output=filename)
        logger.debug(f'Use "{crawler.name}" crawler with seed urls: "{seed}"')
        crawler.crawl()
        crawler.write_output()
        crawler.draw_output()
