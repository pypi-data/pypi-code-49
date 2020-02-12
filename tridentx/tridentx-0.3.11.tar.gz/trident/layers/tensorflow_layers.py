from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import math
import collections
import itertools
import tensorflow as tf
import tensorflow.keras.backend as K
from tensorflow.python.keras.engine.base_layer import Layer
from tensorflow_core.python.keras.utils import conv_utils
from tensorflow.python.framework import tensor_shape
from tensorflow.python.keras.engine.input_spec import InputSpec
from tensorflow.python.ops import nn_ops
from tensorflow.python.client import device_lib
from .tensorflow_activations import get_activation
from itertools import repeat
import inspect


from ..backend.common import *
from ..backend.tensorflow_backend import *

_tf_data_format= 'channels_last'

__all__ = ['InputLayer','Dense', 'Flatten', 'Concatenate','Concate','Add','Subtract', 'Conv1d', 'Conv2d', 'Conv3d',  'TransConv2d', 'TransConv3d','Reshape','Dropout','Lambda','SoftMax','Noise']


_session = get_session()

_device='CPU'
for device in device_lib.list_local_devices():
      if tf.DeviceSpec.from_string(device.name).device_type == 'GPU':
          _device='GPU'
          break

_epsilon = _session.epsilon


def _ntuple(n):
    def parse(x):
        if isinstance(x, collections.Iterable):
            return x
        return tuple(repeat(x, n))

    return parse


_single = _ntuple(1)
_pair = _ntuple(2)
_triple = _ntuple(3)
_quadruple = _ntuple(4)

def get_layer_repr(layer):
    # We treat the extra repr like the sub-module, one item per line
    extra_lines = []
    if hasattr( layer, 'extra_repr' ) and callable( layer.extra_repr ):
        extra_repr = layer.extra_repr()
        # empty string will be split into list ['']
        if extra_repr:
            extra_lines = extra_repr.split('\n')
    child_lines = []
    if isinstance(layer,(tf.keras.Model,tf.keras.Sequential)) and layer.layers is not None:
        for module in layer.layers:
            mod_str = repr(module)
            mod_str = addindent(mod_str, 2)
            child_lines.append('(' + module.name + '): ' + mod_str)
    lines = extra_lines + child_lines

    main_str = layer.__class__.__name__ + '('
    if lines:
        # simple one-liner info, which most builtin Modules will use
        if len(extra_lines) == 1 and not child_lines:
            main_str += extra_lines[0]
        else:
            main_str += '\n  ' + '\n  '.join(lines) + '\n'

    main_str += ')'
    return main_str

class InputLayer(tf.keras.layers.InputLayer):
    def __init__(self, input_shape: (list, tuple,int) = None,batch_size=None,name='',**kwargs):
        if isinstance(input_shape, int):
            input_shape = (input_shape),
        elif isinstance(input_shape, list):
            input_shape = tuple(input_shape)
        super(InputLayer, self).__init__(input_shape=input_shape, batch_size=batch_size,  name=name, **kwargs)

    def __repr__(self):
        return get_layer_repr(self)
    def extra_repr(self):
        s = 'input_shape={input_shape},batch_size= {batch_size},name={name}'
        return s.format(**self.__dict__)


class Dense(tf.keras.layers.Dense):
    def __init__(self, output_filters, use_bias=True, activation=None,input_shape=None,name='', **kwargs ):
        super(Dense, self).__init__(units=output_filters,use_bias=use_bias,activation=get_activation(activation),name=name,**kwargs)
        inp_shape = kwargs.get('input_shape')
        if inp_shape is not None:
            self.input_spec = inp_shape

    def __repr__(self):
        return get_layer_repr(self)

    def extra_repr(self):
        s = 'output_shape={units}, use_bias={use_bias},'+'activation={0}'.format(None if self.activation is None else self.activation.__name__)
        return s.format(**self.__dict__)


class Flatten(tf.keras.layers.Flatten):
    def __init__(self ,name=''):
        super(Flatten, self).__init__(name=name)
    def __repr__(self):
        return get_layer_repr(self)
    def extra_repr(self):
        return ''



class Concate(tf.keras.layers.Concatenate):
    def __init__(self, axis=-1,name='' ):
        super(Concate, self).__init__(axis=axis,name=name)
    def __repr__(self):
        return get_layer_repr(self)
    def extra_repr(self):
        return ''

Concatenate=Concate


