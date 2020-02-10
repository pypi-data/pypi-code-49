from general.utils import MyTask


class Classifier(MyTask):
    def createmodel(self, inputsize, outputsize):
        raise NotImplementedError

    def train(self, trainset, trainlabel):
        raise NotImplementedError

    def evaluate(self, testset, testlabel):
        raise NotImplementedError

    def predict(self, testset):
        raise NotImplementedError

    def predict_classes(self, testset):
        raise NotImplementedError
