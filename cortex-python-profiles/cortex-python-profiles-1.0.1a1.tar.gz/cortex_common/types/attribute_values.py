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
import json
import traceback
import warnings
from functools import total_ordering
from typing import List, Union, Optional, Tuple, Type, Any

import attr
import numpy as np
import pydash
from attr import attrs, fields
from cortex_common.constants import ATTRIBUTE_VALUES as ATTR_VALS, DESCRIPTIONS as DESC
from cortex_common.types import EntityEvent, EntityRelationshipEvent, ProfileRelationshipEvent, ProfileValueTypeSummary, \
    ProfileLink
from cortex_common.utils import describableAttrib, dicts_to_classes, str_or_context, \
    converter_for_union_type, union_type_validator, dict_to_attr_class, attr_class_to_dict, numpy_type_to_python_type, \
    not_none_validator, datetime_to_iso_converter

# Bool is getting consumes by the union since it is a subclass of int ...

Void: Type[Any] = type(None)
PrimitiveJSONUnionType: Type[Any] = Union[str, int, float, bool, Void]
PrimitiveJSONTypes: Type[Any] = PrimitiveJSONUnionType.__args__
PrimitiveJSONTypeHandlers = pydash.merge(dict(zip(PrimitiveJSONTypes[:-1], PrimitiveJSONTypes[:-1])), {Void: lambda x: None})  # type: ignore

ObjectJSONUnionType: Type[Any] = Union[dict, Void]  # type: ignore
ObjectJSONTypes: Type[Any] = ObjectJSONUnionType.__args__  # type: ignore
ObjectJSONTypeHandlers = pydash.merge(dict(zip(ObjectJSONTypes[:-1], ObjectJSONTypes[:-1])), {Void: lambda x: None})  # type: ignore

ListJSONUnionType: Type[Any] = Union[list, Void]  # type: ignore
ListJSONTypes: Type[Any] = ListJSONUnionType.__args__  # type: ignore
ListJSONTypeHandlers = pydash.merge(dict(zip(ListJSONTypes[:-1], ListJSONTypes[:-1])), {Void: lambda x: None})  # type: ignore

JSONUnionTypes: Type[Any] = Union[str, int, float, bool, Void, dict, list]  # type: ignore

# - [ ] Do we put versions on everything ... even it its meant to be nested? or only stuff saved in db?
# Rip version out ... not being used ...
# Make a test to ensure that value is properly set when things are intiilaized ...


__all__ = [
    'StringAttributeValue',
    'NumberAttributeValue',
    'BooleanAttributeValue',
    "WeightAttributeValue",
    "DatetimeAttributeValue",
    "StatisticalSummaryAttributeValue",
    'PercentileAttributeValue',
    'PercentageAttributeValue',
    'TotalAttributeValue',
    'EntityAttributeValue',
    'ListAttributeValue',
    "Dimension",
    'DimensionalAttributeValue',
    'EntityRelationshipAttributeValue',
    'ProfileRelationshipAttributeValue',
    # Depricated ....,
    'CounterAttributeValue',
    # Type Aliases ............
    'ProfileAttributeValueTypes',
    "ProfileAttributeValue",
    "ListOfProfileAttributeValues",
]


class BaseAttributeValue(object):
    """
    Interface Attribute Values Need to Adhere to ...
    Listing required properties ... for all attribute values ...
    """

    @classmethod
    def detailed_schema_type(cls, *args, **kwargs) -> ProfileValueTypeSummary:
        return ProfileValueTypeSummary(  # type: ignore # wait until attr support ...
            outerType=fields(cls).context.default,
            innerTypes=[]
        )

    def __iter__(self):
        return iter(attr_class_to_dict(self, hide_internal_attributes=True).items())


# Does dimensionId now need to be a union of profileLink, string ...
@attrs(frozen=True)
class Dimension(object):
    """
    Representing a single dimension in a dimensional attribute ...
    """
    dimensionId = describableAttrib(
        type=Union[str, ProfileLink],
        converter=converter_for_union_type(None, {str:str, ProfileLink: lambda x: x, dict: lambda x: dict_to_attr_class(x, ProfileLink)}),
        validator=[union_type_validator(Union[str, ProfileLink]), not_none_validator],
        description="What entity does this dimension represent?"
    )
    dimensionValue = describableAttrib(type=Union[str, list, dict, int, bool, float], description="What is the value of this dimension?")


