import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import numpy as np

class ProblemParams:
    def __init__(self, solution):
        self.solution = solution


    def getMetrics(self):
        f = open(self.solution.data_path)
        data_dict = json.load(f)
        news_items=[]
        targets = []
        for key in data_dict.keys():
            news_items.append(data_dict[key]['data'])
            targets.append(data_dict[key]['target'])
        features = self.solution.createFeatures(news_items)
        targets_df = pd.DataFrame(targets)
        X_train, X_test, y_train, y_test = train_test_split(features, targets_df, test_size = self.solution.split)
        self.solution.train(X_train,y_train)
        predictions = self.solution.predict(X_test)
        scores = []
        for i,col in enumerate(predictions.columns):
            scores.append(roc_auc_score(y_test[col], predictions[col]))
        score = np.mean(scores)
        return score