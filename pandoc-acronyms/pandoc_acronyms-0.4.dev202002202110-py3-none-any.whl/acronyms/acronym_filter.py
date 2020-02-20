# a Pandoc filter for acronyms based on panflute.

import panflute
import sys
import re
import click

from acronyms.acronyms import Acronyms
from acronyms.index import Index
from acronyms.logging import debug, info


class Filter:
    """The Filter class manages the configuration of a single filter run."""

    def __init__(self):
        self.acronyms = Acronyms()
        self.index = Index()
        self.suggest = False

    @property
    def acronyms(self):
        return self._acronyms

    @acronyms.setter
    def acronyms(self, value):
        self._acronyms = value

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    @property
    def suggest(self):
        return self._suggest == True

    @suggest.setter
    def suggest(self, value):
        self._suggest = (value == True)

    def run(self, acronymfiles, doc=None):
        if acronymfiles:
            for input in acronymfiles:
                info('Loading acronyms from {}...'.format(input))
                with open(input, "r") as handle:
                    dictionary = Acronyms.Read(handle)
                    self.acronyms.merge(dictionary)
        else:
            info('No acronym definitions specified!')
        return self.process_document(doc)

    def filter_acronyms(self, element, doc):
        """The panflute filter function."""
        if type(element) == panflute.Str:
            pattern = element.text
            replacer = self.acronym_replacer
            element.text = self.process_string_token(pattern, replacer)
            if self.suggest:
                suggestions = self.check_for_suggestions(pattern)
                for suggestion in suggestions:
                    info(suggestion, True)

    def return_acronym_match(self, token):
        """return_acronym_match returns True if the token text is recognized as an acronym."""
        expression = Filter.acronym_pattern_expression()
        match = expression.match(token)
        return match

    def replace_acronym(self, matchtext, acronym, firstuse):
        text = acronym.shortform
        if firstuse:
            text = "{} ({})".format(acronym.longform, acronym.shortform)
        return text

    def acronym_replacer(self, pattern):
        match = self.return_acronym_match(pattern)
        text = match.group(1)
        # is this an acronym?
        acronym = self.acronyms.get(text)
        if not acronym:
            info("Warning: acronym {} undefined.".format(text))
            return
        # register the use of the acronym:
        count = self.index.register(acronym)
        # # is this the first use of the acronym?
        if count == 1:
            info("First use of acronym {} found.".format(text))
            return self.replace_acronym(pattern, acronym, True)
        else:
            debug("Acronym {} found again.".format(text))
            return self.replace_acronym(pattern, acronym, False)

    def check_for_suggestions(self, pattern):
        elements = pattern.split()
        acronyms = self.acronyms.values
        results = []
        for key, acronym in acronyms.items():
            if acronym.shortform in elements:
                results.append('NOTE: "{}" in "{}" could be an acronym. Consider replacing it with [!{}].'.format( acronym.shortform, pattern, key))
        return results

    def process_string_token(self, token, replacer):
        """Parse the token, isolate the acronyms and pass them to the replacer function. Return the reassembled text."""
        rx = Filter.acronym_search_expression()
        result = ""
        while token:
            match = rx.search(token)
            if match:
                (left, right) = match.span()
                result += token[0:left]
                pattern = token[left:right]
                result += replacer(pattern) or ''  # pattern could be empty
                token = token[right:]
            else:
                # no match left in token
                result += token
                token = ""
        return result

    def process_document(self, doc):
        """The entry method to execute the filter."""
        # We need state in the filter function, so we create a filter function that references the filter object:

        def filter_closure(element, doc):
            return self.filter_acronyms(element, doc)

        return panflute.run_filter(filter_closure, doc=doc)

    @staticmethod
    def acronym_pattern_expression():
        return re.compile(r'\[\!(.+)\]')

    @staticmethod
    def acronym_search_expression():
        return re.compile(r'(\[\!.+?\])')
