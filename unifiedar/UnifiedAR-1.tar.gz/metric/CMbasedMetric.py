
import numpy as np
from general.utils import Data


def CMbasedMetric(cm, average=None):
    TP, FP, FN, TN = get_tp_fp_fn_tn(cm)

    accuracy = TP.sum()/cm.sum()
    precision = TP/(TP+FP)
    recall = TP/(TP+FN)
    f1 = 2*recall*precision/(recall+precision)
    for i in range(len(precision)):
        if(np.isnan(precision[i])):
            precision[i] = 0
        if(np.isnan(recall[i])):
            recall[i] = 0
        if(np.isnan(f1[i])):
            f1[i] = 0
    result = {}

    result['accuracy'] = round(accuracy,2)
    if(average is None):
        result['precision'] = precision
        result['recall'] = recall
        result['f1'] = f1
        return result

    validres = ~np.isnan(precision) & ~np.isnan(recall)
    validres[0] = False

    result['precision'] = round(np.average(precision[validres]),2)
    result['recall'] = round(np.average(recall[validres]),2)
    result['f1'] = round(2*result['precision']*result['recall'] / \
        (result['precision']+result['recall']),2)  # np.average(f1[validres])

    return result


def get_tp_fp_fn_tn(cm):
    cm = np.array(cm)
    np.seterr(divide='ignore', invalid='ignore')
    TP = np.diag(cm)
    FP = np.sum(cm, axis=0) - TP
    FN = np.sum(cm, axis=1).T - TP
    num_classes = len(cm)
    TN = []
    for i in range(num_classes):
        temp = np.delete(cm, i, 0)    # delete ith row
        temp = np.delete(temp, i, 1)  # delete ith column
        TN.append(temp.sum())
    return TP, FP, FN, TN
