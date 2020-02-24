import time
from typing import Any, List, Set

from ekrhizoc.bot.helpers import url_utils
from ekrhizoc.settings import IGNORE_FILETYPES


class BaseCrawler:
    def __init__(self):
        self._name = ""
        self._seeds = []
        self._domains = []
        self._ignore_filetypes = set((~IGNORE_FILETYPES).split(","))
        self._visited_urls = set()
        self._to_visit_urls = []
        self._output = ""

    @property
    def name(self) -> str:
        """Getter for name attribute.

        If no name is set, use the module's name.

        Returns:
            The value of the name attribute.
        """
        if "".__eq__(self._name):
            return self.__module__.split(".")[-1].replace("_", "-")
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Setter for name attribute.

        Args:
            value: The value to set the name attribute.
        """
        self._name = value

    @property
    def seeds(self) -> List:
        """Getter for seeds attribute.
        
        Returns:
            The list of the seeds attribute.
        """
        return self._seeds

    @seeds.setter
    def seeds(self, value: List) -> None:
        """Setter for seeds attribute.

        Add to the seeds list all the given seed url
        in their canonicalised form (full url).
        Add to domain list all domains of seeds.

        Args:
            value: The list of seeds.
        """
        for seed in value:
            canonical_url = url_utils.get_full_url(seed)
            self._seeds.append(canonical_url)
            domain = url_utils.get_url_domain(canonical_url)
            if domain not in self._domains:
                self._domains.append(domain)

    @property
    def domains(self) -> List:
        """Getter for domains attribute.
        
        Returns:
            The list of the domains attribute.
        """
        return self._domains

    @property
    def ignore_filetypes(self) -> Set:
        """Getter for ignore filetypes attribute.
        
        Returns:
            The set of the ignore filetypes attribute.
        """
        return self._ignore_filetypes

    @property
    def visited_urls(self) -> Set:
        """Getter for visited urls attribute.
        
        Returns:
            The set of the visited urls attribute.
        """
        return self._visited_urls

    @visited_urls.setter
    def visited_urls(self, value: Set) -> None:
        """Setter for visited urls attribute.

        Args:
            value: The value to set the visited urls attribute.
        """
        self._visited_urls = value

    @property
    def to_visit_urls(self) -> Any:
        """Getter for urls to visit attribute.
        
        Returns:
            The urls to visit attribute (open to Any type).
        """
        return self._to_visit_urls

    @to_visit_urls.setter
    def to_visit_urls(self, value: Any) -> None:
        """Setter for urls to visit attribute.

        Args:
            value: The value to set the urls to visit attribute.
        """
        self._to_visit_urls = value

    @property
    def output(self) -> str:
        """Getter for output attribute.

        If no output is set, use a datetime stamp.

        Returns:
            The value of the output attribute.
        """
        if "".__eq__(self._output):
            return time.strftime("%Y%m%d-%H%M%S")
        return self._output

    @output.setter
    def output(self, value: str) -> None:
        """Setter for output attribute.

        Args:
            value: The value to set the output attribute.
        """
        self._output = value

    def _fetch_page(self, session: Any = None, url: str = "") -> Any:
        """Fetch url page data via a request.

        Args:
            session: Client session for making HTTP requests.
            url: The url to fetch.

        Returns:
            The page data (open to Any type).

        Raises:
            NotImplementedError: If this method is used but not
                defined in the subcommand class. 
        """
        raise NotImplementedError(
            f"Private Method: _fetch_page is undefined for crawler {self.name}"
        )

    def _scrape_links(self, raw_html: Any = None) -> List:
        """Search for links in the url page.

        Args:
            raw_html: The raw html source code of the page.

        Returns:
            A list of found links.

        Raises:
            NotImplementedError: If this method is used but not
                defined in the subcommand class. 
        """
        raise NotImplementedError(
            f"Private Method: _parse_page is undefined for crawler {self.name}"
        )

    def _fetch_links(self, session: Any = None, url: str = "") -> None:
        """Logic function to retrieve url links.

        Args:
            session: Client session for making HTTP requests.
            url: The url to fetch links from.

        Raises:
            NotImplementedError: If this method is used but not
                defined in the subcommand class. 
        """
        raise NotImplementedError(
            f"Private Method: _fetch_links is undefined for crawler {self.name}"
        )

    def crawl(self):
        """The bot entrypoint command.

        Raises:
            NotImplementedError: If this method is used but not
                defined in the subcommand class. 
        """
        raise NotImplementedError(f"Method: crawl is undefined for crawler {self.name}")
