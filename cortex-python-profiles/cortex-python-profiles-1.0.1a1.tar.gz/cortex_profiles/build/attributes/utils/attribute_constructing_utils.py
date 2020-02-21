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

import uuid
from typing import Callable
from typing import List, Optional, Any, Union, cast

import pandas as pd
import pydash

from cortex_common.types.attribute_values import DimensionalAttributeValue, Dimension, TotalAttributeValue, \
    ProfileAttributeValue
from cortex_common.types.attributes import ObservedProfileAttribute, ProfileAttribute, ProfileAttributeType, \
    ListOfAttributes
from cortex_common.utils import str_or_context
from cortex_common.utils.dataframe_utils import df_to_records, df_to_tuples
from cortex_common.utils.object_utils import head
from cortex_common.utils.time_utils import utc_timestamp


def derive_attributes_from_df(
        df:pd.DataFrame,
        attribute_key_pattern:str,
        attribute_class:type,
        attribute_value_constructor:Callable[[Union[pd.DataFrame, dict]], ProfileAttributeValue],
        additional_identifiers:Optional[dict]=None
    ) -> List[ProfileAttribute]:
    """
    Factory method to help create attributes from a df.
    :param df:
    :param attribute_key_pattern:
    :param attribute_class:
    :param attribute_value_constructor:
    :param additional_identifiers:
    :return:
    """
    return [
        attribute_class(
            id=str(uuid.uuid4()),
            attributeKey=attribute_key_pattern.format(**r),
            profileId=str(r["profileId"]),
            createdAt=utc_timestamp(),
            attributeValue=attribute_value_constructor(r)  #type:ignore
        )
        for r in map(lambda x: pydash.merge(additional_identifiers or {}, x), df_to_records(df))
    ]


def _derive_attributes_from_groups_in_df(
        grouped_df:pd.DataFrame,
        group_id_keys:List[str],
        group_id_values:List[Any],
        attribute_key_pattern:str,
        attribute_value_constructor:Callable[[pd.DataFrame, dict], ProfileAttributeValue],
        attribute_class:type,
        additional_identifiers:Optional[dict]=None,
        column_profileId:str="profileId",
        column_profileType:str="profileType"
    ) -> Optional[ProfileAttributeType]:
    """
    Internal helper method to help create attributes from groupings of records in a df.
    :param grouped_df:
    :param group_id_keys:
    :param group_id_values:
    :param attribute_key_pattern:
    :param attribute_value_constructor:
    :param attribute_class:
    :param additional_identifiers:
    :param column_profileId:
    :param column_profileType:
    :return:
    """
    if grouped_df.empty:
        return None
    identifier = dict(zip(group_id_keys, group_id_values))
    identifier = identifier if not additional_identifiers else pydash.merge(identifier, additional_identifiers)
    assert (column_profileId in grouped_df.columns or column_profileId in identifier), f"{column_profileId} must be in df or identifiers ..."
    profileType = str(identifier[column_profileType]) if (column_profileType in grouped_df.columns or column_profileType in identifier) else None
    return attribute_class(
        id=str(uuid.uuid4()),
        attributeKey=attribute_key_pattern.format(**identifier),
        profileId=str(identifier[column_profileId]),
        profileType=profileType,
        createdAt=utc_timestamp(),
        attributeValue=attribute_value_constructor(grouped_df, identifier),
    )


def derive_attributes_from_grouped_df(
        grouped_df:pd.DataFrame,
        attribute_identifiers: List[str],
        attribute_key_pattern:str,
        attribute_class:type,
        attribute_value_constructor:Callable[[pd.DataFrame, dict], ProfileAttributeValue],
        **kwargs,
    ) -> ListOfAttributes:
    """
    Builds attributes by grouping dataframes by the :param attribute_identifiers: and using each of the grouped
        dataframes to constuct the appropriate attribute value.

    :param df: The dataframe to generate dimensional attributes from
    :param attribute_identifiers: The list of identifiers to group by when generating dimensional attributes from the dataframe ...
    :param attribute_key_pattern: The string template of the name of the attribute key that gets populated form the
                                  unique identifier of the grouping that gets transformed into the dimensional attribute.
    :param attribute_class: The class to use for the attribute ...
    :param attribute_value_constructor: The constructor to construct the attribute value from the grouped dataframe.
    :param additional_identifiers:
    :return:
    """
    return cast(
        ListOfAttributes,
        [
            x for x in (
                _derive_attributes_from_groups_in_df(
                    gdf,
                    attribute_identifiers,
                    list(gid),
                    attribute_key_pattern,
                    attribute_value_constructor,
                    attribute_class,
                    **kwargs
                )
                for gid, gdf in grouped_df
            )
            if x is not None
        ]
    )


def derive_attributes_from_groups_in_df(
        df:pd.DataFrame,
        attribute_identifiers:List[str],
        attribute_key_pattern:str,
        attribute_class:type,
        attribute_value_constructor:Callable[[pd.DataFrame, dict], ProfileAttributeValue],
        **kwargs
    ) -> ListOfAttributes:
    """
    Builds attributes by grouping dataframes by the :param attribute_identifiers: and using each of the grouped
        dataframes to constuct the appropriate attribute value.

    :param df: The dataframe to generate dimensional attributes from
    :param attribute_identifiers: The list of identifiers to group by when generating dimensional attributes from the dataframe ...
    :param attribute_key_pattern: The string template of the name of the attribute key that gets populated form the
                                  unique identifier of the grouping that gets transformed into the dimensional attribute.
    :param attribute_class: The class to use for the attribute ...
    :param attribute_value_constructor: The constructor to construct the attribute value from the grouped dataframe.
    :param additional_identifiers:
    :return:
    """
    return derive_attributes_from_grouped_df(
        df.groupby(attribute_identifiers, as_index=False),
        attribute_identifiers,
        attribute_key_pattern,
        attribute_class,
        attribute_value_constructor,
        **kwargs
    )


