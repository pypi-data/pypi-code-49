import typing as ty
import numpy as np
import pandas as pd
import math
from sklearn.metrics import confusion_matrix


class WeightedCentroidDistance:

    def __init__(self, distribution: ty.Dict):
        self.distribution = distribution

    @staticmethod
    def get_distribution(y: ty.List, inverse: bool = False):
        distribution = {}
        unique_values = np.unique(y)
        if inverse is False:
            for zl in unique_values:
                distribution[zl] = y.count(zl)**2
        else:
            for zl in unique_values:
                distribution[zl] = 1 / ((y.count(zl))**2)
            min_val = distribution[min(distribution, key=distribution.get)]
            approved = False
            multiplier = 10
            while approved is False:
                if min_val < 1:
                    min_val = min_val * multiplier
                    multiplier = multiplier * 10
                else:
                    approved = True
            for k, v in distribution.items():
                distribution[k] = int(v * multiplier)
        return distribution

    def get_distance(self, y: ty.List, y_hat: ty.List):
        labels = list(self.distribution.keys())
        numdims = len(labels)

        # Construct a confusion matrix
        confm = confusion_matrix(y, y_hat, labels=labels)
        tprlist = self.__tprfpr(confm, numdims)[0]
        fprlist = self.__tprfpr(confm, numdims)[1]

        tprfprcombine = pd.DataFrame(np.vstack((labels, tprlist, fprlist)).T)
        tprfprcombine.columns = ["class_name", "tpr", "fpr"]
        d = [[k, v] for k, v in self.distribution.items()]
        bothdf = pd.DataFrame(d)
        bothdf.columns = ["class_name", "weight"]
        merged_inner = pd.merge(left=bothdf, right=tprfprcombine, left_on="class_name", right_on="class_name")
        merged_inner_matrix = merged_inner.as_matrix()

        weights_vec = np.asarray(merged_inner_matrix[:, 1])
        tpr_vec = np.asarray(merged_inner_matrix[:, 2])
        fpr_vec = np.asarray(merged_inner_matrix[:, 3])

        tpr_vec2 = []
        for x in tpr_vec:
            val = float(x)
            tpr_vec2.append(val)
        fpr_vec2 = []
        for x in fpr_vec:
            val = float(x)
            fpr_vec2.append(val)
        weights_vec2 = []
        for x in weights_vec:
            val = float(x)
            weights_vec2.append(val)

        weighted_tpr_list = []
        weighted_fpr_list = []
        for g in range(numdims):
            for f in range(int(weights_vec2[g])):
                weighted_tpr_list.append(tpr_vec2[g])
                weighted_fpr_list.append(fpr_vec2[g])

        newaveragenum = np.sum(weights_vec2)
        weighted_avg_tprfpr = [np.sum(weighted_tpr_list) * (1 / newaveragenum), np.sum(weighted_fpr_list) * (1 / newaveragenum)]
        perfecto = [1.0, 0.0]

        weighttprdiff = weighted_avg_tprfpr[0] - perfecto[0]
        weightfprdiff = weighted_avg_tprfpr[1] - perfecto[1]
        weightdistance = 0
        if weighttprdiff == 0 and weightfprdiff == 0:
            pass
        else:
            weightdistance = math.hypot(weighttprdiff, weightfprdiff)

        return weightdistance

    def __tprfpr(self, confm: np.ndarray, numdims: int):
        tprlist = []
        fprlist = []
        for w in range(numdims):
            truepos = confm[w, w]
            trueneg = np.sum(np.diag(confm)) - truepos
            falseneg = sum(confm[w, :]) - truepos
            falsepos = sum(confm[:, w]) - truepos

            addition1 = truepos + falseneg
            addition2 = falsepos + trueneg
            if addition1 == 0 or addition2 == 0:
                tpr = 0
                fpr = 0
            else:
                tpr = truepos / addition1
                fpr = falsepos / addition2

            tprlist.append(tpr)
            fprlist.append(fpr)
        return tprlist, fprlist
