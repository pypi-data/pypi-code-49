import gensim.models as g


class Doc2VecModel:

    def __init__(self, trained_model_fp, alpha, step):
        self.alpha = alpha
        self.step = step
        self.trained_model_fp = trained_model_fp
        self.model = None

    def load_model(self):
        """ load model """
        self.model = g.Doc2Vec.load(self.trained_model_fp)

    def infer_vector(self, doc):
        return self.model.infer_vector(doc, alpha=self.alpha, steps=self.step)


