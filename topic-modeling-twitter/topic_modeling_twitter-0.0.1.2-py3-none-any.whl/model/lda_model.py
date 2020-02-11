import gensim
from gensim.models import CoherenceModel
from gensim.models import LdaModel

# import sys
# sys.path.insert(0, 'topic_modeling_twitter')
from topic_modeling.utils_ import isfloat


class Lda_Model:
    def __init__(self, dictionary=None, doc_term_matrix=None, tokens=None, num_topics=None, alpha=None, eta=None,\
                 passes=None,decay=None):
        self.dictionary = dictionary
        self.doc_term_matrix = doc_term_matrix
        self.tokens = tokens
        self.num_topics = num_topics
        self.alpha = alpha
        self.eta = eta
        self.passes = passes
        self.decay = decay

    def run_model(self):
        # Creating the object for LDA model using gensim library
        Lda = gensim.models.ldamodel.LdaModel

        if isfloat(self.alpha):
            self.alpha = [self.alpha] * self.num_topics

        if isfloat(self.eta):
            self.eta = [self.eta] * len(self.dictionary.keys())

        # Running and Trainign LDA model on the document term matrix.
        self.ldamodel = Lda(self.doc_term_matrix, num_topics=self.num_topics, id2word=self.dictionary, random_state=100,
                       update_every=1,
                       chunksize=500,
                       passes=self.passes,
                       alpha=self.alpha,
                       eta=self.eta,
                       decay=self.decay,
                       per_word_topics=True)

    def save_model(self,output_fp):
        self.ldamodel.save(output_fp)


    def load_model(self,model_file):
        self.ldamodel =LdaModel.load(model_file)

    def get_coherence_value(self):
        coherencemodel = CoherenceModel(model=self.ldamodel, texts=self.tokens, dictionary=self.dictionary, coherence='c_v')
        return coherencemodel.get_coherence()

    # Perplexity: Lower the better. Perplexity = exp(-1. * log-likelihood per word)
    def get_perplexity_value(self):
        return self.ldamodel.log_perplexity(self.doc_term_matrix)

    def get_topic_words(self, num_words_per_topic):
        topics_words = []
        for index, topic in self.ldamodel.show_topics(formatted=False, num_words = num_words_per_topic):
            topic_dict = {"id": int(index)}
            c = 0
            for w in topic:
                topic_dict["word" + str(c)] = w[0]
                c += 1
            topics_words.append(topic_dict)
        return topics_words
