"""
Copyright 2019 Cognitive Scale, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from typing import List, Optional, Union, Callable, Type, cast

import pandas as pd
from cortex_common.types import NumberAttributeValue, StringAttributeValue, \
    BooleanAttributeValue, ListAttributeValue, DimensionalAttributeValue, Dimension, DeclaredProfileAttribute, \
    ProfileAttributeValue
from cortex_common.utils import df_to_records, unique_id, utc_timestamp, str_or_context

PrimitiveAttributeValues = Union[
    NumberAttributeValue, StringAttributeValue,
    BooleanAttributeValue, ListAttributeValue, StringAttributeValue
]


def dimensional_from_dict(d:dict,
                          contextOfDimension:Union[str, Type[ProfileAttributeValue]]=cast(Type[ProfileAttributeValue], StringAttributeValue),
                          contextOfDimensionValue:Union[str, Type[ProfileAttributeValue]]=cast(Type[ProfileAttributeValue], NumberAttributeValue),
                          # profile_link_type: Optional[str] = None,
                          # entity_link_type: Optional[str] = None,
                          key_modifier:Optional[Callable]=None,
                          value_modifier:Optional[Callable]=None) -> DimensionalAttributeValue:
    """
    Converts a dict into a dimensional attribute value
    :param d:
    :param contextOfDimension:
    :param contextOfDimensionValue:
    :param key_modifier:
    :param value_modifier:
    :return:
    """

    return DimensionalAttributeValue(  #type:ignore
        value=[
            Dimension(#type:ignore
                key_modifier(k) if key_modifier else k,
                value_modifier(v) if value_modifier else v
            )
            for k, v in d.items()
        ],
        contextOfDimension=str_or_context(contextOfDimension),
        contextOfDimensionValue=str_or_context(contextOfDimensionValue)
    )


def built_in_attribute_value_constructor(value:Union[int, float, str, bool, list]) -> PrimitiveAttributeValues:
    """
    Converts Primitive Values into Attribute Values.
    :param value:
    :return:
    """
    if isinstance(value, (float, int)):
        return NumberAttributeValue(value=value)  #type:ignore
    if isinstance(value, str):
        return StringAttributeValue(value=value)  #type:ignore
    if isinstance(value, bool):
        return BooleanAttributeValue(value=value)  #type:ignore
    if isinstance(value, list):
        return ListAttributeValue(value=value)  #type:ignore


def derive_declared_attributes_from_key_value_df(
        df:pd.DataFrame,
        profile_id_column:str="profileId",
        key_column:str="key",
        value_column:str="value",
        time_column:Optional[str]=None,
        attribute_value_constructor:Union[type, Callable]=built_in_attribute_value_constructor,
        profile_type:Optional[str]=None
    ) -> List[DeclaredProfileAttribute]:
    """
    Derives attributes from a dataframe that is structured as follows ....
    >>> import pandas as pd
    >>> df = pd.DataFrame([
    >>>    {"profileId": "p1", "key": "profile.name", "value": "Jack"},
    >>>    {"profileId": "p1", "key": "profile.age", "value": 25},
    >>>    {"profileId": "p2", "key": "profile.name", "value": "Jill"},
    >>>    {"profileId": "p2", "key": "profile.age", "value": 26},
    >>> ])

    :param df: The data frame with all of the attributes ...
    :param profile_id_column: The column with the profile Id
    :param key_column: The column containing the key we want to use as the attributeKey
    :param value_column: The column that contains the value of the attribute
    :param attribute_value_constructor: The constructor to construct the attribute Value Class with the Value column in the df.
    :return: List of Declared Attributes derived from the dataframe.
    """
    return [
        DeclaredProfileAttribute(  #type:ignore
            id=unique_id(),
            profileId=str(rec[profile_id_column]),
            profileType=profile_type,
            attributeKey=rec[key_column],
            createdAt=utc_timestamp() if time_column is None else rec[time_column],
            attributeValue=attribute_value_constructor(rec[value_column]),
        )
        for rec in df_to_records(df)
    ]


def derive_declared_attributes_from_value_only_df(
        declarations:pd.DataFrame,
        value_column:str,
        profile_id_column:str="profileId",
        key:Optional[str]=None,
        time_column:Optional[str]=None,
        attribute_value_constructor:Union[type, Callable]=built_in_attribute_value_constructor,
        profile_type:Optional[str]=None,
        profileType_column:Optional[str]=None,
    ) -> List[DeclaredProfileAttribute]:
    """
    Derives attributes from a dataframe that is structured as follows ....
    >>> import pandas as pd
    >>> df = pd.DataFrame([
    >>>     {"profileId": "p3", "name": "Adam", "age": 45},
    >>>     {"profileId": "p4", "name": "Eve", "age": 46},
    >>> ])

    :param df: The data frame with all of the attributes ...
    :param profile_id_column: The column with the profile Id
    :param key: The key to use as the attribute key ... if no key is specified, the name of the value column is used ...
    :param value_column: The column that contains the value of the attribute
    :param attribute_value_constructor: The constructor to construct the Attribute Value Class from the value
                                  stored in the value column for a particular attribute.
    :return: List of Declared Attributes derived from the dataframe.
    """
    return [
        DeclaredProfileAttribute(  #type:ignore
            id=unique_id(),
            profileId=str(rec[profile_id_column]),
            profileType=profile_type if profile_type is not None else rec.get(profileType_column),
            attributeKey=key.format(**rec) if key else value_column,
            attributeValue=attribute_value_constructor(rec[value_column]),
            createdAt=utc_timestamp() if time_column is None else rec[time_column],
    )
        for rec in df_to_records(declarations)
    ]


if __name__ == '__main__':
    # - [x] TODONE ... turn this into an example ...
    pass
