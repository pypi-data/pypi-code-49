from classifier.classifier_abstract import Classifier
import tensorflow as tf
import numpy as np
import logging
logger = logging.getLogger(__file__)

class KerasClassifier(Classifier):
    def applyParams(self, params):
        self.epochs = params['epochs']
        return super().applyParams(params)

    def createmodel(self, inputsize, outputsize):
        self.outputsize = outputsize
        METRICS = [
            #   tf.keras.metrics.TruePositives(name='tp'),
            #   tf.keras.metrics.FalsePositives(name='fp'),
            #   tf.keras.metrics.TrueNegatives(name='tn'),
            #   tf.keras.metrics.FalseNegatives(name='fn'),
            # CategoricalTruePositives(name='tp',num_classes=outputsize,batch_size=500),
            tf.keras.metrics.SparseCategoricalAccuracy(name='acc'),
            # tf.keras.metrics.BinaryAccuracy(name='accuracy'),
            # tf.keras.metrics.Precision(name='precision'),
            # tf.keras.metrics.Recall(name='recall'),
            # tf.keras.metrics.AUC(name='auc'),
        ]

        model = self.getmodel(inputsize, outputsize)
        model.summary()
        model.compile(
            optimizer='adam', loss='sparse_categorical_crossentropy', metrics=METRICS)
        self.model = model
        return model

    def getmodel(self, inputsize, outputsize):
        raise NotImplementedError

    def train(self, trainset, trainlabel):
        return self.model.fit(trainset, trainlabel, epochs=self.epochs)

    def evaluate(self, testset, testlabel):
        self.model.evaluate(testset, testlabel)

    def predict(self, testset):
        # testset  =   np.reshape(testset, (testset.shape[0], 1, testset.shape[1]))
        return self.model.predict(testset)

    def predict_classes(self, testset):
        # testset  =   np.reshape(testset, (testset.shape[0], 1, testset.shape[1]))
        return self.model.predict_classes(testset)

    def save(self, file):
        logger.debug('saving model to %s', file)
        self.model.save(file+'.h5')

    def load(self, file):
        logger.debug('loading model from %s', file)
        if not('.h5' in file):
            file = file+'.h5'
        self.model = tf.keras.models.load_model(file)


class SequenceNN(KerasClassifier):

    def createmodel(self, inputsize, outputsize):
        self.outputsize = outputsize
        if(len(inputsize) == 1):
            inputsize=(1,inputsize[0])
        METRICS = [
            #   tf.keras.metrics.TruePositives(name='tp'),
            #   tf.keras.metrics.FalsePositives(name='fp'),
            #   tf.keras.metrics.TrueNegatives(name='tn'),
            #   tf.keras.metrics.FalseNegatives(name='fn'),
            # CategoricalTruePositives(name='tp',num_classes=outputsize,batch_size=500),
            tf.keras.metrics.SparseCategoricalAccuracy(name='acc'),
            # 'accuracy'
            # tf.keras.metrics.BinaryAccuracy(name='accuracy'),
            # tf.keras.metrics.Precision(name='precision'),
            # tf.keras.metrics.Recall(name='recall'),
            # tf.keras.metrics.AUC(name='auc'),
        ]

        model = self.getmodel(inputsize, outputsize)
        model.summary()
        model.compile(
            optimizer='adam', loss='sparse_categorical_crossentropy', metrics=METRICS)
        self.model = model
        return model

    def train(self, trainset, trainlabel):
        if(len(trainset.shape) == 2):
            trainset = np.reshape(
                trainset, (trainset.shape[0], 1, trainset.shape[1]))
        return super().train(trainset, trainlabel)

    def predict(self, testset):
        if(len(testset.shape) == 2):
            testset = np.reshape(
                testset, (testset.shape[0], 1, testset.shape[1]))
        return self.model.predict(testset)

    def predict_classes(self, testset):
        if(len(testset.shape) == 2):
            testset = np.reshape(
                testset, (testset.shape[0], 1, testset.shape[1]))
        return self.model.predict_classes(testset)


class LSTMTest(SequenceNN):

    def getmodel(self, inputsize, outputsize):

        return tf.keras.models.Sequential([
			# tf.keras.layers.Dense(128, input_shape=inputsize),
            # tf.keras.layers.Embedding(input_dim=inputsize,output_dim=100),
            tf.keras.layers.LSTM(128, activation=tf.nn .relu,input_shape=inputsize),
            #tf.keras.layers.Dense(512, activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(outputsize, activation=tf.nn.softmax)
        ], name=self.shortname())


class SimpleKeras(KerasClassifier):
    def getmodel(self, inputsize, outputsize):
        return tf.keras.models.Sequential([
            tf.keras.layers.Dense(128, input_shape=inputsize),
            tf.keras.layers.Dense(512, activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(outputsize, activation=tf.nn.softmax)
        ], name=self.shortname())


class WangMLP(KerasClassifier):
    from pyActLearn.learning.nn.mlp import MLP

    def getmodel(self, inputsize, outputsize):
        return MLP(inputsize, outputsize, [1000])


class CategoricalTruePositives(tf.keras.metrics.Metric):
    import tensorflow.keras.backend as K

    def __init__(self, num_classes, batch_size,
                 name="categorical_true_positives", **kwargs):
        super(CategoricalTruePositives, self).__init__(name=name, **kwargs)

        self.batch_size = batch_size
        self.num_classes = num_classes

        self.cat_true_positives = self.add_weight(
            name="ctp", initializer="zeros")

    def update_state(self, y_true, y_pred, sample_weight=None):

        y_true = K.argmax(y_true, axis=-1)
        y_pred = K.argmax(y_pred, axis=-1)
        y_true = K.flatten(y_true)

        true_poss = K.sum(K.cast((K.equal(y_true, y_pred)), dtype=tf.float32))

        self.cat_true_positives.assign_add(true_poss)

    def result(self):

        return self.cat_true_positives