@attrs(frozen=True)
class StringAttributeValue(BaseAttributeValue):
    """
    Attributes that have an arbitrary string as their value
    """
    value = describableAttrib(
        type=str,
        default="",
        validator=[attr.validators.instance_of(str), not_none_validator],
        description="What is the value of the string itself?"
    )
    weight = describableAttrib(type=Optional[float], default=None, description=DESC.WEIGHT)
    context = describableAttrib(type=str, default=ATTR_VALS.STRING_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)


@attrs(frozen=True)
class BooleanAttributeValue(BaseAttributeValue):
    """
    Attributes that have an arbitrary boolean as their value
    """
    value = describableAttrib(type=Optional[bool], default=None, description="What is the value of the boolean itself?")
    weight = describableAttrib(type=Optional[float], default=None, description=DESC.WEIGHT)
    context = describableAttrib(type=str, default=ATTR_VALS.BOOLEAN_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)


@attrs(frozen=True)
class EntityAttributeValue(BaseAttributeValue):
    """
    Capturing an raw EntityEvent as a profile attribute ...
    """
    value = describableAttrib(
        type=EntityEvent,
        converter=lambda x: dict_to_attr_class(x, EntityEvent),
        validator=[attr.validators.instance_of(EntityEvent), not_none_validator],
        description="What are the properties of the entity?"
    )
    context = describableAttrib(type=str, default=ATTR_VALS.ENTITY_ATTRIBUTE_VALUE, description=DESC.CONTEXT)


@attrs(frozen=True)
class ListAttributeValue(BaseAttributeValue):
    """
    Attributes that have an arbitrary JSON List / Array as their value.
    """
    value = describableAttrib(
        type=ListJSONUnionType,
        validator=[union_type_validator(ListJSONUnionType), not_none_validator],
        factory=list,
        converter=converter_for_union_type(ListJSONUnionType, ListJSONTypeHandlers),
        description="What is the value of the object itself?")
    context = describableAttrib(type=str, default=ATTR_VALS.LIST_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)

    @classmethod
    def detailed_schema_type(cls, typeOfItems:Optional[Union[str,type]]=None) -> ProfileValueTypeSummary:  #type:ignore
        return ProfileValueTypeSummary(  # type: ignore # waiting for attr support ...
            outerType = fields(cls).context.default,
            innerTypes = [] if typeOfItems is None else [
                ProfileValueTypeSummary(outerType=str_or_context(typeOfItems))  # type: ignore # waiting for attr support ...
            ]
        )


@attrs(frozen=True)
@total_ordering
class BaseNumericAttributeValue(BaseAttributeValue):
    """
    Representing the content of a numeric attribute ...
    # TODO ... figure out how ineritance can come back into the mix ... if all the unit id stuff lives in here ...
    # Then we cnat instantiate Number, Total, ... with just a number ...
    """

    def with_unit(self, unitId:Optional[str], unitContext:Optional[str], unitTitle:Optional[str], unitIsPrefix:Optional[bool]):
        """
        Enriches numeric attribute with unit
        :param unitId:
        :param unitContext:
        :param unitTitle:
        :param unitIsPrefix:
        :return:
        """
        return attr.evolve(  #type:ignore
            self,
            unitId=unitId,
            unitContext=unitContext,
            unitTitle=unitTitle,
            unitIsPrefix=unitIsPrefix,
        )

    def __eq__(self, other):  #type:ignore
        if other is None:
            return False
        return (self.value == other.value)

    def __ne__(self, other):  #type:ignore
        return not (self.value == other.value)

    def __lt__(self, other):  #type:ignore
        return self.value < other.value


