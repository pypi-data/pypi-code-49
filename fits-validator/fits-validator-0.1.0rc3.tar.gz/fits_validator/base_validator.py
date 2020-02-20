"""
Definition of the base objects for the creation of a spec validator
"""
from collections import Counter
from pathlib import Path, PurePath
import logging
from typing import IO, List, Type, Union
import yaml

from astropy.io import fits
from astropy.io.fits.hdu.hdulist import HDUList
import voluptuous as vol

from fits_validator.exceptions import (
    SpecSchemaDefinitionException,
    SpecValidationException,
    ValidationException,
)

logger = logging.getLogger(__name__)


__all__ = ["SpecValidator", "SpecSchema"]


class SpecSchema:
    """
    Define a schema for a spec based upon structured definitions
    in YAML or dicts
    """

    type_map = {"int": int, "float": float, "str": str, "bool": bool}
    # Schemas defined for a spec have the following structure per key
    definition_schema_definition = {
        "required": vol.Any(True, False),
        "type": vol.Any("int", "float", "str", "bool"),
    }
    # Voluptuous schema instance used to validate the definitions
    definition_schema = vol.Schema(definition_schema_definition, extra=vol.ALLOW_EXTRA)

    def __init__(
        self, spec_schema_definitions: Union[Path, PurePath, dict, List[dict]]
    ):
        """
        Constructor for the SpecSchema which builds a voluptuous schema from
        specification definition files in YAML or dicts
        :param spec_schema_definitions: Definition of the spec's schema in one of the following forms
            - Dict definition of the spec schema
            - List of Dict definitions of the spec schema
            - Path to a YAML file defining the spec schema
            - Path to a directory containing YAML files defining spec schema
        the spec spec_validator
        """
        # convert spec schema definitions to a list of dicts
        self.spec_schema_definitions = self._parse_spec_schema_definitions(spec_schema_definitions)
        # validate the dict definition of the spec schema
        self._validate_spec_schema_definitions()
        # generate a voluptuous schema from the dict definitions
        self.spec_schema = self._create_spec_schema()

    @classmethod
    def _parse_spec_schema_definitions(
        cls, spec_schema: Union[Path, PurePath, dict, List[dict]]
    ) -> List[dict]:
        """
        Convert from multiple formats to a list of dicts
        :param spec_schema: Definition(s) of the spec's schema
        :return: List of dicts capturing the spec schema definition
        """
        def yml_file_to_dict(yml_file: Path) -> dict:
            """
            Convert a YAML file to a dict
            :param yml_file: YAML file to convert
            :return: YAML file transformed to a Dict
            """
            with yml_file.open() as yml_io:
                file_spec = yaml.load(yml_io, Loader=yaml.FullLoader)
                if file_spec is False:
                    raise SpecSchemaDefinitionException(
                        "Schema definition not parse-able as yml",
                        errors={"file": yml_file},
                    )
                return file_spec
        if isinstance(spec_schema, dict):
            return [spec_schema]
        if isinstance(spec_schema, list):
            if all([isinstance(item, dict) for item in spec_schema]):
                return spec_schema
        if isinstance(spec_schema, (Path, PurePath)):
            if spec_schema.is_file():
                files = [spec_schema]
            else:  # directory
                files = list(spec_schema.rglob("*.yml"))
            return [yml_file_to_dict(file) for file in files]
        # not a known type
        raise SpecSchemaDefinitionException(
            "Schema definition not a supported type",
            errors={
                "received": type(spec_schema),
                "expected": Union[Path, PurePath, yaml.YAMLObject, List[yaml.YAMLObject]],
            },
        )

    def _validate_spec_schema_definitions(self) -> None:
        """
        Validate the spec schema definitions against the class schema for
        spec schema definitions and raise a SpecSchemaDefinitionException
        on failure
        :return: None
        """
        def validate_definition(definition: dict):
            """
            Validate an individual key's definition against the
            class schema for spec schema definitions and raise a
            SpecSchemaDefinitionException on failure
            :param definition: definition to validate
            :return: None
            """
            for key, spec_schema in definition.items():
                schema_errors = {}
                try:
                    self.definition_schema(spec_schema)
                except vol.MultipleInvalid as e:
                    schema_errors = {error.path[0]: error.msg for error in e.errors}
                if schema_errors:
                    logger.error(f"Errors during schema definition validation. key={key} errors={schema_errors}")
                    raise SpecSchemaDefinitionException(f"Errors during Yaml Validation. key={key}", errors=schema_errors)
        # Validate all definitions in the list of definitions
        map(validate_definition, self.spec_schema_definitions)
        # Validate that there are no key collisions that would result in overwriting a key's schema
        key_counts = Counter(
            [key for definition in self.spec_schema_definitions for key in definition.keys()]
        )
        key_collisions = {k: v for k, v in key_counts.items() if v>1}
        if key_collisions:
            raise SpecSchemaDefinitionException(
                "Schema definitions have key collisions on key names", errors=key_collisions
            )

    def _create_spec_schema(self) -> vol.Schema:
        """
        A voluptuous.spec_validator object to validate headers against.
        Constructed from Spec keywords. 
        """
        def generate_schema_for_key():
            """
            Generate voluptuous schema for a key
            :return: voluptuous schema for a key
            """
            if key_schema.get("values"):
                return vol.All(
                    self.type_map[key_schema.get("type")], vol.Any(*key_schema.get("values"))
                )
            return vol.All(self.type_map[key_schema.get("type")])

        # create data structure to initialize voluptuous schema
        spec_schema = {}
        for definition in self.spec_schema_definitions:
            for key, key_schema in definition.items():
                if key_schema["required"] is True:
                    spec_schema[vol.Required(key)] = generate_schema_for_key()
                else:
                    spec_schema[key] = generate_schema_for_key()
        return vol.Schema(spec_schema, extra=vol.ALLOW_EXTRA)

    def __call__(self, headers: dict):
        """
        Validate headers against the instance spec schema
        raising voluptuous errors on failure
        :param headers: header dict to validate
        :return: None
        """
        return self.spec_schema(headers)


