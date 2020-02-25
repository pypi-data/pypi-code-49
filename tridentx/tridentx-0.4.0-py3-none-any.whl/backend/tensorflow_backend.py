from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys
import numpy as np
from collections import OrderedDict
import random
from itertools import islice
import tensorflow as tf

from tensorflow.python.framework import ops
from tensorflow.python.eager import context
from tensorflow.python.util import object_identity


import copy

from tensorflow.python.keras import layers as layer_module
from tensorflow.python.keras.engine import base_layer
from tensorflow.python.keras.engine import base_layer_utils
from tensorflow.python.keras.engine import input_layer
from tensorflow.python.keras.engine import training
from tensorflow.python.keras.engine import training_utils
from tensorflow.python.keras.saving.saved_model import model_serialization
from tensorflow.python.keras.utils import generic_utils,layer_utils,tf_utils

from tensorflow.python.platform import tf_logging as logging
from tensorflow.python.training.tracking import base as trackable
from tensorflow.python.training.tracking import layer_utils as trackable_layer_utils
from tensorflow.python.util import nest
from tensorflow.python.util import tf_inspect
from tensorflow.python.util.tf_export import keras_export

from ..layers.tensorflow_layers import *
from ..layers.tensorflow_normalizations import *
from ..layers.tensorflow_activations import *
from ..layers.tensorflow_normalizations import *
from ..data.tensorflow_datasets import *
from ..backend.common import floatx, addindent, get_time_suffix, format_time, get_terminal_size, snake2camel, \
    PrintException, to_list, unpack_singleton, enforce_singleton

__all__ = ['register_keras_custom_object', 'to_numpy', 'to_tensor', 'get_flops', 'Input', 'Sequential',
           'ConcatContainer', 'ReplayBuffer', 'print_summary']

version = tf.version
sys.stderr.write('Tensorflow version:{0}.\n'.format(version.VERSION))

if version.VERSION < '2.0.0':
    raise ValueError('Not support Tensorflow below 2.0')


gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    # Restrict TensorFlow to only use the first GPU
    try:
        tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
        tf.config.experimental.set_memory_growth(gpus[0], True)

        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    except RuntimeError as e:
        # Visible devices must be set before GPUs have been initialized
        print(e)


def register_keras_custom_object(cls):
    tf.keras.utils.get_custom_objects()[cls.__name__] = cls
    return cls


def to_numpy(x) -> np.ndarray:
    """
    Convert whatever to numpy array
    :param x: List, tuple, PyTorch tensor or numpy array
    :return: Numpy array
    """
    if isinstance(x, np.ndarray):
        return x
    # elif isinstance(x,EagerTensor):
    #     return x.numpy()
    elif hasattr(x, 'numpy'):
        with context.eager_mode():
            return x.numpy()
    elif isinstance(x, tf.TensorShape):
        return np.array(x.as_list())
    elif isinstance(x, (tf.Tensor, tf.Variable)):
        return tf.keras.backend.get_value(x)
    # elif isinstance(x, tf.Variable):
    #     sess = tf.compat.v1.Session()
    #     x = sess.run(x.value())
    #     return x
    # elif isinstance(x, ops.Tensor):
    #     sess = tf.compat.v1.Session()
    #     x= sess.run(x)
    #     return x

    elif isinstance(x, (list, tuple, int, float)):
        return np.array(x)
    else:
        try:
            x = tf.keras.backend.get_value(x)
            if isinstance(x, np.ndarray):
                return x
        except:
            raise ValueError("Unsupported type")


def to_tensor(x, dtype=None) -> ops.Tensor:
    return ops.convert_to_tensor(x, dtype=dtype)


def get_flops(model):
    run_meta = tf.compat.v1.RunMetadata()
    opts = tf.compat.v1.profiler.ProfileOptionBuilder.float_operation()

    # We use the Keras session graph in the call to the profiler.
    flops = tf.compat.v1.profiler.profile(graph=tf.compat.v1.keras.backend.get_session().graph, run_meta=run_meta,
                                          cmd='op', options=opts)

    return flops.total_float_ops  # Prints the "flops" of the model.


def get_layer_repr(layer):
    # We treat the extra repr like the sub-module, one item per line
    extra_lines = []
    if hasattr(layer, 'extra_repr') and callable(layer.extra_repr):
        extra_repr = layer.extra_repr()
        # empty string will be split into list ['']
        if extra_repr:
            extra_lines = extra_repr.split('\n')
    child_lines = []
    if isinstance(layer, (tf.keras.Model, tf.keras.Sequential)) and layer.layers is not None:
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