@attrs(frozen=True)
class NumberAttributeValue(BaseNumericAttributeValue):
    """
    Representing the content of a numeric attribute as a measuring unit ...
    """
    value = describableAttrib(type=Union[int, float], default=0, description="What numeric value is captured by this attribute value?")
    weight = describableAttrib(type=Union[int, float], default=None, description=DESC.WEIGHT)
    unitId = describableAttrib(type=Optional[str], default=None, description="What is the unique id of the unit? i.e USD, GBP, %, ...")
    unitContext = describableAttrib(type=Optional[str], default=None, description="What type of unit is this? i.e currency, population of country, ...")
    unitTitle = describableAttrib(type=Optional[str], default=None, description="What is the symbol desired to represent the unit?")
    unitIsPrefix = describableAttrib(type=Optional[bool], default=None, description="Should the symbol be before or after the unit?")
    context = describableAttrib(type=str, default=ATTR_VALS.NUMBER_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)


@attrs(frozen=True)
class PercentileAttributeValue(BaseNumericAttributeValue):
    """
    Representing the content of a percentile attribute ...
    """
    value = describableAttrib(type=float, default=0, description="What is the numeric value of the percentile?")
    weight = describableAttrib(type=Union[int, float], default=None, description=DESC.WEIGHT)
    unitId = describableAttrib(type=Optional[str], default=None, description="What is the unique id of the unit? i.e USD, GBP, %, ...")
    unitContext = describableAttrib(type=Optional[str], default=None, description="What type of unit is this? i.e currency, population of country, ...")
    unitTitle = describableAttrib(type=Optional[str], default=None, description="What is the symbol desired to represent the unit?")
    unitIsPrefix = describableAttrib(type=Optional[bool], default=None, description="Should the symbol be before or after the unit?")
    context = describableAttrib(type=str, default=ATTR_VALS.PERCENTILE_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)


@attrs(frozen=True)
class PercentageAttributeValue(BaseNumericAttributeValue):
    """
    Representing the content of a percentage attribute ...
    """
    value = describableAttrib(type=float, default=0, description="What numeric value of the percentage?")
    weight = describableAttrib(type=Union[int, float], default=None, description=DESC.WEIGHT)
    unitId = describableAttrib(type=Optional[str], default=None, description="What is the unique id of the unit? i.e USD, GBP, %, ...")
    unitContext = describableAttrib(type=Optional[str], default=None, description="What type of unit is this? i.e currency, population of country, ...")
    unitTitle = describableAttrib(type=Optional[str], default=None, description="What is the symbol desired to represent the unit?")
    unitIsPrefix = describableAttrib(type=Optional[bool], default=None, description="Should the symbol be before or after the unit?")
    context = describableAttrib(type=str, default=ATTR_VALS.PERCENTAGE_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)


@attrs(frozen=True)
class TotalAttributeValue(BaseNumericAttributeValue):
    """
    Representing the content of a total attribute ...
    """
    value = describableAttrib(type=float, default=0.0, description="What is the current total?")
    weight = describableAttrib(type=Union[int, float], default=None, description=DESC.WEIGHT)
    unitId = describableAttrib(type=Optional[str], default=None, description="What is the unique id of the unit? i.e USD, GBP, %, ...")
    unitContext = describableAttrib(type=Optional[str], default=None, description="What type of unit is this? i.e currency, population of country, ...")
    unitTitle = describableAttrib(type=Optional[str], default=None, description="What is the symbol desired to represent the unit?")
    unitIsPrefix = describableAttrib(type=Optional[bool], default=None, description="Should the symbol be before or after the unit?")
    context = describableAttrib(type=str, default=ATTR_VALS.TOTAL_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)


@attrs(frozen=True)
class WeightAttributeValue(BaseAttributeValue):
    """
    Attributes that captures a weighted value.
    """
    value = describableAttrib(type=float, description=DESC.WEIGHT)
    weight = describableAttrib(type=Optional[float], default=None, description=DESC.WEIGHT)
    context = describableAttrib(type=str, default=ATTR_VALS.WEIGHT_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)


@attrs(frozen=True)
class StatisticalSummaryValue(BaseAttributeValue):
    """
    How do we statistically summarize a list of numbers?
    """
    datapoints = describableAttrib(type=int, default=0, description="How many datapoints were considered?")
    min = describableAttrib(type=Optional[float], default=None, description="What is the minimum value considered in the data points?")
    max = describableAttrib(type=Optional[float], default=None, description="What is the maximum value considered in the data points?")
    average = describableAttrib(type=Optional[float], default=None, description="What is the average of the data points?")
    stddev = describableAttrib(type=Optional[float], default=None, description="What is the std deviation of the data points?")


