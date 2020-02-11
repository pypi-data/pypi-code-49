import collections
import itertools
import logging
import random
from typing import List, Tuple, Dict, Optional, Set, Sequence, Counter

import attr
import math
import numpy

from rho_pdf_diff.document import Page

logger = logging.getLogger(__name__)


@attr.s(auto_attribs=True)
class PairSimilarityCache(object):
    """ A class to compute and cache similarity between (old, new) page pairs
    Note: pages are referenced by page number (1-indexed) """
    old_doc_pages: List[Page]
    new_doc_pages: List[Page]
    score_cache: Dict[Tuple[int, int], float] = attr.ib(init=False)

    def __attrs_post_init__(self):
        self.score_cache = {}

    def _compute_similarity(self, old_page_num: int, new_page_num: int) -> float:
        """ Compute the similarity between two Page objects.  This default
        implementation uses the Jaccard similarity, but this can be
        overridden to use different metrics. """
        if None not in (old_page_num, new_page_num):
            old_page = self.old_doc_pages[old_page_num - 1]
            new_page = self.new_doc_pages[new_page_num - 1]
            old_words = {word.stripped_text for word in old_page.words}
            new_words = {word.stripped_text for word in new_page.words}
            intersection = old_words.intersection(new_words)
            union = old_words.union(new_words)
            if len(union) != 0:
                return len(intersection) / len(union)
            else:
                return 0.0
        else:
            return 0.0

    def get_similarity_score(self,
                             old_page_num: int,
                             new_page_num: int) -> float:
        """ Get the similarity score from score_cache if it exists, otherwise
        compute the similarity.  If the key isn't already in the score cache,
        write the result to the cache. """
        cache_key = (old_page_num, new_page_num)
        similarity_score = self.score_cache.get(
            cache_key, self._compute_similarity(old_page_num, new_page_num))
        self.score_cache.setdefault(cache_key, similarity_score)
        return similarity_score


def hash_page_pairs_sequence(pairs: Sequence[Tuple[int, int]]) -> int:
    return hash(tuple(pairs))


@attr.s(auto_attribs=True, frozen=True)
class PageSequenceScore(object):
    page_number_pairs: Sequence[Tuple[int, int]] = attr.ib(converter=tuple)
    similarity_score: float

    @property
    def pad_locations(self) -> Tuple[List[int], List[int]]:
        """ Return indices (0-indexed) of None elements of whichever sequence
        has them """
        return ([i for i, x in enumerate(self.page_number_pairs) if x[0] is None],
                [i for i, x in enumerate(self.page_number_pairs) if x[1] is None])


