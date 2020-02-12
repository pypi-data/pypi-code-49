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

# Keras Imports
from tensorflow.keras.layers import BatchNormalization, ReLU
from tensorflow.keras.layers import MaxPool2D, AvgPool2D, GlobalAvgPool2D

# CNN2SNN Imports
import cnn2snn.quantization_ops as qops
from cnn2snn.quantization_layers import conv2d, separable_conv2d, dense
from cnn2snn.quantization_layers import activationDiscreteRelu


def _get_weight_quantizer(bitwidth):
    """Returns a weight quantizer according to the bitwidth.

    Args:
        bitwidth: (integer) The quantization bitwidth for weights. If
            'bitwidth' is zero, the weights are not quantized (float).

    Returns:
        a WeightQuantizer object.
    """
    if bitwidth == 0:
        return qops.WeightFloat()
    elif isinstance(bitwidth, int) and bitwidth > 0:
        if bitwidth <= 2:
            # For very low bitwidth, we must use a lower theshold otherwise we
            # set too many weights to zero
            return qops.WeightQuantizer(threshold=1, bitwidth=bitwidth)
        else:
            return qops.WeightQuantizer(threshold=3, bitwidth=bitwidth)
    else:
        raise ValueError("'bitwidth' argument must be a positive integer, "
                            "or zero for float weights.")


def _add_pooling_layer(x, pooling_type, pool_size, padding, layer_base_name):
    """Add a pooling layer in the graph.

    From an input tensor 'x', the function returns the output tensor after
    a pooling layer defined by 'pooling_type'.

    Args:
        x (tf.Tensor): the input tensor
        pooling_type (str): type of pooling among the following: 'max',
            'avg' or 'global_avg'.
        pool_size (int or tuple of 2 integers): factors by which to
            downscale (vertical, horizontal). (2, 2) will halve the input in
            both spatial dimension. If only one integer is specified, the same
            window length will be used for both dimensions.
        padding (str): one of "valid" or "same" (case-insensitive).
        layer_base_name (str): base name for the pooling layer.

    Returns:
        tf.Tensor: an output tensor after pooling
    """
    if pooling_type == 'max':
        return MaxPool2D(pool_size=pool_size, padding=padding,
                        name=layer_base_name + '_maxpool')(x)
    elif pooling_type == 'avg':
        return AvgPool2D(pool_size=pool_size, padding=padding,
                        name=layer_base_name + '_avgpool')(x)
    elif pooling_type == 'global_avg':
        return GlobalAvgPool2D(name=layer_base_name + '_global_avg')(x)
    else:
        raise ValueError("'pooling_type' argument must be max', "
                            "'avg' or 'global_avg'.")


def _add_activation_layer(x, bitwidth, layer_name):
    """Add an activation layer in the graph.

    From an input tensor 'x', the function returns the output tensor after
    an activation layer defined by 'bitwidth'.

    Args:
        x (tf.Tensor): the input tensor
        bitwidth (int): the quantization bitwidth for the ReLU6
            activation. If 'bitwidth' is zero, the activations are not
            quantized (float ReLU6).
        layer_name (str): This name will be used as the name of the added
            activation layer.

    Returns:
        tf.Tensor: an output tensor after activation.
    """
    if bitwidth == 0:
        return ReLU(6., name=layer_name)(x)
    elif isinstance(bitwidth, int) and bitwidth > 0:
        return activationDiscreteRelu(bitwidth=bitwidth, name=layer_name)(x)
    else:
        raise ValueError("'bitwidth' argument must be a positive integer, "
                            "or zero for float activation.")


def conv_block(inputs, filters,
                kernel_size,
                weight_quantization=0,
                activ_quantization=0,
                pooling=None,
                pool_size=(2, 2),
                add_batchnorm=False,
                **kwargs):
    """Adds a quantized convolutional layer with optional layers in the
    following order: max pooling, batch normalization, quantized activation.

    Args:
        inputs (tf.Tensor): input tensor of shape `(rows, cols, channels)`
        filters (int): the dimensionality of the output space
            (i.e. the number of output filters in the convolution).
        kernel_size (int or tuple of 2 integers): specifying the
            height and width of the 2D convolution kernel.
            Can be a single integer to specify the same value for
            all spatial dimensions.
        weight_quantization (int): quantization bitwidth for weights
            (usually 2, 4 or 8). For float weights (no quantization), set the
            value to zero.
        activ_quantization (int) quantization bitwidth for activation
            (usually 1, 2 or 4). For a float activation (ReLU 6), set the
            value to zero. For no activation, set it to None.
        pooling (str): add a pooling layer of type 'pooling' among the
            values 'max', 'avg', 'global_max' or 'global_avg', with pooling
            size set to pool_size. If 'None', no pooling will be added.
        pool_size (int or tuple of 2 integers): factors by which to
            downscale (vertical, horizontal). (2, 2) will halve the input in
            both spatial dimension. If only one integer is specified, the same
            window length will be used for both dimensions.
        add_batchnorm (bool): add a tf.keras.BatchNormalization layer
        **kwargs: arguments passed to the tf.keras.Conv2D layer, such as
            strides, padding, use_bias, weight_regularizer, etc.

    Returns:
        tf.Tensor: output tensor of conv2D block.
    """
    if 'activation' in kwargs.keys() and kwargs['activation']:
        raise ValueError("Keyword argument 'activation' in conv_block must be None.")
    if 'strides' in kwargs.keys():
        if kwargs['strides'] != 1 and kwargs['strides'] != (1,1):
            print("WARNING: Keyword argument 'strides' is not supported in "
                            "conv_block except for the first layer.")
    if 'dilation_rate' in kwargs.keys():
        if kwargs['dilation_rate'] != 1 and kwargs['dilation_rate'] != (1,1):
            raise ValueError("Keyword argument 'dilation_rate' is not "
                            "supported in conv_block.")

    weight_quantizer = _get_weight_quantizer(weight_quantization)
    conv_layer = conv2d(filters, kernel_size, modifier=weight_quantizer, **kwargs)

    x = inputs
    x = conv_layer(x)

    if pooling:
        x = _add_pooling_layer(x, pooling, pool_size,
                                conv_layer.padding, conv_layer.name)

    if add_batchnorm:
        x = BatchNormalization(name=conv_layer.name + '_BN')(x)

    if activ_quantization is not None:
        x = _add_activation_layer(x, activ_quantization, conv_layer.name + '_relu')

    return x