def Input(input_shape: (list, tuple, int) = None, batch_size=None, name=''):
    if isinstance(input_shape, int):
        input_shape = input_shape,
    elif isinstance(input_shape, list):
        input_shape = tuple(input_shape)
    return tf.keras.Input(shape=input_shape, batch_size=batch_size, name=name, dtype=tf.float32)

class Container(tf.keras.Model):
  """Linear stack of layers.

  Arguments:
      layers: list of layers to add to the model.

  Example:

  ```python
  # Optionally, the first layer can receive an `input_shape` argument:
  model = Sequential()
  model.add(Dense(32, input_shape=(500,)))
  # Afterwards, we do automatic shape inference:
  model.add(Dense(32))

  # This is identical to the following:
  model = Sequential()
  model.add(Dense(32, input_dim=500))

  # And to the following:
  model = Sequential()
  model.add(Dense(32, batch_input_shape=(None, 500)))

  # Note that you can also omit the `input_shape` argument:
  # In that case the model gets built the first time you call `fit` (or other
  # training and evaluation methods).
  model = Sequential()
  model.add(Dense(32))
  model.add(Dense(32))
  model.compile(optimizer=optimizer, loss=loss)
  # This builds the model for the first time:
  model.fit(x, y, batch_size=32, epochs=10)

  # Note that when using this delayed-build pattern (no input shape specified),
  # the model doesn't have any weights until the first call
  # to a training/evaluation method (since it isn't yet built):
  model = Sequential()
  model.add(Dense(32))
  model.add(Dense(32))
  model.weights  # returns []

  # Whereas if you specify the input shape, the model gets built continuously
  # as you are adding layers:
  model = Sequential()
  model.add(Dense(32, input_shape=(500,)))
  model.add(Dense(32))
  model.weights  # returns list of length 4

  # When using the delayed-build pattern (no input shape specified), you can
  # choose to manually build your model by calling `build(batch_input_shape)`:
  model = Sequential()
  model.add(Dense(32))
  model.add(Dense(32))
  model.build((None, 500))
  model.weights  # returns list of length 4
  ```
  """

  @trackable.no_automatic_dependency_tracking
  def __init__(self, layers=None, name=None):
    super(Container, self).__init__(name=name, autocast=False)
    self.supports_masking = True
    self._build_input_shape = None
    self._compute_output_and_mask_jointly = True

    self._layer_call_argspecs = {}

    # Add to the model any layers passed to the constructor.
    if layers:
      if not isinstance(layers, (list, tuple)):
        layers = [layers]
      tf_utils.assert_no_legacy_layers(layers)
      for layer in layers:
        self.add(layer)

  @property
  def layers(self):
    # Historically, `sequential.layers` only returns layers that were added
    # via `add`, and omits the auto-generated `InputLayer` that comes at the
    # bottom of the stack.
    # `Trackable` manages the `_layers` attributes and does filtering
    # over it.
    layers = super(Container, self).layers
    if layers and isinstance(layers[0], input_layer.InputLayer):
      return layers[1:]
    return layers[:]

  @property
  @trackable_layer_utils.cache_recursive_attribute('dynamic')
  def dynamic(self):
    return any(layer.dynamic for layer in self.layers)

  @trackable.no_automatic_dependency_tracking
  def add(self, layer):
    pass

  @trackable.no_automatic_dependency_tracking
  def pop(self):
    pass

  @base_layer_utils.default
  def build(self, input_shape=None):
      pass

  def call(self, inputs, training=None, mask=None):  # pylint: disable=redefined-outer-name
    pass

  def compute_output_shape(self, input_shape):
    pass

  def compute_mask(self, inputs, mask):
    pass

  def predict_proba(self, x, batch_size=32, verbose=0):
    pass

  def predict_classes(self, x, batch_size=32, verbose=0):
      pass

  def get_config(self):
    layer_configs = []
    for layer in self.layers:
      layer_configs.append(generic_utils.serialize_keras_object(layer))
    # When constructed using an `InputLayer` the first non-input layer may not
    # have the shape information to reconstruct `Sequential` as a graph network.
    if (self._is_graph_network and layer_configs and
        'batch_input_shape' not in layer_configs[0]['config'] and
        isinstance(self._layers[0], input_layer.InputLayer)):
      batch_input_shape = self._layers[0]._batch_input_shape
      layer_configs[0]['config']['batch_input_shape'] = batch_input_shape

    config = {
        'name': self.name,
        'layers': copy.deepcopy(layer_configs)
    }
    if self._build_input_shape:
      config['build_input_shape'] = self._build_input_shape
    return config

  @classmethod
  def from_config(cls, config, custom_objects=None):
    if 'name' in config:
      name = config['name']
      build_input_shape = config.get('build_input_shape')
      layer_configs = config['layers']
    else:
      name = None
      build_input_shape = None
      layer_configs = config
    model = cls(name=name)
    for layer_config in layer_configs:
      layer = layer_module.deserialize(layer_config,
                                       custom_objects=custom_objects)
      model.add(layer)
    if not model.inputs and build_input_shape:
      model.build(build_input_shape)
    return model

  @property
  def input_spec(self):
    if self.layers and hasattr(self.layers[0], 'input_spec'):
      return self.layers[0].input_spec
    return None

  @property
  def _trackable_saved_model_saver(self):
    return model_serialization.SequentialSavedModelSaver(self)



