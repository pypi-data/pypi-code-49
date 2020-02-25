from collections.abc import MutableMapping, Sequence
from abc import ABC
from koala_crawler.exceptions.crawler_exceptions import InvalidGraphObject


class GraphObjectBase(ABC):

    def __init__(self, obj: MutableMapping, required_fields: Sequence):
        self._required_fields = required_fields
        self._validate_required_object_fields(obj)

    def as_json(self) -> MutableMapping:
        raise NotImplementedError()

    def _validate_required_object_fields(self, obj):
        for field in self._required_fields:
            if field not in obj:
                raise InvalidGraphObject(self.__class__.__name__, self._required_fields, field)
