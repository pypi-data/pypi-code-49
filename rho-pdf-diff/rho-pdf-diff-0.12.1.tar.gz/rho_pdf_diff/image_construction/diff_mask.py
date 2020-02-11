import logging

import attr
from reportlab.lib.colors import Color
from reportlab.pdfgen.canvas import Canvas
from typing import List, Iterator, Union, Dict, BinaryIO

from rho_pdf_diff.document import Word, Page
from rho_pdf_diff.text_diff import Diff

logger = logging.getLogger(__name__)


def build_blank_page_image(width: float,
                           height: float,
                           file: Union[str, BinaryIO]) -> Canvas:
    """ Return a blank canvas of given dimensions, which will ultimately save
    to the file (filename or writeable file object.) """
    c = Canvas(file, pagesize=(width, height), bottomup=False)
    return c


class SpanStyle(object):
    """ Base class for determining how to draw a diff (e.g. bounding rectangle,
    strikethrough, underline, color, etc.).  Typically there will be one
    DiffStyle for additions and one for removals. """
    
    def mark_one_span(self, words: List[Word], canvas: Canvas) -> Canvas:
        """ Define how to draw a diff on a document, given the diffs have
        already been split into lines. """
        raise NotImplementedError
    
    @staticmethod
    def split_words_to_boxes(words: List[Word], line_height_tolerance: float) \
            -> Iterator[List[Word]]:
        """ If e.g. a line break is in the middle of a span of words, we
        need to ensure the words on each line are marked up separately. """
        if words:
            last_word = words[0]
            chunk = []
            for word in words:
                word_height = last_word.height
                last_y = last_word.y_min
                current_y = word.y_min
                if abs(last_y - current_y) < line_height_tolerance * word_height:
                    chunk.append(word)
                else:
                    yield chunk
                    chunk = [word]
                last_word = word
            if chunk:
                yield chunk  # need to ensure last chunk of words is yielded
    
    def mark_words(self, words: List[Word], canvas: Canvas,
                   line_height_tolerance: float = 0.05) -> Canvas:
        continuous_chunks = self.split_words_to_boxes(
            words=words, line_height_tolerance=line_height_tolerance)
        for chunk in continuous_chunks:
            if chunk:
                canvas = self.mark_one_span(words=chunk, canvas=canvas)
        return canvas


@attr.s(auto_attribs=True)
class HighlightStyle(SpanStyle):
    color: Color  # set w/ RGBA, CMYK, etc.
    
    def mark_one_span(self, words: List[Word], canvas: Canvas) -> Canvas:
        x_min = words[0].x_min
        x_max = words[-1].x_max
        width = x_max - x_min
        y_min = words[0].y_min
        y_max = words[0].y_max
        height = y_max - y_min
        canvas.setFillColor(self.color)
        canvas.setStrokeColor(self.color)
        canvas.rect(x=x_min, y=y_min, width=width, height=height, fill=1)
        return canvas


def extract_words_on_page_from_diff(diff: Diff, page_num: int) -> List[Word]:
    """ Diffs can span multiple pages, but we're drawing diff overlays one
    page at a time. """
    return [word for word in diff.words if word.page_number == page_num]


def build_page_diff_overlay(page: Page,
                            diffs: List[Diff],
                            style_map: Dict[str, SpanStyle],
                            file: Union[str, BinaryIO]) -> Canvas:
    """ Combines text and bounding box info from a Page and Diff objects with
    information about how to draw bounding boxes in a file.  This image doesn't
    contain doc text, but is an overlay to put on top of the actual doc.

    The file (filename or file object) is necessary here because reportlab's
    Canvas requires it knows where to write to at instantiation """
    
    logger.debug("Drawing overlay for {0} diffs...".format(len(diffs)))
    canvas = build_blank_page_image(
        width=page.width, height=page.height, file=file)
    
    for diff in diffs:
        page_words = extract_words_on_page_from_diff(diff=diff,
                                                     page_num=page.page_number)
        diff_style = style_map[diff.diff_type]
        canvas = diff_style.mark_words(words=page_words, canvas=canvas)
    
    return canvas