class Sequential(tf.keras.Sequential):
    def __init__(self, *layers, name=''):
        super(Sequential, self).__init__(name=name)
        if len(layers) > 1:
            for layer in layers:
                if isinstance(layer, tf.keras.Sequential):
                    self.add(layer)
                elif isinstance(layer, (tuple, list)):
                    self.add(Sequential(list(layer)))
                else:
                    self.add(layer)
        elif len(layers) == 1 and isinstance(layers[0], tf.keras.layers.Layer):
            self.add(layers[0])
        elif len(layers) == 1 and isinstance(layers[0], list):
            for layer in layers[0]:
                self.add(layer)
        elif len(layers) == 1 and isinstance(layers[0], OrderedDict):
            for k, v in layers[0].items():
                v.__name__ = k
                self.add(v)

    def _get_item_by_idx(self, iterator, idx):
        return next(islice(iterator, idx, None))

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return self.layers[idx]
        else:
            return self._get_item_by_idx(self.layers, idx)

    def __setitem__(self, idx, module):
        key = self._get_item_by_idx(self._modules.keys(), idx)
        return setattr(self, key, module)

    def __delitem__(self, idx):
        if isinstance(idx, slice):
            for key in self.layers[idx]:
                delattr(self, key)
        else:
            key = self._get_item_by_idx(self.layers, idx)
            delattr(self, key)

    def __len__(self):
        return len(self.layers)

    def __dir__(self):
        keys = super(Sequential, self).__dir__()
        keys = [key for key in keys if not key.isdigit()]
        return keys

    def __repr__(self):
        return get_layer_repr(self)

    @property
    def trainable_weights(self):
        if self.trainable:
            nested = self._gather_children_attribute('trainable_weights')
            return self._dedup_weights(self._trainable_weights + nested)
        else:
            return []

    @property
    def non_trainable_weights(self):
        if self.trainable:
            nested = self._gather_children_attribute('non_trainable_weights')
            non_trainable_weights = self._non_trainable_weights + nested
        else:
            nested = self._gather_children_attribute('weights')
            non_trainable_weights = (self._trainable_weights + self._non_trainable_weights + nested)
        return self._dedup_weights(non_trainable_weights)

    @property
    def weights(self):
        """Returns the list of all layer variables/weights.

        Returns:
          A list of variables.
        """
        return self.trainable_weights + self.non_trainable_weights


class Combine(tf.keras.Model):
    r"""A sequential container.
    Modules will be added to it in the order they are passed in the constructor.
    Alternatively, an ordered dict of modules can also be passed in.

    To make it easier to understand, here is a small example::

        # Example of using Sequential
        model = nn.Sequential(
                  nn.Conv2d(1,20,5),
                  nn.ReLU(),
                  nn.Conv2d(20,64,5),
                  nn.ReLU()
                )

        # Example of using Sequential with OrderedDict
        model = nn.Sequential(OrderedDict([
                  ('conv1', nn.Conv2d(1,20,5)),
                  ('relu1', nn.ReLU()),
                  ('conv2', nn.Conv2d(20,64,5)),
                  ('relu2', nn.ReLU())
                ]))
    """

    def __init__(self, *args):
        super(Combine, self).__init__()
        self._built = False

        if len(args) == 1 and isinstance(args[0], OrderedDict):
            for key, module in args[0].items():
                module.__name__ = key
                self._layers.append(module)
        elif len(args) == 1 and isinstance(args[0], (list)):
            for idx, module in enumerate(args[0]):
                self._layers.append(module)
        else:
            for idx, module in enumerate(args):
                self._layers.append(module)

    @property
    def layers(self):
        return self._layers

    def __len__(self):
        return len(self._layers)

    def __dir__(self):
        keys = super(Combine, self).__dir__()
        keys = [key for key in keys if not key.isdigit()]
        return keys

    def call(self, inputs, training=None, mask=None):  # pylint: disable=redefined-outer-name
        if self._is_graph_network:
            if not self.built:
                self._init_graph_network(self.inputs, self.outputs, name=self.name)
            return super(Combine, self).call(inputs, training=training, mask=mask)

        outputs = []
        for layer in self._layers:
            outputs.append(layer(inputs))
        return tuple(outputs)