class Add(tf.keras.layers.Add):
    def __init__(self,name='' ):
        super(Add, self).__init__(name=name)
    def __repr__(self):
        return get_layer_repr(self)
    def extra_repr(self):
        return ''


class Subtract(tf.keras.layers.Subtract):
    def __init__(self ,name=''):
        super(Subtract, self).__init__(name=name)
    def __repr__(self):
        return get_layer_repr(self)
    def extra_repr(self):
        return ''



class SoftMax(tf.keras.layers.Softmax):
    def __init__(self ,axis=-1,name='', **kwargs):
        super(SoftMax, self).__init__(axis=-1,name=name, **kwargs)
    def __repr__(self):
        return get_layer_repr(self)
    def extra_repe(self):
        return 'axis={0}'.format(self.axis)


#
# class Conv(Layer):
#   """Abstract N-D convolution layer (private, used as implementation base).
#
#   This layer creates a convolution kernel that is convolved
#   (actually cross-correlated) with the layer input to produce a tensor of
#   outputs. If `use_bias` is True (and a `bias_initializer` is provided),
#   a bias vector is created and added to the outputs. Finally, if
#   `activation` is not `None`, it is applied to the outputs as well.
#
#   Arguments:
#     rank: An integer, the rank of the convolution, e.g. "2" for 2D convolution.
#     filters: Integer, the dimensionality of the output space (i.e. the number
#       of filters in the convolution).
#     kernel_size: An integer or tuple/list of n integers, specifying the
#       length of the convolution window.
#     strides: An integer or tuple/list of n integers,
#       specifying the stride length of the convolution.
#       Specifying any stride value != 1 is incompatible with specifying
#       any `dilation_rate` value != 1.
#     padding: One of `"valid"`,  `"same"`, or `"causal"` (case-insensitive).
#     data_format: A string, one of `channels_last` (default) or `channels_first`.
#       The ordering of the dimensions in the inputs.
#       `channels_last` corresponds to inputs with shape
#       `(batch, ..., channels)` while `channels_first` corresponds to
#       inputs with shape `(batch, channels, ...)`.
#     dilation_rate: An integer or tuple/list of n integers, specifying
#       the dilation rate to use for dilated convolution.
#       Currently, specifying any `dilation_rate` value != 1 is
#       incompatible with specifying any `strides` value != 1.
#     activation: Activation function. Set it to None to maintain a
#       linear activation.
#     use_bias: Boolean, whether the layer uses a bias.
#     kernel_initializer: An initializer for the convolution kernel.
#     bias_initializer: An initializer for the bias vector. If None, the default
#       initializer will be used.
#     kernel_regularizer: Optional regularizer for the convolution kernel.
#     bias_regularizer: Optional regularizer for the bias vector.
#     activity_regularizer: Optional regularizer function for the output.
#     kernel_constraint: Optional projection function to be applied to the
#         kernel after being updated by an `Optimizer` (e.g. used to implement
#         norm constraints or value constraints for layer weights). The function
#         must take as input the unprojected variable and must return the
#         projected variable (which must have the same shape). Constraints are
#         not safe to use when doing asynchronous distributed training.
#     bias_constraint: Optional projection function to be applied to the
#         bias after being updated by an `Optimizer`.
#     trainable: Boolean, if `True` the weights of this layer will be marked as
#       trainable (and listed in `layer.trainable_weights`).
#     name: A string, the name of the layer.
#   """
#
#   def __init__(self, rank,kernel_size, num_filters, strides, auto_pad,padding_mode, activation,use_bias, dilation, groups, transposed,name,filter_rate, trainable,**kwargs):
#     super(Conv, self).__init__(
#         trainable=trainable,
#         name=name,
#         **kwargs)
#     self.rank = rank
#     self.num_filters = num_filters
#     self.kernel_size = kernel_size
#     self.strides = strides
#     self.padding = conv_utils.normalize_padding(padding)
#     if (self.padding == 'causal' and not isinstance(self,  (Conv1D, SeparableConv1D))):
#       raise ValueError('Causal padding is only supported for `Conv1D`'
#                        'and ``SeparableConv1D`.')
#     self.data_format = 'channel_last'
#     self.dilation_rate =dilation
#     self.activation = get_activation(activation)
#     self.use_bias = use_bias
#     self.groups=groups
#     self.filter_rate=filter_rate
#     self.input_spec = InputSpec(ndim=self.rank + 2)
#
#   def build(self, input_shape):
#     input_shape = tensor_shape.TensorShape(input_shape)
#     input_filter = self._get_input_channel(input_shape)
#     if self.num_filters is None and self.filter_rate is not None:
#         self.num_filters=input_filter*self.filter_rate
#     kernel_shape = self.kernel_size + (input_filter, self.num_filters)
#
#     self.kernel = self.add_weight(
#         name='kernel',
#         shape=kernel_shape,
#         initializer=self.kernel_initializer,
#         regularizer=self.kernel_regularizer,
#         constraint=self.kernel_constraint,
#         trainable=True,
#         dtype=self.dtype)
#     if self.use_bias:
#       self.bias = self.add_weight(
#           name='bias',
#           shape=(self.num_filters,),
#           initializer=self.bias_initializer,
#           regularizer=self.bias_regularizer,
#           constraint=self.bias_constraint,
#           trainable=True,
#           dtype=self.dtype)
#     else:
#       self.bias = None
#     channel_axis = self._get_channel_axis()
#     self.input_spec = InputSpec(ndim=self.rank + 2,
#                                 axes={channel_axis: input_filter})
#
#     self._build_conv_op_input_shape = input_shape
#     self._build_input_channel = input_filter
#     self._padding_op = self._get_padding_op()
#     self._conv_op_data_format = conv_utils.convert_data_format(
#         self.data_format, self.rank + 2)
#     self._convolution_op = nn_ops.Convolution(
#         input_shape,
#         filter_shape=self.kernel.shape,
#         dilation_rate=self.dilation_rate,
#         strides=self.strides,
#         padding=self._padding_op,
#         data_format=self._conv_op_data_format)
#     self.built = True
#
#   def call(self, inputs):
#     # Check if the input_shape in call() is different from that in build().
#     # If they are different, recreate the _convolution_op to avoid the stateful
#     # behavior.
#     call_input_shape = inputs.get_shape()
#     recreate_conv_op = (
#         call_input_shape[1:] != self._build_conv_op_input_shape[1:])
#
#     if recreate_conv_op:
#       self._convolution_op = nn_ops.Convolution(
#           call_input_shape,
#           filter_shape=self.kernel.shape,
#           dilation_rate=self.dilation_rate,
#           strides=self.strides,
#           padding=self._padding_op,
#           data_format=self._conv_op_data_format)
#
#     # Apply causal padding to inputs for Conv1D.
#     if self.padding == 'causal' and self.__class__.__name__ == 'Conv1D':
#       inputs = array_ops.pad(inputs, self._compute_causal_padding())
#
#     outputs = self._convolution_op(inputs, self.kernel)
#
#     if self.use_bias:
#         outputs = nn.bias_add(outputs, self.bias, data_format='NHWC')
#
#     if self.activation is not None:
#       return self.activation(outputs)
#     return outputs
#
#   def compute_output_shape(self, input_shape):
#     input_shape = tensor_shape.TensorShape(input_shape).as_list()
#     if self.data_format == 'channels_last':
#       space = input_shape[1:-1]
#       new_space = []
#       for i in range(len(space)):
#         new_dim = conv_utils.conv_output_length(
#             space[i],
#             self.kernel_size[i],
#             padding=self.padding,
#             stride=self.strides[i],
#             dilation=self.dilation_rate[i])
#         new_space.append(new_dim)
#       return tensor_shape.TensorShape([input_shape[0]] + new_space +
#                                       [self.filters])
#     else:
#       space = input_shape[2:]
#       new_space = []
#       for i in range(len(space)):
#         new_dim = conv_utils.conv_output_length(
#             space[i],
#             self.kernel_size[i],
#             padding=self.padding,
#             stride=self.strides[i],
#             dilation=self.dilation_rate[i])
#         new_space.append(new_dim)
#       return tensor_shape.TensorShape([input_shape[0], self.filters] +
#                                       new_space)
#
#   def get_config(self):
#     config = {
#         'filters': self.filters,
#         'kernel_size': self.kernel_size,
#         'strides': self.strides,
#         'padding': self.padding,
#         'data_format': self.data_format,
#         'dilation_rate': self.dilation_rate,
#         'activation': activations.serialize(self.activation),
#         'use_bias': self.use_bias,
#         'kernel_initializer': initializers.serialize(self.kernel_initializer),
#         'bias_initializer': initializers.serialize(self.bias_initializer),
#         'kernel_regularizer': regularizers.serialize(self.kernel_regularizer),
#         'bias_regularizer': regularizers.serialize(self.bias_regularizer),
#         'activity_regularizer':
#             regularizers.serialize(self.activity_regularizer),
#         'kernel_constraint': constraints.serialize(self.kernel_constraint),
#         'bias_constraint': constraints.serialize(self.bias_constraint)
#     }
#     base_config = super(Conv, self).get_config()
#     return dict(list(base_config.items()) + list(config.items()))
#
#   def _compute_causal_padding(self):
#     """Calculates padding for 'causal' option for 1-d conv layers."""
#     left_pad = self.dilation_rate[0] * (self.kernel_size[0] - 1)
#     if self.data_format == 'channels_last':
#       causal_padding = [[0, 0], [left_pad, 0], [0, 0]]
#     else:
#       causal_padding = [[0, 0], [0, 0], [left_pad, 0]]
#     return causal_padding
#
#   def _get_channel_axis(self):
#     if self.data_format == 'channels_first':
#       return 1
#     else:
#       return -1
#
#   def _get_input_channel(self, input_shape):
#     channel_axis = self._get_channel_axis()
#     if input_shape.dims[channel_axis].value is None:
#       raise ValueError('The channel dimension of the inputs '
#                        'should be defined. Found `None`.')
#     return int(input_shape[channel_axis])
#
#   def _get_padding_op(self):
#     if self.padding == 'causal':
#       op_padding = 'valid'
#     else:
#       op_padding = self.padding
#     if not isinstance(op_padding, (list, tuple)):
#       op_padding = op_padding.upper()
#     return op_padding

