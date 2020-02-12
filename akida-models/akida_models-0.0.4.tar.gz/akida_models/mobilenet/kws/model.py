#!/usr/bin/env python
# ******************************************************************************
# Copyright 2019 Brainchip Holdings Ltd.
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

from tensorflow.keras import Model
from tensorflow.keras.layers import Input, Reshape, Activation
from tensorflow.keras.utils import get_file

from ...quantization_blocks import conv_block, separable_conv_block

BASE_WEIGHT_PATH = 'http://data.brainchip.com/models/mobilenet/'

def mobilenet_kws(input_shape,
                  classes=None,
                  include_top=True,
                  weights=None,
                  weights_quantization=0,
                  activ_quantization=0,
                  input_weights_quantization=None):
    """Instantiates a MobileNet-like model for the "Keyword Spotting" example.

    This model is based on the MobileNet architecture, mainly with fewer layers.
    The weights and activations are quantized such that it can be converted into
    an Akida model.

    This architecture is originated from https://arxiv.org/pdf/1711.07128.pdf
    and was created for the "Keyword Spotting" (KWS) or "Speech Commands"
    dataset.

    Args:
        input_shape (tuple): input shape tuple of the model
        classes (int): optional number of classes to classify words into, only
            be specified if `include_top` is True.
        include_top (bool): whether to include the fully-connected
            layer at the top of the model.
        weights (str): one of `None` (random initialization), 'kws' for
            pretrained weights or the path to the weights file to be loaded.
        weights_quantization (int): sets all weights in the model to have
            a particular quantization bitwidth except for the weights in the
            first layer.

            * '0' implements floating point 32-bit weights.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.
        activ_quantization: sets all activations in the model to have a
            particular activation quantization bitwidth.

            * '0' implements floating point 32-bit activations.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.
        input_weights_quantization: sets weight quantization in the first layer.
            Takes precedence over global weight_quantization variable.

            * 'None' implements the same bitwidth as the other weights.
            * '0' implements floating point 32-bit weights.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.

    Returns
        tf.keras.model: a quantized Keras model for MobileNet/KWS
    """
    # Overrides input weights quantization if None
    if input_weights_quantization is None:
        input_weights_quantization = weights_quantization

    # Check weights
    if not (weights in {None, 'kws'} or os.path.exists(weights)):
        raise ValueError('The `weights` argument should be either '
                         '`None` (random initialization) '
                         'or `kws` to load weights over http '
                         'or the path to the weights file to be loaded.')

    if include_top and not classes:
        raise ValueError("If 'include_top' is True, 'classes' must be set.")

    # Check if KWS pretrained weights are compatible with given arguments
    if weights == 'kws':
        if include_top and classes != 12:
            raise ValueError("If using 'weights' as 'kws' with 'include_top' as "
                             "true, classes should be 12")
        quant_params = (input_weights_quantization,
                        weights_quantization,
                        activ_quantization)
        if quant_params != (8, 4, 4):
            raise ValueError("If 'weights' is 'kws', quantization parameters "
                             "(input_weights_quantization, weights_quantization"
                             ", activ_quantization) must be (8,4,4)")
        if input_shape[-1] != 1:
            raise ValueError("If weights is 'kws', the input must have 1 "
                             f"channel; got input_shape={input_shape}")
        if tuple(input_shape) != (49, 10, 1):
            print("'input_shape' is different from (49, 10, 1). Weights for "
                  "input shape (49, 10, 1) will be loaded as default.")

    img_input = Input(shape=input_shape)

    x = conv_block(img_input, filters=32, kernel_size=(5,5),
            padding='same',
            strides=(2, 2),
            use_bias=False,
            name='conv_0',
            weight_quantization=input_weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters = 64,
            kernel_size=(3,3),
            padding='same',
            use_bias=False,
            name='separable_1',
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters = 64,
            kernel_size=(3,3),
            padding='same',
            use_bias=False,
            name='separable_2',
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters = 64,
            kernel_size=(3,3),
            padding='same',
            use_bias=False,
            name='separable_3',
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters = 64,
            kernel_size=(3,3),
            padding='same',
            use_bias=False,
            name='separable_4',
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters = 64,
            kernel_size=(3,3),
            padding='same',
            use_bias=False,
            name='separable_5',
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            pooling='global_avg',
            add_batchnorm=True)

    if include_top:
        shape = (1, 1, int(64))
        x = Reshape(shape, name='reshape_1')(x)

        x = separable_conv_block(x,
                filters = classes,
                kernel_size=(3,3),
                padding='same',
                use_bias=False,
                name='separable_6',
                weight_quantization=weights_quantization,
                activ_quantization=None)

        x = Activation('softmax', name='act_softmax')(x)
        x = Reshape((classes,), name='reshape_2')(x)

    model = Model(img_input, x, name='mobilenet_kws')

    # Load weights.
    if weights == 'kws':
        if include_top:
            model_name = (f'mobilenet_kws_wq{weights_quantization}'
                          f'_aq{activ_quantization}.hdf5')
        else:
            model_name = (f'mobilenet_kws_wq{weights_quantization}'
                          f'_aq{activ_quantization}_no_top.hdf5')
        weights_path = get_file(fname=model_name,
                                origin=BASE_WEIGHT_PATH + model_name,
                                cache_subdir='models')
        model.load_weights(weights_path)
    elif weights is not None:
        model.load_weights(weights)

    return model
