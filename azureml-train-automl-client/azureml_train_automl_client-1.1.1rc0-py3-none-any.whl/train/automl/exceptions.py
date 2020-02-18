# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Defines custom exceptions produced by automated ML."""

from azureml._common.exceptions import AzureMLException
from azureml._common._error_response._error_response_constants import ErrorCodes
from azureml.exceptions import UserErrorException
from automl.client.core.common import exceptions


class ConfigException(exceptions.ConfigException, UserErrorException):
    """An exception related to invalid user configuration.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.VALIDATION_ERROR


class AuthorizationException(UserErrorException):
    """An exception related to invalid user configuration.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.AUTHORIZATION_ERROR


class FeatureUnavailableException(AuthorizationException):
    """An exception indicating that a specified feature is not available for user workspace type.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.FEATUREUNAVAILABLE_ERROR


# TODO this should move to azureml.exceptions
class ValidationException(exceptions.DataException, UserErrorException):
    """An exception representing errors caught when validating inputs.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.VALIDATION_ERROR


class BadArgumentException(ValidationException, exceptions.DataException):
    """An exception related to data validation.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.BADARGUMENT_ERROR


class MissingValueException(BadArgumentException, exceptions.DataException):
    """An exception related to data validation.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.BLANKOREMPTY_ERROR


class InvalidValueException(BadArgumentException, exceptions.DataException):
    """An exception related to data validation.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.INVALID_ERROR


class MalformedValueException(BadArgumentException, exceptions.DataException):
    """An exception related to data validation.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.MALFORMED_ERROR


# TODO this should move to azureml.exceptions
class DataException(ValidationException, exceptions.DataException):
    """An exception related to data validation.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.INVALIDDATA_ERROR


# TODO this should move to azureml.exceptions
class SystemException(AzureMLException):
    """An exception for internal errors that happen within the SDK.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    _error_code = ErrorCodes.SYSTEM_ERROR


class ServiceException(SystemException):
    """An exception related to JOS.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    _error_code = ErrorCodes.SERVICE_ERROR


class ClientException(AzureMLException, exceptions.ClientException):
    """An exception related to a client error.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    _error_code = ErrorCodes.SYSTEM_ERROR


class OnnxConvertException(ClientException):
    """An exception related to ONNX conversion.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.ONNX_ERROR


class DataValidationException(ValidationException):
    """An exception for issues caught while validating user data.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.VALIDATION_ERROR


class ForecastingDataException(DataValidationException):
    """An exception related to malformed data for a forecasting scenario.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.INVALIDFORECASTINGDATA_ERROR


class DataPrepValidationException(DataValidationException):
    """An exception related to the dataprep validation service.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.DATAPREPVALIDATION_ERROR


class DataScriptException(DataValidationException):
    """An exception for issues with user's get_data script.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.DATASCRIPT_ERROR


class ScenarioNotSupportedException(ValidationException):
    """An exception raised for unsupported or unimplemented scenarios.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.SCENARIONOTSUPORTED_ERROR


class OptionalDependencyMissingException(ScenarioNotSupportedException):
    """An exception raised when an a soft dependency is missing.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.OPTIONALSCENARIONOTENABLED_ERROR


class EarlyTerminationException(UserErrorException):
    """An exception raised for a user-generated interrupt.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.EARLYTERMINATION_ERROR


class AutoMLExperimentException(SystemException):
    """An exception representing an error that occurred during AutoML runtime.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.EXPERIMENTRUN_ERROR


class PreTrainingException(AutoMLExperimentException):
    """An exception raised for anything that goes wrong before fitting a model.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.PRETRAINING_ERROR


class CacheException(PreTrainingException):
    """An exception raised for cache issues.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.CACHE_ERROR


class FeaturizationException(PreTrainingException):
    """An exception for issues that arise during featurization.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.FEATURIZATION_ERROR


class ProblemInfoException(PreTrainingException):
    """An exception raised during the calculation data characteristics.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.PROBLEMINFO_ERROR


class TrainingException(AutoMLExperimentException):
    """An exception for issues that arise during model training.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.TRAINING_ERROR


class MetricCalculationException(TrainingException):
    """An exception raised when a metric can't be calculated.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.METRICCALCULATION_ERROR


class ModelFitException(TrainingException):
    """An exception for failure to fit the model.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    #  _error_code = ErrorCodes.MODELFIT_ERROR


class PostTrainingException(AutoMLExperimentException):
    """An exception for failures after a model has already been fitted.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.POSTTRAINING_ERROR


class ModelExplanationException(PostTrainingException):
    """An exception for failures while trying to explain the model.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.MODELEXPLANATION_ERROR


class OnnxException(PostTrainingException):
    """An exception for failures while trying to run ONNX operations.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.ONNX_ERROR


class DataprepException(ClientException):
    """An exception related to Dataprep.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    # TODO - define a code for this
    # _error_code = ErrorCodes.DATAPREPVALIDATION_ERROR


# TODO this should move to azureml.exceptions
class NotFoundException(ValidationException):
    """An exception raised when a resource could not be found.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.NOTFOUND_ERROR


class InvalidRunState(ScenarioNotSupportedException):
    """An exception when trying to use a run that is not in a valid state for the given operation.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.INVALIDRUNSTATE_ERROR


class ApiInvocationException(ServiceException):
    """An exception is thrown when API invocation fails.

    :param exception_message: A message describing the error.
    :type exception_message: str
    :param inner_exception: An optional message, for example, from a previously handled exception.
    :type inner_exception: str
    :param target: The name of the element that caused the exception to be raised.
    :type target: str
    :param details: Any additional information about the error such as other error responses or stack traces.
    :type details: str
    """

    _error_code = ErrorCodes.APIINVOCATION_ERROR


class UnhashableEntryException(DataException, exceptions.DataException):
    """An exception related to unhashable entry in the input data.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.UNHASHABLEENTRY_ERROR


class FileNotFoundException(exceptions.AutoMLException):
    """
    Exception related to file not being found.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.FILENOTFOUND_ERROR


class FetchNextIterationException(exceptions.JasmineServiceException):
    """
    Exception related to failing to fetch the next iteration from Jasmine.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.FETCHNEXTITERATION_ERROR