def separable_conv_block(inputs, filters, kernel_size,
                         weight_quantization=0,
                         activ_quantization=0,
                         pooling=None,
                         pool_size=(2, 2),
                         add_batchnorm=False,
                         **kwargs):
    """Adds a quantized separable convolutional layer with optional layers in
    the following order: global average pooling, max pooling, batch
    normalization, quantized activation.

    Args:
        inputs (tf.Tensor): input tensor of shape `(height, width, channels)`
        filters (int): the dimensionality of the output space
            (i.e. the number of output filters in the pointwise convolution).
        kernel_size (int or tuple of 2 integers): specifying the
            height and width of the 2D convolution window. Can be a single
            integer to specify the same value for all spatial dimensions.
        weight_quantization (int): quantization bitwidth for weights
            (usually 2, 4 or 8). For float weights (no quantization), set the
            value to zero.
        activ_quantization (int): quantization bitwidth for activation
            (usually 1, 2 or 4). For a float activation (ReLU 6), set the
            value to zero. For no activation, set it to None.
        pooling (str): add a pooling layer of type 'pooling' among the
            values 'max', 'avg', 'global_max' or 'global_avg', with pooling
            size set to pool_size. If 'None', no pooling will be added.
        pool_size (int or tuple of 2 integers): factors by which to
            downscale (vertical, horizontal). (2, 2) will halve the input in
            both spatial dimension. If only one integer is specified, the same
            window length will be used for both dimensions.
        add_batchnorm (bool): add a tf.keras.BatchNormalization layer
        **kwargs: arguments passed to the tf.keras.SeparableConv2D layer,
            such as strides, padding, use_bias, etc.

    Returns:
        tf.Tensor: output tensor of separable conv block.
    """
    if 'activation' in kwargs.keys() and kwargs['activation']:
        raise ValueError("Keyword argument 'activation' in separable_conv_block"
                         " must be None.")
    if 'strides' in kwargs.keys():
        if kwargs['strides'] != 1 and kwargs['strides'] != (1, 1):
            raise ValueError("Keyword argument 'strides' is not supported in "
                             "separable_conv_block.")
    if 'dilation_rate' in kwargs.keys():
        if kwargs['dilation_rate'] != 1 and kwargs['dilation_rate'] != (1, 1):
            raise ValueError("Keyword argument 'dilation_rate' is not "
                             "supported in separable_conv_block.")
    if 'depth_multiplier' in kwargs.keys():
        if kwargs['depth_multiplier'] != 1:
            raise ValueError("Keyword argument 'depth_multiplier' is not "
                             "supported in separable_conv_block.")

    weight_quantizer = _get_weight_quantizer(weight_quantization)
    separable_layer = separable_conv2d(filters, kernel_size,
                                       modifier=weight_quantizer, **kwargs)

    x = inputs
    x = separable_layer(x)

    if pooling:
        x = _add_pooling_layer(x, pooling, pool_size,
                               separable_layer.padding, separable_layer.name)

    if add_batchnorm:
        x = BatchNormalization(name=separable_layer.name + '_BN')(x)

    if activ_quantization is not None:
        x = _add_activation_layer(x, activ_quantization,
                                  separable_layer.name + '_relu')

    return x


def dense_block(inputs, units,
                weight_quantization=0,
                activ_quantization=0,
                add_batchnorm=False,
                **kwargs):
    """Adds a quantized dense layer with optional layers in the following
    order: batch normalization, quantized activation.

    Args:
        inputs (tf.Tensor): Input tensor of shape `(rows, cols, channels)`
        units (int): dimensionality of the output space
        weight_quantization (int): quantization bitwidth for weights
            (usually 2, 4 or 8). For float weights (no quantization), set the
            value to zero.
        activ_quantization (int): quantization bitwidth for activation
            (usually 1, 2 or 4). For a float activation (ReLU 6), set the
            value to zero. For no activation, set it to None.
        add_batchnorm (bool): add a tf.keras.BatchNormalization layer
        **kwargs: arguments passed to the tf.keras.Dense layer, such as
            use_bias, kernel_initializer, weight_regularizer, etc.

    Returns:
        tf.Tensor: output tensor of the dense block.
    """
    if 'activation' in kwargs.keys() and kwargs['activation']:
        raise ValueError("Keyword argument 'activation' in separable_conv_block"
                            " must be None.")

    weight_quantizer = _get_weight_quantizer(weight_quantization)
    dense_layer = dense(units, modifier=weight_quantizer, **kwargs)

    x = inputs
    x = dense_layer(x)

    if add_batchnorm:
        x = BatchNormalization(name=dense_layer.name + '_BN')(x)

    if activ_quantization is not None:
        x = _add_activation_layer(x, activ_quantization,
                                    dense_layer.name + '_relu')

    return x
