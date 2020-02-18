# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Exceptions thrown by AutoML."""
import json
from typing import Any, cast, List, Optional, Type, TypeVar
from ._error_response_constants import ErrorCodes


ExceptionT = TypeVar('ExceptionT', bound='AutoMLException')


class ErrorTypes:
    """Possible types of errors."""

    User = 'User'
    Service = 'Service'
    Client = 'Client'
    Resource = 'Resource'
    Unclassified = 'Unclassified'
    All = {User, Service, Client, Resource, Unclassified}


class AutoMLException(Exception):
    """Exception with an additional field specifying what type of error it is."""

    error_type = ErrorTypes.Unclassified

    def __init__(self,
                 exception_message: str = "",
                 error_type: str = ErrorTypes.Unclassified,
                 target: Optional[str] = None,
                 details: Optional[List[str]] = None,
                 has_pii: bool = True):
        """
        Construct a new AutoMLException.

        :param exception_message: A message describing the error.
        :type exception_message: str
        :param error_type: Error code corresponding to the exception. Defaults to Unclassified.
        :type error_type: str
        :param target: The name of the element that caused the exception to be thrown.
        :type target: str
        :param details: Any additional information for the error, such as other error responses or stack traces.
        :type details: builtin.list(str)
        :param has_pii: Boolean representing whether the Exception message has any PII information.
        :type has_pii: bool
        """
        super().__init__(exception_message)
        self.error_type = error_type
        self._exception_message = exception_message
        self._target = target
        self._details = details
        self._inner_exception = None     # type: Optional[BaseException]
        self._has_pii = has_pii
        if has_pii:
            self._generic_msg = None            # type: Optional[str]
        else:
            self._generic_msg = exception_message

    def __repr__(self) -> str:
        """Return string representation of the exception."""
        return "{}:\n\tMessage: {}\n\tInnerException {}\n\tErrorResponse \n{}".format(
            self.__class__.__name__,
            self._exception_message,
            self._inner_exception,
            self._serialize_json(indent=4))

    def __str__(self) -> str:
        """Return string representation of the exception."""
        return self.__repr__()

    @classmethod
    def from_exception(cls: 'Type[ExceptionT]', e: BaseException, msg: Optional[str] = None,
                       target: Optional[str] = None, has_pii: bool = True) -> ExceptionT:
        """
        Convert an arbitrary exception to this exception type. The resulting exception is marked as containing PII.

        :param e: the original exception object
        :param msg: optional message to use instead of the original exception message
        :param target: optional string pointing to the target of the exception
        :param has_pii: whether this exception contains PII or not
        :return: a new exception of this type, preserving the original stack trace
        """
        if not msg and isinstance(e, cls):
            return cast(ExceptionT, e)

        new_exception = cast(ExceptionT, cls(exception_message=(msg or str(e)), target=target, has_pii=has_pii)
                             .with_traceback(e.__traceback__))
        new_exception._inner_exception = e
        return new_exception

    @classmethod
    def create_without_pii(cls: 'Type[ExceptionT]', msg: str = "",
                           target: Optional[str] = None) -> ExceptionT:
        """
        Create an exception that is tagged as not containing PII.

        :param msg: optional message to use instead of the original exception message
        :param target: optional string pointing to the target of the exception
        :return:
        """
        exception = cls(exception_message=msg, target=target, has_pii=False)
        return exception

    def with_generic_msg(self: ExceptionT, msg: str) -> ExceptionT:
        """
        Attach a generic error message that will be used in telemetry if this exception contains PII.

        :param msg: the generic message to use
        :return: this object
        """
        self._generic_msg = msg
        self._has_pii = True
        return self

    @property
    def has_pii(self) -> bool:
        """Check whether this exception's message contains PII or not."""
        return cast(bool, getattr(self, '_has_pii', False))

    @property
    def pii_free_msg(self) -> str:
        """Fallback message to use for situations where printing PII-containing information is inappropriate."""
        fallback_message = getattr(self, '_generic_msg', None) or '[Hidden as it may contain PII]'  # type: str
        message = self._exception_message or fallback_message if not self.has_pii else fallback_message  # type: str
        return message

    @property
    def target(self) -> Optional[str]:
        """Name of the element that caused the exception to be thrown."""
        return self._target

    def get_error_type(self):
        """Get the error code for this exception."""
        return getattr(self, "_error_code", self.error_type)

    def _serialize_json(self, indent: Optional[int] = None) -> str:
        """
        Serialize this exception as an ErrorResponse json.

        :return: json string
        """
        error_ret = {}
        error_out = {}  # type: Any
        for super_class in self.__class__.mro():
            if super_class.__name__ == AutoMLException.__name__:
                break
            try:
                error_code = getattr(super_class, '_error_code')
                if error_out != {}:
                    # Flatten the tree in case we have something like System > System > System > System
                    prev_code = error_out.get('code')
                    if prev_code is None or error_code != prev_code:
                        error_out = {"code": error_code, "inner_error": error_out}
                else:
                    error_out = {"code": error_code}
            except AttributeError:
                break

        error_out['message'] = self._exception_message
        if self._target is not None:
            error_out['target'] = self._target
        if self._details is not None:
            error_out['details'] = self._details
        error_ret['error'] = error_out

        return json.dumps(error_ret, indent=indent, sort_keys=True)