@attr.s(auto_attribs=True)
class PageAlignment(object):
    old_pages: List[Page]
    new_pages: List[Page]
    pair_scores_cache: PairSimilarityCache = attr.ib(init=False, repr=False)
    sequences_tried_cache: Set[PageSequenceScore] = attr.ib(init=False,
                                                            repr=False)
    old_doc_insert_after: Counter[int] = attr.ib(init=False)
    new_doc_insert_after: Counter[int] = attr.ib(init=False)
    top_candidate: PageSequenceScore = attr.ib(init=False)
    num_virtual_pads: int = attr.ib(init=False)

    # The following are parameters for the optimization of similarity score. We aim for the first step
    # of the algorithm to accept a worse state 98% of the time based on heuristics, but this could be
    # changed if someone really wanted. 'annealing_iterations' controls how long this runs for. This is
    # set short, and we can turn this up to around 5000 while keeping the timing under a few minutes.

    first_step_acceptance_probability: float = 0.98
    tmin: float = 1e-2
    annealing_iterations: int = 2500

    def __attrs_post_init__(self):
        self.pair_scores_cache = PairSimilarityCache(
            old_doc_pages=self.old_pages, new_doc_pages=self.new_pages)
        self.sequences_tried_cache = set()
        self.old_doc_insert_after = collections.Counter()
        self.new_doc_insert_after = collections.Counter()

    @property
    def doc_to_pad(self):
        if len(self.old_pages) < len(self.new_pages):
            result = 'old'
        elif len(self.new_pages) < len(self.old_pages):
            result = 'new'
        else:  # equal length pages
            result = 'neither'
        return result

    @property
    def base_sequence(self):
        """ The sequence with pads added to the top and bottom of both docs to make them equal in length """

        def get_page_numbers(pages: List[Page]) -> List[int]:
            return [page.page_number for page in pages]

        self.num_virtual_pads = max(1, abs(len(self.old_pages) - len(self.new_pages)))
        virtual_pads = [None for x in range(0, self.num_virtual_pads)]

        old_page_nums = virtual_pads + get_page_numbers(self.old_pages)
        new_page_nums = virtual_pads + get_page_numbers(self.new_pages)

        return list(itertools.zip_longest(old_page_nums, new_page_nums))

    def score_page_pairs(self, page_pairs: List[Tuple[int, int]]) -> float:
        scores = (self.pair_scores_cache.get_similarity_score(x, y) \
                  for x, y in page_pairs)
        return sum(scores)

    def generate_modified_candidate(self,
                                    existing_candidate: PageSequenceScore) \
            -> PageSequenceScore:
        """ Take an existing candidate, randomly select a pad and swap it with a page
         and return the resulting candidate.
        """

        def generate_token_sequence(which_doc: str) -> List[str]:
            page_pair_column = 0
            if which_doc == 'new':
                page_pair_column = 1
            tokens = []
            pad_idxs = [idx for idx in existing_candidate.pad_locations[page_pair_column]]
            for i, _ in enumerate(existing_candidate.page_number_pairs):
                if i in pad_idxs:
                    tokens.append('pad')
                else:
                    tokens.append('page')
            return tokens

        def rebuild_page_sequence(tokens: List[str]) -> List[Optional[int]]:
            page_sequence = []
            page_num_counter = 1
            for token in tokens:
                if token == 'page':
                    page_sequence.append(page_num_counter)
                    page_num_counter += 1
                else:
                    page_sequence.append(None)
            return page_sequence

        def rebuild_page_pairs(which_doc: str, moved_pages: List[Optional[int]]) \
                -> List[Tuple[int, int]]:

            page_pair_column = 1
            if which_doc == 'new':
                page_pair_column = 0

            unchanged_doc_pages = [x[page_pair_column] for x in existing_candidate.page_number_pairs]

            if which_doc == 'old':
                result = list(zip(moved_pages, unchanged_doc_pages))
            else:
                result = list(zip(unchanged_doc_pages, moved_pages))
            return result

        def pad_move(token: List[str]) -> List[str]:
            """Implements an atomic 'move' for the simulated annealing optimization we seek to carry out.
            We define this as a single pairwise swap between a pad and a page."""

            def swap_positions(list, pos1, pos2):
                # popping both the elements from list
                first_ele = list.pop(pos1)
                second_ele = list.pop(pos2 - 1)

                # inserting in each others positions
                list.insert(pos1, second_ele)
                list.insert(pos2, first_ele)

                return list

            # find and select a pad, page pair at random to swap
            pad_idxs = [i for i, x in enumerate(token) if x == 'pad']
            swapped_pad_idx = random.sample(pad_idxs, 1)[0]
            swapped_page_idx = random.randint(0, len(token) - 1)

            while swapped_page_idx in pad_idxs:
                swapped_page_idx = random.randint(0, len(token) - 1)

            swap_positions(token, swapped_pad_idx, swapped_page_idx)
            return token

        new_or_old = random.choice(('new', 'old'))
        # Todo: I'm not sure this is the best way to do this. This works ok, but it's fairly nondeterministic
        #  on long documents.
        sequence_token = generate_token_sequence(new_or_old)
        moved_tokens = pad_move(sequence_token)
        moved_page_sequence = rebuild_page_sequence(tokens=moved_tokens)
        page_pairs = rebuild_page_pairs(new_or_old, moved_pages=moved_page_sequence)
        similarity_score = self.score_page_pairs(page_pairs=page_pairs)
        next_result = PageSequenceScore(page_number_pairs=page_pairs,
                                        similarity_score=similarity_score)
        if next_result not in self.sequences_tried_cache:
            self.sequences_tried_cache.add(next_result)

        return next_result

    def initialize_search(self):
        base_pairs_sequence = self.base_sequence
        score = self.score_page_pairs(page_pairs=base_pairs_sequence)
        first_result = PageSequenceScore(page_number_pairs=base_pairs_sequence,
                                         similarity_score=score)
        self.top_candidate = first_result

    def build_insert_after_counts(self):
        """ Gets the number of pages to insert after each page in each doc, for
         the current maximal scoring sequence in the search cache. """
        cleaned_page_number_pairs = [x for x in self.top_candidate.page_number_pairs if x != (None, None)]
        score = self.score_page_pairs(page_pairs=cleaned_page_number_pairs)
        self.top_candidate = PageSequenceScore(page_number_pairs=cleaned_page_number_pairs,
                                               similarity_score=score)
        current_old_page = 0
        current_new_page = 0
        for old_page_num, new_page_num in cleaned_page_number_pairs:
            if isinstance(old_page_num, int):
                current_old_page = old_page_num
            else:  # old page is None
                self.old_doc_insert_after.update([current_old_page])
            if isinstance(new_page_num, int):
                current_new_page = new_page_num
            else:  # new page is None
                self.new_doc_insert_after.update([current_new_page])

    def set_alignment(self):
        logger.debug("Beginning page alignment!")
        self.initialize_search()
        current_candidate = self.top_candidate

        if self.doc_to_pad != 'neither':

            initial_objective_differential = abs(self.generate_modified_candidate(self.top_candidate).similarity_score - \
                                                 self.top_candidate.similarity_score)

            tmax, tmin = - initial_objective_differential / math.log(self.first_step_acceptance_probability), self.tmin

            temperature_schedule = numpy.logspace(numpy.log10(tmax), numpy.log10(tmin), num=self.annealing_iterations)

            for t in temperature_schedule:
                test_candidate = self.generate_modified_candidate(current_candidate)
                if boltzmann_weight(current_candidate, test_candidate, t) > random.uniform(0, 1):
                    current_candidate = test_candidate
                    logger.debug("Current best score: {0}".format(current_candidate.similarity_score))
            self.top_candidate = current_candidate

        self.build_insert_after_counts()
        logger.debug("Finished page alignment!")


def boltzmann_weight(old_candidate, new_candidate, temperature):
    # Note that we seek to maximize a positive energy function, so there is no minus sign in the exponent.
    objective_differential = new_candidate.similarity_score - old_candidate.similarity_score
    return math.exp(objective_differential / temperature)
