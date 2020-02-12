"""
Cleans email bodies. Can remove html, greetings and split to sentences

Use `html_to_sentences` to split html input
"""
import html
import re

import contractions
from email_reply_parser import EmailReplyParser
from syntok import segmenter

from clean import constants
from clean.html_stripper import strip_tags


NAME_ALLOWANCE = 2 # reduced as its now words instead of characters


def reply(text):
    return split(clean(text))

def clean(text, keepcase=False):
    """
    Removes html, cleans.
    """
    text = html.unescape(text)

    if not keepcase:
        text = text.lower()

    text = re.sub(r"<br>", '\n', text)

    text = _remove_with(text, constants.HTML_QUOTES, '')
    text = strip_tags(text)

    text = _remove_quoted_email(text)
    text = _remove_empty_lines(text)

    text = _remove_with_replacements(text, constants.ENTITIES)
    # text = _remove_with_replacements(text, constants.REPLACEMENTS)
    text = _remove_with(text, constants.SPACES, ' ')

    text = contractions.fix(text)

    return text



def split(text):
    """
    Split input text into sentences/headers/footers, remove greetings and all
    text after farewell.
    """
    paragraphs = text.splitlines()
    tokenised_texts = [segmenter.process(paragraph) \
        for paragraph in paragraphs]
    all_sentences = []
    for tokenised_text in tokenised_texts:
        sentences = [''.join(map(str, sentence)).strip() \
            for paragraph in tokenised_text for sentence in paragraph]
        all_sentences.extend(sentences)
    useful_sentences = []
    for i, sentence in enumerate(all_sentences):
        if i < 2:
            sentence = _strip_greeting(sentence)
        if i > 0:
            # if there is anything after the first comma, its probably
            # not a farewell
            # TODO(hii): Use POS tagging for word after greeting 
            # to figure out if its indeed a farewell
            if len(','.join(sentence.split(",")[1:]).strip()) == 0:
                if  _contains_valid_farewell(sentence):
                    break

        if sentence:
            useful_sentences.append(sentence)
    return useful_sentences

def _contains_valid_farewell(sentence):
    valid_farewell = False
    # for multi lingual emails, it is common to split farewell by /
    for variation in re.split('/|\|', sentence):
        variation = variation.strip()
        farewell = _get_farewell(variation.lower())
        if farewell and len(variation.split(" ")) <= (len(farewell.split(" ")) + NAME_ALLOWANCE):
            valid_farewell = True
            break
    return valid_farewell

def _remove_with(text, regexes, replacement):
    for r in regexes:
        text = r.sub(replacement, text)
    return text


def _remove_with_replacements(text, patterns):
    for p, r in patterns:
        text = p.sub(r, text)
    return text


def _remove_quoted_email(text):
    non_quoted_sentences = [
        sentence for sentence in text.split("\n")
        if not re.match(constants.QUOTED_EMAILS_MATCHER, text)
    ]
    text = '\n'.join(non_quoted_sentences)
    return text


def _strip_greeting(sentence):
    lowered_sentence = sentence.lower()
    greeting = _get_greeting(lowered_sentence)
    # strips from detected greeting to the closest comma
    # e.g 'hi anna,' -> ''
    # e.g 'hi andrew, how are you?' -> ' how are you'
    if greeting:
        sentence = sentence[len(greeting):]
        return ','.join(sentence.split(',')[1:]).strip()
    return sentence

def _get_greeting(sentence):
    for g in constants.GREETINGS:
        if sentence.startswith(g):
            return g

def _get_farewell(sentence):
    for f in constants.FAREWELLS:
        if sentence.startswith(f):
            return f


def _remove_empty_lines(text):
    return '\n'.join([s for s in text.splitlines() if s.strip()])
