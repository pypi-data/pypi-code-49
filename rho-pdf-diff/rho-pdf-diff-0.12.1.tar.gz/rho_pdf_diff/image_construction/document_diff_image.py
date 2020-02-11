import collections
import itertools
import logging
import tempfile
from typing import List, Iterator, Tuple, Dict

import attr
import pdfrw
from reportlab.lib.colors import Color
from toolz import take

from rho_pdf_diff.document import Document
from rho_pdf_diff.document_creation import build_document
from rho_pdf_diff.filter_rules import CapitalizationFilter, PunctuationFilter
from rho_pdf_diff.image_construction.annealing_page_alignment import PageAlignment
from rho_pdf_diff.image_construction.diff_mask import SpanStyle, HighlightStyle, \
    build_page_diff_overlay, build_blank_page_image
from rho_pdf_diff.text_diff import DiffResult, Diff

logger = logging.getLogger(__name__)


def get_diffs_on_page(diffs: List[Diff], page_num: int) -> List[Diff]:
    return [diff for diff in diffs if (diff.begin_page <= page_num) and
            (diff.end_page >= page_num)]


class DiffImageError(Exception):
    def __init__(self, error_msg):
        print(error_msg)

    pass


# todo: break into overlay_one_page or similar
# todo: need a way for a padding page to be used in either new or old doc
def set_overlay_on_pages(doc: Document,
                         diffs: List[Diff],
                         original_doc_path: str,
                         style_map: Dict[str, SpanStyle]) \
        -> List[pdfrw.PdfDict]:
    original_pdf = NewPdfReader(original_doc_path)

    if doc.page_count > len(original_pdf.pages):
        error_msg = "Failed to produce diff involving {}. PDFReader stopped " \
                    "before the end of the file." \
            .format(original_doc_path)
        raise DiffImageError(error_msg)

    pages_with_overlay = []

    for page_num, (page, pdf_page) in enumerate(
            zip(doc.pages, original_pdf.pages), start=1):
        page_diffs = get_diffs_on_page(diffs=diffs, page_num=page_num)
        with tempfile.NamedTemporaryFile(suffix='.pdf') as tmp:
            overlay_canvas = build_page_diff_overlay(
                page=page, diffs=page_diffs, style_map=style_map,
                file=tmp.name)
            overlay_canvas.showPage()
            overlay_canvas.save()
            overlay_pdf = NewPdfReader(tmp.name)
            merged = pdfrw.PageMerge(pdf_page).add(
                overlay_pdf.pages[0], prepend=False).render()
            pages_with_overlay.append(merged)
    return pages_with_overlay


def build_empty_filler_page(width: int, height: int) -> pdfrw.PdfDict:
    # todo: write some watermark image on blank page indicating the page wasn't
    #  in the original
    with tempfile.NamedTemporaryFile(suffix='.pdf') as tmp:
        canvas = build_blank_page_image(
            width=width, height=height, file=tmp.name)
        canvas.drawString(10, 10, "<Blank filler page>")
        canvas.showPage()
        canvas.save()
        pdf = NewPdfReader(tmp.name)
    pdf_page = pdf.pages[0]
    return pdf_page


