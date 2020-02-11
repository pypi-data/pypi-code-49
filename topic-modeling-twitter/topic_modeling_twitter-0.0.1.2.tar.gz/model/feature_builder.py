from gensim import corpora
from nltk.tokenize import TweetTokenizer
from gensim.models import Phrases

class Feature_builder:
    def __init__(self, corpus, bi_trigram, min_ngram_freq=1, ngram_thresh=1):
        self.corpus = corpus
        self.bi_trigram = bi_trigram
        self.min_ngram_freq = min_ngram_freq
        self.ngram_thresh = ngram_thresh


    def _tokenize_text(self):
        if self.bi_trigram:
            tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
            tokenized_corpus = [tknzr.tokenize(txt.lower()) for txt in self.corpus]
            bigram_model = Phrases(tokenized_corpus, min_count=self.min_ngram_freq, threshold=self.ngram_thresh)
            trigram_model = Phrases(bigram_model[tokenized_corpus], min_count=self.min_ngram_freq, threshold=self.ngram_thresh)
            tokens = list(trigram_model[bigram_model[tokenized_corpus]])
        else:
            tokens = [str(doc).split() for doc in self.corpus]

        return tokens

    # Preparing Document-Term Matrix
    def _create_doc_term_matrix(self, tokens, dictionary_create):
        # Creating the term dictionary of our courpus, where every unique term is assigned an index.
        # corpus = [str(doc).split() for doc in corpus]

        if (dictionary_create is None):
            dictionary = corpora.Dictionary(tokens)
        else:
            dictionary = dictionary_create

        # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
        doc_term_matrix = [dictionary.doc2bow(doc) for doc in tokens]
        return (dictionary,doc_term_matrix)

    def create_feature_matrix(self, dictionary_create=None):
        tokens = self._tokenize_text()
        dictionary, doc_term_matrix = self._create_doc_term_matrix(tokens, dictionary_create)
        return (dictionary, doc_term_matrix, tokens)

