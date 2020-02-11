from sklearn.cluster import Birch
from sklearn import metrics

class BirchClusteringModel:

    def __init__(self, docs, branching_factor, n_clusters, threshold, compute_labels):
        self.docs = docs
        self.branching_factor = branching_factor
        self.n_clusters = n_clusters
        self.threshold = threshold
        self.compute_labels = compute_labels
        self.model = None
        self.clusters = None
        self.labels = None
        self.silhouette_score = None



    def run_model(self):

        self.model = Birch(branching_factor =self.branching_factor, n_clusters =self.n_clusters, threshold =self.threshold, compute_labels =self.compute_labels)

        self.model.fit(self.docs)

    def predict_model(self, pred_docs):
        self.clusters = self.model.predict(pred_docs)

    def get_labels(self):
        self.labels = self.model.labels_


    def get_silhouette_score(self):
        self.silhouette_score = metrics.silhouette_score(self.docs, self.labels, metric='euclidean')