def simple_dimensional_attribute_value_constructor(
        context_of_dimension_id:Union[type, str],
        context_of_dimension_value:Union[type, str],
        column_for_dimension_id:str,
        column_for_dimension_value:str,
        dimension_value_constructor:Optional[Callable]=None,
        dimension_id_constructor:Optional[Callable]=None
    ):
    """
    Responsible for providing a constuctor that is capable of building a dimensional attribute value ...

    :param context_of_dimension_id: The context to use for the dimensionId.
    :param context_of_dimension_value: The context to use for the dimensionValue.
    :param column_for_dimension_id: The column from the group to use as the dimensionId.
    :param column_for_dimension_value: The column from the group to use as the dimensionValue.
    :return:
    """

    def attribute_value_factory_method(grouped_df:pd.DataFrame, identifiers:dict):
        """
        Constucts an Dimensional Attribute Value given a grouped dataframe and the identifiers of the group
        :param grouped_df:
        :param identifiers:
        :return:
        """
        return DimensionalAttributeValue(  #type:ignore
            contextOfDimension=str_or_context(context_of_dimension_id).format(**identifiers),  #type:ignore
            contextOfDimensionValue=str_or_context(context_of_dimension_value),
            value=list(sorted(
                [
                    Dimension(  #type:ignore
                        dimensionId=x if dimension_id_constructor is None else dimension_id_constructor(x),
                        dimensionValue=y if dimension_value_constructor is None else dimension_value_constructor(y)
                    )
                    for x, y in df_to_tuples(grouped_df, [column_for_dimension_id, column_for_dimension_value])
                ],
                key=lambda d: d.dimensionValue
            ))
        )
    return attribute_value_factory_method


def simple_counter_attribute_value_constructor(
        column_of_counter:str,
        attribute_value_class:Union[type, Callable]=TotalAttributeValue,
        counter_deriver=lambda column: sum(column)
    ):
    """
    Responsible for providing a constructor that is capable of building a counter attribute from a grouped dataframe ...

    :param column_of_counter:
    :param attribute_class:
    :return:
    """
    def attribute_value_factory_method(grouped_df:pd.DataFrame, identifiers:dict):
        """
        Constructs an Dimensional Attribute Value given a grouped DataFrame and the identifiers of the group
        :param grouped_df:
        :param identifiers:
        :return:
        """
        value = counter_deriver(grouped_df[column_of_counter])
        return attribute_value_class(value=value) if isinstance(attribute_value_class, type) else attribute_value_class(value)
    return attribute_value_factory_method


def simple_attribute_value_selector_constructor(
        column_to_select_value_from:str,
        attribute_value_class:Union[type, Callable]=TotalAttributeValue
    ):
    """
    Responsible for providing a constructor that is capable of building a counter attribute from a grouped dataframe ...

    :param column_of_counter:
    :param attribute_class:
    :return:
    """
    def attribute_value_factory_method(grouped_df:pd.DataFrame, identifiers:dict):
        """
        Constructs an Dimensional Attribute Value given a grouped DataFrame and the identifiers of the group
        :param grouped_df:
        :param identifiers:
        :return:
        """
        value = head(list(grouped_df[column_to_select_value_from]))
        return attribute_value_class(value=value) if isinstance(attribute_value_class, type) else attribute_value_class(value)
    return attribute_value_factory_method


def derive_quantile_config_for_column(df:pd.DataFrame, column_name:str, quantile_config:dict) -> dict:
    """
    Determines all the values in the different quantiles ...???
    :param df:
    :param column_name:
    :param quantile_config:
    :return:
    """
    return {
        key: list(map(lambda x: df[column_name].quantile(x), values)) for key, values in quantile_config.items()
    }


def determine_bucket_from_quartile_config(value:object, config:dict) -> str:
    """
    Buckets quantile values???
    :param value:
    :param config:
    :return:
    """
    # Taking tail for values on the edge to be more generous
    return [key for key, values in config.items() if (value >= values[0] and value <= values[1])][-1]


def high_med_low_bucket(df:pd.DataFrame, column_name:str, quantile_config:dict) -> pd.Series:
    """
    ???
    :param df:
    :param column_name:
    :param quantile_config:
    :return:
    """
    return df[column_name].map(lambda x: determine_bucket_from_quartile_config(x, quantile_config))


if __name__ == '__main__':
    # print([
    #     (gid, list(gdf["a"]), list(gdf["b"]))
    #     for gid, gdf in pd.DataFrame([{"a":1, "b": 2}]).groupby(["a", "b"])
    # ])

    df = pd.DataFrame([
        {"profileId": "1", "interaction": "like"},
        {"profileId": "1", "interaction": "like"},
        {"profileId": "1", "interaction": "dislike"},
        {"profileId": "1", "interaction": "like"}
    ])

    for attribute in derive_attributes_from_groups_in_df(
        df,
        ["profileId", "interaction"],
        "countOf.interaction[{interaction}]",
        ObservedProfileAttribute,
        lambda grouped_df, identifiers: TotalAttributeValue(value=len(list(grouped_df["interaction"])))  #type:ignore
    ):
        print(attribute)

