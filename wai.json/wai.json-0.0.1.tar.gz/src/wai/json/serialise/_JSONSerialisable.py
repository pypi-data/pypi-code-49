import json
from abc import abstractmethod
from typing import IO

from wai.common.decorator import ensure_error_type

from ..error import JSONSerialisationError
from ..raw import RawJSONElement
from ..validator import JSONValidator


class JSONSerialisable:
    """
    Interface class for objects which can serialise themselves to JSON.
    """
    @abstractmethod
    def _serialise_to_raw_json(self) -> RawJSONElement:
        """
        Performs the actual serialisation.

        :return:    The JSON representation.
        """
        pass

    @ensure_error_type(JSONSerialisationError, "Error converting {self.__class__.__qualname__} to raw JSON: {0}")
    def to_raw_json(self, validate: bool = True) -> RawJSONElement:
        """
        Converts the state of this object to a raw JSON element.

        :param validate:    Whether to validate the serialised JSON if possible.
        :return:            The raw JSON.
        """
        # Get the raw JSON representation
        raw_json: RawJSONElement = self._serialise_to_raw_json()

        # Validate the JSON if we are capable
        if validate and isinstance(self, JSONValidator):
            self.validate_raw_json(raw_json)

        return raw_json

    @ensure_error_type(JSONSerialisationError, "Error converting {self.__class__.__qualname__} to JSON string: {0}")
    def to_json_string(self, validate: bool = True) -> str:
        """
        Serialises this object to a JSON-format string.

        :param validate:    Whether to validate the serialised JSON if possible.
        :return:            The JSON string.
        """
        return json.dumps(self.to_raw_json(validate))

    @ensure_error_type(JSONSerialisationError, "Error writing {self.__class__.__qualname__} to stream: {0}")
    def write_json_to_stream(self, stream: IO[str], validate: bool = True) -> None:
        """
        Writes this object as JSON to a string-stream.

        :param validate:    Whether to validate the serialised JSON if possible.
        :param stream:      The stream to write to.
        """
        json.dump(self.to_raw_json(validate), stream)

    @ensure_error_type(JSONSerialisationError, "Error saving {self.__class__.__qualname__} to '{filename}': {0}")
    def save_json_to_file(self, filename: str, validate: bool = True) -> None:
        """
        Saves this object to the given file.

        :param validate:    Whether to validate the serialised JSON if possible.
        :param filename:    The name of the file to save to.
        """
        with open(filename, 'w') as file:
            self.write_json_to_stream(file, validate)
