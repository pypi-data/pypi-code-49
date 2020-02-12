import re
from syntok import segmenter

from neon_goby import constants
from neon_goby.matchers import FAREWELL_MATCHER, LEGAL_MATCHER, SIGNATURE_MATCHER


NAME_ALLOWANCE = 2 # reduced as its now words instead of characters

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
        if i > 1:
            # if there is anything after the first comma, its probably
            # not a farewell
            # TODO(hii): Use POS tagging for word after greeting 
            # to figure out if its indeed a farewell
            if len(','.join(sentence.split(",")[1:]).strip()) == 0:
                if  _contains_valid_farewell(sentence.lower().strip()):
                    break
            
            # strip signatures
            if SIGNATURE_MATCHER.match(sentence.lower().strip()):
                break

            # strip legal
            if LEGAL_MATCHER.match(sentence.lower().strip()):
                break

        if sentence:
            useful_sentences.append(sentence)
    return useful_sentences



def _strip_greeting(sentence):
    lowered_sentence = sentence.lower()
    greeting = _get_greeting(lowered_sentence)
    # strips from detected greeting to the closest comma
    # e.g 'hi anna,' -> ''
    # e.g 'hi andrew, how are you?' -> ' how are you'

    # TODO(hii): POS tagging also needed here
    # failure cases:
    # hello anna\n how are you?
    num_words = len(sentence.strip().split(" "))
    if greeting and ((',' in sentence) or num_words == 2):
        sentence = sentence[len(greeting):]
        return ','.join(sentence.split(',')[1:]).strip()
    return sentence

def _get_greeting(sentence):
    for g in constants.GREETINGS:
        if sentence.startswith(g):
            return g

def _contains_valid_farewell(sentence):
    valid_farewell = False
    # for multi lingual emails, it is common to split farewell by /
    for variation in re.split(r'/|\|', sentence):
        variation = variation.strip()
        farewell = _get_farewell(variation.lower())
        if farewell and len(variation.split(" ")) <= (len(farewell.split(" ")) + NAME_ALLOWANCE):
            valid_farewell = True
            break
    return valid_farewell

def _get_farewell(sentence):
    result = FAREWELL_MATCHER.search(sentence.strip())
    if result:
        return result.group(0)
