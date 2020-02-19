from tensorflow.keras.datasets import cifar10
import numpy as np
import tensorflow as tf


def cifar10_validation_set(subtract_pixel_mean=True, limit=None):
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    num_classes = 10

    # Normalize data.
    x_train = x_train.astype('float32') / 255
    x_test = x_test.astype('float32') / 255

    # If subtract pixel mean is enabled
    if subtract_pixel_mean:
        x_train_mean = np.mean(x_train, axis=0)
        x_train -= x_train_mean
        x_test -= x_train_mean

    y_test = tf.keras.utils.to_categorical(y_test, num_classes)
    if limit:
        return x_test[:limit], y_test[:limit]
    return x_test, y_test