def compute_output_shape(self, input_shape):
    shape = input_shape
    for layer in self.layers:
        shape = layer.compute_output_shape(shape)
    return shape


class ConcatContainer(tf.keras.Model):
    r"""A sequential container.
    Modules will be added to it in the order they are passed in the constructor.
    Alternatively, an ordered dict of modules can also be passed in.

    To make it easier to understand, here is a small example::

        # Example of using Sequential
        model = nn.Sequential(
                  nn.Conv2d(1,20,5),
                  nn.ReLU(),
                  nn.Conv2d(20,64,5),
                  nn.ReLU()
                )

        # Example of using Sequential with OrderedDict
        model = nn.Sequential(OrderedDict([
                  ('conv1', nn.Conv2d(1,20,5)),
                  ('relu1', nn.ReLU()),
                  ('conv2', nn.Conv2d(20,64,5)),
                  ('relu2', nn.ReLU())
                ]))
    """

    def __init__(self, *args, **kwargs):
        super(ConcatContainer, self).__init__()
        self.axis = kwargs.get('axis', -1)
        if len(args) == 1 and isinstance(args[0], OrderedDict):
            for key, module in args[0].items():
                self._modules[len(self._modules)] = module
        else:
            for idx, module in enumerate(args):
                self._modules[idx] = module
        self.to(self.device)

    def _get_item_by_idx(self, iterator, idx):
        """Get the idx-th item of the iterator"""
        size = len(self)
        idx = idx.__index__()
        if not -size <= idx < size:
            raise IndexError('index {} is out of range'.format(idx))
        idx %= size
        return next(islice(iterator, idx, None))

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return self.__class__(OrderedDict(list(self._modules.items())[idx]))
        else:
            return self._get_item_by_idx(self._modules.values(), idx)

    def __setitem__(self, idx, module):
        key = self._get_item_by_idx(self._modules.keys(), idx)
        return setattr(self, key, module)

    def __delitem__(self, idx):
        if isinstance(idx, slice):
            for key in list(self._modules.keys())[idx]:
                delattr(self, key)
        else:
            key = self._get_item_by_idx(self._modules.keys(), idx)
            delattr(self, key)

    def __len__(self):
        return len(self._modules)

    def __dir__(self):
        keys = super(ConcatContainer, self).__dir__()
        keys = [key for key in keys if not key.isdigit()]
        return keys

    def call(self, x, **kwargs):
        results = []
        for module in self._modules.values():
            x1 = module(x)
            results.append(x1)
        return tf.concat(results, axis=-1)


class ReplayBuffer:
    def __init__(self, max_size=1000):
        assert max_size > 0, "Empty buffer or trying to create a black hole. Be careful."
        self.max_size = max_size
        self.data = []

    def push_and_pop(self, data):
        to_return = []
        for element in data.data:
            element = tf.keras.backend.expand_dims(element, 0)
            if len(self.data) < self.max_size:
                self.data.append(element)
                to_return.append(element)
            else:
                if random.uniform(0, 1) > 0.5:
                    i = random.randint(0, self.max_size - 1)
                    to_return.append(self.data[i].clone())
                    self.data[i] = element
                else:
                    to_return.append(element)
        return tf.concat(to_return,axis=-1)



def count_params(weights):
    """Count the total number of scalars composing the weights.

    Arguments:
        weights: An iterable containing the weights on which to compute params

    Returns:
        The total number of scalars composing the weights
    """
    return int(sum(np.prod(p.shape.as_list()) for p in object_identity.ObjectIdentitySet(weights)))