@attrs(frozen=True)
class StatisticalSummaryAttributeValue(BaseAttributeValue):
    """
    Representing the content of a percentage attribute ...
    """
    value = describableAttrib(
        type=StatisticalSummaryValue,
        converter=lambda x: dict_to_attr_class(x, StatisticalSummaryValue),
        description="What is the statistical summary for a given range of data?"
    )
    context = describableAttrib(type=str, default=ATTR_VALS.STATISTICAL_SUMMARY_ATTRIBUTE_VALUE, description=DESC.CONTEXT)

    @staticmethod
    def fromListOfValues(values:List[Union[int, float]]) -> 'StatisticalSummaryAttributeValue':
        return StatisticalSummaryAttributeValue(  # type: ignore # waiting for attr support ...
            value=StatisticalSummaryValue(  # type: ignore # waiting for attr support ...
                datapoints=numpy_type_to_python_type(np.size(values)),
                min=numpy_type_to_python_type(np.min(values)),
                max=numpy_type_to_python_type(np.max(values)),
                average=numpy_type_to_python_type(np.average(values)),
                stddev=numpy_type_to_python_type(np.std(values)),
            )
        )


@attrs(frozen=True)
class DatetimeAttributeValue(BaseAttributeValue):
    """
    Attributes that captures a weighted value.
    """
    value = describableAttrib(
        type=str,
        converter=datetime_to_iso_converter,
        description=DESC.WEIGHT
    )
    weight = describableAttrib(type=Optional[float], default=None, description=DESC.WEIGHT)
    context = describableAttrib(type=str, default=ATTR_VALS.DATETIME_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)


@attrs(frozen=True)
class EntityRelationshipAttributeValue(BaseAttributeValue):
    """
    Attributes that have an arbitrary string as their value
    """
    value = describableAttrib(
        type=EntityRelationshipEvent,
        converter=lambda x: dict_to_attr_class(x, EntityRelationshipEvent),
        validator=[attr.validators.instance_of(EntityRelationshipEvent), not_none_validator],
        description="What is the value of the entity relationship itself?"
    )
    weight = describableAttrib(type=Optional[float], default=None, description=DESC.WEIGHT)
    context = describableAttrib(type=str, default=ATTR_VALS.ENTITY_REL_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)


@attrs(frozen=True)
class ProfileRelationshipAttributeValue(EntityRelationshipAttributeValue):
    """
    Attributes that have an arbitrary string as their value
    """
    value = describableAttrib(
        type=ProfileRelationshipEvent,
        converter=lambda x: dict_to_attr_class(x, ProfileRelationshipEvent),
        validator=[attr.validators.instance_of(ProfileRelationshipEvent), not_none_validator],
        description="What is the value of the profile relationship itself?"
    )
    weight = describableAttrib(type=Optional[float], default=None, description=DESC.WEIGHT)
    context = describableAttrib(type=str, default=ATTR_VALS.PROFILE_REL_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)


@attrs(frozen=True)
class CounterAttributeValue(BaseNumericAttributeValue):
    """
    Depreciated Counter ...
    """
    value = describableAttrib(type=int, default=0, description="What is the current count?")
    weight = describableAttrib(type=Optional[Union[int, float]], default=None, description=DESC.WEIGHT)
    unitId = describableAttrib(type=Optional[str], default=None, description="What is the unique id of the unit? i.e USD, GBP, %, ...")
    unitContext = describableAttrib(type=Optional[str], default=None, description="What type of unit is this? i.e currency, population of country, ...")
    unitTitle = describableAttrib(type=Optional[str], default=None, description="What is the symbol desired to represent the unit?")
    unitIsPrefix = describableAttrib(type=Optional[bool], default=None, description="Should the symbol be before or after the unit?")
    context = describableAttrib(type=str, default=ATTR_VALS.COUNTER_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)

    def __attrs_post_init__(self):
        """
        Post init to provide deprication warning ...
        :return:
        """
        warnings.warn(f"deprecated_in={'1.0.0'}, details={'Use TotalAttributeValue instead.'}")


