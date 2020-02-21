"""
Common Exceptions for the fits-validator
"""

from dataclasses import dataclass


__all__ = [
    "ValidationException",
    "SpecSchemaDefinitionException",
    "SpecValidationException",
]


class ValidationException(Exception):
    """
    Base Exception for the validator
    """
    def __init__(self, message: str = "Errors during validation", errors: dict = None):
        self.message = message
        self.errors = errors

    def __str__(self):
        return f"{self.message}: errors={self.errors}"


class SpecSchemaDefinitionException(ValidationException):
    """
    Exception when validating the YAML Schemas
    """


class SpecValidationException(ValidationException):
    """
    Default spec validation exception
    """