def print_summary(model, line_length=None, positions=None, print_fn=None):
    """Prints a summary of a model.

    Arguments:
        model: Keras model instance.
        line_length: Total length of printed lines
            (e.g. set this to adapt the display to different
            terminal window sizes).
        positions: Relative or absolute positions of log elements in each line.
            If not provided, defaults to `[.33, .55, .67, 1.]`.
        print_fn: Print function to use.
            It will be called on each line of the summary.
            You can set it to a custom function
            in order to capture the string summary.
            It defaults to `print` (prints to stdout).
    """
    if print_fn is None:
        print_fn = print

    if model.__class__.__name__ == 'Sequential':
        sequential_like = True
    elif not model._is_graph_network:
        # We treat subclassed models as a simple sequence of layers, for logging
        # purposes.
        sequential_like = True
    else:
        sequential_like = True
        nodes_by_depth = model._nodes_by_depth.values()
        nodes = []
        for v in nodes_by_depth:
            if (len(v) > 1) or (len(v) == 1 and len(nest.flatten(v[0].inbound_layers)) > 1):
                # if the model has multiple nodes
                # or if the nodes have multiple inbound_layers
                # the model is no longer sequential
                sequential_like = False
                break
            nodes += v
        if sequential_like:
            # search for shared layers
            for layer in model.layers:
                flag = False
                for node in layer._inbound_nodes:
                    if node in nodes:
                        if flag:
                            sequential_like = False
                            break
                        else:
                            flag = True
                if not sequential_like:
                    break

    if sequential_like:
        line_length = line_length or 98
        positions = positions or [.33, .55, .67, 1.]
        if positions[-1] <= 1:
            positions = [int(line_length * p) for p in positions]
        # header names for the different log elements
        to_display = ['Layer (type)', 'Output Shape', 'Param #', 'Block']
    else:
        line_length = line_length or 98
        positions = positions or [.33, .55, .67, 1.]
        if positions[-1] <= 1:
            positions = [int(line_length * p) for p in positions]
        # header names for the different log elements
        to_display = ['Layer (type)', 'Output Shape', 'Param #', 'Connected to']
        relevant_nodes = []
        for v in model._nodes_by_depth.values():
            relevant_nodes += v

    def print_row(fields, positions):
        line = ''
        for i in range(len(fields)):
            if i > 0:
                line = line[:-1] + ' '
            line += str(fields[i])
            line = line[:positions[i]]
            line += ' ' * (positions[i] - len(line))
        print_fn(line)

    print_fn('Model: "{}"'.format(model.name))
    print_fn('_' * line_length)
    print_row(to_display, positions)
    print_fn('=' * int(line_length * 0.66))

    def print_layer_summary(layer, block=None):
        """Prints a summary for a single layer.

        Arguments:
            layer: target layer.
        """
        try:
            output_shape = layer.output_shape
        except AttributeError:
            output_shape = 'multiple'
        except RuntimeError:  # output_shape unknown in Eager mode.
            output_shape = '?'
        name = layer.name
        cls_name = layer.__class__.__name__

        if isinstance(layer, Sequential):
            fields = [name + ' (' + cls_name + ')', 'block', layer.count_params(), block]
            print_row(fields, positions)
            for sublayer in layer.layers:
                print_layer_summary(sublayer, block=name)
        else:
            fields = [name + ' (' + cls_name + ')', output_shape, layer.count_params(), block]
            print_row(fields, positions)

    def print_layer_summary_with_connections(layer):
        """Prints a summary for a single layer (including topological connections).

        Arguments:
            layer: target layer.
        """
        try:
            output_shape = layer.output_shape
        except AttributeError:
            output_shape = 'multiple'
        connections = []
        for node in layer._inbound_nodes:
            if relevant_nodes and node not in relevant_nodes:
                # node is not part of the current network
                continue

            for inbound_layer, node_index, tensor_index, _ in node.iterate_inbound():
                connections.append('{}[{}][{}]'.format(inbound_layer.name, node_index, tensor_index))

        name = layer.name
        cls_name = layer.__class__.__name__
        if not connections:
            first_connection = ''
        else:
            first_connection = connections[0]
        fields = [name + ' (' + cls_name + ')', output_shape, layer.count_params(), first_connection]
        print_row(fields, positions)
        if len(connections) > 1:
            for i in range(1, len(connections)):
                fields = ['', '', '', connections[i]]
                print_row(fields, positions)

    layers = model.layers
    for i in range(len(layers)):
        if sequential_like:
            print_layer_summary(layers[i])
        else:
            print_layer_summary_with_connections(layers[i])
        if i == len(layers) - 1:
            print_fn('=' * line_length)
        else:
            print_fn('_' * line_length)

    model._check_trainable_weights_consistency()
    if hasattr(model, '_collected_trainable_weights'):
        trainable_count = count_params(model._collected_trainable_weights)
    else:
        trainable_count = count_params(model.trainable_weights)

    non_trainable_count = count_params(model.non_trainable_weights)

    print_fn('Total params: {:,}'.format(trainable_count + non_trainable_count))
    print_fn('Trainable params: {:,}'.format(trainable_count))
    print_fn('Non-trainable params: {:,}'.format(non_trainable_count))
    print_fn('_' * line_length)
