"""Wrapper class for TensorFlow Keras RNNs with trainable initial states."""

import tensorflow as tf

from .utils.keras import register_keras_custom_object


@register_keras_custom_object
class TrainableInitialStateRNN(tf.keras.layers.Wrapper):
    """Wrapper class for RNNs with trainable initial state variables.

    Parameters
    ----------
    layer : tf.keras.Layer
        An RNN instance (or a Bidirectional instance wrapping an RNN instance).

    initializer : str, callable, or list/tuple of str/callable, optional.
        The initializer for the initial state tensor(s), or a list or tuple of
        initializers, one for each initial state. If not specified, initial
        states will be initialized to zeros.

    regularizer : str, callable, or list/tuple of str/callable, optional.
        The regularizer for the initial state tensor(s), or a list or tuple of
        regularizers, one for each initial state. If not specified, initial
        states will not be regularized.

    constraint : str, callable, or list/tuple of str/callable, optional.
        The constraint for the initial state tensor(s), or a list or tuple of
        constraints, one for each initial state. If not specified, initial
        states will not be constrained.

    **kwargs : keyword arguments
        Additional keyword arguments for :class:`tf.keras.layers.Wrapper` (e.g.,
        `name`).
    """

    def __init__(self, layer, *, initializer=None, regularizer=None,
                 constraint=None, **kwargs):
        super().__init__(layer=layer, **kwargs)

        # Base layer must be an RNN or a bidirectional RNN
        rnn_types = (tf.keras.layers.RNN, tf.keras.layers.Bidirectional)
        if not isinstance(self.layer, rnn_types):
            raise TypeError(
                f'Expected RNN or Bidirectional layer; got layer={self.layer}',
            )

        # Figure out number of initial state tensors and their shapes
        # TODO: are there any RNN classes where this information isn't known
        #  before the layers are built?
        if isinstance(self.layer, tf.keras.layers.Bidirectional):
            # Bidirectional layers have initial states for the forward and
            # backward layers
            layers = [self.layer.forward_layer, self.layer.backward_layer]
        else:
            # Just an RNN subclass
            layers = [self.layer]
        # Concatenate all the state sizes into one list
        # TODO: this assumes that an RNN instance has a cell attribute with a
        #  state_size attribute. Are there any RNN classes where this isn't the
        #  case?
        # TODO: the use of tf.nest.flatten assumes that each layer's cell's
        #  state_size is a scalar. Are there any RNN classes where this isn't
        #  the case?
        self._state_sizes = sum((tf.nest.flatten(layer.cell.state_size)
                                 for layer in layers), [])
        n_states = len(self._state_sizes)

        # By default, initialize the initial states to zeros
        if initializer is None:
            initializer = 'zeros'

        # Get one initializer, regularizer, constraint for each initial state
        initializer = _one_for_each_state(initializer, n_states=n_states,
                                          name='initializer')
        regularizer = _one_for_each_state(regularizer, n_states=n_states,
                                          name='regularizer')
        constraint = _one_for_each_state(constraint, n_states=n_states,
                                         name='constraint')

        # Store initializers, regularizers, and constraints
        self.initializer = list(map(tf.keras.initializers.get, initializer))
        self.regularizer = list(map(tf.keras.regularizers.get, regularizer))
        self.constraint = list(map(tf.keras.constraints.get, constraint))

        # Variable(s) to be created when this layer is built
        self.initial_state = None

    def get_config(self) -> dict:
        """Get the configuration of the layer as a JSON-serializable dict."""
        config = super().get_config()
        config.update(
            initializer=list(map(tf.keras.initializers.serialize, self.initializer)),
            regularizer=list(map(tf.keras.regularizers.serialize, self.regularizer)),
            constraint=list(map(tf.keras.constraints.serialize, self.constraint)),
        )
        return config

    def build(self, input_shape=None):
        """Build this layer's underlying RNN and initial state tensors.

        Parameters
        ----------
        input_shape : TensorShape, or list of TensorShape
            Shape(s) of the input to the RNN.
        """
        # Build the wrapped layer in the superclass's build() method
        super().build(input_shape=input_shape)

        self.initial_state = []
        for i, (size, initializer, regularizer, constraint) in \
                enumerate(zip(self._state_sizes, self.initializer,
                              self.regularizer, self.constraint)):
            self.initial_state.append(
                self.add_weight(
                    name=f'initial_state_{i}',
                    shape=size,
                    dtype=tf.dtypes.float32,
                    initializer=initializer,
                    regularizer=regularizer,
                    trainable=True,
                    constraint=constraint,
                ),
            )

    def call(self, inputs, *args, **kwargs):
        """Run the RNN on input data.

        Parameters
        ----------
        inputs : tensor-like, or nested structure of list or tensor-like
            Inputs to the underlying RNN. This should not include the initial
            state.

        *args : positional arguments
            Additional positional arguments to pass to the underlying RNN.

        **kwargs : keyword arguments
            Keyword arguments for the underlying RNN. If an `initial_state`
            keyword argument is present, its value is used instead of this
            layer's `initial_state` variable(s).

        Returns
        -------
        :class:`tf.Tensor`
            The output of the underlying RNN.
        """
        # If the user passes an initial_state, favor using it over this layer's
        # initial state variable
        initial_state = kwargs.pop('initial_state', None)
        if initial_state is None:
            # Repeat each initial state variable for each element in the batch
            inputs_list = tf.nest.flatten(inputs)
            batch_size = tf.shape(inputs_list[0])[0]
            initial_state = [_batch_state(state=state, batch_size=batch_size)
                             for state in self.initial_state]
        return self.layer(inputs, *args, initial_state=initial_state, **kwargs)


def _batch_state(state: tf.Tensor, batch_size: tf.Tensor) -> tf.Tensor:
    """Repeat a state tensor along a new batch dimension."""
    shape = tf.concat([[batch_size], tf.shape(state)], axis=0)
    state = tf.broadcast_to(state, shape=shape)
    return state


def _one_for_each_state(value, n_states: int, name: str) -> list:
    """Duplicate a value for each initial state if there is only one value."""
    if isinstance(value, (tuple, list)):
        if len(value) != n_states:
            raise ValueError(f'When `{name}\' is a list or tuple, it '
                             'must contain exactly as many values as '
                             'initial states of the underlying RNN. '
                             f'Expected: {n_states}, got: {len(value)}')
    else:
        # Just duplicate the value for each state
        value = [value] * n_states
    return value
