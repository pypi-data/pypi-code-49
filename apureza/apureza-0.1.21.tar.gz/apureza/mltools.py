# -*- coding: utf-8 -*-

""" Machine learning tools

More detailed description.
"""
import copy
import numpy as np
import warnings
from abc import abstractmethod
from functools import wraps

from keras import Sequential
from keras.callbacks import EarlyStopping
from keras.layers import Dense, BatchNormalization
from keras.utils import to_categorical
from scipy.stats import pearsonr
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from apureza.exceptions import KerasMlpError, DataWarning, DataError


def return_new_instance(method):
    @wraps(method)
    def _return_new_instance(self, *args, **kwargs):
        output = method(self, *args, **kwargs)
        if isinstance(output, np.ndarray):
            new_self = self.__class__(output)
            return new_self
        else:
            return output
    return _return_new_instance


def pearson(x, y):
    """ Compute pearson correlation coefficient

    :param x: numpy array
    :param y: numpy array
    :return:
    """
    try:
        cc, p_value = pearsonr(x, y)
    except TypeError:
        try:
            cc, p_value = pearsonr(x.flatten(), y.flatten())
        except ValueError:
            raise DataError("Input must have the same length")
    except Exception as e:
        raise DataError("Unknown error:\n '%s'" % e)

    return cc, p_value


class Data:

    _normalizer = None
    _standardizer = None

    def __init__(self, data):
        """ Data constructor

        :param data: numpy array
        """
        try:
            if data.ndim == 1:
                data = data.reshape(-1, 1)
        except AttributeError:
            raise DataError("Input must be a numpy array but is '%s'" % type(data))

        self._data = data

    def _inv_scale(self, scaler_name):
        scaler_name = "_" + scaler_name
        scale_data = self.copy()

        if self.__getattribute__(scaler_name):
            scale_data.__setattr__(scaler_name, None)
            scale_data._data = self.__getattribute__(scaler_name).inverse_transform(self._data)

        return scale_data

    def _scale(self, scaler_name, scaler):
        scaler_name = "_" + scaler_name
        scale_data = self.copy()

        if not self.__getattribute__(scaler_name):
            scale_data.__setattr__(scaler_name, scaler)
            scale_data._data = scaler.fit_transform(self._data)
        else:
            warnings.warn("Cannot scale data that have already been scaled", DataWarning)

        return scale_data

    @return_new_instance
    def __getitem__(self, item):
        return self._data.__getitem__(item)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)

    def copy(self):
        return copy.deepcopy(self)

    @return_new_instance
    def from_categorical(self, axis=1):
        """ Convert binary class matrix to class vector (integers)

        :return:
        """
        return self._data.argmax(axis=axis)
        # return np.apply_along_axis(np.argwhere, axis=1, arr=self._data).flatten()

    def normalize(self, lower_bound=0, upper_bound=1):
        """ Normalize data

         Rescale from original range to the new range [lower_bound; upper_bound]
        :param lower_bound: lower bound of the new range
        :param upper_bound: upper bound of the new range
        :return:
        """
        return self._scale("normalizer", MinMaxScaler(feature_range=(lower_bound, upper_bound)))

    def normalize_inv(self):
        """ Inverse normalization transform

        :return:
        """
        return self._inv_scale("normalizer")

    def standardize(self):
        """ Standardize data

        Standardization: rescaling distribution of values so that
        the mean of observed values is 0 and standard deviation is 1.
        :return:
        """
        return self._scale("standardizer", StandardScaler())

    def standardize_inv(self):
        """ Inverse standardization transform

        :return:
        """
        return self._inv_scale("standardizer")

    @return_new_instance
    def to_categorical(self, lower_bound, upper_bound, nb_of_classes):
        """ Converts data to binary class matrix.

        :param lower_bound: lower bound of data range
        :param upper_bound: upper bound of data range
        :param nb_of_classes: number of classes to categorize
        :return:
        """
        # Classes from 0 to nb_of_classes (right upper bin not included)
        category = np.digitize(self._data, np.linspace(lower_bound, upper_bound, nb_of_classes + 1)) - 1

        # Classes from 0 to nb_of_classes - 1 (right upper bin now included)
        category[category == nb_of_classes] = category[category == nb_of_classes] - 1

        return to_categorical(category)

    def to_csv(self, path_to_file, delimiter=","):
        """ Write to csv file

        :return:
        """
        np.savetxt(path_to_file, self._data, delimiter=delimiter)

    @property
    def values(self):
        return self._data.copy()

    @property
    def normalizer(self):
        return self._normalizer

    @property
    def standardizer(self):
        return self._standardizer

    @classmethod
    def from_csv(cls, path_to_file, delimiter=","):
        return cls(np.genfromtxt(path_to_file, delimiter=delimiter))


