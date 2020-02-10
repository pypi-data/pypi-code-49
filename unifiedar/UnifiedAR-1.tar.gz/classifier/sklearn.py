from classifier.classifier_abstract import Classifier
import sklearn.ensemble
import sklearn.neighbors
import sklearn.svm
import sklearn.tree
import sklearn.multiclass
import numpy as np


class sklearnClassifier(Classifier):

    def createmodel(self, inputsize, outputsize):
        self.outputsize = outputsize
        self.inputsize = inputsize
        self.model = self.getmodel(inputsize, outputsize)
        return self.model

    def getmodel(self, inputsize, outputsize):
        raise NotImplementedError

    def train(self, trainset, trainlabel):
        return self.model.fit(trainset, trainlabel)

    def evaluate(self, testset, testlabel):
        self.model.evaluate(testset, testlabel)

    def predict(self, testset):
        try:
            return self.model.predict_proba(testset)
        except AttributeError:
            res=np.zeros((len(testset),self.outputsize))
            cls=self.predict_classes(testset)
            for i in range(0,len(testset)):
                 res[i]=cls[i]
            return res

    def predict_classes(self, testset):
        return self.model.predict(testset)


class UAR_KNN(sklearnClassifier):
    def applyParams(self, params):
        self.k = params.get('k', 5)
        return super().applyParams(params)

    def getmodel(self, inputsize, outputsize):
        return sklearn.neighbors.KNeighborsClassifier(n_neighbors=self.k)


class UAR_RandomForest(sklearnClassifier):
    def getmodel(self, inputsize, outputsize):
        return sklearn.ensemble.RandomForestClassifier(n_estimators=self.n_estimators, random_state=self.random_state)


class UAR_SVM(sklearnClassifier):
    def getmodel(self, inputsize, outputsize):
        # return sklearn.svm.SVC(kernel=self.kernel,gamma=0.001, C=100., probability=True)
        return sklearn.svm.SVC( kernel=self.kernel,gamma=self.gamma,C=self.C, decision_function_shape='ovr',probability=True)

class UAR_SVM2(sklearnClassifier):
    def getmodel(self, inputsize, outputsize):
        # return sklearn.svm.SVC(kernel=self.kernel,gamma=0.001, C=100., probability=True)
        model1=sklearn.svm.SVC( kernel=self.kernel,gamma=self.gamma,C=self.C, decision_function_shape='ovr',probability=True)
        return sklearn.multiclass.OneVsOneClassifier(model1)


class UAR_DecisionTree(sklearnClassifier):
    def getmodel(self, inputsize, outputsize):
        return sklearn.tree.DecisionTreeClassifier()
