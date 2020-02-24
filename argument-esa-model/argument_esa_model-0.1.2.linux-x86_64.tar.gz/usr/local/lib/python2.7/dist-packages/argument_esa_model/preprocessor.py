import re
import pickle
import pandas as pd
from collections import Counter
from nltk.stem import WordNetLemmatizer 

class Preprocessor:


    def __init__(self, vocab_path):
        self._lemmatizer = WordNetLemmatizer()
        if vocab_path is not None:
            self._vocab = set(pickle.load(open(vocab_path,"rb")))


    def preprocess(self, input, lemma = False):
        df = pd.read_csv(input)
        preprocessed = {}
        for index, row in df.iterrows():
            preprocessed[row["concept"]] = self.to_bow(row["text"], lemma)
        return preprocessed


    def tokenize(self, text, lemma):
        text = text.lower()
        text = text.replace("\n", " ").replace("\r", " ")
        text = re.sub(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", " ", text)
        tokens = re.sub("[^A-Za-z]+", " ", text).replace("  ", " ")
        if lemma:
            tokens = [self._lemmatizer.lemmatize(word.strip()) for word in tokens.split(" ")]
            tokens = [t for t in tokens if not len(t) < 4]
            tokens = [t for t in tokens if t in self._vocab]
        else:
            tokens = tokens.split(" ")
            tokens = [t for t in tokens if not len(t) < 4]
        return tokens 


    def to_bow(self, text, lemma):
        return dict(Counter(self.tokenize(text, lemma)))