class SpecValidator:
    """
    Validates a FITS Headers against a schema
    """

    def __init__(
        self,
        spec_schema: Union[Path, PurePath, dict, List[dict], SpecSchema],
        SchemaValidationException: Type[SpecValidationException] = SpecValidationException,
    ):
        """
        Constructor for the SpecValidator
        :param spec_schema: Definition of the spec's schema in one of the following forms
            - SpecSchema instance
            - Dict definition of the spec schema
            - List of Dict definitions of the spec schema
            - Path to a YAML file defining the spec schema
            - Path to a directory containing YAML files defining spec schema
        :param SchemaValidationException: SpecValidationException or subclass of SpecValidationException
            to raise if spec_validator validation fails
        """
        # Callable for validating a dict against the defined spec_validator
        if isinstance(spec_schema, SpecSchema):
            self.spec_schema = spec_schema
        else:
            self.spec_schema = SpecSchema(spec_schema)

        # Exception raised when spec validation fails
        self.SchemaValidationException = SchemaValidationException

    @staticmethod
    def _headers_to_dict(headers: Union[HDUList, dict, fits.header.Header, str, IO]) -> dict:
        """
        Convert headers from multiple types to a dict
        :param headers: Headers to convert to a dict
        :return: Dict of the headers
        """
        if isinstance(headers, dict):
            return headers
        if isinstance(headers, fits.header.Header):
            return dict(headers)
        if isinstance(headers, HDUList):
            return dict(headers[0].header)
        # If headers are of any other type, see if it is a file and try to open that
        # or else raise an error.
        try:
            with fits.open(headers) as hdus:
                headers = dict(hdus[0].header)
                return headers
        except (ValueError, FileNotFoundError, OSError, IndexError) as exc:
            logger.error(f"Cannot parse headers: detail = {exc}")
            raise ValidationException(f"Cannot parse headers", errors={type(exc): str(exc)})

    def __call__(self, headers: Union[HDUList, dict, fits.header.Header, str, IO]) -> None:
        """
        Validate a header against the instance spec_schema

        :param headers: The headers to validate in the following formats:
            string file path
            File like object
            HDUList object
            fits.header.Header object
            Dictionary of header keys and values
        :return: None
        :raises: SpecValidationException or subclass
        """
        # normalize headers into a dict
        headers = self._headers_to_dict(headers)
        # validate headers against the instance spec_validator
        validation_errors = {}
        try:
            self.spec_schema(headers)
        except vol.MultipleInvalid as e:
            validation_errors = {
                error.path[0]: f"{error.msg}. Actual value: " \
                               f"{headers.get(error.path[0], 'Required keyword not present')}"
                for error in e.errors
            }
        # Raise exception if we have errors
        if validation_errors:
            logger.error(f"Errors during validation: errors={validation_errors}")
            raise self.SchemaValidationException(errors=validation_errors)
        logger.debug("Schema validation succeeded")
