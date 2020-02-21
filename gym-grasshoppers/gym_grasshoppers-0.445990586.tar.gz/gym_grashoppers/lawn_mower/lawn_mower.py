from typing import Tuple
from shapely.geometry import Point
from gym_grashoppers.exception.invalid_lawn_mower_exception import InvalidLawnMowerException


class LawnMower:
    """This class is used to represent a lawn mower."""
    INITIAL_VOLUME = 0.

    def __init__(self, x: float, y: float, angle: float, height: float, radius: float, maximum_volume: float,
                 mulching: bool) -> None:
        super().__init__()

        self._position = Point(x, y)

        self._initial_angle = angle
        self._angle = angle
        if self._angle is None:
            raise InvalidLawnMowerException('The starting angle of the lawn mower is missing!')

        self._height = height
        if self._height is None or self._height == '':
            raise InvalidLawnMowerException('The mow height of the lawn mower is missing!')

        self._current_volume = self.INITIAL_VOLUME
        self._maximum_volume = maximum_volume
        self._mulching = mulching
        if (self._maximum_volume is None or self._maximum_volume <= 0.) and \
                (self._mulching is False or self._mulching is None):
            raise InvalidLawnMowerException('The maximum volume of the lawn mower is necessary when the lawn mower '
                                            'can not mulch!')

        self._radius = radius
        if self._radius is None or self._radius <= 0.:
            raise InvalidLawnMowerException('The radius of the lawn mower is missing!')

    @property
    def position(self) -> Point:
        return self._position

    @position.setter
    def position(self, value: Tuple[float, float]):
        self._position = Point(value[0], value[1])

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, value: float):
        self._angle = value

    @property
    def height(self):
        return self._height

    @property
    def current_volume(self) -> float:
        return self._current_volume

    @current_volume.setter
    def current_volume(self, value: float):
        self._current_volume = value

    @property
    def maximum_volume(self) -> float:
        return self._maximum_volume

    @property
    def mulching(self) -> bool:
        return self._mulching

    def reset(self, x: float, y: float) -> None:
        """This method is used to reset the lawn mower to its initial values."""
        self._position = Point(x, y)
        self._angle = self._initial_angle
        self._current_volume = self.INITIAL_VOLUME
