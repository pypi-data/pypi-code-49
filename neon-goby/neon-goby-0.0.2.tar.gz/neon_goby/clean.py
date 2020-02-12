"""
Cleans email bodies. Can remove html, greetings and split to sentences

Use `html_to_sentences` to split html input
"""
import contractions
import html
import re
import unicodedata

from email_reply_parser import EmailReplyParser
from bs4 import BeautifulSoup, Comment

from neon_goby import constants

def clean(text):
    """
    Removes html, cleans.
    """
    text = html.unescape(text)
    text = unicodedata.normalize('NFKD', text)

    # handle outlook quotes
    text = _remove_with(text, constants.HTML_QUOTES, '')

    text = strip_html(text)
    text = _remove_quoted_email(text)
    text = _remove_empty_lines(text)

    text = replace_entities(text)
    text = contractions.fix(text)

    return text

def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    # only apply stripping if text is html
    if soup.find('html'):
        for quoted_div in soup.findAll('div', {"class": "gmail_quote"}):
            quoted_div.decompose()

        for style_section in soup.findAll('style'):
            style_section.decompose()

        text = soup.get_text()

    return text

def _remove_with(text, regexes, replacement):
    for r in regexes:
        text = r.sub(replacement, text)
    return text

def replace_entities(text):
    for pattern, replacement in constants.ENTITIES:
        text = pattern.sub(replacement, text)
    return text

def _remove_quoted_email(string):
    string = _remove_with(string, constants.PREPENDED_TEXT, '')
    string = EmailReplyParser.read(string).reply
    for quote_pattern in constants.QUOTED_EMAILS:
        if re.match(quote_pattern, string):
            string = re.split(quote_pattern, string)[0]
    return string

def _remove_empty_lines(text):
    return '\n'.join([s for s in text.splitlines() if s.strip()])
