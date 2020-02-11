# coding: utf-8

import re
import string

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# text analysis libraries
import gensim
import nltk
from nltk.corpus import stopwords,wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from stop_words import get_stop_words


# Normalization functions:
def remove_puncs(text):
    """Remove punctuations from a given text"""
    exclude = list(string.punctuation)
    exclude = exclude +["…","–","—","’"]
    exclude = [s for s in exclude if s not in ("@", "#","/")]

    punc_free = ''.join(ch for ch in text if ch not in exclude)

    """replace / with space"""
    punc_free = re.sub(r'/', ' ', punc_free)
    return punc_free


def remove_stopwords(text):
    """Remove a list of English stopwords from a given text
       Combining the list of stop words from three packages: nltk, genism and stop_words
    """
    stop_nltk = list(stopwords.words('english'))
    stop_words = get_stop_words('english')
    stop_words = stop_words + [w for w in stop_nltk if w not in stop_words]
    added_stop = ["&amp;", "amp", 'want', 'wants', 'give', 'via','may','put','make',\
                  'makes','said','u','mo','ap', 'says','takes','say','rt',\
                  'gets', 'need', 'needs','th', 'thats','taken','tell','told', 'tells','nearly','\'s','giving','html','rt']
    stop_words = stop_words + added_stop

    stop_words = stop_words + [token for token in stop_words if token not in gensim.parsing.preprocessing.STOPWORDS]

    stop_free = " ".join([i for i in text.split() if i not in stop_words])
    return stop_free


def remove_url(text):
    """Remove URLs from a given text """

    text = re.sub(r"(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*", '',\
           text, flags=re.MULTILINE)  #Remove URLs starting with http,including some spaces, not all


    text = re.sub(r"(pic.twitter.com\/)[^\s]+", " ", text, flags=re.MULTILINE)  #Remove links like pic.twitter.com/[Ywlr6v0PDr]
    return text


def remove_numbers(text):
    """Remove numbers from a given text"""
    text = re.sub(r"[0-9]+", "", text, flags=re.MULTILINE)
    return text


def remove_short_words(text):
    """Remove words with length of 1 from a given text"""
    return re.sub(r'\b\w{1}\b', '', text)


def remove_common_words(text):
    """Remove the most frequent words from a given text"""
    common_words=['bayer','monsanto','bayermonsanto','#bayer', '#monsanto','monsantobayer','bayers',
                  'mons', '#bayers']
    common_free = " ".join([w for w in text.split() if w not in common_words])
    return common_free

def count_usernames(text):
    """Count user-names mentioned in a given text"""
    usr_count = len(re.findall(r'(^|[^@\w])@(\w{1,15})\b', text))
    return usr_count

def remove_usernames(text):
    """Remove user-names from a given text"""
    username_free = re.sub(r'(^|[^@\w])@(\w{1,15})\b', "", text)
    return username_free


# Lemmatization functions

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


def lemmatization(text, to_list= False):
    """Lemmatizing a given text"""
    lemma = WordNetLemmatizer()
    if (to_list):
        normalized = [lemma.lemmatize(w, get_wordnet_pos(w)) for w in text]
    else:
        normalized = " ".join(lemma.lemmatize(w, get_wordnet_pos(w)) for w in text.split())

    return normalized


def find_hashtags(text):
    """Find the hashtags in a given text"""
    hashtags = re.findall('(#\w*[0-9a-zA-Z]+\w*[0-9a-zA-Z])', text)
    return hashtags

def weight_hashtags(text, hashtags, ntimes):
    """gives ntimes weight to the hashtags identified in the given text"""
    weighted_hashtags = hashtags * (ntimes -1)
    text = ' '.join(weighted_hashtags)+' '+text
    return text


def remove_hash_sign(text):
    """Remove the hashtag signs from a given text"""
    no_hash = re.sub('#', ' ', text)
    return no_hash


def remove_extra_spaces(text):
    """Remove extra spaces from a given text"""
    text = ' '.join(text.split())
    return text

def clean_text(doc, lemmatization,no_hash_sign = False, hashtags_weight=1):
    """ Clean a given text including removing stop-words, punctuations etc

    Parameters:
    doc (str): a piece of text, i.e. tweet
    lemmatization (bool): specify if lemmatization is required
    no_hash_sign (bool):  specify if hash sign should be removed, default is False
    hashtags_weight (int): weight of hashtag, default is 1

    Returns:
    int:Returning value

    """


    text = doc.lower()
    url_free = remove_url(text)
    user_counts = count_usernames(text)
    username_free = remove_usernames(url_free)
    number_free = remove_numbers(username_free)

    punc_free = remove_puncs(number_free)

    if (lemmatization):
        punc_free = lemmatization(punc_free)

    stop_free = remove_stopwords(punc_free)

    short_free = remove_short_words(stop_free)
    normalized = remove_common_words(short_free)

    normalized = remove_extra_spaces(normalized)  # remove extra spaces in text

    hashtags = find_hashtags(text)

    words_count = len([word for word in normalized.split(' ') if word not in hashtags])

    if hashtags_weight > 1:  # Weight hashtags
        normalized = weight_hashtags(normalized, hashtags, hashtags_weight)

    if no_hash_sign:  # Remove hashtag sign
        normalized = remove_hash_sign(normalized)

    return normalized, user_counts, len(hashtags), words_count
