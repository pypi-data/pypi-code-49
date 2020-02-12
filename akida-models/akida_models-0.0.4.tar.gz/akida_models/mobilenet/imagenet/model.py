#!/usr/bin/env python

"""MobileNet v1 models for Keras and Akida
MobileNet is a general architecture and can be used for multiple use cases.
(general description from keras.applications still included immediately below).

AKIDA
This specific version includes parameter options to generate a mobilenet version
with
- overall architecture compatible with Akida (conv stride 2 replaced with max pool)
- options to binarize or ternarize both weights and activations
- options to customize (including remove) batch norm + activation layers
between the depthwise and pointwise components of the depthwise_conv_block
- different initialization options

General Mobilenet V1 Notes:
Depending on the use case, it can use different input layer size and
different width factors. This allows different width models to reduce
the number of multiply-adds and thereby
reduce inference cost on mobile devices.
MobileNets support any input size greater than 32 x 32, with larger image sizes
offering better performance.
The number of parameters and number of multiply-adds
can be modified by using the `alpha` parameter,
which increases/decreases the number of filters in each layer.
By altering the image size and `alpha` parameter,
all 16 models from the paper can be built, with ImageNet weights provided.
The paper demonstrates the performance of MobileNets using `alpha` values of
1.0 (also called 100 % MobileNet), 0.75, 0.5 and 0.25.
For each of these `alpha` values, weights for 4 different input image sizes
are provided (224, 192, 160, 128).
The following table describes the size and accuracy of the 100% MobileNet
on size 224 x 224:
----------------------------------------------------------------------------
Width Multiplier (alpha) | ImageNet Acc |  Multiply-Adds (M) |  Params (M)
----------------------------------------------------------------------------
|   1.0 MobileNet-224    |    70.6 %     |        529        |     4.2     |
|   0.75 MobileNet-224   |    68.4 %     |        325        |     2.6     |
|   0.50 MobileNet-224   |    63.7 %     |        149        |     1.3     |
|   0.25 MobileNet-224   |    50.6 %     |        41         |     0.5     |
----------------------------------------------------------------------------
The following table describes the performance of
the 100 % MobileNet on various input sizes:
------------------------------------------------------------------------
      Resolution      | ImageNet Acc | Multiply-Adds (M) | Params (M)
------------------------------------------------------------------------
|  1.0 MobileNet-224  |    70.6 %    |        529        |     4.2     |
|  1.0 MobileNet-192  |    69.1 %    |        529        |     4.2     |
|  1.0 MobileNet-160  |    67.2 %    |        529        |     4.2     |
|  1.0 MobileNet-128  |    64.4 %    |        529        |     4.2     |
------------------------------------------------------------------------
The weights for all 16 models are obtained and translated
from TensorFlow checkpoints found at
https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md
# Reference
- [MobileNets: Efficient Convolutional Neural Networks for
   Mobile Vision Applications](https://arxiv.org/pdf/1704.04861.pdf))
"""

import os
import warnings

# Tensorflow/Keras Imports
import tensorflow.keras.utils as keras_utils
from tensorflow.keras import Model
from tensorflow.keras.utils import get_file
from tensorflow.keras.layers import (Input, BatchNormalization, MaxPool2D,
                                     GlobalAvgPool2D, Reshape, Dropout,
                                     Activation)

# cnn2snn Imports
from cnn2snn import (WeightQuantizer, WeightFloat,
                     QuantizedConv2D, QuantizedSeparableConv2D)

# Local utils
from ...quantization_blocks import _add_activation_layer

BASE_WEIGHT_PATH = 'http://data.brainchip.com/models/mobilenet/'

def _obtain_input_shape(input_shape,
                        default_size,
                        min_size,
                        include_top):
    """Internal utility to compute/validate a model's input shape.

    Args:
        input_shape: either None (will return the default model input shape),
            or a user-provided shape to be validated.
        default_size: default input width/height for the model.
        min_size: minimum input width/height accepted by the model.
        include_top: whether the model is expected to
            be linked to a classifier via a Flatten layer.

    Returns:
        tuple of integers: input shape (may include None entries).

    Raises:
        ValueError: in case of invalid argument values.
    """
    if input_shape and len(input_shape) == 3:
        if input_shape[-1] not in {1, 3}:
            warnings.warn(
                'This model usually expects 1 or 3 input channels. '
                'However, it was passed an input_shape with ' +
                str(input_shape[-1]) + ' input channels.')
        default_shape = (default_size, default_size, input_shape[-1])
    else:
        default_shape = (default_size, default_size, 3)

    if input_shape:
        if input_shape is not None:
            if len(input_shape) != 3:
                raise ValueError(
                    '`input_shape` must be a tuple of three integers.')
            if ((input_shape[0] is not None and input_shape[0] < min_size) or
                (input_shape[1] is not None and input_shape[1] < min_size)):
                raise ValueError('Input size must be at least ' +
                                    str(min_size) + 'x' + str(min_size) +
                                    '; got `input_shape=' +
                                    str(input_shape) + '`')
    else:
        if include_top:
            input_shape = default_shape
        else:
            input_shape = (None, None, 3)
    if include_top:
        if None in input_shape:
            raise ValueError('If `include_top` is True, '
                             'you should specify a static `input_shape`. '
                             'Got `input_shape=' + str(input_shape) + '`')
    return input_shape


