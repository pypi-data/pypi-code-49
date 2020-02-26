"""
Static types for raw JSON objects.
"""
from typing import Dict, Union, List, Tuple

# The type of a raw JSON object in Python-land
RawJSONObject = Dict[str, 'RawJSONElement']

# The type of a raw JSON array in Python-land
RawJSONArray = Union[List['RawJSONElement'], Tuple['RawJSONElement', ...]]

# The type of a raw JSON string in Python-land
RawJSONString = str

# The type of an arbitrary raw JSON number in Python-land
RawJSONNumber = Union[int, float]

# The type of a raw JSON bool in Python-land
RawJSONBool = bool

# The type of a raw JSON null in Python-land
RawJSONNull = None

# The type of a raw JSON primitive
RawJSONPrimitive = Union[RawJSONString, RawJSONNumber, RawJSONBool, RawJSONNull]

# The type of an arbitrary raw JSON element in Python-land
RawJSONElement = \
    Union[
        RawJSONObject,  # Object
        RawJSONArray,  # Array
        RawJSONPrimitive  # Any primitive
    ]
