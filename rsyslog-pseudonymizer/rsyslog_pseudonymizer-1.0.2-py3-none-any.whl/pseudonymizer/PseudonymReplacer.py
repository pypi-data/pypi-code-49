import math

from .IPv4Pseudonymizer import IPv4Pseudonymizer
from .IPv6Pseudonymizer import IPv6Pseudonymizer
from .MatrixIDPseudonymizer import MatrixIDPseudonymizer
from .EmailPseudonymizer import EmailPseudonymizer
from .DomainPseudonymizer import DomainPseudonymizer
from .UsernamePseudonymizer import UsernamePseudonymizer

def get_default_identifier_types():
    domain_pseudonymizer = DomainPseudonymizer()
    identifier_types = [
        IPv4Pseudonymizer(),
        IPv6Pseudonymizer(),
        EmailPseudonymizer(domain_pseudonymizer, UsernamePseudonymizer),
        MatrixIDPseudonymizer(domain_pseudonymizer, UsernamePseudonymizer),
        domain_pseudonymizer
    ]
    return identifier_types

class PseudonymReplacer(object):
    def __init__(self, identifier_types):
        self.__identifier_types = identifier_types

    def pseudonymize_text(self, text):
        return _pseudonymize_text_with_identifiers(
            self.__identifier_types,
            text
        )

def _update_next_pseudonyms(identifier_types, text, next_pseudonyms, start):
    next_pseudonym = None
    next_match = None
    next_start = math.inf
    for identifier in identifier_types:
        entry = next_pseudonyms.get(identifier)
        if entry is False:
            continue # no next match for this identifier
        if entry is None or entry[1].start() < start:
            regex = identifier.get_regex()
            regex_start = start
            pseudonym_info = None
            while True:
                match = regex.search(text, regex_start)
                if match is None:
                    break
                pseudonym_info = identifier.get_pseudonym(match.group())
                if pseudonym_info is not None:
                    break
                regex_start = match.start() + 1
            if pseudonym_info is None:
                next_pseudonyms[identifier] = False
                continue
            pseudonym = pseudonym_info.formatted
            next_pseudonyms[identifier] = (pseudonym, match)
        else:
            (pseudonym, match) = entry
        match_length = match.end() - match.start()
        if next_start > match.start() or \
                (next_start == match.start() and next_length < match_length):
            next_pseudonym = pseudonym
            next_match = match
            next_start = match.start()
            next_length = match_length
    return (next_pseudonym, next_match)

def _pseudonymize_text_with_identifiers(identifier_types, text):
    result = []
    next_pseudonyms = {}
    start = 0
    while True:
        (next_pseudonym, next_match) = _update_next_pseudonyms(
             identifier_types, text, next_pseudonyms, start)
        if next_pseudonym is None:
            break
        if next_match.start() > start:
            result.insert(len(result), text[start:next_match.start()])
        result.insert(len(result), next_pseudonym)
        start = max(start + 1, next_match.end())
    if start < len(text):
        result.insert(len(result), text[start:])
    return "".join(result)
