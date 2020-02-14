"""
The main module for the spec 122 validator
"""


from typing import Union
import os
import glob
from pathlib import Path
import logging

from astropy.io import fits
from astropy.io.fits.hdu.hdulist import HDUList
from voluptuous import Schema, MultipleInvalid, Required, All, Any, ALLOW_EXTRA
import yaml

from fits_validator.exceptions import Spec122ValidationException, Spec214ValidationException, YamlSchemaException

logger = logging.getLogger(__name__)

class BuildSchema:
    """
    Build a schema for use in validating multiple formats of spec data
    """
    
    type_map = {"int": int, "float": float, "str": str, "bool": bool}

    def __init__(self, path):
        self.path = path
        
        # make a list of yml files to be used
        self.yml_files = []
        for file in path.rglob("*.yml"):
            self.yml_files.append(file)
        # send to open .yml files and validate
        self._validate_spec_definition_files()
        # send to create voluptuous schema to be used with file validation
        self._create_validation_schema()


    def _validate_spec_definition_files(self) -> None:
        """
        Open Spec files and validate them using the Spec vol schema

        :return: None
        :raises: YamlValidationException
        """
        # open .yml file
        self.specdicts = []
        for file_name in self.yml_files:
            with open(file_name) as ymlstring:
                stream = yaml.load(ymlstring, Loader=yaml.FullLoader)
                self.specdicts.append(stream)
                self._validate_spec_definition(stream)

    def _validate_spec_definition(self, stream):
        """
        Spec keyword validation
        """
        for key, spec_schema in stream.items():
            schema_errors = {}
            try:
                self.validate_spec_schema(spec_schema)
            except MultipleInvalid as e:
                for error in e.errors:
                    message = error.msg
                    keyword = error.path[0]
                    schema_errors.update(((keyword, message),))
            if schema_errors:
                logger.error(f"Errors during Yaml Validation. Keyword:{key} Error:{schema_errors}")
                raise YamlSchemaException(key=key, errors=schema_errors)
    
    def _generate_voluptuous_schema_for_required_key(self, key_schema: dict) -> Union[type, object]:
        """
        Create a dictionary from spec required keys


        :param key_schema:
        :return: volschema
        """
        if key_schema.get("values"):
            volschema = All(self.type_map[key_schema.get("type")], Any(*key_schema.get("values")))
        else:
            volschema = All(self.type_map[key_schema.get("type")])
        return volschema

    def _generate_voluptuous_schema_for_key(self, key_schema: dict) -> Union[type, object]:
        """
        Create a dictionary from spec122 non-required keys

        :param key_schema:
        :return: volschema
        """
        if key_schema.get("values"):
            volschema = All(self.type_map[key_schema.get("type")], Any(*key_schema.get("values")))
        else:
            volschema = All(self.type_map[key_schema.get("type")])
        return volschema
    
    @property
    def validate_spec_schema(self):
        """
        Make a voluptuous schema to validate Spec yaml files
        """
        schemafromyml = {
            "required": Any(True, False),
            "type": Any("int", "float", "str", "bool"),
        }
        specschema = Schema(schemafromyml, extra=ALLOW_EXTRA)
        return specschema

    def _create_validation_schema(self):
        """
        A voluptuous.schema object to validate headers against. 
        Constructed from Spec keywords. 
        """

        ymlschema = {}
        # populate dictionary to go into schema
        for specdict in self.specdicts:
            for key, key_schema in specdict.items():
                if key_schema["required"] is True:
                    ymlschema[Required(key)] = self._generate_voluptuous_schema_for_required_key(
                        key_schema
                    )
                else:
                    ymlschema[key] = self._generate_voluptuous_schema_for_key(key_schema)
        schema = Schema(ymlschema, extra=ALLOW_EXTRA)
        self.schema = schema

class ParsetoDictMixIn:
    """
    Extract headers from input files and make sure they are dictionaries.
    """
    @staticmethod
    def _headers_to_dict(headers):

        # if headers are already a dictionary, good.
        if isinstance(headers, dict):
            return headers
        # if headers are HDUList, read them into a ditionary.
        if isinstance(headers, HDUList):
            return dict(headers[0].header)
        # If headers are of any other type, see if it is a file and try to open that
        # or else raise an error.
        try:
            with fits.open(headers) as hdus:
                headers = dict(hdus[0].header)
                return headers
        except ValueError as exc:
            logger.error(f"Cannot open file: detail = {exc}")
            raise Exception(f"Cannot open file: detail = {exc}")
        except FileNotFoundError:
            logger.error("File does not exist!")
            raise Exception("File does not exist!")

class Spec122Validation(ParsetoDictMixIn):
    """
    Validate input data against spec122 schema
    """
    
    def __init__(self):
        #instantiate the base classes for Spec122 validation
        self.path = Path("fits_validator/spec122")
        self.buildschema = BuildSchema(self.path)

    
    def validate(self, headers: Union[HDUList, dict, str]):
        """
        Validate the header against the schema.


        Usage:
        ------
        > from validator import FitsValidator
        > val = FitsValidator()
        > val.validate(input)


        :param headers: The headers to validate in the following formats:
            string file path
            HDUList object
            Dictionary of header keys and values
        :return: None

        :raises: Spec122ValidationException
        ______
        all_errors: dict
            dictionary of keywords and their corresponding errors
        """

        self.headers = self._headers_to_dict(headers)

        all_errors = {}

        try:
            self.buildschema.schema(self.headers)
        except MultipleInvalid as e:
            for error in e.errors:
                message = error.msg
                keyword = error.path[0]
                message = (
                    message
                    + f". Actual value: {self.headers.get(keyword, 'Required keyword not present')}"
                )
                all_errors.update(((keyword, message),))

        # Raise exception if we have errors
        if all_errors:
            logger.error(f"Errors during Ingest Validation: {all_errors}")
            raise Spec122ValidationException(errors=all_errors)
        logger.debug('No errors during ingest validation')
        return True



class Spec214Validation(ParsetoDictMixIn):
    """
    Validate input data against spec214 schema
    """
    def __init__(self):
        #instantiate the base classes for Spec122 validation
        self.path = Path("fits_validator/spec214")
        self.buildschema = BuildSchema(self.path)


    
    def validate(self, headers: Union[HDUList, dict, str]):
        """
        Validate the header against the schema.


        Usage:
        ------
        > from validator import FitsValidator
        > val = FitsValidator()
        > val.validate(input)


        :param headers: The headers to validate in the following formats:
            string file path
            HDUList object
            Dictionary of header keys and values
        :return: None

        :raises: Spec214ValidationException
        ______
        all_errors: dict
            dictionary of keywords and their corresponding errors
        """

        self.headers = self._headers_to_dict(headers)

        all_errors = {}

        try:
            self.buildschema.schema(self.headers)
        except MultipleInvalid as e:
            for error in e.errors:
                message = error.msg
                keyword = error.path[0]
                message = (
                    message
                    + f". Actual value: {self.headers.get(keyword, 'Required keyword not present')}"
                )
                all_errors.update(((keyword, message),))

        # Raise exception if we have errors
        if all_errors:
            logger.error(f"Errors during Ingest Validation: {all_errors}")
            raise Spec214ValidationException(errors=all_errors)
        logger.debug('No errors during ingest validation')
        return True

