import spacy
from multiprocessing import Pool

class SimpleSpacyCleaner:
    """
    A simple spacy cleaner that removes stopwords, punctuation, digits and does lemmatization
    """
    def __init__(self, spacy_model):
        """
        Loading the spacy model to clean text
        :param spacy_model: e.g., en_core_web_sm
        """
        self.spacy = spacy.load(spacy_model, disable=["tagger", "parser", "ner"])

    def clean(self, text):
        """
        cleaning text: removing stopwords, punctuation, digits and doing lemmatization
        :param text:
        :return:
        """

        text = " ".join(text.split())

        doc = self.spacy(text)

        tokens = [token.lemma_.strip() for token in doc if
                  not token.is_stop
                  and not self.spacy.vocab[token.lemma_].is_stop
                  and not token.is_punct
                  and not token.is_digit
                  ]
        text = " ".join(tokens)

        return text.lower()

    def parallel_cleaner(self, list_of_texts, n_cpus):
        """
        parallel cleaning of texts using Pool
        :param list_of_texts:
        :param n_cpus:
        :return:
        """

        p = Pool(n_cpus)

        data = p.map(self.clean, list_of_texts)
        data = [x for x in data if x is not None]
        p.terminate()
        p.join()

        return data
