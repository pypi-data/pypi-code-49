import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import itertools
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, matthews_corrcoef
from sklearn.metrics import f1_score, confusion_matrix, precision_recall_curve
from sklearn.metrics import auc, roc_auc_score, roc_curve, classification_report
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split


def split_data(self, X, y, test_size=0.2):
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=test_size,
                                                        random_state=42)
    print("Number transactions X_train dataset: ", X_train.shape)
    print("Number transactions y_train dataset: ", y_train.shape)
    print("Number transactions X_test dataset: ", X_test.shape)
    print("Number transactions y_test dataset: ", y_test.shape)
    print("Before OverSampling, counts of label '1': {}".format(
        y_train[y_train['class'] == 1].count()))
    print("Before OverSampling, counts of label '0': {} \n".format(
        y_train[y_train['class'] == 0].count()))
    return X_train, X_test, y_train, y_test


def upsample_data(X_train, y_train):
    sm = SMOTE(random_state=2)
    X_train_res, y_train_res = sm.fit_sample(X_train, y_train['class'].ravel())
    print('After OverSampling, the shape of train_X: {}'.format(
        X_train_res.shape))
    print('After OverSampling, the shape of train_y: {} \n'.format(
        y_train_res.shape))
    print("After OverSampling, counts of label '1': {}".format(
        sum(y_train_res == 1)))
    print("After OverSampling, counts of label '0': {}".format(
        sum(y_train_res == 0)))
    return X_train_res, y_train_res


class MLModel(object):
    def __init__(self, model):
        self.model = model

    def fit(self, X_train, y_train):
        X_train = np.array(X_train)
        y_train = np.array(y_train)
        self.model.fit(X_train, y_train.ravel())

    def plot_confusion_matrix(self,
                              cm,
                              classes,
                              normalize=True,
                              title='Confusion matrix',
                              cmap=plt.cm.cubehelix_r):
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)

        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=0)
        plt.yticks(tick_marks, classes)
        plt.colorbar()
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j,
                     i,
                     cm[i, j],
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

    def metrics(self, X, y, class_names=["TDC", "Autism"]):
        y_pre = self.predict(X)
        print("Accuracy", accuracy_score(y, y_pre))
        cnf_matrix = confusion_matrix(y, y_pre)
        precision = cnf_matrix[1, 1] / (cnf_matrix[0, 1] + cnf_matrix[1, 1])
        recall = cnf_matrix[1, 1] / (cnf_matrix[1, 0] + cnf_matrix[1, 1])
        print("Recall:{}".format(recall))
        print("Precision: {}".format(precision))
        f1_score = 2 * ((recall * precision) / (recall + precision))
        print("F1 Score: {}".format(f1_score))
        print("MCC Score: {}".format(matthews_corrcoef(y, y_pre)))
        plt.figure()
        self.plot_confusion_matrix(cnf_matrix,
                                   classes=class_names,
                                   title='Confusion matrix',
                                   normalize=False)
        plt.show()

    def save(path):
        pickle.dump(self.model, open(path, "wb"))

    def plot_auc(self, X_test, y_test):
        y_pred_sample_score = self.predict_proba(X_test)
        fpr, tpr, thresholds = roc_curve(y_test, y_pred_sample_score[:, 1])
        roc_auc = auc(fpr, tpr)
        # Plot ROC
        plt.title('Receiver Operating Characteristic (Test Set)')
        plt.plot(fpr, tpr, 'b', label='AUC = %0.3f' % roc_auc)
        plt.legend(loc='lower right')
        plt.plot([0, 1], [0, 1], 'r--')
        plt.xlim([-0.1, 1.0])
        plt.ylim([-0.1, 1.01])
        plt.ylabel('True Positive Rate')
        plt.xlabel('False Positive Rate')
        plt.show()

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)