from abc import ABC, abstractmethod
from typing import Iterable, Optional, List, Callable, Any, Iterator, Type

from ....error import JSONError, OptionalDisallowed
from ....raw import RawJSONElement
from ....serialise import JSONValidatedBiserialisable
from ....schema import JSONSchema, regular_array
from ....validator import StaticJSONValidator
from ..._typing import PropertyValueType
from .._Property import Property


class ArrayProxy(StaticJSONValidator, JSONValidatedBiserialisable['ArrayProxy'], ABC):
    """
    Class which acts like an array, but validates its elements using a property.
    """
    def __init__(self, initial_values: Optional[Iterable] = None):
        # The list values
        self._values: List[PropertyValueType] = []

        # Add any initial values
        if initial_values is not None:
            self.__iadd__(initial_values)

        # Make sure the list is long enough
        if len(self._values) < self.min_elements():
            raise JSONError(f"Array proxy initialised with {len(self._values)} elements "
                            f"when the minimum is {self.min_elements()}")

    @staticmethod
    @abstractmethod
    def element_property() -> Property:
        """
        Gets the property which is used to validate elements of the array.
        """
        pass

    @staticmethod
    @abstractmethod
    def min_elements() -> int:
        """
        The minimum-allowed length of this array.
        """
        pass

    @staticmethod
    @abstractmethod
    def max_elements() -> Optional[int]:
        """
        The maximum-allowed length of this array.
        """
        pass

    @staticmethod
    @abstractmethod
    def unique_elements() -> bool:
        """
        Whether the elements of this array have to be distinct
        from one another.
        """
        pass

    @staticmethod
    def specify(element_property: Property,
                min_elements: int = 0,
                max_elements: Optional[int] = None,
                unique_elements: bool = False) -> Type['ArrayProxy']:
        """
        Creates a specific array proxy-type.

        :param element_property:    The property to use to validate array elements.
        :param min_elements:        The minimum number of elements allowed in the array.
        :param max_elements:        The maximum number of elements allowed in the array.
        :param unique_elements:     Whether array elements have to be unique.
        :return:                    The array proxy-type matching the specification.
        """
        # Create the proxy-type as a closure
        class ClosureArrayProxy(ArrayProxy):
            @staticmethod
            def element_property() -> Property:
                return element_property

            @staticmethod
            def min_elements() -> int:
                return min_elements

            @staticmethod
            def max_elements() -> Optional[int]:
                return max_elements

            @staticmethod
            def unique_elements() -> bool:
                return unique_elements

        return ClosureArrayProxy

    def _serialise_to_raw_json(self) -> RawJSONElement:
        return [value.to_raw_json() if isinstance(value, JSONValidatedBiserialisable) else value
                for value in self._values]

    @classmethod
    def _deserialise_from_raw_json(cls, raw_json: RawJSONElement) -> 'ArrayProxy':
        return cls(raw_json)

    @classmethod
    def _get_json_validation_schema(cls) -> JSONSchema:
        return regular_array(
            cls.element_property().get_json_validation_schema(),
            cls.min_elements(),
            cls.max_elements(),
            cls.unique_elements()
        )

    def __init_subclass__(cls, **kwargs):
        # Make sure the sub-property isn't optional
        if cls.element_property().is_optional:
            raise OptionalDisallowed("Can't use optional sub-property with array proxies")

        # Make sure min_elements is not negative
        if cls.min_elements() < 0:
            raise JSONError(f"min_elements must be non-negative, got {cls.min_elements()}")

        super().__init_subclass__(**kwargs)

    # ------------ #
    # LIST METHODS #
    # ------------ #

    def append(self, value):
        # Make sure we're not already at max length
        if len(self._values) == self.max_elements():
            raise JSONError(f"Tried to append to list already of maximum size ({self.max_elements()})")

        # Make sure the unique-elements constraint isn't violated
        if self.unique_elements() and value in self:
            raise JSONError(f"Attempted to add non-unique element")

        self._values.append(self.element_property().validate_value(value))

    def clear(self):
        # Make sure clearing the list wouldn't violate the minimum size
        if self.min_elements() > 0:
            raise JSONError(f"Cannot clear array when minimum size "
                            f"({self.min_elements()}) is greater than zero")

        # Clear the key-list
        self._values.clear()

    def copy(self):
        return type(self)(self)

    def count(self, value) -> int:
        try:
            value = self.element_property().validate_value(value)
            return self._values.count(value)
        except Exception:
            return 0

    def extend(self, iterable: Iterable):
        for value in iterable:
            self.append(value)

    def index(self, value, start: int = 0, stop: int = -1) -> int:
        value = self.element_property().validate_value(value)
        return self._values.index(value, start, stop)

    def insert(self, index: int, value):
        # Make sure we're not already at max length
        if len(self._values) == self.max_elements():
            raise JSONError(f"Tried to insert into list already of maximum size ({self.max_elements()})")

        # Make sure the unique-elements constraint isn't violated
        if self.unique_elements() and value in self:
            raise JSONError(f"Attempted to insert non-unique element")

        self._values.insert(index, self.element_property().validate_value(value))

    def pop(self, index: int = -1):
        # Make sure we're not already at min length
        if len(self._values) == self.min_elements():
            raise JSONError(f"Tried to pop from list already of minimum size ({self.min_elements()})")

        return self._values.pop(index)

    def remove(self, value):
        self.pop(self.index(value))

    def reverse(self):
        self._values.reverse()

    def sort(self, *,
             key: Optional[Callable[[Any], Any]] = lambda k: k,
             reverse: bool = False):
        self._values.sort(key=key, reverse=reverse)

    def __add__(self, x: List) -> List:
        return self[:] + x

    def __contains__(self, value) -> bool:
        return self.element_property().validate_value(value) in self._values

    def __delitem__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(ArrayProxy.__delitem__.__qualname__)

    def __eq__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(ArrayProxy.__eq__.__qualname__)

    def __getitem__(self, y):
        return self._values[y]

    def __ge__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(ArrayProxy.__ge__.__qualname__)

    def __gt__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(ArrayProxy.__gt__.__qualname__)

    def __iadd__(self, x: Iterable):
        for value in x:
            self.append(value)

    def __imul__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(ArrayProxy.__imul__.__qualname__)

    def __iter__(self) -> Iterator:
        return iter(self._values)

    def __len__(self) -> int:
        return len(self._values)

    def __le__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(ArrayProxy.__le__.__qualname__)

    def __lt__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(ArrayProxy.__lt__.__qualname__)

    def __mul__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(ArrayProxy.__mul__.__qualname__)

    def __ne__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(ArrayProxy.__ne__.__qualname__)

    def __repr__(self):
        # TODO: Implement
        raise NotImplementedError(ArrayProxy.__repr__.__qualname__)

    def __reversed__(self):
        return reversed(self._values)

    def __rmul__(self, *args, **kwargs):
        # TODO: Implement
        raise NotImplementedError(ArrayProxy.__rmul__.__qualname__)

    def __setitem__(self, index: int, value):
        # Validate the value
        value = self.element_property().validate_value(value)

        # Make sure the unique-elements constraint isn't violated
        if self.unique_elements() and value in self._values and self._values[index] != value:
            raise JSONError(f"Attempted to set element to non-unique element")

        self._values[index] = value

    def __str__(self):
        return str(self._values)
