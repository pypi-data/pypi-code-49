import logging
from typing import List, Tuple, Optional, Iterator

import attr
import diff_match_patch
from cytoolz import cons

from rho_pdf_diff.document import Document, Word

logger = logging.getLogger(__name__)


def run_document_diff(text_1: str, text_2: str) -> List[Tuple[int, str]]:
    """ Use the diff-match-patch library to get a text diff between the two
    full text docs, cleaned up for human readability."""
    logger.debug("Beginning text diff...")
    diffs = diff_match_patch.diff(text_1, text_2, checklines=False)
    processed_diffs = create_diff_text_code_tuples(diffs, text_1, text_2)
    logger.debug("Finished text diff!  Beginning semantic cleanup...")
    logger.debug("Finished semantic cleanup!")

    return processed_diffs


def create_diff_text_code_tuples(changes: List[Tuple[str, int]],
                                 text_1: str,
                                 text_2: str) -> List[Tuple[int, str]]:
    processed_diffs = []
    start_idx_left, start_idx_right = 0, 0
    for op, length in changes:
        if op == "=":
            processed_diffs.append(
                (0, text_1[start_idx_left: start_idx_left + length]))
            start_idx_left += length
            start_idx_right += length
        if op == "+":
            processed_diffs.append(
                (1, text_2[start_idx_right: start_idx_right + length]))
            start_idx_right += length
        if op == "-":
            processed_diffs.append(
                (-1, text_1[start_idx_left: start_idx_left + length]))
            start_idx_left += length
    return processed_diffs


@attr.s(auto_attribs=True)
class EqualitySpan(object):
    text: str
    old_doc_start_char: int
    new_doc_start_char: int
    old_doc_end_char: int = attr.ib(init=False)
    new_doc_end_char: int = attr.ib(init=False)
    old_doc_start_page: int = attr.ib(init=False)
    new_doc_start_page: int = attr.ib(init=False)
    old_doc_end_page: int = attr.ib(init=False)
    new_doc_end_page: int = attr.ib(init=False)
    diff_type: str = attr.ib(init=False)

    def __attrs_post_init__(self):
        self.old_doc_end_char = self.old_doc_start_char + len(self.text)
        self.new_doc_end_char = self.new_doc_start_char + len(self.text)
        self.diff_type = 'equality'

    def get_one_doc_page_num(self,
                             doc: Document,
                             self_property: str) -> int:
        char_idx = getattr(self, self_property)
        word_idx = doc.character_to_word_map[char_idx]
        page_num = doc.words[word_idx].page_number
        return page_num

    def set_page_ranges(self, old_doc: Document, new_doc: Document):
        self.old_doc_start_page = self.get_one_doc_page_num(
            doc=old_doc, self_property='old_doc_start_char')
        self.old_doc_end_page = self.get_one_doc_page_num(
            doc=old_doc, self_property='old_doc_end_char')
        self.new_doc_start_page = self.get_one_doc_page_num(
            doc=new_doc, self_property='new_doc_start_char')
        self.new_doc_end_page = self.get_one_doc_page_num(
            doc=new_doc, self_property='new_doc_end_char')

    @property
    def old_doc_page_range(self) -> range:
        return range(self.old_doc_start_page, self.old_doc_end_page + 1)

    @property
    def new_doc_page_range(self) -> range:
        return range(self.new_doc_start_page, self.new_doc_end_page + 1)


DIFF_TYPES = ('equality', 'solo_insertion', 'solo_deletion', 'change_insertion',
              'change_deletion')


@attr.s(auto_attribs=True)
class Span(object):
    text: str
    words: List[Word]
    start_char_idx: int
    end_char_idx: int = attr.ib(init=False)

    def _remove_extra_words(self):
        """ Sometimes an extra Word gets pulled in to either end of a diff,
        remove these here. """
        # todo: investigate why this is needed - why are character indices and
        #  word indices sometimes off?
        first_stripped = self.words[0].stripped_text
        if (first_stripped not in self.text and
                self.text not in first_stripped):
            _ = self.words.pop(0)
        if self.words:
            last_stripped = self.words[-1].stripped_text
            if (last_stripped not in self.text and
                    self.text not in last_stripped):
                _ = self.words.pop(-1)
        if not self.words:
            self.is_relevant = False

    def __attrs_post_init__(self):
        self.end_char_idx = self.start_char_idx + len(self.text)
        self._remove_extra_words()

    @property
    def begin_page(self):
        return min(word.page_number for word in self.words)

    @property
    def end_page(self):
        return max(word.page_number for word in self.words)


