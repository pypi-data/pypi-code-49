from fastcore.all import *

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

pd.set_option('display.max_rows', 999)
pd.set_option('precision', 3)


import hdf5storage

import matplotlib.pyplot as plt

#typing
from typing import Dict, Union, Callable, Optional, Tuple

Number = Union[float, int]
File = Union[Path, str]
All = slice(None)