@attrs(frozen=True)
class IntegerAttributeValue(NumberAttributeValue):
    """
    Depreciated Integer ...
    """
    context = describableAttrib(type=str, default=ATTR_VALS.INTEGER_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)

    def __attrs_post_init__(self):
        """
        Post init to provide deprication warning ...
        :return:
        """
        warnings.warn(f"deprecated_in={'1.0.0'}, details={'Use NumberAttributeValue instead.'}")


@attrs(frozen=True)
class DecimalAttributeValue(NumberAttributeValue):
    """
    Depreciated Decimal ...
    """

    context = describableAttrib(type=str, default=ATTR_VALS.DECIMAL_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)

    def __attrs_post_init__(self):
        """
        Post init to provide deprication warning ...
        :return:
        """
        warnings.warn(f"deprecated_in={'1.0.0'}, details={'Use NumberAttributeValue instead.'}")


valid_dimension_ids = Union[StringAttributeValue, ProfileLink]
valid_dimension_values = Union[CounterAttributeValue, TotalAttributeValue, BooleanAttributeValue]


@attrs(frozen=True)
class DimensionalAttributeValue(BaseAttributeValue):
    """
    Representing the content of a 2-dimensional attribute.
    """
    value = describableAttrib(
        type=List[Dimension],
        converter=lambda x: dicts_to_classes(x, Dimension),
        description="What are the different dimensions captured in the attribute value?"
    )
    contextOfDimension = describableAttrib(
        type=Optional[str],
        converter=lambda x: x if isinstance(type(None), str) else str_or_context(x),
        default=None,
        description="What type are the dimensions?")
    contextOfDimensionValue = describableAttrib(
        type=Optional[str],
        converter=lambda x: x if isinstance(x, (type(None), str)) else str_or_context(x),
        default=None,
        description="What type are the values associated with the dimension?"
    )
    context = describableAttrib(type=str, default=ATTR_VALS.DIMENSIONAL_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)

    @classmethod
    def detailed_schema_type(cls,  #type:ignore
                             firstDimensionType:Optional[Union[str,Type[valid_dimension_ids]]]=StringAttributeValue,
                             secondDimensionType:Optional[Union[str,Type[valid_dimension_values]]]=CounterAttributeValue,
                             ) -> ProfileValueTypeSummary:
        """
        What is the value type def for this instance?
        :param firstDimensionType:
        :param secondDimensionType:
        :return:
        """
        return ProfileValueTypeSummary(  # type: ignore # waiting for attr support ...
            outerType = fields(cls).context.default,
            innerTypes = [
                ProfileValueTypeSummary(outerType=str_or_context(firstDimensionType)),  # type: ignore # waiting for attr support ...
                ProfileValueTypeSummary(outerType=str_or_context(secondDimensionType))  # type: ignore # waiting for attr support ...
            ]
        )


ProfileAttributeValue = Union[
    StringAttributeValue,
    BooleanAttributeValue,
    EntityAttributeValue,
    ListAttributeValue,

    PercentileAttributeValue,
    PercentageAttributeValue,
    StatisticalSummaryAttributeValue,
    NumberAttributeValue,
    TotalAttributeValue,
    CounterAttributeValue,
    DecimalAttributeValue,
    IntegerAttributeValue,

    WeightAttributeValue,

    DimensionalAttributeValue,
    DatetimeAttributeValue,
    EntityRelationshipAttributeValue,
    ProfileRelationshipAttributeValue,
    # Depricated ...

]


# MyPy Bug ... Cant use variable inside union ... it throws things off!
ListOfProfileAttributeValues = Union[
    List[StringAttributeValue],
    List[BooleanAttributeValue],
    List[EntityAttributeValue],
    List[ListAttributeValue],
    List[PercentileAttributeValue],
    List[PercentageAttributeValue],
    List[TotalAttributeValue],
    List[DimensionalAttributeValue],
    List[WeightAttributeValue],
    List[StatisticalSummaryAttributeValue],
    List[DatetimeAttributeValue],
    List[EntityRelationshipAttributeValue],
    List[ProfileRelationshipAttributeValue],
    # Depricated ..]
    List[CounterAttributeValue],
    List[DecimalAttributeValue],
    List[IntegerAttributeValue],
]

