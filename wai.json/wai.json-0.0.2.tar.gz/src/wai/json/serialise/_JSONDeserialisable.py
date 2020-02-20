import json
from abc import abstractmethod
from typing import TypeVar, Generic, IO

from wai.common.decorator import ensure_error_type

from ..error import JSONSerialisationError
from ..raw import RawJSONElement
from ..validator import JSONValidator

# The type of the object that is deserialised
SelfType = TypeVar("SelfType", bound="JSONDeserialisable")


class JSONDeserialisable(Generic[SelfType]):
    """
    Interface for classes which can deserialise instances from JSON.
    """
    @classmethod
    @abstractmethod
    def _deserialise_from_raw_json(cls, raw_json: RawJSONElement) -> SelfType:
        """
        Implements the actual deserialisation from JSON.

        :param raw_json:    The raw JSON representation.
        :return:            An instance of the type.
        """
        pass

    @classmethod
    @ensure_error_type(JSONSerialisationError, "Error deserialising raw JSON {raw_json}: {0}")
    def from_raw_json(cls, raw_json: RawJSONElement, validate: bool = True) -> SelfType:
        """
        Instantiates an object of this type from a raw JSON element.

        :param raw_json:    The raw JSON element.
        :param validate:    Whether to validate the JSON before deserialisation.
        :return:            The object instance.
        """
        # Validate the raw JSON if we are capable
        if validate and issubclass(cls, JSONValidator):
            cls.validate_raw_json(raw_json)

        # Deserialise
        return cls._deserialise_from_raw_json(raw_json)

    @classmethod
    @ensure_error_type(JSONSerialisationError, "Error deserialising JSON string '{json_string}': {0}")
    def from_json_string(cls, json_string: str, validate: bool = True) -> SelfType:
        """
        Instantiates an object of this type from a JSON-format string.

        :param json_string:     The JSON-format string to parse.
        :param validate:        Whether to validate the JSON before deserialisation.
        :return:                The object instance.
        """
        raw_json = json.loads(json_string)

        return cls.from_raw_json(raw_json, validate)

    @classmethod
    @ensure_error_type(JSONSerialisationError, "Error reading JSON from stream: {0}")
    def read_json_from_stream(cls, stream: IO[str], validate: bool = True) -> SelfType:
        """
        Instantiates an object of this type from the given string-stream.

        :param stream:      The stream to read from.
        :param validate:    Whether to validate the JSON before deserialisation.
        :return:            The object instance.
        """
        return cls.from_raw_json(json.load(stream), validate)

    @classmethod
    @ensure_error_type(JSONSerialisationError, "Error loading JSON from file '{filename}': {0}")
    def load_json_from_file(cls, filename: str, validate: bool = True) -> SelfType:
        """
        Loads an instance of this class from the given file.

        :param filename:    The name of the file to load from.
        :param validate:    Whether to validate the JSON before deserialisation.
        :return:            The instance.
        """
        with open(filename, 'r') as file:
            return cls.read_json_from_stream(file, validate)
