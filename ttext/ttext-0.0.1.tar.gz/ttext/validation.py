# encoding=utf-8

import re

from ttext.unicode import force_unicode
from ttext.extractor import Extractor
from ttext.regex import REGEXEN

MAX_LENGTH = 280

DEFAULT_TCO_URL_LENGTHS = {
  'short_url_length': 23,
  'short_url_length_https': 23,
  'characters_reserved_per_media': 0,
}

WEIGHTS = {
    'scale': 100,
    'default_weight': 200,
    'ranges': [
        {
            'start': 0,
            'end': 4351,
            'weight': 100
        },
        {
            'start': 8192,
            'end': 8205,
            'weight': 100
        },
        {
            'start': 8208,
            'end': 8223,
            'weight': 100
        },
        {
            'start': 8242,
            'end': 8247,
            'weight': 100
        }
    ]
}

class Validation(object):
    def __init__(self, text, **kwargs):
        self.text = force_unicode(text)
        self.parent = kwargs.get('parent', False)

    def tweet_length(self, options = {}):
        """
        Returns the length of the string as it would be displayed. This is equivilent to the length of the Unicode NFC
        (See: http://www.unicode.org/reports/tr15). This is needed in order to consistently calculate the length of a
        string no matter which actual form was transmitted. For example:

             U+0065  Latin Small Letter E
         +   U+0301  Combining Acute Accent
         ----------
         =   2 bytes, 2 characters, displayed as é (1 visual glyph)
             … The NFC of {U+0065, U+0301} is {U+00E9}, which is a single chracter and a +display_length+ of 1

         The string could also contain U+00E9 already, in which case the canonicalization will not change the value.

        After NFC normalization, all characters in the tweet are weighted against a set of twitter rules that define
        relative weights for different ranges of characters as defined here:

        https://developer.twitter.com/en/docs/developer-utilities/twitter-text.html

        Finally, every url is extracted and counted as a fixed number of characters
        """

        assert (not self.parent or not getattr(self.parent, 'has_been_linked', False) ), 'The validator should only be run on text before it has been modified.'

        for key in DEFAULT_TCO_URL_LENGTHS:
            if not key in options:
                options[key] = DEFAULT_TCO_URL_LENGTHS[key]

        collective_weight = 0
        for char in self.text:
            codepoint = ord(char)
            char_weight = WEIGHTS['default_weight']
            if codepoint >= 0xd800 and codepoint <= 0xdbff:
                # This is a surrogate character, don't count it
                char_weight = 0
            else:
                for rng in WEIGHTS['ranges']:
                    if rng['start'] <= codepoint <= rng['end']:
                        char_weight = rng['weight']
            collective_weight = collective_weight + char_weight

        length = collective_weight / WEIGHTS['scale']

        for url in Extractor(self.text).extract_urls_with_indices():
            # remove the link of the original URL
            length += url['indices'][0] - url['indices'][1]
            # add the length of the t.co URL that will replace it
            length += options.get('short_url_length_https') if url['url'].lower().find('https://') > -1 else options.get('short_url_length')

        if self.parent and hasattr(self.parent, 'tweet_length'):
            self.parent.tweet_length = length
        return length

    def tweet_invalid(self):
        """
        Check the text for any reason that it may not be valid as a Tweet. This is meant as a pre-validation
        before posting to api.twitter.com. There are several server-side reasons for Tweets to fail but this pre-validation
        will allow quicker feedback.

        Returns false if this text is valid. Otherwise one of the following Symbols will be returned:

            "Too long":: if the text is too long
            "Empty text":: if the text is empty
            "Invalid characters":: if the text contains non-Unicode or any of the disallowed Unicode characters
        """

        valid = True # optimism
        validation_error = None

        if not self.tweet_length():
            valid, validation_error = False, 'Empty text'

        if self.tweet_length() > MAX_LENGTH:
            valid, validation_error = False, 'Too long'

        if re.search(ur''.join(REGEXEN['invalid_control_characters']), self.text):
            valid, validation_error = False, 'Invalid characters'

        if self.parent and hasattr(self.parent, 'tweet_is_valid'):
            self.parent.tweet_is_valid = valid
        if self.parent and hasattr(self.parent, 'tweet_validation_error'):
            self.parent.tweet_validation_error = validation_error

        return validation_error if not valid else False

    def valid_tweet_text(self):
        return not self.tweet_invalid()

    def valid_username(self):
        if not self.text:
            return False

        extracted = Extractor(self.text).extract_mentioned_screen_names()

        return len(extracted) == 1 and extracted[0] == self.text[1:]

    def valid_list(self):
        match = re.compile(ur'^%s$' % REGEXEN['valid_mention_or_list'].pattern).search(self.text)
        return bool(match is not None and match.groups()[0] == "" and match.groups()[3])

    def valid_hashtag(self):
        if not self.text:
            return False

        extracted = Extractor(self.text).extract_hashtags()

        return len(extracted) == 1 and extracted[0] == self.text[1:]

    def valid_url(self, unicode_domains = True, require_protocol = True):
        if not self.text:
            return False

        url_parts = REGEXEN['validate_url_unencoded'].match(self.text)

        if not (url_parts and url_parts.string == self.text):
            return False

        scheme, authority, path, query, fragment = url_parts.groups()

        if not (
            (
                not require_protocol
                or (
                    self._valid_match(scheme, REGEXEN['validate_url_scheme'])
                    and re.compile(ur'^https?$', re.IGNORECASE).match(scheme)
                )
            )
            and (
                path == ''
                or self._valid_match(path, REGEXEN['validate_url_path'])
            )
            and self._valid_match(query, REGEXEN['validate_url_query'], True)
            and self._valid_match(fragment, REGEXEN['validate_url_fragment'], True)
        ):
            return False

        return bool(
            (
                unicode_domains
                and self._valid_match(authority, REGEXEN['validate_url_unicode_authority'])
                and REGEXEN['validate_url_unicode_authority'].match(authority).string == authority
            )
            or (
                not unicode_domains
                and self._valid_match(authority, REGEXEN['validate_url_authority'])
                and REGEXEN['validate_url_authority'].match(authority).string == authority
            )
        )

    def _valid_match(self, string, re_obj, optional = False):
        if optional and string is None:
            return True
        match = re_obj.match(string)
        if optional:
            return not (string and (match is None or not match.string[match.span()[0]:match.span()[1]] == string))
        else:
            return bool(string and match and match.string[match.span()[0]:match.span()[1]] == string)
