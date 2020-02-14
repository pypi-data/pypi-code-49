import requests
import json
import spacy
import numpy as np
import nltk
from nltk.corpus import stopwords
import gensim
from gensim.models import LdaModel
import re
from scipy.stats import entropy
from pkg_resources import resource_filename
from gensim.utils import simple_preprocess
from gensim.models.wrappers import LdaMallet
from bs4 import BeautifulSoup
import en_core_web_sm

def get_similar(lib):
    number_of_topics = 30 # Number of topics LDA was trained on
    
    # Download library's description
    try:
        lib_response = requests.get("https://pypi.org/pypi/{}/json".format(lib))
        lib_data = lib_response.json()
        lib_sum = lib_data["info"]["summary"]
        lib_desc = lib_data["info"]["description"]
    except:
        return None
    
    # Stop words
    nltk.download('stopwords', quiet=True)

    # Necessary files
    lda_file = resource_filename(__name__, 'lda.model')
    doc_topic_dist_file = resource_filename(__name__, 'topic_distribution.npy')
    name_list_file = resource_filename(__name__, 'lda_names_list.txt')
    bigram_file = resource_filename(__name__, 'bigram.model')
    trigram_file = resource_filename(__name__, 'trigram.model')

    # Load our LDA model
    lda = LdaModel.load(lda_file)
    
    bigram_mod = gensim.models.phrases.Phraser.load(bigram_file)
    trigram_mod = gensim.models.phrases.Phraser.load(trigram_file)
    
    # Preprocess text
    data = lib + " " + lib_sum + " " + lib_desc
    data = re.sub(r'\S*@\S*\s?', '', data)
    data = re.sub(r'\s+', ' ', data)
    data = re.sub(r"\'", "", data)
    data_words = list(sent_to_words(data))
    data_words_nostops = remove_stopwords(data_words)
    data_words_trigrams = make_trigrams(data_words_nostops, trigram_mod, bigram_mod)
    
    # Load spacy for lemmatization
    nlp = en_core_web_sm.load()

    data_lemmatized = lemmatization(nlp, data_words_trigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
    
    # Term Document Frequency
    corpus = lda.id2word.doc2bow(data_lemmatized)
    
    # Topic distribution of our wanted library
    doc_distribution = [0] * number_of_topics
    for l in lda.get_document_topics(bow=corpus):
        doc_distribution[l[0]] = l[1]
    doc_distribution = np.array(doc_distribution)
    
    # Topic distribution of all documents in the model
    doc_topic_dist = np.load(doc_topic_dist_file)
    
    # Get the most similar library id
    most_sim_ids = get_most_similar_documents(doc_distribution,doc_topic_dist)
    
    # Extract the name of the library
    wanted_id = most_sim_ids[0]
    with open(name_list_file, "r") as f:
        result = f.readlines()[wanted_id]
    result = result.strip()
    
    return result
    
def search_pypi_web(lib):
    # Check against available rules
    name_list_file = resource_filename(__name__, 'rule_names_list.txt')
    check_names = set()
    with open(name_list_file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            check_names.add(line)

    # Download library's description
    try:
        lib_response = requests.get("https://pypi.org/pypi/{}/json".format(lib))
        lib_data = lib_response.json()
        lib_sum = lib_data["info"]["summary"]
        lib_desc = lib_data["info"]["description"]
    except:
        return None

    # Preprocess query
    data = lib + " " + lib_sum + " " + lib_desc
    data = re.sub(r'\S*@\S*\s?', '', data)
    data = re.sub(r'\s+', ' ', data)
    data = re.sub(r"\'", "", data)
    data_words = list(sent_to_words(data))
    data_words = remove_stopwords(data_words)
    data_words = "+".join(data_words)
    # 1000 is the limit
    # on 1001 pypi will refuse to search
    if len(data_words) > 1000:
        data_words = data_words[:1000]

    result = ""
    found = False
    page = 1 # Start from 1st page
    
    while not found:
        if page == 10: # If not found this far then stop
            return None
        response = requests.get("https://pypi.org/search/?q={}&page={}".format(data_words, page))
        soup = BeautifulSoup(response.text, 'html.parser')
        a_list = soup.find_all("span", class_="package-snippet__name")
        for i in a_list:
            if i.text in check_names:
                result = i.text
                found = True
        page += 1
      
    return result
    
    
def sent_to_words(sentence):
    yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations


def remove_stopwords(texts):
    stop_words = stopwords.words('english')
    return [word for word in simple_preprocess(str(texts)) if word not in stop_words]


def make_trigrams(texts, trigram_mod, bigram_mod):
    return trigram_mod[bigram_mod[texts]]


def lemmatization(nlp, texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    doc = nlp(" ".join(texts)) 
    texts_out = [token.lemma_ for token in doc if token.pos_ in allowed_postags]
    return texts_out
    
  
def jensen_shannon(query, matrix):
    """
    This function implements a Jensen-Shannon similarity
    between the input query (an LDA topic distribution for a document)
    and the entire corpus of topic distributions.
    It returns an array of length M where M is the number of documents in the corpus
    """
    p = query[None,:].T
    q = matrix.T
    m = 0.5*(p + q)
    return np.sqrt(0.5*(entropy(p,m) + entropy(q,m)))
    
    
def get_most_similar_documents(query,matrix,k=1):
    """
    This function implements the Jensen-Shannon distance above
    and retruns the top k indices of the smallest jensen shannon distances
    """
    sims = jensen_shannon(query,matrix) # list of jensen shannon distances
    return sims.argsort()[:k] # the top k positional index of the smallest Jensen Shannon distances
