import re
from unicodedata import normalize


from advertools.regex import HASHTAG, HASHTAG_RAW


def test_hashtag_found_in_different_positions():
    s = '#start #middle #end'
    assert HASHTAG.findall(s) == ['#start', '#middle', '#end']


def test_hashtag_found_for_different_scripts():
    s = '#latin #عربي #русский #ελληνικά #汉语 #ภาษาไทย'
    assert HASHTAG.findall(s) == s.split()


def test_hashtag_takes_only_word_chars():
    s = 'one#two #three! #four, #five? #six-seven'
    assert HASHTAG.findall(s) == ['#three', '#four', '#five', '#six']


def test_hashtag_takes_both_hashtag_signs():
    s = '＃one #two'
    assert HASHTAG.findall(s) == s.split()