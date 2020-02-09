import numpy as np
import pandas as pd
from collections import Counter
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_recall_fscore_support as prfc_metrics


__all__ = ['multiclass_cross_val_results', 'calc_class_weights']


def multiclass_cross_val_results(features_matrix, labels, model, 
                                 n_folds=3, random_state=42, shuffle=True, 
                                 labels_names=None):
    res = []
    stratified_k_fold = StratifiedKFold(n_splits=n_folds, random_state=random_state, shuffle=shuffle)
    for train_index, test_index in stratified_k_fold.split(features_matrix, labels):
        scaler = StandardScaler()
        train_features_matrix = scaler.fit_transform(features_matrix[train_index])
        test_features_matrix = scaler.transform(features_matrix[test_index])
        model = model.fit(train_features_matrix, labels[train_index])
        test_labels_predict = model.predict(test_features_matrix)
        metrics_per_label = prfc_metrics(labels[test_index], test_labels_predict, average=None)[:-1]
        res.append(metrics_per_label)
    res = np.asarray(res).mean(axis=0).T
    res = np.vstack((res, res.mean(axis=0)[np.newaxis, :]))

    if labels_names is None:
        labels_names = [str(i) for i in range(res.shape[0] - 1)]
    labels_names += ('mean',)

    return pd.DataFrame.from_records(
        res, columns=['precision', 'recall', 'f1-score'],
        index=tuple(labels_names) + ('mean',)
    )


def calc_class_weights(labels, mode='ratio_from_max'):
    """
    :param labels: iterable, classes labels
    :param mode: str, determine classes weights calculation strategy
        options:
            - ratio_from_max
            (default: ratio_from_max).
    :return: dict, class label to class weight
    >>> labels = [1,1,1,2,2,3]
    >>> calc_class_weights(labels)
    {1: 1.0, 2: 1.5, 3: 3.0}
    """
    if mode == 'ratio_from_max':
        labels_counter = Counter(labels)
        max_label_count = max(labels_counter.values())
        return {label: max_label_count/label_count 
                for label, label_count in labels_counter.items()}
    else:
        raise NotImplementedError()
