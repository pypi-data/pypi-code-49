from abc import ABC

from wai.common.decorator import ensure_error_type

from ..error import JSONSerialisationError
from ._JSONSerialisable import JSONSerialisable
from ._JSONDeserialisable import JSONDeserialisable, SelfType


class JSONBiserialisable(JSONSerialisable, JSONDeserialisable[SelfType], ABC):
    """
    Interface for classes which implement both JSONSerialisable and
    JSONDeserialisable[T].
    """
    @ensure_error_type(JSONSerialisationError, "Error copying object using JSON serialisation: {0}")
    def json_copy(self, validate: bool = True) -> SelfType:
        """
        Creates a copy of this object by serialising to JSON and
        then deserialising again.

        :param validate:    Whether to validate the serialised JSON.
        :return:            The copy of this object.
        """
        # Only validate in one direction
        return self.from_raw_json(self.to_raw_json(validate), False)