ProfileAttributeValueTypes: Tuple[Any, ...] = ProfileAttributeValue.__args__ # type: ignore


def load_profile_attribute_value_from_dict(d:dict) -> Optional[BaseAttributeValue]:
    """
    Uses the context to load the appropriate profile attribute value type from a dict.
    :param d:
    :return:
    """
    if d is None:
        return None
    context_to_value_type = {
        attr.fields(x).context.default: x
        for x in ProfileAttributeValueTypes
    }
    value_type_to_use = context_to_value_type.get(d.get("context"), None)
    if value_type_to_use is None:
        print("Unrecognized Attribute Value Type: {}".format(d.get("context")))
        return None
    try:
        return dict_to_attr_class(d, value_type_to_use)
    except TypeError as e:
        print(e)
        print(traceback.format_exc())
        print(traceback.format_tb(e.__traceback__))
        print(f"Could not load profile attribute value from dict: {json.dumps(d)}")
        raise e


# ------------------------------------------------------------------------------


# - [ ] TODO ... should we have a daily counter attribute value ...
# - [ ] TODO should we bring add insight attribute vals back ... so we can show insights as attributes?

# class PlacementAttributeContent 1st, 2nd, 3rd ...
# class {Rank/Score}AttributeContent

#  ... This is to support things like saving insights into profiles ... and bookmarking for example the most recently presented insight to the user ...
# This will give us a complete story as to the insights being presented to the user ...
# Getting a timeline of the presented insights to a user would be valuable!
# We could also link attributes to insights this way! (Profile Attribute Links!)
# @attrs(frozen=True)
# class InsightAttributeValue(BaseAttributeValue):
#     """
#     Representing a concept ...
#     """
#     value = describableAttrib(type=Insight, converter=lambda x: converter_for_classes(x, Insight), description="What is the insight itself?")
#     context = describableAttrib(type=str, default=CONTEXTS.INSIGHT_ATTRIBUTE_VALUE, description=CONTEXT_DESCRIPTION)
#     summary = describableAttrib(type=str, description=ATTRIBUTE_SUMMARY_DESCRIPTION)
#
#     @summary.default
#     def summarize(self):
#         return "Insight<type={},id={}>\"".format(self.value.insightType, self.value.id)

# - [ ] TODO ... are we getting rid of counter, total?
# @attrs(frozen=True)
# class CounterAttributeValue(NumericWithUnitValue):
#     """
#     Representing the content of a counter attribute ...
#     """
#     value = describableAttrib(type=int, default=0, description="What is the numeric value of the current total?")
#     context = describableAttrib(type=str, default=ATTR_VALS.COUNTER_PROFILE_ATTRIBUTE_VALUE, description=DESC.CONTEXT)
#     summary = describableAttrib(type=str, description=DESC.ATTRIBUTE_SUMMARY)
#
#     @summary.default  # type: ignore # waiting until attr support ...
#     def summarize(self):
#         return "{}{}{}".format(
#             ("{}".format(self.unitTitle) if (self.unitIsPrefix and self.unitTitle) else ""),
#             ("{}".format(self.value)),
#             ("{}".format(self.unitTitle) if (self.unitTitle and not self.unitIsPrefix) else "")
#         )


if __name__ == '__main__':
    pass
    # import datetime, arrow
    # print(DatetimeAttributeValue(datetime.datetime.now()))  #type:ignore
    # print(DatetimeAttributeValue(arrow.utcnow().datetime))  #type:ignore
    # print(
    #     Dimension(  #type:ignore
    #         dimensionId=ProfileLink(  #type:ignore
    #             profileId="profileId",
    #             schemaId="schemaId",
    #         ),
    #         dimensionValue="123"
    #     )
    # )
    # print(
    #     Dimension(  #type:ignore
    #         dimensionId="123",
    #         dimensionValue="123"
    #     )
    # )
    # print(
    #     Dimension(  #type:ignore
    #         dimensionId=123,
    #         dimensionValue="123"
    #     )
    # )
