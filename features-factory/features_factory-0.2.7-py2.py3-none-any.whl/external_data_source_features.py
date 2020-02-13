from typing import List

import pandas as pd

from features_factory.composed_features import ComposedFeature
from features_factory.feature_archetype import FeatureArchetype


class ValueFromExternalDfFeature(ComposedFeature):
    """
    Feature that allows to merge a column coming from an external dataframe.

    E.g.
        Given df

        location    date        id
        paris       2020-01-01  IBADGA6
        paris       2020-01-08  JHSKW67
        florence    2020-01-01  683GHJ9

        and external_df

        location    date        weather
        paris       2020-01-01  rainy
        paris       2020-01-08  cloudy
        florence    2020-01-01  sunny
        florence    2020-01-08  sunny

        We would like to add the weather information to df.

        Simply execute:

        >   location = StringInputFeature(name='location')
        >   date = DateInputFeature(name='date')
        >   weather = ValueFromExternalDfFeature(name='local_weather', dependencies=[location, date],
                                                 external_df=external_df, external_value_column='weather')
        >   weather.insert_into(df=df)

        location        date        id          local_weather
        paris           2020-01-01  IBADGA6     rainy
        paris           2020-01-08  JHSKW67     cloudy
        florence        2020-01-01  683GHJ9     sunny
    """

    def __init__(self, name: str, dependencies: List[FeatureArchetype],
                 external_df: pd.DataFrame, external_value_column: str):
        super().__init__(name=name, dependencies=dependencies)
        self._external_df = external_df
        self._external_column_to_keep = external_value_column
        self._verify_df_contains_necessary_columns()

    def generate(self, df: pd.DataFrame, **kwargs) -> pd.Series:
        merged = df.merge(self._external_df, how='left', on=self._dependencies_names)
        return merged[self._external_column_to_keep]

    def _verify_df_contains_necessary_columns(self):
        necessary_columns = self._dependencies_names + [self._external_column_to_keep]
        if not set(necessary_columns).issubset(set(self._external_df.columns)):
            raise ExternalDfMissesNecessaryColumns


class ExternalDfMissesNecessaryColumns(ValueError):
    pass
