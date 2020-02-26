import pandas as pd
from pythainlp import word_tokenize, sent_tokenize
import pickle

def create_word_list(source_path, destination_path):
    data = pd.read_csv(source_path, sep=',', doublequote=True)
    result = list()
    for sentence in data.message:
        words = word_tokenize(sentence, engine='newmm', keep_whitespace=False)
        striped_word = [ word.strip() for word in words if len(word) > 1 and word.strip() != '']
        result.extend(striped_word)
    print('Tokenize completed')
    with open(destination_path, 'wb') as f:
        pickle.dump(result, f)

def create_hashtag_list(source_path, destination_path):
    data = pd.read_csv(source_path, sep=',', doublequote=True)
    result = list()
    for sentence in data.message:
        words = sent_tokenize(sentence, engine='attacut')
        hashtag = [ word.strip() for word in words if word[0] == '#']
        result.extend(hashtag)
    with open(destination_path, 'wb') as f:
        pickle.dump(result, f)