@attr.s(auto_attribs=True)
class DiffImageWriter(object):
    original_new_doc_path: str
    original_old_doc_path: str
    diff_result: DiffResult
    style_map: Dict[str, SpanStyle] = None
    align_pages: bool = True
    page_alignment: PageAlignment = attr.ib(init=False)

    def __attrs_post_init__(self):
        if self.align_pages:
            self.page_alignment = PageAlignment(
                old_pages=self.diff_result.old_doc.pages,
                new_pages=self.diff_result.new_doc.pages)
            self.page_alignment.set_alignment()
        if self.style_map is None:
            red = Color(red=0.883, green=0.445, blue=0.414, alpha=0.3)
            yellow = Color(red=0.887, green=0.895, blue=0.355, alpha=0.3)
            green = Color(red=0.477, green=0.934, blue=0.484, alpha=0.3)
            self.style_map = {
                'solo_insertion': HighlightStyle(color=green),
                'solo_deletion': HighlightStyle(color=red),
                'change_insertion': HighlightStyle(color=yellow),
                'change_deletion': HighlightStyle(color=yellow)
            }

    def get_diff_page_pairs(self) -> Iterator[Tuple[pdfrw.PdfDict, pdfrw.PdfDict]]:
        new_doc_pdf_pages = set_overlay_on_pages(
            doc=self.diff_result.new_doc,
            diffs=self.diff_result.insertion_diffs,
            original_doc_path=self.original_new_doc_path,
            style_map=self.style_map)
        old_doc_pdf_pages = set_overlay_on_pages(
            doc=self.diff_result.old_doc,
            diffs=self.diff_result.deletion_diffs,
            original_doc_path=self.original_old_doc_path,
            style_map=self.style_map)

        page_width = int(self.diff_result.old_doc.pages[0].width)
        page_height = int(self.diff_result.old_doc.pages[0].height)
        blank_page = build_empty_filler_page(width=page_width,
                                             height=page_height)
        if self.align_pages:
            new_doc_pdf_pages = insert_blank_pages(
                pdf_pages=new_doc_pdf_pages,
                insertion_map=self.page_alignment.new_doc_insert_after,
                fill_page=blank_page)
            old_doc_pdf_pages = insert_blank_pages(
                pdf_pages=old_doc_pdf_pages,
                insertion_map=self.page_alignment.old_doc_insert_after,
                fill_page=blank_page)
        page_pairs = itertools.zip_longest(old_doc_pdf_pages, new_doc_pdf_pages,
                                           fillvalue=blank_page)
        yield from page_pairs

    def write_diff_pdf(self, output_path: str):
        x_offset = int(max(self.diff_result.new_doc.pages[0].width, self.diff_result.old_doc.pages[0].width))
        writer = pdfrw.PdfWriter()
        try:
            for old_page, new_page in self.get_diff_page_pairs():
                pages = pdfrw.PageMerge() + (old_page, new_page)
                pages[1].x = x_offset
                writer.addpage(pages.render())

        except pdfrw.errors.PdfNotImplementedError:
            error_msg = "Failed to produce diff between {} and {}. Xobjects with these compression parameters " \
                        "not supported: {{'/Length', '/Filter'}}".format(self.original_old_doc_path,
                                                                         self.original_new_doc_path)
            raise DiffImageError(error_msg)

        except ValueError:
            error_msg = "Failed to produce diff between {} and {}. PDF stream objects formatted incorrectly. " \
                .format(self.original_old_doc_path, self.original_new_doc_path)
            raise DiffImageError(error_msg)

        except pdfrw.errors.PdfParseError:
            error_msg = "Failed to produce diff between {} and {}. PDF failed to parse correctly. ".format(
                self.original_old_doc_path, self.original_new_doc_path)
            raise DiffImageError(error_msg)

        except FileNotFoundError:
            error_msg = "Failed to produce diff between {} and {}. Path to pdf lead to invalid/non-existent file. " \
                .format(
                self.original_old_doc_path, self.original_new_doc_path)
            raise DiffImageError(error_msg)

        writer.write(output_path)


def insert_blank_pages(pdf_pages: List[pdfrw.PdfDict],
                       insertion_map: collections.Counter,
                       fill_page: pdfrw.PdfDict) -> List[pdfrw.PdfDict]:
    """ Insert blank pages after any page in the insertion map with a value
    greater than 0. """

    def get_n_pads(n: int) -> List[pdfrw.PdfDict]:
        return list(take(n, itertools.repeat(fill_page)))

    result = []
    first_page_insertions = insertion_map.get(0, 0)
    first_page_pads = get_n_pads(first_page_insertions)
    result += first_page_pads
    for page_num, content_page in enumerate(pdf_pages, start=1):
        result.append(content_page)
        page_insertions = insertion_map.get(page_num, 0)
        pads = get_n_pads(n=page_insertions)
        result += pads
    return result


class NewPdfReader(pdfrw.PdfReader):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def findxref(self, fdata):
        ''' Find the cross reference section at the end of a file
        '''
        startloc = fdata.rfind('startxref')
        if startloc < 0:
            raise pdfrw.PdfParseError('Did not find "startxref" at end of file')
        source = pdfrw.tokens.PdfTokens(fdata, startloc, False, self.verbose)
        tok = source.next()
        assert tok == 'startxref'  # (We just checked this...)
        tableloc = source.next_default()
        if not tableloc.isdigit():
            source.exception('Expected table location')
        if source.next_default().rstrip('\x00').lstrip('%') != 'EOF':
            source.exception('Expected %%EOF')
        return startloc, pdfrw.tokens.PdfTokens(fdata, int(tableloc), True, self.verbose)


if __name__ == '__main__':
    pdf_1_path = 'tmp/a4b16fbb-2966-4388-9d04-a88e452ad528.pdf'
    doc_1 = build_document(path_to_pdf=pdf_1_path)
    pdf_2_path = 'tmp/c2d2effe-d35d-4db7-9602-d11985d63468.pdf'
    doc_2 = build_document(path_to_pdf=pdf_2_path)
    filters = [CapitalizationFilter(), PunctuationFilter()]
    # filters = []
    diff_result = DiffResult(new_doc=doc_2, old_doc=doc_1,
                             filter_rules=filters)
    image_writer = DiffImageWriter(
        original_old_doc_path=pdf_1_path, original_new_doc_path=pdf_2_path,
        diff_result=diff_result)
    image_writer.write_diff_pdf(output_path='fulljamz.pdf')