def _depthwise_block(inputs, filters,
                    name, add_maxpool,
                    weight_quantizer, activ_quantization):

    x = QuantizedSeparableConv2D(filters=filters, kernel_size=(3, 3),
                                 use_bias=False,
                                 padding='same', name=name,
                                 quantizer=weight_quantizer)(inputs)

    if add_maxpool:
        x = MaxPool2D(pool_size=(2, 2), padding='same', name=name+'_maxpool')(x)
    x = BatchNormalization(name=name+'_BN')(x)
    x = _add_activation_layer(x, activ_quantization, name+'_relu')

    return x

def _get_weight_quantizer(bitwidth):
    """Returns a weight quantizer according to the bitwidth.

    # Args
        bitwidth (int): The quantization bitwidth for weights. If
            'bitwidth' is zero, the weights are not quantized (float).

    # Returns
        WeightQuantizer: a weight quantizer object.
    """
    if bitwidth == 0:
        return WeightFloat()
    elif isinstance(bitwidth, int) and bitwidth > 0:
        return WeightQuantizer(threshold=1, bitwidth=bitwidth)
    else:
        raise ValueError("'bitwidth' argument must be a positive integer, "
                            "or zero for float weights.")

def mobilenet_imagenet(input_shape=None,
              alpha=1.0,
              dropout=1e-3,
              include_top=True,
              weights=None,
              pooling=None,
              classes=1000,
              weights_quantization=0,
              activ_quantization=0,
              input_weights_quantization=None):
    """Instantiates the MobileNet architecture.

    Args:
        input_shape (tuple): optional shape tuple.
        alpha (float): controls the width of the model.

            * If `alpha` < 1.0, proportionally decreases the number of filters
              in each layer.
            * If `alpha` > 1.0, proportionally increases the number of filters
              in each layer.
            * If `alpha` = 1, default number of filters from the paper are used
              at each layer.
        dropout (float): dropout rate
        include_top (bool): whether to include the fully-connected
            layer at the top of the model.
        weights (str): one of `None` (random initialization), 'imagenet' for
             pretrained weights or the path to the weights file to be loaded.
        pooling (str): Optional pooling mode for feature extraction
            when `include_top` is `False`.

            * `None` means that the output of the model will be the 4D tensor
              output of the last convolutional block.
            * `avg` means that global average pooling will be applied to the
              output of the last convolutional block, and thus the output of the
              model will be a 2D tensor.
        classes (int): optional number of classes to classify images
            into, only to be specified if `include_top` is True.
        weight_quantization (int): sets all weights in the model to have
            a particular quantization bitwidth except for the weights in the
            first layer.

            * '0' implements floating point 32-bit weights.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.
        activ_quantization: sets all activations in the model to have a
            particular activation quantization bitwidth.

            * '0' implements floating point 32-bit activations.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.
        input_weight_quantization: sets weight quantization in the first layer.
            Takes precedence over global weight_quantization variable.

            * '0' implements floating point 32-bit weights.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.

    Returns:
        A Keras model instance.

    Raises:
        ValueError: in case of invalid argument for `weights`,
            or invalid input shape.
    """
    # check if overrides have been provided and override
    if input_weights_quantization is None:
        input_weights_quantization = weights_quantization

    # Check weights
    if not (weights in {None, 'imagenet'} or os.path.exists(weights)):
        raise ValueError('The `weights` argument should be either '
                         '`None` (random initialization) '
                         'or `imagenet` to load weights over http '
                         'or the path to the weights file to be loaded.')

    # Check if imagenet pretrained weights are compatible with given arguments
    if weights == 'imagenet':
        quant_params = (weights_quantization,
                        activ_quantization,
                        input_weights_quantization)
        if classes != 1000:
            raise ValueError("If 'weights' is 'imagenet', classes should be 1000")
        if quant_params != (4, 4, 8) and quant_params != (0, 0, 0) :
            raise ValueError("If 'weights' is 'imagenet', quantization parameters "
                             "(weights_quantization, activ_quantization, "
                             " input_weights_quantization) must be (4, 4, 8) or"
                             " (0, 0, 0)")
        if input_shape[-1] !=  3:
            raise ValueError("If 'weights' is 'imagenet', channel number"
                             " must be 3")
        if input_shape[0] != 224 or input_shape[1] != 224:
            print("If 'weights' is 'imagenet', weights trained for input (224, 224) "
                  "will be used")


    # Determine proper input shape and default size.
    if input_shape is None:
        default_size = 224
    else:
        rows = input_shape[0]
        cols = input_shape[1]

        if rows == cols and rows in [128, 160, 192, 224]:
            default_size = rows
        else:
            default_size = 224

    input_shape = _obtain_input_shape(input_shape,
                                      default_size=default_size,
                                      min_size=32,
                                      include_top=include_top)

    rows = input_shape[0]
    cols = input_shape[1]

    img_input = Input(shape=input_shape)

    weight_quantizer = _get_weight_quantizer(weights_quantization)
    weight_quantizer_fl = _get_weight_quantizer(input_weights_quantization)

    x = QuantizedConv2D(filters=int(32*alpha), kernel_size=(3, 3),
                        use_bias=False, strides=(2, 2),
                        padding='same',
                        name='conv_0',
                        quantizer=weight_quantizer_fl)(img_input)
    x = BatchNormalization(name='conv_0_BN')(x)
    x = _add_activation_layer(x, activ_quantization, 'conv_0_relu')

    x = _depthwise_block(x, int(64*alpha), 'separable_1', False,
                         weight_quantizer, activ_quantization)

    x = _depthwise_block(x, int(128*alpha), 'separable_2', True,
                         weight_quantizer, activ_quantization)

    x = _depthwise_block(x, int(128*alpha), 'separable_3', False,
                         weight_quantizer, activ_quantization)

    x = _depthwise_block(x, int(256*alpha), 'separable_4', True,
                         weight_quantizer, activ_quantization)

    x = _depthwise_block(x, int(256*alpha), 'separable_5', False,
                         weight_quantizer, activ_quantization)

    x = _depthwise_block(x, int(512*alpha), 'separable_6', True,
                         weight_quantizer, activ_quantization)

    x = _depthwise_block(x, int(512*alpha), 'separable_7', False,
                         weight_quantizer, activ_quantization)

    x = _depthwise_block(x, int(512*alpha), 'separable_8', False,
                         weight_quantizer, activ_quantization)

    x = _depthwise_block(x, int(512*alpha), 'separable_9', False,
                         weight_quantizer, activ_quantization)

    x = _depthwise_block(x, int(512*alpha), 'separable_10', False,
                         weight_quantizer, activ_quantization)

    x = _depthwise_block(x, int(512*alpha), 'separable_11', False,
                         weight_quantizer, activ_quantization)

    x = _depthwise_block(x, int(1024*alpha), 'separable_12', True,
                         weight_quantizer, activ_quantization)

    # Last separable layer with global pooling
    x = QuantizedSeparableConv2D(filters=int(1024*alpha), kernel_size=(3, 3),
                                 use_bias=False, padding='same',
                                 name='separable_13',
                                 quantizer=weight_quantizer)(x)

    if include_top or pooling == 'avg':
        x = GlobalAvgPool2D(name='separable_13_global_avg')(x)
    x = BatchNormalization(name='separable_13_BN')(x)
    x = _add_activation_layer(x, activ_quantization, 'separable_13_relu')


    if include_top:
        shape = (1, 1, int(1024 * alpha))

        x = Reshape(shape, name='reshape_1')(x)
        x = Dropout(dropout, name='dropout')(x)

        x = QuantizedSeparableConv2D(filters=classes, kernel_size=(3, 3),
                                     use_bias=False, padding='same',
                                     name='separable_14',
                                     quantizer=weight_quantizer)(x)
        x = Activation('softmax', name='act_softmax')(x)
        x = Reshape((classes,), name='reshape_2')(x)

    # Create model.
    model = Model(img_input, x, name='mobilenet_%0.2f_%s' % (alpha, rows))
    # Load weights.
    if weights == 'imagenet':
        if  include_top:
            include_top_file_name=''
        else:
            include_top_file_name='_no_top'
        if input_weights_quantization == 0:
            model_name = (f'mobilenet_imagenet{include_top_file_name}.h5')
        else:
            model_name = (f'mobilenet_imagenet_wq{weights_quantization}'
                         f'_aq{activ_quantization}{include_top_file_name}.h5')
        weights_path = get_file(fname=model_name,
                                origin=BASE_WEIGHT_PATH + model_name,
                                cache_subdir='models')
        model.load_weights(weights_path)
    elif weights is not None:
        model.load_weights(weights)

    return model
