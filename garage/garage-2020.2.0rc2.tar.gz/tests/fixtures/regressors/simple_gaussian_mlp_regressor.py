"""Simple GaussianMLPRegressor for testing."""
import numpy as np
import tensorflow as tf

from garage.tf.regressors import StochasticRegressor
from tests.fixtures.models import SimpleGaussianMLPModel


class SimpleGaussianMLPRegressor(StochasticRegressor):
    """Simple GaussianMLPRegressor for testing.

    Args:
        input_shape (tuple[int]): Input shape of the training data.
        output_dim (int): Output dimension of the model.
        name (str): Model name, also the variable scope.
        args (list): Unused positionl arguments.
        kwargs (dict): Unused keyword arguments.

    """

    # pylint: disable=unused-argument
    def __init__(self, input_shape, output_dim, name, *args, **kwargs):
        super().__init__(input_shape, output_dim, name)

        self.model = SimpleGaussianMLPModel(output_dim=self._output_dim)

        self._ys = None
        self._initialize()

    def _initialize(self):
        """Initialize graph."""
        input_ph = tf.compat.v1.placeholder(tf.float32,
                                            shape=(None, ) + self._input_shape)
        with tf.compat.v1.variable_scope(self._name) as vs:
            self._variable_scope = vs
            self.model.build(input_ph)

    def fit(self, xs, ys):
        """Fit with input data xs and label ys.

        Args:
            xs (numpy.ndarray): Input data.
            ys (numpy.ndarray): Label of input data.

        """
        self._ys = ys

    def predict(self, xs):
        """Predict ys based on input xs.

        Args:
            xs (numpy.ndarray): Input data.

        Return:
            np.ndarray: The predicted ys.

        """
        if self._ys is None:
            mean = tf.compat.v1.get_default_session().run(
                self.model.networks['default'].mean,
                feed_dict={self.model.networks['default'].input: xs})
            self._ys = np.full((len(xs), 1), mean)

        return self._ys

    def get_params_internal(self):
        """Get the params, which are the trainable variables.

        Returns:
            List[tf.Variable]: A list of trainable variables in the current
            variable scope.

        """
        return self._variable_scope.trainable_variables()

    def __setstate__(self, state):
        """Object.__setstate__.

        Args:
            state (dict): Unpickled state.

        """
        super().__setstate__(state)
        self._initialize()
