from typing import Callable, Dict, Union, Tuple

import numpy as np
from nptyping import Array

from ..method import lms, nlms


class Method:
    methods: Dict[str, Callable] = {
        "lms": lms,
        "nlms": nlms,
    }


def init_w(method: str, shape: int) -> Array:
    res: Array[float, shape[0], shape[1]]
    if method == "random":
        res = np.random.normal(0, 0.5, shape, dtype="float64")
    elif method == "zeros":
        res = np.zeros(shape, dtype="float64")
    elif method == "unit":
        res = np.zeros(shape, dtype="float64")
        res[0] = 1.0
    return res
