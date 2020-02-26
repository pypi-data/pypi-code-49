from abc import ABC

import pandas as pd
from features_factory.feature_archetype import FeatureArchetype
from features_factory.input_data_error import InputDataError


class GeneratedFeature(FeatureArchetype, ABC):

    def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
        ie = InputDataError()
        if self.name() in df.columns:
            ie.add_column_that_would_be_overwritten(self.name())
        return ie
