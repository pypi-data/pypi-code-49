# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Utility methods used by automated machine learning."""
from typing import cast, Union, Optional
import json

from azureml._common._error_response.utils import is_error_code
from azureml._common._error_response._error_response_constants import ErrorHierarchy
from automl.client.core.common import utilities as common_utilities
from automl.client.core.common.exceptions import AutoMLException
from azureml.exceptions import ServiceException as AzureMLServiceException
from msrest.exceptions import HttpOperationError

from . import _constants_azureml
from .exceptions import (FeatureUnavailableException,
                         MissingValueException,
                         MalformedValueException,
                         InvalidValueException)


def friendly_http_exception(exception: Union[AzureMLServiceException, HttpOperationError], api_name: str) -> None:
    """
    Friendly exceptions for a http exceptions. This will pass through json formatted error responses.

    :param exception: exception raised from a network call.
    :param api_name: name of the API call made.
    :raise: AutoMLException
    """
    if hasattr(exception, 'error'):
        try:
            json.loads(exception.error)
            json.loads(exception.error.error)
            raise exception
        except Exception:
            pass
    try:
        status_code = exception.error.response.status_code

        # Raise bug with msrest team that response.status_code is always 500
        if status_code == 500:
            try:
                message = exception.message
                substr = 'Received '
                substr_idx = message.find(substr) + len(substr)
                status_code = int(message[substr_idx:substr_idx + 3])
            except Exception:
                pass
    except Exception:
        raise exception.with_traceback(exception.__traceback__)

    if status_code in _constants_azureml.HTTP_ERROR_MAP:
        http_error = _constants_azureml.HTTP_ERROR_MAP[status_code]
    else:
        http_error = _constants_azureml.HTTP_ERROR_MAP['default']
    if api_name in http_error:
        error_message = http_error[api_name]
    elif status_code == 400:
        # 400 bad request could be basically anything. Just pass the original exception message through
        error_message = exception.message
    else:
        error_message = http_error['default']
    raise AutoMLException(
        "{0} error raised. {1}".format(http_error['Name'], error_message), http_error['type']
    ).with_traceback(exception.__traceback__) from exception


def _raise_exception(e: AzureMLServiceException) -> None:
    if is_error_code(e, ErrorHierarchy.FEATUREUNAVAILABLE_ERROR) is True:
        raise FeatureUnavailableException(_get_error_message(e)) from None
    if is_error_code(e, ErrorHierarchy.INVALID_ERROR) is True:
        raise InvalidValueException(_get_error_message(e)) from None
    if is_error_code(e, ErrorHierarchy.MALFORMED_ERROR) is True:
        raise MalformedValueException(_get_error_message(e)) from None
    if is_error_code(e, ErrorHierarchy.BLANKOREMPTY_ERROR) is True:
        raise MissingValueException(_get_error_message(e)) from None


def _get_error_message(e: AzureMLServiceException) -> str:
    error_message = None
    try:
        error_message = json.loads(e.response.content)['error']['message']
    except Exception:
        error_message = e.response.content
        pass
    return cast(str, error_message)


def get_primary_metrics(task):
    """
    Get the primary metrics supported for a given task as a list.

    :param task: string "classification" or "regression".
    :return: A list of the primary metrics supported for the task.
    """
    return common_utilities.get_primary_metrics(task)


def _get_package_version():
    """
    Get the package version string.

    :return: The version string.
    """
    from . import __version__
    return __version__


def _is_gpu() -> bool:
    is_gpu = False
    try:
        import torch
        is_gpu = torch.cuda.is_available()
    except ImportError:
        pass
    return is_gpu
