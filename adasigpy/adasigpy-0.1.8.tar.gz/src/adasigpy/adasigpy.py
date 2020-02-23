import numpy as np

from .domain.method import Method, init_w
from .interface.filter import AdaptiveSignalProcesserABC


class AdaptiveSignalProcesser(AdaptiveSignalProcesserABC):
    def __init__(self, model, shape, mu, w_init, lambda_):
        self.method = Method.methods[model]
        self.mu = mu
        self.w = init_w(w_init, shape)
        self.lambda_ = lambda_

    def adopt(self, d, x):
        len_d, len_x = len(d), len(x)
        if len_d != len_x:
            raise ValueError(
                f"2 arrays should have same length. But now, 'd' has {len_d} and 'x' has {len_x}."
            )
        self.method(d, x, self.w, self.mu, self.lambda_)

    def update(self, d, x):
        len_d, len_x = len(d), len(x)
        if len_d != len_x:
            raise ValueError(
                f"2 arrays should have same length. But now, 'd' has {len_d} and 'x' has {len_x}."
            )
        w_delta = self.method(d, x, self.w, self.mu, self.lambda_)
        self.w = self.w + w_delta
        return self.w
