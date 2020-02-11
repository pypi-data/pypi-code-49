""" Include specific filters here """
import re
import string
from typing import List, Set

from rho_pdf_diff.text_diff import DiffFilter, Diff


class CapitalizationFilter(DiffFilter):
    """ Throw away changes which only differ by capitalization """

    @staticmethod
    def remove_caps_only_diffs(diffs: List[Diff]) -> List[Diff]:
        def diffs_are_same(diff: Diff) -> bool:
            result = (diff.text.strip().lower() ==
                      diff.corresponding_text.strip().lower())
            return result

        def mark_diff(diff: Diff) -> Diff:
            if diffs_are_same(diff=diff):
                diff.is_relevant = False
            return diff

        return [mark_diff(diff) for diff in diffs]

    def run_filter(self, diff_result: 'DiffResult'):
        diff_result.change_insertion_diffs = self.remove_caps_only_diffs(
            diffs=diff_result.change_insertion_diffs)
        diff_result.change_deletion_diffs = self.remove_caps_only_diffs(
            diffs=diff_result.change_deletion_diffs)


class PunctuationFilter(DiffFilter):
    """ Throw away solo diffs (not changes) which have
    only punctuation. """

    @staticmethod
    def remove_punct_only_diffs(diffs: List[Diff]) -> List[Diff]:
        def diff_is_punct_only(diff: Diff) -> bool:
            return all(char in string.punctuation for char
                       in diff.text.strip())

        def mark_diff(diff: Diff) -> Diff:
            if diff_is_punct_only(diff=diff):
                diff.is_relevant = False
            return diff

        return [mark_diff(diff) for diff in diffs]

    def run_filter(self, diff_result: 'DiffResult'):
        diff_result.solo_insertion_diffs = self.remove_punct_only_diffs(
            diffs=diff_result.solo_insertion_diffs)
        diff_result.solo_deletion_diffs = self.remove_punct_only_diffs(
            diffs=diff_result.solo_deletion_diffs)


class RegexFilter(DiffFilter):
    remove_regex: str = r'[^A-Za-z0-9]+'

    def remove_regex_matches(self, diffs: List[Diff]) -> List[Diff]:
        def diff_is_bad_regex_only(diff: Diff) -> bool:
            m = re.fullmatch(self.remove_regex, diff.text.strip())
            return bool(m)

        def mark_diff(diff: Diff) -> Diff:
            if diff_is_bad_regex_only(diff=diff):
                diff.is_relevant = False
            return diff

        return [mark_diff(diff) for diff in diffs]

    def run_filter(self, diff_result: 'DiffResult'):
        diff_result.solo_insertion_diffs = self.remove_regex_matches(
            diffs=diff_result.solo_insertion_diffs)
        diff_result.solo_deletion_diffs = self.remove_regex_matches(
            diffs=diff_result.solo_deletion_diffs)
        diff_result.change_insertion_diffs = self.remove_regex_matches(
            diffs=diff_result.change_insertion_diffs)
        diff_result.change_deletion_diffs = self.remove_regex_matches(
            diffs=diff_result.change_deletion_diffs)


class SameTextFilter(DiffFilter):
    # todo: this may be over-aggressive removing any insertion that is also a
    #  deletion anywhere in the doc.  It may be more approrpiate to only
    #  consider diffs within some context window as being equivalent.
    min_char_length: int = 2  # only dedupe diffs at least this long

    @staticmethod
    def get_diff_text(diff: Diff) -> str:
        """ Override this if removing case sensitivity, stripping whitespace,
        and standardizing non-alphanumeric characters are not desired. """
        def remove_non_alphanumeric_ends(text: str) -> str:
            first_removed = re.sub(r'^[^A-Za-z0-9]+', '', text)
            return re.sub(r'[^A-Za-z0-9]+$', '', first_removed)

        def standardize_non_alphanumeric_chars(text: str) -> str:
            """ Replace any non-alphanumeric char w/ aerial tramway """
            return re.sub(r'[^A-Za-z0-9]', '\u1f6a1', text)

        return standardize_non_alphanumeric_chars(
            remove_non_alphanumeric_ends(diff.text.lower().strip()))

    def mark_duplicate_diffs(self,
                             diffs: List[Diff],
                             compare_texts: Set[str]) -> List[Diff]:
        def mark_diff(diff: Diff) -> Diff:
            diff_text = self.get_diff_text(diff)
            if (diff_text in compare_texts) and (
                    len(diff_text) >= self.min_char_length):
                diff.is_relevant = False
            return diff

        return [mark_diff(diff) for diff in diffs]

    def run_filter(self, diff_result: 'DiffResult'):
        insertion_texts = {self.get_diff_text(diff) for diff
                           in diff_result.insertion_diffs}
        deletion_texts = {self.get_diff_text(diff) for diff
                          in diff_result.deletion_diffs}
        diff_result.solo_insertion_diffs = self.mark_duplicate_diffs(
            diffs=diff_result.solo_insertion_diffs,
            compare_texts=deletion_texts)
        diff_result.change_insertion_diffs = self.mark_duplicate_diffs(
            diffs=diff_result.change_insertion_diffs,
            compare_texts=deletion_texts)
        diff_result.solo_deletion_diffs = self.mark_duplicate_diffs(
            diffs=diff_result.solo_deletion_diffs,
            compare_texts=insertion_texts)
        diff_result.change_deletion_diffs = self.mark_duplicate_diffs(
            diffs=diff_result.change_deletion_diffs,
            compare_texts=insertion_texts)
