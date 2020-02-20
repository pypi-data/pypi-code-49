"""
Package for working with "raw" JSON. Raw JSON is JSON represented
as Python primitives, as defined by the built-in Python "json" module.

The mapping from JSON types to Python types is as follows:

JSON                Python
====                ======
Object      <->     dict
Array       <->     list, tuple
String      <->     str
Number      <->     int, float
Boolean     <->     bool
Null        <->     None
"""
from ._deep_copy import deep_copy
from ._dynamic import (
    is_raw_json_object,
    is_raw_json_array,
    is_raw_json_string,
    is_raw_json_number,
    is_raw_json_bool,
    is_raw_json_null,
    is_raw_json_primitive,
    is_raw_json_element,
    is_raw_json_element_type
)
from ._typing import (
    RawJSONObject,
    RawJSONArray,
    RawJSONString,
    RawJSONNumber,
    RawJSONBool,
    RawJSONNull,
    RawJSONPrimitive,
    RawJSONElement
)
