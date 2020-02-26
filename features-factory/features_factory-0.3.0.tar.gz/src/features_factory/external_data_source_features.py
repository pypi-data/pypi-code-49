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
        >   weather = ValueFromExternalDfFeature(name='weather', dependencies=[location, date],
                                                 external_df=external_df)
        >   weather.insert_into(df=df)

        location        date        id          weather
        paris           2020-01-01  IBADGA6     rainy
        paris           2020-01-08  JHSKW67     cloudy
        florence        2020-01-01  683GHJ9     sunny
    """

    def __init__(self, name: str, dependencies: List[FeatureArchetype],
                 external_df: pd.DataFrame):
        super().__init__(name=name, dependencies=dependencies)
        self._external_df = external_df
        self._verify_df_contains_necessary_columns()

    def generate(self, df: pd.DataFrame, **kwargs) -> pd.Series:
        merged = df.merge(self._external_df, how='left', on=self._dependencies_names)
        return merged[self.name()]

    def _verify_df_contains_necessary_columns(self):
        necessary_columns = self._dependencies_names + [self.name()]
        missing_columns = [col for col in necessary_columns if col not in self._external_df.columns]
        if len(missing_columns) > 0:
            raise ExternalDfMissesNecessaryColumns('Missing columns are: {}'.format(missing_columns))


class ExternalDfMissesNecessaryColumns(ValueError):
    pass
