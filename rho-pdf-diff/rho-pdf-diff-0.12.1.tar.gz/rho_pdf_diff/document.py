""" Data structures which capture text and location data given by the
pdftotext tool"""
import logging
from typing import List, Dict

import attr
from bs4 import Tag

logger = logging.getLogger(__name__)


# todo: write decorator to log input when one of the `from_*` classmethods fails
#  unexpectedly

# todo: evaluate the code in pdf_to_bboxes from command_line.py to see if we
#  want to reproduce the codes_to_avoid logic

@attr.s(auto_attribs=True)
class Word(object):
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    raw_text: str
    word_idx: int
    page_number: int

    @classmethod
    def from_xml(cls, word_tag: Tag, word_idx: int, page_number: int):
        """ From a <word> XML tag parsed by bs4 (lxml-xml parser)
        """
        try:
            return cls(
                x_min=float(word_tag['xMin']),
                x_max=float(word_tag['xMax']),
                y_min=float(word_tag['yMin']),
                y_max=float(word_tag['yMax']),
                raw_text=word_tag.text,
                word_idx=word_idx,
                page_number=page_number
            )
        except Exception as e:
            logger.exception(e)
            logger.warning(word_tag)

    @property
    def width(self) -> float:
        return self.x_max - self.x_min

    @property
    def height(self) -> float:
        return self.y_max - self.y_min

    @property
    def stripped_text(self) -> str:
        return self.raw_text.strip()

    @property
    def has_eol_hyphen(self) -> bool:
        return (self.stripped_text.endswith('-') or
                self.stripped_text.endswith('\u00AD'))

    @property
    def text(self):
        if not self.has_eol_hyphen:
            result = self.stripped_text + ' '
        else:
            result = self.stripped_text
        return result



@attr.s(auto_attribs=True)
class Page(object):
    words: List[Word] = attr.ib(repr=False)
    width: float
    height: float
    page_number: int

    @property
    def full_text(self) -> str:
        """ Get the text of the current page as the text of each Word separated
        by spaces """
        return ''.join((word.text for word in self.words))

    @classmethod
    def from_xml(cls, page_tag: Tag, page_number: int):
        """ From a <page> tag parsed by bs4 """
        word_tags = page_tag.find_all('word')
        words = [Word.from_xml(t, word_idx=i, page_number=page_number) for i, t
                 in enumerate(word_tags)]
        try:
            return cls(
                words=words,
                width=float(page_tag['width']),
                height=float(page_tag['height']),
                page_number=page_number
            )
        except Exception as e:
            logger.exception(e)
            logger.warning("Failed trying to build Page!")


@attr.s(auto_attribs=True)
class CharacterToWordMap(object):
    """ Maps a character index relative to the full document to a word index
    relative to the full document. """
    start_idx_map: Dict[int, int]

    def __getitem__(self, item: int) -> int:
        word_idx = None
        current_char_idx = item
        while word_idx is None:
            word_idx = self.start_idx_map.get(current_char_idx)
            if word_idx is None:
                current_char_idx -= 1
                if current_char_idx < 0:
                    raise ValueError("No word found at or before character "
                                     "index {0}!".format(item))
        return word_idx

    def __setitem__(self, key: int, value: int):
        self.start_idx_map[key] = value

    @classmethod
    def from_words(cls, words: List[Word]):
        logger.info("Building character to word map...")
        start_idx_map = {}
        char_idx = 0
        for i, word in enumerate(words):
            start_idx_map[char_idx] = i
            char_idx += len(word.text)
        return cls(start_idx_map=start_idx_map)


@attr.s(auto_attribs=True)
class Document(object):
    pages: List[Page]
    character_to_word_map: CharacterToWordMap = attr.ib(init=False, repr=False)
    words: List[Word] = attr.ib(init=False, repr=False)

    def __attrs_post_init__(self):
        self.words = [word for page in self.pages for word in page.words]
        self.character_to_word_map = CharacterToWordMap.from_words(
            words=self.words)

    @property
    def page_count(self):
        return len(self.pages)

    @property
    def full_text(self) -> str:
        """ Get the text of the document as the value of each Page.full_text
        separated by spaces

        Override this if there are special preprocessing rules (e.g. lowercase
        everything before running text diff). """
        return ''.join((word.text for word in self.words))

    @classmethod
    def from_xml(cls, doc_tag: Tag):
        """ Takes a <doc> XML tag parsed by bs4 """
        page_tags = doc_tag.find_all('page')
        pages = [Page.from_xml(page_tag=t, page_number=i) for i, t
                 in enumerate(page_tags, start=1)]
        return cls(pages=pages)
