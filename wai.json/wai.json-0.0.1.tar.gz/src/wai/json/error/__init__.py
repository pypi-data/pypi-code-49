"""
Package for specialised error types to do with processing JSON.
"""
from ._JSONError import JSONError
from ._JSONPropertyError import JSONPropertyError
from ._JSONSchemaError import JSONSchemaError
from ._JSONSerialisationError import JSONSerialisationError
from ._JSONValidationError import JSONValidationError
from ._OfPropertySelectionError import OfPropertySelectionError
from ._OptionalDisallowed import OptionalDisallowed
from ._RequiredDisallowed import RequiredDisallowed
from ._SchemaDefinitionRedefined import SchemaDefinitionRedefined
