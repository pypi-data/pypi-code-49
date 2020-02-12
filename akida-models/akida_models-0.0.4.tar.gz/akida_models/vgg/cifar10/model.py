#!/usr/bin/env python
# ******************************************************************************
# Copyright 2020 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************

import os

from tensorflow.keras.layers import Input, Flatten
from tensorflow.keras import Model
from tensorflow.keras.utils import get_file

from ...quantization_blocks import conv_block, dense_block

BASE_WEIGHT_PATH = 'http://data.brainchip.com/models/vgg/'

def vgg_cifar10(input_shape,
                classes=10,
                weights=None,
                weights_quantization=0,
                activ_quantization=0,
                input_weights_quantization=None):
    """Instantiates a vgg-like model for the "Cifar-10" example.
    This model is based on the vgg architecture, mainly with fewer layers.
    The weights and activations are quantized such that it can be converted into
    an Akida model.
    This architecture is inspired by vgg.

    Args:
        input_shape (tuple): input shape tuple of the model
        classes (int): number of classes to classify images into
        weights (str): one of `None` (random initialization), 'cifar10' for
            pretrained weights or the path to the weights file to be loaded.
        weights_quantization (int): sets all weights in the model to have
            a particular quantization bitwidth except for the weights in the
            first layer.

            * '0' implements floating point 32-bit weights
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.
        activ_quantization: sets all activations in the model to have a.
            particular activation quantization bitwidth.

            * '0' implements floating point 32-bit activations.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.
        input_weights_quantization: sets weight quantization in the first layer.
            Takes precedence over global weight_quantization variable.

            * 'None' implements the same bitwidth as the other weights.
            * '0' implements floating point 32-bit weights.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.

    Returns:
        tf.keras.model: a quantized Keras model for vgg/cifar10
    """
    # Overrides input weights quantization if None
    if input_weights_quantization is None:
        input_weights_quantization = weights_quantization

    # Check weights
    if not (weights in {None, 'cifar10'} or os.path.exists(weights)):
        raise ValueError('The `weights` argument should be either '
                         '`None` (random initialization) '
                         'or `cifar10` to load weights over http '
                         'or the path to the weights file to be loaded.')

    # Check if imagenet pretrained weights are compatible with given arguments
    if weights == 'cifar10':
        quant_params = (weights_quantization,
                        activ_quantization,
                        input_weights_quantization)
        if classes != 10:
            raise ValueError("If 'weights' is 'cifar10', classes should be 10")
        if quant_params != (2, 2, 2):
            raise ValueError("If 'weights' is 'cifar10', quantization parameters "
                             "(weights_quantization, activ_quantization, "
                             " input_weights_quantization) must be (2, 2, 2); "
                             f" got quantization parameters={quant_params}")
        if input_shape != (32,32,3):
            raise ValueError("If 'weights' is 'cifar10', input shape must be "
                             f" (32,32,3) ; got input_shape={input_shape}")

    img_input = Input(shape=input_shape)

    x = conv_block(img_input, filters=128, kernel_size=(3, 3), name='conv_0',
            padding='same',
            use_bias=False,
            weight_quantization=input_weights_quantization,
            activ_quantization=activ_quantization,
            pooling=None,
            add_batchnorm=True)

    x = conv_block(x, filters=128, kernel_size=(3, 3), name='conv_1',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            pooling='max',
            add_batchnorm=True)

    x = conv_block(x, filters=256, kernel_size=(3, 3), name='conv_2',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            pooling=None,
            add_batchnorm=True)

    x = conv_block(x, filters=256, kernel_size=(3, 3), name='conv_3',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            pooling='max',
            add_batchnorm=True)

    x = conv_block(x, filters=512, name='conv_4',
            kernel_size=(3, 3),
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            pooling=None,
            add_batchnorm=True)

    x = conv_block(x, filters=512, kernel_size=(3, 3), name='conv_5',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            pooling='max',
            add_batchnorm=True)

    x = Flatten()(x)

    x = dense_block(x, units=1024, name='dense_6',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = dense_block(x, units=1024, name='dense_7',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = dense_block(x, units=classes, name='dense_8',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=None,
            add_batchnorm=False)

    model = Model(img_input, x, name='vgg_cifar10')

    # Load weights
    if weights == 'cifar10':
        model_name = (f'vgg_cifar10_wq{weights_quantization}'
                      f'_aq{activ_quantization}.hdf5')
        weights_path = get_file(fname=model_name,
                                origin=BASE_WEIGHT_PATH + model_name,
                                cache_subdir='models')
        model.load_weights(weights_path)
    elif weights is not None:
        model.load_weights(weights)

    return model
