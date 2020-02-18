"""Parses academic websites for their bibtex and converts to various formats."""
from dataclasses import dataclass
from urllib.parse import urljoin

from pybtex.database import parse_string  # type: ignore
from pyquery import PyQuery as pq  # type: ignore
import requests
import yaml


@dataclass
class BibTeXURLStrategy:
    """The strategy for finding the bib file URL.

    Attributes:
        strategy: one of {arxiv, nips}
    """

    strategy: str

    def bib_url(self, url: str) -> str:  # noqa: TYP101
        """Get the url of the bib file depending on the strategy."""
        page = requests.get(url)
        d = pq(page.content)
        if self.strategy == "arxiv":
            el = d('a:Contains("bibtex")')
            bib_page_url = el.attr["href"]
            page = requests.get(bib_page_url)
            d = pq(page.content)
            el = d('a[href$=".bib"]')
            return el.attr["href"]
        elif self.strategy == "nips":
            el = d('a:Contains("BibTeX")')
            return urljoin(url, el.attr["href"])
        else:
            raise ValueError("Invalid strategy")


@dataclass
class BibTeXPage:
    """A webpage that contains BibTeX.

    Attributes:
        url: The original url
        strategy: A BibTeXURLStrategy to obtain the bib url
    """

    url: str
    strategy: BibTeXURLStrategy

    def bibtex_url(self) -> str:  # noqa: TYP101
        """Get the URL of the bibtex file."""
        return self.strategy.bib_url(url=self.url)

    def bibtex(self) -> str:  # noqa: TYP101
        """Get the bibtex as a string."""
        page = requests.get(self.bibtex_url())
        return str(page.content.decode("utf-8"))

    def as_yaml(self) -> str:  # noqa: TYP101
        """Get the bibtex as yaml."""
        d = parse_string(self.bibtex(), bib_format="bibtex")
        s = yaml.load(d.to_string(bib_format="yaml"), Loader=yaml.SafeLoader)
        return yaml.dump(list(s["entries"].values())[0])

    def as_dict(self) -> dict:  # noqa: TYP101
        """Get the bibtex as a dictionary."""
        d = parse_string(self.bibtex(), bib_format="bibtex")
        try:
            res = d.entries.values()[0].fields
        except IndexError:
            res = dict()
        return dict(res)