class Conv1d(tf.keras.layers.Conv1D):
    def __init__(self, kernel_size, num_filters, strides, input_shape=None ,auto_pad=True,padding_mode=PaddingMode.replicate, activation=None, use_bias=False, dilation=1,
                 groups=1, name='', filter_rate=None,**kwargs):
        kernel_size = _single(kernel_size)
        strides = _single(strides)
        dilation = _single(dilation)
        activation = get_activation(activation)
        if num_filters is None and filter_rate is not None:
            num_filters=filter_rate
        super(Conv1d, self).__init__(self,filters=num_filters, kernel_size=kernel_size, strides=strides,
                                     padding='same'if auto_pad else 'valid', dilation_rate=dilation, activation=activation, use_bias=use_bias,data_format='channels_last',name=name,**kwargs)
        self.groups=groups
        inp_shape = kwargs.get('input_shape')
        if inp_shape is not None:
            self.input_spec = inp_shape
    @property
    def num_filters(self):
        return super().filters

    @num_filters.setter
    def num_filters(self,value):
        self.filters=_single(value)

    @property
    def auto_pad(self):
        return super().padding=='same'

    @auto_pad.setter
    def auto_pad(self, value):
        self.padding ='same'if value else 'valid'

    @property
    def dilation(self):
        return super().dilation_rate

    @dilation.setter
    def dilation(self, value):
        self.dilation_rate =_single(value)


    def __repr__(self):
        return get_layer_repr(self)


    def extra_repr(self):
        s = 'kernel_size={kernel_size}, num_filters={num_filters},strides={strides}'
        if 'activation' in self.__dict__ and self.__dict__['activation'] is not None:
            if inspect.isfunction(self.__dict__['activation']):
                s += ', activation={0}'.format(self.__dict__['activation'].__name__)
            elif isinstance(self.__dict__['activation'], tf.keras.layers.Layer):
                s += ', activation={0}'.format(self.__dict__['activation']).__repr__()
        s += ',auto_pad={0}'.format(self.padding == 'same') + ',use_bias={use_bias} ,dilation={dilation_rate}'
        if self.groups != 1:
            s += ', groups={groups}'

        #     if self.bias is None:
        #         s += ', use_bias=False'
        return s.format(**self.__dict__)




