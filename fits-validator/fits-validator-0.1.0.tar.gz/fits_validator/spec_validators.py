"""
Validators configured for specific Fits Specs
"""
from pathlib import Path

import fits_validator as fv
from fits_validator.exceptions import SpecValidationException
from fits_validator.base_validator import SpecValidator


__all__ = [
    "spec122_validator",
    "Spec122ValidationException",
    "spec214_validator",
    "Spec214ValidationException"
]


############
# SPEC-122 #
############


class Spec122ValidationException(SpecValidationException):
    """
    Exception when validating a spec 122 file
    """


spec122_validator = SpecValidator(
    spec_schema=Path(f"{fv.__path__[0]}/spec122"),
    SchemaValidationException=Spec122ValidationException
)


############
# SPEC-214 #
############


class Spec214ValidationException(SpecValidationException):
    """
    Exception when validating a spec 214 file
    """


spec214_validator = SpecValidator(
    spec_schema=Path(f"{fv.__path__[0]}/spec214"),
    SchemaValidationException=Spec214ValidationException
)
