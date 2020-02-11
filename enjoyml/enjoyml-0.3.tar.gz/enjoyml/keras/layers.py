import numpy as np
from keras import backend as K
from keras import layers

MAX_MODE = 'max'
AVERAGE_MODE = 'average'
AVAILABLE_POOL_MODES = (MAX_MODE, AVERAGE_MODE)

pool_mode_to_base_layer = {
    MAX_MODE: layers.MaxPool2D,
    AVERAGE_MODE: layers.AvgPool2D,
}

pool_mode_to_func = {
    MAX_MODE: K.max,
    AVERAGE_MODE: K.mean,
}


class FixedPooling2D(layers.Layer):
    def __init__(self, output_size, pool_mode=MAX_MODE, iterations=10, random_state=42, **kwargs):
        if pool_mode not in AVAILABLE_POOL_MODES:
            raise Exception(f'[{self.__class__.__name__}] Unknown pooling mode: {pool_mode}.'
                            f' Available options: {AVAILABLE_POOL_MODES}')
        self.output_size = output_size
        self.pool_mode = pool_mode
        self.iterations = iterations
        self.random_state = random_state
        self.kernel_size = None
        self.base_pool_layer = None
        super().__init__(**kwargs)

    def _get_base_pool_layer(self, input_size, output_size):
        input_height, input_width = input_size
        output_height, output_width = output_size
        self.kernel_size = input_height // output_height, input_width // output_width
        PoolClassLayer = pool_mode_to_base_layer[self.pool_mode]
        return PoolClassLayer(self.kernel_size, padding='same')

    def _random_reduce(self, tensor, row_steps, col_steps, seed_up):
        reduce_func = pool_mode_to_func[self.pool_mode]
        random = np.random.RandomState(self.random_state + seed_up)
        while row_steps > 0 or col_steps > 0:
            if row_steps > 0:
                i = random.randint(0, tensor.get_shape()[1] - 1)
                pooled_tensor_row = K.expand_dims(
                    reduce_func([tensor[:, i, :, :], tensor[:, i + 1, :, :]], axis=0),
                    axis=1
                )
                tensor = K.concatenate([
                    tensor[:, :i, :, :],
                    pooled_tensor_row,
                    tensor[:, (i + 2):, :, :]
                ], axis=1)
                row_steps -= 1
            if col_steps > 0:
                j = random.randint(0, tensor.get_shape()[2] - 1)
                pooled_tensor_col = K.expand_dims(
                    reduce_func([tensor[:, :, j, :], tensor[:, :, j + 1, :]], axis=0),
                    axis=2
                )
                tensor = K.concatenate([
                    tensor[:, :, :j, :],
                    pooled_tensor_col,
                    tensor[:, :, (j + 2):, :]
                ], axis=2)
                col_steps -= 1
        return tensor

    def build(self, input_shape):
        dimension = len(input_shape)
        if dimension != 4:
            raise Exception(f'[{self.__class__.__name__}] Invalid dimension: expected 4 dims, get {dimension}.')
        if input_shape[1] < self.output_size[0] or input_shape[2] < self.output_size[1]:
            raise Exception(f'[{self.__class__.__name__}] Input shape must be greater or equal to output size.')
        self.base_pool_layer = self._get_base_pool_layer(input_shape[-3: -1], self.output_size)
        super().build(input_shape)  # Be sure to call this at the end

    def call(self, tensor, **kwargs):
        base_pooled_tensor = self.base_pool_layer(tensor)
        base_pooled_shape = base_pooled_tensor.get_shape()
        row_reduce_steps = base_pooled_shape[1] - self.output_size[0]
        col_reduce_steps = base_pooled_shape[2] - self.output_size[1]
        result = 0
        for iter_n in range(self.iterations):
            pooled_tensor = K.identity(base_pooled_tensor)
            pooled_tensor = self._random_reduce(
                pooled_tensor, seed_up=iter_n, row_steps=row_reduce_steps, col_steps=col_reduce_steps
            )
            result += pooled_tensor
        return result / self.iterations

    def compute_output_shape(self, input_shape):
        return (input_shape[0],) + self.output_size + (input_shape[-1],)
