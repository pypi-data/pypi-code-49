"""Optional utilities for converting sources of data into PyTorch-compatible datasets."""
PAST_IND_KEY = 'PAST_REGRESSOR'
PAST_DEP_KEY = 'PAST_REGRESSAND'
FUTURE_IND_KEY = 'FUTURE_REGRESSOR'
FUTURE_DEP_KEY = 'FUTURE_REGRESSAND'

from forecast.data.sources.data_source import AbstractDataSource, DataSourceConfig  # noqa: F401