class UserException(AutoMLException):
    """
    Exception related to user error.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.USER_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new UserException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, ErrorTypes.User, target, **kwargs)


class DataException(UserException):
    """
    Exception related to data validations.

    :param exception_message: Details on the exception.
    """

    # Targets
    MISSING_DATA = 'MissingData'

    _error_code = ErrorCodes.INVALIDDATA_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new DataException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)


class ConfigException(AutoMLException):
    """
    Exception related to invalid user config.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.VALIDATION_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new ConfigException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, ErrorTypes.User, target, **kwargs)


class ArgumentException(AutoMLException):
    """
    Exception related to invalid user config.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.VALIDATION_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new ConfigException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, ErrorTypes.User, target, **kwargs)


class ServiceException(AutoMLException):
    """
    Exception related to JOS.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.SYSTEM_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new ServiceException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, ErrorTypes.Service, target, **kwargs)


class ClientException(AutoMLException):
    """
    Exception related to client.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.SYSTEM_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new ClientException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, ErrorTypes.Client, target, **kwargs)


class FitException(ClientException):
    """
    Exception related to fit in external pipelines, models, and transformers.

    :param message: Details on the exception.
    """

    _error_code = ErrorCodes.FIT_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new FitException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)


class TransformException(ClientException):
    """
    Exception related to transform in external pipelines and transformers.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.TRANSFORM_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new TransformException.

        :param message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)


class PredictionException(ClientException):
    """
    Exception related to prediction in external pipelines and transformers.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.PREDICTION_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new PredictionException.

        :param message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)


class UntrainedModelException(ClientException):
    """UntrainedModelException."""

    def __init__(self, exception_message="Fit needs to be called before predict.", target=None, **kwargs):
        """Create a UntrainedModelException."""
        super().__init__("UntrainedModelException: {0}".format(exception_message), target=target, **kwargs)


class InvalidArgumentException(ClientException):
    """Exception related to arguments that were not expected by a component."""

    _error_code = ErrorCodes.BADARGUMENT_ERROR

    def __init__(self, exception_message, error_detail=None, target=None, **kwargs):
        """Create a InvalidArgumentException."""
        if error_detail is not None:
            super().__init__(
                exception_message="InvalidArgumentException: {0}, {1}".format(exception_message, error_detail),
                target=target, **kwargs)
        else:
            super().__init__(exception_message="InvalidArgumentException: {0}".format(exception_message),
                             target=target, **kwargs)


class DataErrorException(AutoMLException):
    """
    Exception related to errors seen while processing data at training or inference time.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.DATA_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new DataErrorException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, ErrorTypes.Client, target, **kwargs)


class RawDataSnapshotException(AutoMLException):
    """
    Exception related to capturing the raw data snapshot to be used at the inference time.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.RAWDATASNAPSHOT_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new RawDataSnapshotException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, ErrorTypes.Client, target, **kwargs)


class ResourceException(AutoMLException):
    """
    Exception related to resource usage.

    :param exception_message: Details on the exception.
    """

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new ResourceException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, ErrorTypes.Resource, target, **kwargs)


class OnnxConvertException(ClientException):
    """Exception related to ONNX convert."""

    # TODO - define a code for this
    # _error_code = ErrorCodes.ONNX_ERROR


class DataprepException(ClientException):
    """Exceptions related to Dataprep."""

    # TODO - define a code for this
    # _error_code = ErrorCodes.DATAPREPVALIDATION_ERROR


class DataShapeError(UserException):
    """The class of errors related to the data frame shape."""

    _error_code = ErrorCodes.DATASHAPE_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new DataShapeError.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)


class LabelMissingException(DataException):
    """Exception related to label missing from input data.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.INPUTLABELMISSING_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new LabelMissingException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)