class Conv2d(tf.keras.layers.Conv2D):
    def __init__(self, kernel_size, num_filters, strides, input_shape=None, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, name='',filter_rate=None,**kwargs):
        kernel_size = _pair(kernel_size)
        strides = _pair(strides)
        dilation = _pair(dilation)
        activation = get_activation(activation)
        super(Conv2d, self).__init__(filters=num_filters, kernel_size=kernel_size, strides=strides,  padding='same'if auto_pad else 'valid', dilation_rate=dilation, activation=activation, use_bias=use_bias,data_format='channels_last',name=name,**kwargs)
        self.groups=groups
        inp_shape=kwargs.get('input_shape')
        if inp_shape is not None:
            self.input_spec=inp_shape
    @property
    def num_filters(self):
        return super().filters

    @num_filters.setter
    def num_filters(self,value):
        self.filters=_pair(value)

    @property
    def auto_pad(self):
        return super().padding=='same'

    @auto_pad.setter
    def auto_pad(self, value):
        self.padding ='same'if value else 'valid'

    @property
    def dilation(self):
        return super().dilation_rate

    @dilation.setter
    def dilation(self, value):
        self.dilation_rate =_pair(value)
    def __repr__(self):
        return get_layer_repr(self)


    def extra_repr(self):
        s = 'kernel_size={kernel_size}, {filters},strides={strides}'
        if 'activation' in self.__dict__ and self.__dict__['activation'] is not None:
            if inspect.isfunction(self.__dict__['activation']):
                s += ', activation={0}'.format(self.__dict__['activation'].__name__)
            elif isinstance(self.__dict__['activation'], tf.keras.layers.Layer):
                s += ', activation={0}'.format(self.__dict__['activation']).__repr__()
        s += ',auto_pad={0}'.format(self.padding == 'same') + ',use_bias={use_bias} ,dilation={dilation_rate}'
        if self.groups != 1:
            s += ', groups={groups}'

        #     if self.bias is None:
        #         s += ', use_bias=False'
        return s.format(**self.__dict__)