class ImgData(Data):
    """ Image data

    """


class NeuralNetwork:

    model = None

    @abstractmethod
    def build(self, *args, **kwargs):
        pass

    @abstractmethod
    def train(self, *args, **kwargs):
        pass

    @abstractmethod
    def predict(self, *args, **kwargs):
        pass


class KerasMlp(NeuralNetwork):
    """ Keras-based multilayer perceptron

    """
    dataset = dict(test=None, train=None, valid=None)

    def __init__(self):

        self.model = Sequential()

    def build(self, nb_inputs, nb_outputs, nb_hidden_layer=1, hidden_activation=('sigmoid',), nb_hidden_units=(32,),
              output_activation='linear'):
        """ Build network architecture

        :param nb_inputs: number of input units
        :param nb_outputs: number of output units
        :param nb_hidden_layer: number of hidden layer
        :param hidden_activation: activation function type for each hidden layer
        :param nb_hidden_units: number of hidden units for each hidden layer
        :param output_activation: output activation function type
        :return:
        """
        try:
            assert nb_hidden_layer == len(hidden_activation) == len(nb_hidden_units)
        except AssertionError:
            raise KerasMlpError("Hidden attributes must have the same size:\n -nb of hidden layers=%d\n -hidden "
                                "activation functions=%d\n -hidden units tuple length=%d" %
                                (nb_hidden_layer, len(hidden_activation), len(nb_hidden_units)))
        # Hidden layers
        for layer in range(nb_hidden_layer):
            if layer == 0:
                self.model.add(BatchNormalization(input_shape=(nb_inputs,)))
            else:
                self.model.add(BatchNormalization())
            self.model.add(Dense(units=nb_hidden_units[layer], activation=hidden_activation[layer]))

        # Output layer
        self.model.add(Dense(units=nb_outputs, activation=output_activation))

        return self

    def train(self, input_data, output_target, batch_size=None, validation_split=0.3, epochs=100,
              early_stopping=True, stop_after=10, min_delta=1e-6, monitor='val_loss', optimizer='rmsprop',
              loss_function='mean_squared_error', metrics=None):
        """ Train neural network

        :param input_data: Input data (numpy array)
        :param output_target: Output target(s) as numpy array
        :param batch_size: number of samples per gradient update
        :param validation_split: value for validation samples within data
        :param epochs:
        :param early_stopping:
        :param stop_after: nb of epochs to stop after (if early_stopping is True)
        :param min_delta: minimum change in the monitored quantity to qualify as an improvement
        :param monitor: which loss to monitor for early stopping ('loss' or 'val_loss')
        :param optimizer: optimizer name
        :param loss_function: loss function name
        :param metrics: see keras metrics (to assess accuracy of the network)
        :return:
        """

        # Compile model
        self.model.compile(optimizer=optimizer, loss=loss_function, metrics=metrics)

        # Early stopping
        if early_stopping:
            early_stopping = [EarlyStopping(monitor=monitor, min_delta=min_delta, patience=stop_after,
                                            restore_best_weights=True)]
        else:
            early_stopping = None

        # Train model using keras "fit" model function
        self.model.fit(input_data, output_target, callbacks=early_stopping, batch_size=batch_size,
                       validation_split=validation_split, epochs=epochs)

        return self

    def predict(self, input_data, *args, **kwargs):
        """

        :param input_data: numpy array
        :param args:
        :param kwargs:
        :return:
        """
        return self.model.predict(input_data)


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    rgb = Data.from_csv("/home/ird/Desktop/Apureza project/FOTO/FOTO "
                        "code/window_size=40/rgb.csv").normalize(-1, 1)
    # rgb = Data.from_csv("/home/ird/Desktop/Apureza project/FOTO/FOTO "
    #                     "code/window_size=40/rgb_mean_intensity_is_centered_and_psd_is_normalized_by_variance.tif")
    density = Data.from_csv("/home/ird/Documents/apureza/data/density.csv").normalize()
    ann = KerasMlp().build(nb_inputs=3, nb_outputs=1, nb_hidden_layer=3, nb_hidden_units=(64, 32, 64),
                           hidden_activation=('sigmoid', 'sigmoid', 'sigmoid'), output_activation='linear').train(
        rgb.values, density.values, batch_size=64, validation_split=0.6, epochs=300, early_stopping=False,
        optimizer="rmsprop", loss_function='mean_squared_error', metrics=['accuracy'])
    estimated_density = ann.predict(rgb.values)
    measured_density = density.values
    print("corr coeff = %.2f (p-value = %f)" % pearson(measured_density, estimated_density))
    plt.figure(1)
    plt.imshow(estimated_density.reshape(88, 125))
    plt.figure(2)
    plt.imshow(measured_density.reshape(88, 125))
    plt.show()
