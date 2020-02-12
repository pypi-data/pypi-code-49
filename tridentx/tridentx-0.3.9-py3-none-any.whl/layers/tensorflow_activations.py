from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import six
from ..backend.common import *
import inspect
import numpy as np
import six
import tensorflow as tf
from tensorflow.keras import backend as K


__all__ = ['Identity','Sigmoid','Tanh','Relu','Relu6','LeakyRelu','LeakyRelu6','SmoothRelu','PRelu','Swish','Elu','HardSigmoid','HardSwish','Selu','LecunTanh','SoftSign','SoftPlus','HardTanh','Logit','LogLog','Mish','Softmax','BertGELU','GPTGELU','identity','sigmoid','tanh','relu','relu6','leaky_relu','leaky_relu6','smooth_relu','p_relu','swish','elu','hard_sigmoid','hard_swish','selu','lecun_tanh','soft_sign','soft_plus','hard_tanh','logit','log_log','mish','softmax','bert_gelu','gpt_gelu','get_activation']


def identity(x):
    return x


class Identity(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(Identity, self).__init__(name=name)
    def call(self, x, mask=None):
        return x
    def get_output_shape_for(self, input_shape):
        return input_shape





def sigmoid(x):
    return tf.nn.sigmoid(x)



class Sigmoid(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(Sigmoid, self).__init__(name=name)
    def call(self, x, mask=None):
        return sigmoid(x)
    def get_output_shape_for(self, input_shape):
        return input_shape

def tanh(x):
    return tf.nn.tanh(x)

class Tanh(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(Tanh, self).__init__(name=name)
    def call(self, x, mask=None):
        return tanh(x)
    def get_output_shape_for(self, input_shape):
        return input_shape

def relu(x,upper_limit=None):
    if upper_limit is not None and upper_limit<=0:
        raise ValueError('Upper limit should greater than 0!')
    elif upper_limit is not None:
        return K.clip(tf.nn.relu(x),0,upper_limit)
    return tf.nn.relu(x)



class Relu(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(Relu, self).__init__(name=name)
    def call(self, x, mask=None):
        return relu(x)
    def get_output_shape_for(self, input_shape):
        return input_shape

def relu6(x):
    return K.clip(tf.nn.relu(x),0,6)


class Relu6(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(Relu6, self).__init__(name=name)
    def call(self, x, mask=None):
        return relu6(x)
    def get_output_shape_for(self, input_shape):
        return input_shape



def leaky_relu(x,alpha=0.01,upper_limit=None):
    if upper_limit is not None:
        return K.clip(tf.nn.leaky_relu(x,alpha), -np.inf, upper_limit)
    return tf.nn.leaky_relu(x,alpha)



class LeakyRelu(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(LeakyRelu, self).__init__(name=name)
    def call(self, x, mask=None):
        return leaky_relu(x)
    def get_output_shape_for(self, input_shape):
        return input_shape

def leaky_relu6(x,alpha=0.01):
    return K.clip(tf.nn.leaky_relu(x,alpha), -6, 6)

class LeakyRelu6(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(LeakyRelu6, self).__init__(name=name)
    def call(self, x, mask=None):
        return leaky_relu6(x)
    def get_output_shape_for(self, input_shape):
        return input_shape


def elu(x,alpha=0.01,upper_limit=None):
    if upper_limit is not None:
        return K.clip(tf.nn.elu(x,alpha),-np.inf,upper_limit)
    return tf.nn.elu(x,alpha)

class Elu(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(Elu, self).__init__(name=name)
    def call(self, x, mask=None):
        return elu(x)
    def get_output_shape_for(self, input_shape):
        return input_shape

lrelu=leaky_relu


def smooth_relu(x,upper_limit=None):
    if upper_limit is not None:
        return K.clip(tf.math.log(1 + tf.math.exp(x)),-np.inf,upper_limit)
    return tf.math.log(1 + tf.math.exp(x))

class SmoothRelu(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(SmoothRelu, self).__init__(name=name)
    def call(self, x, mask=None):
        return smooth_relu(x)
    def get_output_shape_for(self, input_shape):
        return input_shape

def p_relu(x,upper_limit=None):
    if upper_limit is not None:
        return K.clip(tf.keras.layers.PReLU()(x),-np.inf,upper_limit)
    return tf.keras.layers.PReLU()(x)

PRelu=tf.keras.layers.PReLU


def swish(x):
    return tf.nn.sigmoid(x) * x


class Swish(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(Swish, self).__init__(name=name)
    def call(self, x, mask=None):
        return swish(x)
    def get_output_shape_for(self, input_shape):
        return input_shape


def selu(x):
    return tf.nn.selu(x)


class Selu(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(Selu, self).__init__(name=name)
    def call(self, x, mask=None):
        return selu(x)
    def get_output_shape_for(self, input_shape):
        return input_shape



def lecun_tanh(x):
    return 1.7159 * tf.nn.tanh(2/3 * x)

class LecunTanh(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(LecunTanh, self).__init__(name=name)
    def call(self, x, mask=None):
        return lecun_tanh(x)
    def get_output_shape_for(self, input_shape):
        return input_shape



def soft_sign(x):
    return tf.nn.softsign(x)

class SoftSign(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(SoftSign, self).__init__(name=name)
    def call(self, x, mask=None):
        return soft_sign(x)
    def get_output_shape_for(self, input_shape):
        return input_shape


def soft_plus(x):
    return tf.nn.softplus(x)

class SoftPlus(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(SoftPlus, self).__init__(name=name)
    def call(self, x, mask=None):
        return soft_plus(x)
    def get_output_shape_for(self, input_shape):
        return input_shape


def hard_sigmoid(x):
    return relu6(x+3)/6

class HardSigmoid(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(HardSigmoid, self).__init__(name=name)
    def call(self, x, mask=None):
        return hard_sigmoid(x)
    def get_output_shape_for(self, input_shape):
        return input_shape

def hard_tanh(x):
    return tf.keras.backend.clip(x,-1,1)

class HardTanh(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(HardTanh, self).__init__(name=name)
    def call(self, x, mask=None):
        return hard_tanh(x)
    def get_output_shape_for(self, input_shape):
        return input_shape

def hard_swish(x):
    return  x * hard_sigmoid(x)

class HardSwish(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(HardSwish, self).__init__(name=name)
    def call(self, x, mask=None):
        return hard_swish(x)
    def get_output_shape_for(self, input_shape):
        return input_shape

def logit(x):
        return tf.math.log(x / (1 - x))


class Logit(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(Logit, self).__init__(name=name)
    def call(self, x, mask=None):
        return logit(x)
    def get_output_shape_for(self, input_shape):
        return input_shape


def log_log(x):
    return  1-tf.math.exp(-tf.math.exp(x))

class LogLog(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(LogLog, self).__init__(name=name)
    def call(self, x, mask=None):
        return log_log(x)
    def get_output_shape_for(self, input_shape):
        return input_shape



def softmax(x):
    return tf.nn.softmax(x)

Softmax=tf.keras.layers.Softmax


def mish(x):
    return x*tf.nn.tanh(tf.nn.softplus(x))



class Mish(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(Mish, self).__init__(name=name)
    def call(self, x, mask=None):
        return mish(x)
    def get_output_shape_for(self, input_shape):
        return input_shape


def bert_gelu(x):

  """Gaussian Error Linear Unit.
  This is a smoother version of the RELU.
  Original paper: https://arxiv.org/abs/1606.08415
  Args:
    x: float Tensor to perform activation.
  Returns:
    `x` with the GELU activation applied.
  """
  return x *  0.5 * (1.0 + tf.nn.tanh((np.sqrt(2 / np.pi) * (x + 0.044715 * tf.pow(x, 3)))))


class BertGELU(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(BertGELU, self).__init__(name=name)
    def call(self, x, mask=None):
        return bert_gelu(x)
    def get_output_shape_for(self, input_shape):
        return input_shape



def gpt_gelu(x):
    return 0.5 * x * (1 + tf.math.tanh(tf.math.sqrt(2 /np.pi) * (x + 0.044715 * tf.math.pow(x, 3))))

class GPTGELU(tf.keras.layers.Layer):
    def __init__(self,name=''):
        super(GPTGELU, self).__init__(name=name)
    def call(self, x, mask=None):
        return gpt_gelu(x)
    def get_output_shape_for(self, input_shape):
        return input_shape


def get_activation(fn_name):
    if fn_name is None:
        return None
    fn_modules = ['trident.layers.tensorflow_activations']
    try:
        if isinstance(fn_name,str) and fn_name in __all__:
            if  fn_name.islower():
                 activation_fn = get_function(fn_name, fn_modules)
                 return activation_fn
            else:
                try:
                    activation_fn = get_class(fn_name,  fn_modules)
                    return activation_fn()
                except Exception:
                    activation_fn = get_function(camel2snake(fn_name), fn_modules)
                    return activation_fn
        if getattr(fn_name, '__module__', None) == 'trident.layers.tensorflow_activations':
            if inspect.isfunction(fn_name):
                return fn_name
            elif isinstance(fn_name, tf.keras.layers.Layer):
                return fn_name()
        else:
            if callable(fn_name) :
                result=inspect.getfullargspec(fn_name)
                if 1<=len(result.args)<=2:
                    return fn_name if inspect.isfunction(fn_name) else fn_name()
                else:
                    raise ValueError('Unknown activation function/ class')
    except Exception:
        return None

