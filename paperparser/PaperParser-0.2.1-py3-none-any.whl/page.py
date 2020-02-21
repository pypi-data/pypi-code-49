"""Parses academic websites for their bibtex and converts to various formats."""
from dataclasses import dataclass

from pybtex.database import parse_string  # type: ignore

from .abstract_parser import abstract
from .bibtex_parser import bibtex


@dataclass
class BibTeXPage:
    """A webpage that contains BibTeX.

    Attributes:
        url: The original url
        strategy: A strategy to obtain the bib url
    """

    url: str
    strategy: str

    def abstract(self) -> str:  # noqa: TYP101
        """Get the abstract of the bibtex file."""
        return abstract(self.strategy, self.url)

    def bibtex(self) -> str:  # noqa: TYP101
        """Get the bibtex as a string."""
        return bibtex(self.strategy, self.url)

    def as_dict(self) -> dict:  # noqa: TYP101
        """Get the bibtex as a dictionary."""
        d = parse_string(self.bibtex(), bib_format="bibtex")
        try:
            res = d.entries.values()[0].fields
        except IndexError:
            res = dict()
        return dict(res)
