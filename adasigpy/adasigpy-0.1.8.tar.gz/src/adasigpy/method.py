import numpy as np
from nptyping import Array


def lms(d: Array, x: Array, w: Array, mu: float, _) -> Array:
    """
    lms Least-Mean-Square filtering.

    Args:
        d (Array): Desired values.
        x (Array): Input(recorded) values.
        w (Array): Filter-weight matrix.
        mu (float): Step size.
        _ ([dummy argument]): DO NOT SET ANY VALUE.

    Returns:
        Array: Modified value array of w.
    """
    N = len(x)

    y = np.zeros_like(d)
    e = np.zeros_like(d)

    # w_delta: 係数行列wの更新量
    w_delta = np.zeros_like(w)

    for k in range(N):
        y[k] = np.dot(w.T, x[k])
        e[k] = d[k] - y[k]
        # 2 * J = e ** 2
        diff_J_for_w_ = e[k] * x[k]
        w_delta = mu * diff_J_for_w_
    return w_delta


def nlms(d: Array, x: Array, w: Array, mu: float, lambda_: float = 1.0) -> Array:
    """
    Normalized-LMS filtering.

    Args:
        d (Array): Desired values.
        x (Array): Input(recorded) values.
        w (Array): Filter-weight matrix.
        mu (float): Step size.
        lambda_ (float, optional): Learning rate. Defaults to 1.0.

    Returns:
        Array: Modified value array of w.
    """

    N = len(x)

    y = np.zeros_like(d)
    e = np.zeros_like(d)

    # w_delta: 係数行列wの更新量
    w_delta = np.zeros_like(w)

    for k in range(N):
        y[k] = np.dot(w.T, x[k])
        e[k] = d[k] - y[k]
        # 2 * J = e ** 2 - sum(w[i] ** 2 for i in range(N))
        diff_J_for_w_ = e[k] * x[k]
        w_delta = mu / (np.dot(x[k], x[k]) + lambda_) * diff_J_for_w_

    return w_delta
