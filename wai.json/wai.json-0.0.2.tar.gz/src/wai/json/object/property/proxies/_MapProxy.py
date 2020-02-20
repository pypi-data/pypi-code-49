from abc import abstractmethod, ABC
from typing import Iterable, Optional, Dict, Union, Mapping, Type

from ....error import OptionalDisallowed
from ....serialise import JSONValidatedBiserialisable
from ....schema import JSONSchema, standard_object
from ....validator import StaticJSONValidator
from ..._typing import RawJSONElement, PropertyValueType
from .._Property import Property


class MapProxy(StaticJSONValidator, JSONValidatedBiserialisable['MapProxy'], ABC):
    """
    Class which acts like a map, but validates its elements using a property.
    """
    def __init__(self,
                 initial_values: Optional[Union[Iterable, Mapping]] = None,
                 **kwargs):
        # The values in the map
        self._values: Dict[str, PropertyValueType] = {}

        # Add any initial values
        self.update(initial_values, **kwargs)

    @staticmethod
    @abstractmethod
    def value_property() -> Property:
        """
        Gets the property which is used to validate elements of the map.
        """
        pass

    @staticmethod
    def specify(value_property: Property) -> Type['MapProxy']:
        """
        Creates a specific map proxy-type.

        :param value_property:      The property to use to validate map values.
        :return:                    The map proxy-type matching the specification.
        """
        # Create the proxy-type as a closure
        class ClosureMapProxy(MapProxy):
            @staticmethod
            def value_property() -> Property:
                return value_property

        return ClosureMapProxy

    def _serialise_to_raw_json(self) -> RawJSONElement:
        return {key: value.to_raw_json() if isinstance(value, JSONValidatedBiserialisable) else value
                for key, value in self._values.items()}

    @classmethod
    def _deserialise_from_raw_json(cls, raw_json: RawJSONElement) -> 'MapProxy':
        return cls(raw_json)

    @classmethod
    def _get_json_validation_schema(cls) -> JSONSchema:
        return standard_object(additional_properties=cls.value_property().get_json_validation_schema())

    def __init_subclass__(cls, **kwargs):
        # Make sure the sub-property isn't optional
        if cls.value_property().is_optional:
            raise OptionalDisallowed("Can't use optional sub-property with maps")

        super().__init_subclass__(**kwargs)

    # ------------ #
    # DICT METHODS #
    # ------------ #

    def clear(self):
        self._values.clear()

    def copy(self):
        return type(self)(self)

    @staticmethod
    def fromkeys(seq, value):
        # TODO: Implement
        raise NotImplementedError(MapProxy.fromkeys.__qualname__)

    def get(self, k: str, default=None):
        return self._values.get(k, default)

    def items(self):
        return self._values.items()

    def keys(self):
        return self._values.keys()

    def pop(self, k, d=None):
        return self._values.pop(k, d)

    def popitem(self):
        return self._values.popitem()

    def setdefault(self, key, default):
        if key not in self:
            self[key] = default

        return self[key]

    def update(self, E=None, **F):
        if E is not None:
            if hasattr(E, "keys") and callable(E.keys):
                for k in E:
                    self[k] = E[k]
            else:
                for k, v in E:
                    self[k] = v

        for k in F:
            self[k] = F[k]

    def values(self):
        return self._values.values()

    def __contains__(self, key: str) -> bool:
        return key in self._values

    def __delitem__(self, key: str):
        del self._values[key]

    def __eq__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(MapProxy.__eq__.__qualname__)

    def __getitem__(self, y):
        return self._values[y]

    def __ge__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(MapProxy.__ge__.__qualname__)

    def __gt__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(MapProxy.__gt__.__qualname__)

    def __iter__(self):
        return iter(self._values)

    def __len__(self):
        return len(self._values)

    def __le__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(MapProxy.__le__.__qualname__)

    def __lt__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(MapProxy.__lt__.__qualname__)

    def __ne__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(MapProxy.__ne__.__qualname__)

    def __repr__(self):
        # TODO: Implement
        raise NotImplementedError(MapProxy.__repr__.__qualname__)

    def __setitem__(self, key: str, value):
        self._values[key] = self.value_property().validate_value(value)

    def __str__(self):
        return str(self._values)
