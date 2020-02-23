#  Copyright 2020 Maruan Al-Shedivat. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  =============================================================================
"""Entropy-based activity regularizers."""

from tensorflow.python.keras import backend as K
from tensorflow.python.keras.regularizers import Regularizer


class OutputEntropy(Regularizer):
    """Encourages models with higher output entropy across mini-batches."""

    def __init__(self, attention, coeff=0.0):
        self.attention = attention
        self.coeff = coeff

    def __call__(self, x):
        batch_size = K.cast(K.shape(x)[0], K.floatx())
        # <float32> [batch_size, num_explanations].
        att_renormed = self.attention / K.mean(self.attention, axis=0)
        # <float32> [num_explanations, num_classes].
        probs = K.dot(K.transpose(att_renormed), x) / batch_size
        # <float32> [num_explanations].
        neg_entropy = K.sum(probs * K.log(probs), axis=1)
        return self.coeff * K.mean(neg_entropy)

    def __str__(self):
        config = self.get_config()
        return "{name:s}({coeff:f})".format(**config)

    def get_config(self):
        return {"name": self.__class__.__name__, "coeff": float(self.coeff)}


# Aliases.


def output_entropy_reg(attention, coeff=0.0):
    return OutputEntropy(attention, coeff=coeff)
