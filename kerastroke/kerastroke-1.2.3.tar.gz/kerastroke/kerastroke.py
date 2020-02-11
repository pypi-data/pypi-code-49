import keras
import random
import numpy as np

from keras.layers import Layer
from keras.callbacks import Callback

import warnings

"""
class StrokeLayer(Layer):

    def __init__(self, previous_layer=None, volatility_ratio=.1):
        warnings.warn("DO NOT USE THE STROKE LAYER, IT DOES NOT FUNCTION AS PLANNED.\nINSTEAD USE THE STROKE CALLBACK.")
        super(StrokeLayer, self).__init__()
        self.player = previous_layer
        self.num_outputs = previous_layer.output_shape[-1]
        self.vratio = volatility_ratio

    def call(self, input):
        weights = self.player.get_weights()[0]
        biases = self.player.get_weights()[1]
        print(type(weights))
        num_weights = len(weights)
        for stricken in range(0, int(num_weights * self.vratio)):
            index = random.randint(0, num_weights)
            weights[index] = random.uniform(-.05, .05)
        self.set_weights([weights, biases])
        return input

    def build(self, input_shape):
        weights = self.player.get_weights()[0]
        biases = self.player.get_weights()[1]
        tup = self.player.output_shape
        for _, dim in enumerate(tup):
            self.output_dim=dim
        self.kernel = self.add_weight(name='kernel',
                                      shape=(input_shape[1], self.output_dim),
                                      initializer='uniform',
                                      trainable=True)
        self.set_weights([weights, biases])
        super(StrokeLayer, self).build(input_shape)
"""
class Stroke(Callback):

    def __init__(self, stroke=True, minweight=-.05, maxweight=.05, volatility_ratio=.05, decay=None, index=None, verbose=False, pruning=True, pruningmin=0.0, pruningmax=0.2):
        assert isinstance(stroke, bool), "stroke must be a boolean"
        self.stroke = stroke

        assert isinstance(minweight, float), "minweight must be a float"
        self.minweight = minweight

        assert isinstance(maxweight, float), "maxweight must be a float"
        self.maxweight = maxweight

        assert isinstance(volatility_ratio, float), "volatility_ratio must be a float"
        assert volatility_ratio < 1.0, "volatility_ratio must be less than 1.0"
        self.vratio = volatility_ratio

        assert isinstance(verbose, bool), "verbose must be a boolean"
        self.verbose = verbose

        if(not index is None):
            assert isinstance(index, int), "index must be a int"
        self.index = index
        if(not decay is None):
            assert isinstance(decay, float), "decay must be a float"
        self.decay = decay

        assert isinstance(pruning, bool), "pruning must be a boolean"
        self.pruning = pruning

        assert isinstance(pruningmin, float), "pruningmin must be a float"
        self.pruningmin = pruningmin

        assert isinstance(pruningmax, float), "pruningmax must be a float"
        self.pruningmax = pruningmax

    def on_epoch_end(self, batch, logs=None):
        if(self.stroke):
            if(self.index is None):

                weights = self.model.get_weights()[0]
                biases = self.model.get_weights()[1]

                num_weights = len(np.nditer(weights))

                for stricken in range(int(num_weights * self.vratio)):
                    weights[tuple(map(lambda x: np.random.randint(0, x), weights.shape))] = random.uniform(self.minweight, self.maxweight)

                self.model.set_weights([weights,  biases])

                if(self.verbose):
                    out = ("Gave " + self.model.name + " a stroke on " + str(int(self.vratio * 100)) + "% of its weights.")
                    print(out)

            else:
                weights = self.model.get_layer(index=self.index).get_weights()[0]
                biases = self.model.get_layer(index=self.index).get_weights()[1]

                num_weights = len(np.diter(weights))

                for stricken in range(int(num_weights * self.vratio)):
                    weights[tuple(map(lambda x: np.random.randint(0, x), weights.shape))] = np.uniform(self.minweight, self.maxweight)

                self.model.get_layer(index=self.index).set_weights([weights,  biases])

                if(self.verbose):
                    out = ("Gave " + self.model.get_layer(index=self.index).name + " a stroke on " + str(int(self.vratio * 100)) + "% of its weights.")
                    print(out)

        if(self.pruning):
            weights = self.model.get_weights()[0].copy()
            biases = self.model.get_weights()[1].copy()

            new_weights = np.empty_like(weights)
            for weight in np.nditer(new_weights, op_flags = ['readwrite']):
                if(weight >= self.pruningmin and weight <= self.pruningmax):
                    weight = 0;

            self.model.set_weights([weights, biases])


        if(not self.decay is None and self.vratio > .01 and self.vratio < 1.0):
            self.vratio = self.vratio * self.decay
            if(self.verbose):
                print("Linear decay has reduced volatility_ratio by " + str(int(self.decay * 100)) + "%")
