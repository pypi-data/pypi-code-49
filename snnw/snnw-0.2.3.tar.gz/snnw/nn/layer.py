import numpy as np

from snnw.nn.weight_init import kaiming


class Layer:
    # These layers are fully connected by default
    def __init__(self, layer_type, in_size, out_size, activation):
        # only type supported is fully connected
        assert (layer_type == "fully_connected"), "only fully connected layers are supported"
        self.layer_type = "fully_connected"
        # in_size is number of neuron in previous layer
        self.in_size = in_size
        # out_size is number of neurons in current layer
        self.out_size = out_size
        # activation function name
        self.activation = activation
        # make random weight array
        self.weights = kaiming(in_size, out_size)
        # make random bias array
        self.biases = np.zeros(shape=(1, self.out_size))
        # make output array
        self.output = None
