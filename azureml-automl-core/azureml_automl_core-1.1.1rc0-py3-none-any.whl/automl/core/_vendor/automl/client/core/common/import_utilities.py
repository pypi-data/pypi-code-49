# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Utility methods for validation and conversion."""
import logging
from typing import Any


def import_fbprophet(raise_on_fail: bool = True) -> Any:
    """Import and return the fbprophet module.

    :param raise_on_fail: whether an exception should be raise if import fails, defaults to False
    :type raise_on_fail: bool, optional
    :return: fbprophet module if it's installed, otherwise None
    :rtype: Any
    """
    class _NoPlotlyFilter(logging.Filter):
        def filter(self, record):
            return not (
                record.getMessage() == 'Importing plotly failed. Interactive plots will not work.' or
                record.getMessage() == 'Importing matplotlib failed. Plotting will not work.')

    logger = logging.getLogger('fbprophet')
    logger.addFilter(_NoPlotlyFilter())
    try:
        import fbprophet
        return fbprophet
    except ImportError:
        if raise_on_fail:
            raise
        else:
            return None