class FeaturizationOffException(DataException):
    """Exception related to featurization not being enabled.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.FEATURIZATIONOFF_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new FeaturizationOffException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)


class DataSamplesSizeException(DataException):
    """Exception related to X and y having different number of samples.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.DATASAMPLESMISMATCH_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new DataSamplesMismatchException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)


class ValidationException(UserException):
    """An exception representing errors caught when validating inputs.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.VALIDATION_ERROR


class BadArgumentException(ValidationException):
    """An exception related to data validation.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.BADARGUMENT_ERROR


class MissingValueException(BadArgumentException):
    """An exception related to data validation.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.BLANKOREMPTY_ERROR


class InvalidValueException(BadArgumentException):
    """An exception related to data validation.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.INVALID_ERROR


class MalformedValueException(BadArgumentException):
    """An exception related to data validation.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.MALFORMED_ERROR


class OutOfRangeException(BadArgumentException):
    """An exception related to unhashable entry in the input data.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.UNHASHABLEENTRY_ERROR


class UnhashableEntryException(DataException):
    """An exception related to unhashable entry in the input data.

    :param exception_message: A message describing the error.
    :type exception_message: str
    """

    _error_code = ErrorCodes.UNHASHABLEENTRY_ERROR


class DataFormatException(DataException):
    """Exception related to input data not being in the expected format.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.DATAFORMAT_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new DataFormatException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)


class AllLabelsMissingException(DataException):
    """Exception related to input data missing all labels.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.ALLLABELSMISSING_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new AllLabelsMissingException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)


class InsufficientMemoryException(UserException):
    """Exception related to insufficient memory."""

    _error_code = ErrorCodes.INSUFFICIENTMEMORY_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new InsufficientMemoryException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)


class DiskSpaceUnavailableException(UserException):
    """Exception related to insufficient disk space."""

    _error_code = ErrorCodes.DISKSPACEUNVAILABLE_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new DiskSpaceUnavailableException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)


class AutoMLEnsembleException(ClientException):
    """Exception for AutoML ensembling related errors."""

    # Targets
    CONFIGURATION = 'Configuration'
    MISSING_MODELS = 'MissingModels'
    MODEL_NOT_FIT = 'ModelNotFit'

    _error_code = ErrorCodes.AUTOMLENSEMBLE_ERROR

    def __init__(self, exception_message, error_detail=None, target=None, **kwargs):
        """Create an AutoMLEnsemble exception."""
        if error_detail is not None:
            super().__init__(
                exception_message="AutoMLEnsembleException: {0}, {1}".format(exception_message, error_detail),
                target=target, **kwargs)
        else:
            super().__init__(exception_message="AutoMLEnsembleException: {0}".format(exception_message))


class PipelineRunException(ClientException):
    """Exception for pipeline run related errors."""

    # Targets
    PIPELINE_RUN_REQUIREMENTS = 'PipelineRunRequirements'
    PIPELINE_OUTPUT = 'PipelineOutput'

    _error_code = ErrorCodes.PIPELINEEXECUTION_ERROR

    def __init__(self, exception_message, error_detail=None, target=None, **kwargs):
        """Create a PipelineRunException exception."""
        if error_detail is not None:
            super().__init__(
                exception_message="PipelineRunException: {0}, {1}".format(exception_message, error_detail),
                target=target, **kwargs)
        else:
            super().__init__(exception_message="PipelineRunException: {0}".format(exception_message),
                             target=target, **kwargs)


class JasmineServiceException(ServiceException):
    """
    Exception related to the class of errors by Jasmine.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.JASMINESERVICE_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new JasmineServiceException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)


class RunStateChangeException(ServiceException):
    """
    Exception related to failing to change the state of the run.

    :param exception_message: Details on the exception.
    """

    _error_code = ErrorCodes.STATECHANGE_ERROR

    def __init__(self, exception_message="", target=None, **kwargs):
        """
        Construct a new RunStateChangeException.

        :param exception_message: details on the exception.
        """
        super().__init__(exception_message, target, **kwargs)