# note: diff-match-patch has no notion of "change" distinct from solo
# insertions and deletions.  The idea is important if you need to be able to
# write rules to determine if a change is relevant, e.g. if synonyms or
# abbreviations are the only change between a specific insert and the
# corresponding deletion.
@attr.s(auto_attribs=True)
class Diff(Span):
    diff_type_code: int  # either -1, 0, or 1 (from diff-match-patch)
    diff_type: str = attr.ib(validator=attr.validators.in_(DIFF_TYPES))
    is_relevant: bool = True
    corresponding_text: Optional[str] = None  # if diff is a change


class DiffFilter(object):

    def run_filter(self, diff_result: 'DiffResult'):
        raise NotImplementedError()


@attr.s(auto_attribs=True)
class DiffResult(object):
    """ Contains full document diff """
    # todo: keep track of equality diffs to match pages
    # todo: add a page mapping here in init
    new_doc: Document
    old_doc: Document
    filter_rules: List[DiffFilter] = attr.Factory(list)
    text_diffs: List[Tuple[int, str]] = attr.ib(init=False, repr=False)
    solo_insertion_diffs: List[Diff] = attr.ib(init=False, repr=False)
    solo_deletion_diffs: List[Diff] = attr.ib(init=False, repr=False)
    change_insertion_diffs: List[Diff] = attr.ib(init=False, repr=False)
    change_deletion_diffs: List[Diff] = attr.ib(init=False, repr=False)
    equality_spans: List[EqualitySpan] = attr.ib(init=False, repr=False)

    # Note change_insertion_diffs has *only* the insertion text, etc., and
    # change_deletion_diffs has *only* deletion text, etc.

    def __attrs_post_init__(self):
        self.solo_insertion_diffs = []
        self.solo_deletion_diffs = []
        self.change_insertion_diffs = []
        self.change_deletion_diffs = []
        self.equality_spans = []
        self.text_diffs = run_document_diff(self.old_doc.full_text,
                                            self.new_doc.full_text)
        self.process_raw_diffs()
        self.filter_processed_diffs()

    @property
    def insertion_diffs(self):
        return [diff for diff in self.solo_insertion_diffs +
                self.change_insertion_diffs if diff.is_relevant]

    @property
    def deletion_diffs(self):
        return [diff for diff in self.solo_deletion_diffs +
                self.change_deletion_diffs if diff.is_relevant]

    def filter_processed_diffs(self):
        """ Remove any diffs according to rules defined here.  The default
        behavior is to do nothing. """
        for diff_filter in self.filter_rules:
            diff_filter.run_filter(diff_result=self)

    def _process_equality_diff(self, diff_text: str, new_doc_idx: int,
                               old_doc_idx: int) -> Tuple[EqualitySpan, int, int]:
        """ For strings that are the same in both old and new, move the
        character index for both docs. """
        equality_span = EqualitySpan(
            text=diff_text, old_doc_start_char=old_doc_idx,
            new_doc_start_char=new_doc_idx)
        return (equality_span,
                new_doc_idx + len(diff_text),
                old_doc_idx + len(diff_text))

    def _process_insertion_diff(self, diff_text: str, new_doc_idx: int,
                                old_doc_idx: int) -> Tuple[Diff, int, int]:
        """ For diffs with a string in the new doc but not in the old, build
        the Diff object and move the new doc index forward. """
        diff_words = get_words_from_character_range(
            doc=self.new_doc, char_start_idx=new_doc_idx,
            char_end_idx=new_doc_idx + len(diff_text))
        diff = Diff(text=diff_text, diff_type_code=1, words=diff_words,
                    start_char_idx=new_doc_idx, diff_type='solo_insertion')
        return diff, new_doc_idx + len(diff_text), old_doc_idx

    def _process_deletion_diff(self, diff_text: str, new_doc_idx: int,
                               old_doc_idx: int) -> Tuple[Diff, int, int]:
        """ For diffs with a string in the old but not in the new, build the
        Diff object and move the old doc index forward. """
        diff_words = get_words_from_character_range(
            doc=self.old_doc, char_start_idx=old_doc_idx,
            char_end_idx=old_doc_idx + len(diff_text))
        diff = Diff(text=diff_text, diff_type_code=-1, words=diff_words,
                    start_char_idx=old_doc_idx, diff_type='solo_deletion')
        return diff, new_doc_idx, old_doc_idx + len(diff_text)

    def _process_change_diffs(self, insertion_text: str,
                              deletion_text: str,
                              new_doc_idx: int,
                              old_doc_idx: int) -> Tuple[Diff, Diff, int, int]:
        new_end_idx = new_doc_idx + len(insertion_text)
        old_end_idx = old_doc_idx + len(deletion_text)
        new_diff_words = get_words_from_character_range(
            doc=self.new_doc, char_start_idx=new_doc_idx,
            char_end_idx=new_end_idx)
        old_diff_words = get_words_from_character_range(
            doc=self.old_doc, char_start_idx=old_doc_idx,
            char_end_idx=old_end_idx)
        
        new_diff = Diff(text=insertion_text, diff_type_code=1,
                        diff_type='change_insertion', words=new_diff_words,
                        start_char_idx=new_doc_idx,
                        corresponding_text=deletion_text)
        old_diff = Diff(text=deletion_text, diff_type_code=-1,
                        diff_type='change_deletion', words=old_diff_words,
                        start_char_idx=old_doc_idx,
                        corresponding_text=insertion_text)
        return new_diff, old_diff, new_end_idx, old_end_idx

    def generate_diff_results(self) -> Iterator[Diff]:
        new_doc_idx = 0
        old_doc_idx = 0
        diff_iter = iter(self.text_diffs)

        def diff_text_len_margin(new_diff_text, old_diff_text, margin=0.90):
            return abs(len(new_diff_text) - len(old_diff_text)) / max(len(old_diff_text), len(new_diff_text)) < margin

        while True:
            # for diff_code, diff_text in diff_iter:
            try:
                diff_code, diff_text = next(diff_iter)
            except StopIteration:
                break
            if diff_text.strip():
                if diff_code == 0:
                    span, new_doc_idx, old_doc_idx = self._process_equality_diff(
                        diff_text=diff_text, new_doc_idx=new_doc_idx,
                        old_doc_idx=old_doc_idx)
                    span.set_page_ranges(old_doc=self.old_doc,
                                         new_doc=self.new_doc)
                    yield span
                elif diff_code == 1:
                    try:
                        next_diff_code, next_diff_text = next(diff_iter)
                    except StopIteration:
                        next_diff_code = None
                    if next_diff_code == -1 and diff_text_len_margin(diff_text, next_diff_text):
                        (new_diff, old_diff,
                         new_doc_idx, old_doc_idx) = self._process_change_diffs(
                            insertion_text=diff_text,
                            deletion_text=next_diff_text,
                            new_doc_idx=new_doc_idx,
                            old_doc_idx=old_doc_idx)
                        yield new_diff
                        yield old_diff
                    else:
                        if next_diff_code is not None:
                            diff_iter = cons((next_diff_code, next_diff_text),
                                             diff_iter)
                            (diff, new_doc_idx,
                             old_doc_idx) = self._process_insertion_diff(
                                diff_text=diff_text, new_doc_idx=new_doc_idx,
                                old_doc_idx=old_doc_idx)
                            yield diff
                elif diff_code == -1:
                    try:
                        next_diff_code, next_diff_text = next(diff_iter)
                    except StopIteration:
                        next_diff_code = None
                    if next_diff_code == 1 and diff_text_len_margin(diff_text, next_diff_text):
                        (new_diff, old_diff,
                         new_doc_idx, old_doc_idx) = self._process_change_diffs(
                            insertion_text=next_diff_text, deletion_text=diff_text,
                            new_doc_idx=new_doc_idx, old_doc_idx=old_doc_idx)
                        yield new_diff
                        yield old_diff
                    else:
                        if next_diff_code is not None:
                            diff_iter = cons((next_diff_code, next_diff_text),
                                             diff_iter)
                            (diff, new_doc_idx,
                             old_doc_idx) = self._process_deletion_diff(
                                diff_text=diff_text, new_doc_idx=new_doc_idx,
                                old_doc_idx=old_doc_idx)
                            yield diff
                else:
                    raise ValueError("Invalid diff code {0} received!"
                                     .format(diff_code))

    def process_raw_diffs(self):
        """ Take the diffs from diff-match-patch and combine with bounding
        box info available in each Document object at the word level to generate
        Diff objects in the self.addition_diffs and self.removal_diffs lists
         """
        diff_results = self.generate_diff_results()

        for result in diff_results:
            if result.diff_type == 'equality':
                self.equality_spans.append(result)
            elif result.diff_type == 'solo_insertion':
                self.solo_insertion_diffs.append(result)
            elif result.diff_type == 'solo_deletion':
                self.solo_deletion_diffs.append(result)
            elif result.diff_type == 'change_insertion':
                self.change_insertion_diffs.append(result)
            elif result.diff_type == 'change_deletion':
                self.change_deletion_diffs.append(result)
            else:
                raise ValueError("Invalid diff type {0} found!"
                                 .format(result.diff_type))


def get_words_from_character_range(doc: Document, char_start_idx: int,
                                   char_end_idx: int) -> List[Word]:
    word_start_idx = doc.character_to_word_map[char_start_idx]
    word_end_idx = doc.character_to_word_map[char_end_idx]
    word_slice = doc.words[word_start_idx:word_end_idx + 1]
    return word_slice
