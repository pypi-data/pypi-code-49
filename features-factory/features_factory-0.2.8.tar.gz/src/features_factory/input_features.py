import datetime
from typing import Tuple

import pandas as pd

from features_factory.embedded_data import country_code_iso_alpha2_map
from features_factory.feature_archetype import FeatureArchetype
from features_factory.input_data_error import InputDataError


class InputFeature(FeatureArchetype):
    """
    Input features are features that should come directly from the data and do not need any modification.
    This class facilitate the creation of input features of several kind.
    """

    def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
        ie = InputDataError()
        if self.name() not in df.columns:
            ie.add_missing_column(self.name())
        return ie

    def get_dependencies(self, **kwargs) -> Tuple[FeatureArchetype]:
        return tuple()

    def generate(self, df: pd.DataFrame, **kwargs) -> pd.Series:
        return df[self._name]


class ProvidedInputFeatureWithControlOnNaN(InputFeature):
    """
    Input feature class that verifies that there are no NaN
    """

    def __init__(self, name: str, allow_nan: bool = False):
        super().__init__(name)
        self.allow_nan = allow_nan

    def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
        ie = super().verify_input(df)

        if not self.allow_nan:
            if self.name() not in ie.get_missing_columns():
                if df[self.name()].hasnans:
                    ie.add_column_with_nan(self.name())

        return ie


class SimpleTypeInputFeature(ProvidedInputFeatureWithControlOnNaN):
    """
    Input feature class that verifies that there are no NaN and that the column dtype corresponds to the type_name
    given at init time.
    """

    def __init__(self, name: str, type_name: str, allow_nan: bool = False):
        super().__init__(name, allow_nan)
        self.type_name = type_name

    def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
        ie = super().verify_input(df)
        if self.name() not in ie.get_missing_columns():
            if self.type_name not in df[self.name()].dtype.name and \
                    not (self.allow_nan and df[self.name()].hasnans):
                ie.add_column_with_wrong_format(self.name())
        return ie


class BoolInputFeature(SimpleTypeInputFeature):

    def __init__(self, name: str, allow_nan: bool = False):
        super().__init__(name, 'bool', allow_nan)


class IntInputFeature(SimpleTypeInputFeature):

    def __init__(self, name: str, allow_nan: bool = False):
        super().__init__(name, 'int', allow_nan)


class FloatInputFeature(SimpleTypeInputFeature):

    def __init__(self, name: str, allow_nan: bool = False):
        super().__init__(name, 'float', allow_nan)


class DateTimeInputFeature(SimpleTypeInputFeature):

    def __init__(self, name: str, allow_nan: bool = False):
        super().__init__(name, 'datetime', allow_nan)


class ObjectInputFeature(SimpleTypeInputFeature):

    def __init__(self, name: str, allow_nan: bool = False):
        super().__init__(name, 'object', allow_nan)


class StringInputFeature(ObjectInputFeature):

    def __init__(self, name: str, allow_nan: bool = False, verification_sample_size: int = None):
        super().__init__(name, allow_nan)
        self._verification_sample_size = verification_sample_size

    def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
        df_to_verify = df.copy()
        if self._verification_sample_size is not None:
            df_to_verify = df.sample(self._verification_sample_size)

        ie = super().verify_input(df_to_verify)
        if self.name() not in ie.get_missing_columns():
            if self.name() not in ie.get_columns_with_wrong_format():
                are_values_of_the_right_type = df_to_verify[self.name()].apply(lambda x: isinstance(x, str))
                if self.allow_nan:
                    are_values_of_the_right_type = are_values_of_the_right_type | df_to_verify[self.name()].isnull()
                if not all(are_values_of_the_right_type):
                    ie.add_column_with_wrong_format(self.name(),
                                                    value=df_to_verify[~are_values_of_the_right_type][self.name()]
                                                    .values[0])
        return ie


class StringTimestampInputFeature(StringInputFeature):

    def __init__(self, name: str, allow_nan: bool = False, verification_sample_size: int = None,
                 timestamp_format: str = None):
        super().__init__(name, allow_nan, verification_sample_size)
        self._timestamp_format = timestamp_format

    def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
        df_to_verify = df.copy()
        if self._verification_sample_size is not None:
            df_to_verify = df.sample(self._verification_sample_size)

        ie = super().verify_input(df_to_verify)
        if self.name() not in ie.get_missing_columns():
            if self.name() not in ie.get_columns_with_wrong_format():
                try:
                    if self._timestamp_format is not None:
                        df_to_verify[self.name()].apply(lambda x: datetime.datetime.strptime(x, self._timestamp_format))
                    else:
                        df_to_verify[self.name()].apply(lambda x: pd.to_datetime(x, format=self._timestamp_format))
                except ValueError as e:
                    ie.add_column_with_wrong_format(self.name(),
                                                    value=e.__str__())
        return ie


class DateInputFeature(ObjectInputFeature):

    def __init__(self, name: str, allow_nan: bool = False, verification_sample_size: int = None):
        super().__init__(name, allow_nan)
        self._verification_sample_size = verification_sample_size

    def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
        df_to_verify = df.copy()
        if self._verification_sample_size is not None:
            df_to_verify = df.sample(self._verification_sample_size)

        ie = super().verify_input(df_to_verify)
        if self.name() not in ie.get_missing_columns():
            if self.name() not in ie.get_columns_with_wrong_format():
                are_values_of_the_right_type = df_to_verify[self.name()].apply(
                    lambda x: isinstance(x, datetime.date) and not isinstance(x, datetime.datetime))
                if self.allow_nan:
                    are_values_of_the_right_type = are_values_of_the_right_type | df_to_verify[self.name()].isnull()
                if not all(are_values_of_the_right_type):
                    ie.add_column_with_wrong_format(self.name(),
                                                    value=df_to_verify[~are_values_of_the_right_type][self.name()]
                                                    .values[0])
        return ie


class CountryCodeInputFeature(StringInputFeature):

    def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
        df_to_verify = df.copy()
        if self._verification_sample_size is not None:
            df_to_verify = df.sample(self._verification_sample_size)

        ie = super().verify_input(df_to_verify)
        if self.name() not in ie.get_missing_columns():
            if self.name() not in ie.get_columns_with_wrong_format():
                are_values_of_the_right_type = df_to_verify[self.name()].apply(lambda x:
                                                                               x in country_code_iso_alpha2_map.keys())
                if self.allow_nan:
                    are_values_of_the_right_type = are_values_of_the_right_type | df_to_verify[self.name()].isnull()
                if not all(are_values_of_the_right_type):
                    ie.add_column_with_wrong_format(self.name(),
                                                    value=df_to_verify[~are_values_of_the_right_type][self.name()]
                                                    .values[0])
        return ie