class Conv3d(tf.keras.layers.Conv3D):
    def __init__(self, kernel_size, num_filters, strides, input_shape=None, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, name='',filter_rate=None,**kwargs):
        kernel_size = _triple(kernel_size)
        strides = _triple(strides)
        dilation = _triple(dilation)
        activation = get_activation(activation)
        super(Conv3d, self).__init__(filters=num_filters, kernel_size=kernel_size, strides=strides,
                                     padding='same' if auto_pad else 'valid', dilation_rate=dilation,
                                     activation=activation, use_bias=use_bias, data_format='channels_last',name=name, **kwargs)
        self.groups=groups

        inp_shape = kwargs.get('input_shape')
        if inp_shape is not None:
            self.input_spec = inp_shape
    @property
    def num_filters(self):
        return super().filters

    @num_filters.setter
    def num_filters(self, value):
        self.filters = _triple(value)

    @property
    def auto_pad(self):
        return super().padding == 'same'

    @auto_pad.setter
    def auto_pad(self, value):
        self.padding = 'same' if value else 'valid'

    @property
    def dilation(self):
        return super().dilation_rate

    @dilation.setter
    def dilation(self, value):
        self.dilation_rate = _triple(value)

    def __repr__(self):
        return get_layer_repr(self)
    def extra_repr(self):
        s = 'kernel_size={kernel_size}, {filters},strides={strides}'
        if 'activation' in self.__dict__ and self.__dict__['activation'] is not None:
            if inspect.isfunction(self.__dict__['activation']):
                s += ', activation={0}'.format(self.__dict__['activation'].__name__)
            elif isinstance(self.__dict__['activation'], tf.keras.layers.Layer):
                s += ', activation={0}'.format(self.__dict__['activation']).__repr__()
        s += ',auto_pad={0}'.format(self.padding == 'same') + ',use_bias={use_bias} ,dilation={dilation_rate}'
        if self.groups != 1:
            s += ', groups={groups}'

        #     if self.bias is None:
        #         s += ', use_bias=False'
        return s.format(**self.__dict__)




class TransConv2d(tf.keras.layers.Conv2DTranspose):
    def __init__(self, kernel_size, num_filters, strides, input_shape=None, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, name='',filter_rate=None,**kwargs):
        kernel_size = _pair(kernel_size)
        strides = _pair(strides)
        dilation = _pair(dilation)
        activation = get_activation(activation)
        super(TransConv2d, self).__init__( filters=num_filters, kernel_size=kernel_size, strides=strides,
                                     padding='same' if auto_pad else 'valid', dilation_rate=dilation,
                                     activation=activation, use_bias=use_bias,data_format='channels_last',name=name, **kwargs)
        self.groups = groups
        inp_shape = kwargs.get('input_shape')
        if inp_shape is not None:
            self.input_spec = inp_shape
        @property
        def num_filters(self):
            return super().filters

        @num_filters.setter
        def num_filters(self, value):
            self.filters = _pair(value)

        @property
        def auto_pad(self):
            return super().padding == 'same'

        @auto_pad.setter
        def auto_pad(self, value):
            self.padding = 'same' if value else 'valid'

        @property
        def dilation(self):
            return super().dilation_rate

        @dilation.setter
        def dilation(self, value):
            self.dilation_rate = _pair(value)
    def __repr__(self):
        return get_layer_repr(self)

    def extra_repr(self):
        s = 'kernel_size={kernel_size}, {filters},strides={strides}'
        if 'activation' in self.__dict__ and self.__dict__['activation'] is not None:
            if inspect.isfunction(self.__dict__['activation']):
                s += ', activation={0}'.format(self.__dict__['activation'].__name__)
            elif isinstance(self.__dict__['activation'], tf.keras.layers.Layer):
                s += ', activation={0}'.format(self.__dict__['activation']).__repr__()
        s += ',auto_pad={0}'.format(self.padding == 'same') + ',use_bias={use_bias} ,dilation={dilation_rate}'
        if self.groups != 1:
            s += ', groups={groups}'

        #     if self.bias is None:
        #         s += ', use_bias=False'
        return s.format(**self.__dict__)



