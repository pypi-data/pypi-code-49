"""
Test for the base validator
"""
import pytest

from fits_validator.base_validator import SpecSchema, SpecValidator
from fits_validator.exceptions import (
    ValidationException, SpecSchemaDefinitionException, SpecValidationException
)


@pytest.mark.skip
def test_spec_schema():
    pass
    # TODO Path, PurePath, dict, List[dict] inputs
    # TODO required T/F
    # TODO Types "int", "float", "str", "bool"
    # TODO Value lists


@pytest.mark.skip
def test_spec_schema_invalid():
    pass
    # TODO not yaml, yaml but not valid, dict not valid, list dict 1 not valid, key collision


@pytest.mark.skip
def test_spec_validator():
    pass
    # TODO schema has T/F for all types
    # TODO pass in SpecSchema instance
    # TODO all header types HDUList, dict, fits.header.Header, str, IO


@pytest.mark.skip
def test_spec_validator_invalid_header_type():
    pass
    # TODO invalid header types


@pytest.mark.skip
def test_spec_validator_invalid_header():
    pass
    # TODO schema validation failure

# TODO confirm all exceptions have their own pytest.raises() test
