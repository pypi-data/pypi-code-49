"""
qwikstart.exceptions
-----------------------

All exceptions used in the qwikstart code base are defined here.
"""


class QwikstartException(Exception):
    """Base exception class. All qwikstart-specific exceptions should subclass this."""


class RepoLoaderError(QwikstartException):
    """Exception raised when loading task specification fails."""


class TaskParserError(QwikstartException):
    """Exception raised when parsing task specification fails."""


class OperationDefinitionError(QwikstartException):
    """Exception raised when an operation is improperly defined."""


# ----------------------
# User-facing exceptions
# ----------------------


class UserFacingError(QwikstartException):
    """Base exception for errors that are meant to be displayed to users."""


class ConfigurationError(UserFacingError):
    """User-facing exception raised during qwikstart configuration."""


class OperationError(UserFacingError):
    """User-facing exception raised during execution of operation."""