class TransConv3d(tf.keras.layers.Conv3DTranspose):
    def __init__(self, kernel_size, num_filters, strides, input_shape=None, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, name='', filter_rate=None,**kwargs):
        kernel_size = _triple(kernel_size)
        strides = _triple(strides)
        dilation = _triple(dilation)
        activation = get_activation(activation)
        super(TransConv3d, self).__init__( filters=num_filters, kernel_size=kernel_size, strides=strides,input_shape=input_shape,
                                     padding='same' if auto_pad else 'valid', dilation_rate=dilation,
                                     activation=activation, use_bias=use_bias,data_format='channels_last',name=name, **kwargs)
        self.groups = groups

        @property
        def num_filters(self):
            return super().filters

        @num_filters.setter
        def num_filters(self, value):
            self.filters = _triple(value)

        @property
        def auto_pad(self):
            return super().padding == 'same'

        @auto_pad.setter
        def auto_pad(self, value):
            self.padding = 'same' if value else 'valid'

        @property
        def dilation(self):
            return super().dilation_rate

        @dilation.setter
        def dilation(self, value):
            self.dilation_rate = _triple(value)
    def __repr__(self):
        return get_layer_repr(self)

    def extra_repr(self):
        s = 'kernel_size={kernel_size}, {filters},strides={strides}'
        if 'activation' in self.__dict__ and self.__dict__['activation'] is not None:
            if inspect.isfunction(self.__dict__['activation']):
                s += ', activation={0}'.format(self.__dict__['activation'].__name__)
            elif isinstance(self.__dict__['activation'], tf.keras.layers.Layer):
                s += ', activation={0}'.format(self.__dict__['activation']).__repr__()
        s += ',auto_pad={0}'.format(self.padding == 'same') + ',use_bias={use_bias} ,dilation={dilation_rate}'
        if self.groups != 1:
            s += ', groups={groups}'

        #     if self.bias is None:
        #         s += ', use_bias=False'
        return s.format(**self.__dict__)




class Lambda(tf.keras.layers.Lambda):
    """
    Applies a lambda function on forward()
    Args:
        lamb (fn): the lambda function
    """

    def __init__(self, function,name=''):
        super(Lambda, self).__init__(function=function, output_shape=None, arguments={},name=name)
        self.function = function

    def __repr__(self):
        return get_layer_repr(self)

    def extra_repr(self):
        s = 'function={0}'.format("".join(inspect.getsourcelines(self.function)[0]))



class Reshape(tf.keras.layers.Reshape):
    def __init__(self, target_shape,name='', **kwargs ):
        super(Reshape, self).__init__(target_shape,name=name, **kwargs)
    def __repr__(self):
        return get_layer_repr(self)

    def extra_repr(self):
        s = 'target_shape={0}'.format(self.target_shape)


class Dropout(tf.keras.layers.Dropout):
    def __init__(self, dropout_rate=0,name='' ):
        super(Dropout, self).__init__(dropout_rate,name=name)
    @property
    def dropout_rate(self):
        return self.rate
    @dropout_rate.setter
    def dropout_rate(self,value):
        self.rate=value

    def __repr__(self):
        return get_layer_repr(self)

    def extra_repr(self):
        s = 'dropout_rate={0}'.format(self.dropout_rate)



class Noise(tf.keras.layers.GaussianNoise):
    def __init__(self, stddev=0.1,name='' ):
        super(Noise, self).__init__(stddev=stddev,name=name)

    def __repr__(self):
        return get_layer_repr(self)

    def extra_repr(self):
        s = 'stddev={0}'.format(self.stddev)


