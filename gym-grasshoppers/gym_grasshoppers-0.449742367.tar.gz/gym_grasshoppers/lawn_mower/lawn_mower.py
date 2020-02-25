from typing import Tuple
from shapely.geometry import Point
from gym_grasshoppers.exception.invalid_lawn_mower_exception import InvalidLawnMowerException


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
        elif not isinstance(self._angle, float):
            raise InvalidLawnMowerException('The starting angle of the lawn mower is not a float!')
        elif self._angle < -180:
            raise InvalidLawnMowerException('The starting angle of the lawn mower must be higher than -180°!')
        elif self._angle > 180:
            raise InvalidLawnMowerException('The starting angle of the lawn mower must be lower than 180°!')

        self._height = height
        if self._height is None:
            raise InvalidLawnMowerException('The mow height of the lawn mower is missing!')
        elif not isinstance(self._height, float):
            raise InvalidLawnMowerException('The mow height of the lawn mower is not a float!')
        elif self._height <= 0.:
            raise InvalidLawnMowerException('The mow height of the lawn mower must be higher than 0!')

        self._current_volume = self.INITIAL_VOLUME
        self._maximum_volume = maximum_volume
        if self._maximum_volume is None:
            raise InvalidLawnMowerException('The maximum volume of the lawn mower is missing!')
        elif not isinstance(self._maximum_volume, float):
            raise InvalidLawnMowerException('The maximum volume of the lawn mower is not a float!')
        elif self._maximum_volume < 0.:
            raise InvalidLawnMowerException('The maximum volume of the lawn mower can not be negative!')

        self._mulching = mulching
        if self.mulching is None:
            raise InvalidLawnMowerException('The mulching option of the lawn mower is missing!')
        elif not isinstance(self._mulching, bool):
            raise InvalidLawnMowerException('The mulching option of the lawn mower is not a bool!')

        if self._maximum_volume == 0. and not self._mulching:
            raise InvalidLawnMowerException('The maximum volume of the lawn mower must be higher than zero when the '
                                            'lawn mower can not mulch!')

        self._radius = radius
        if self._radius is None:
            raise InvalidLawnMowerException('The radius of the lawn mower is missing!')
        elif not isinstance(self._radius, float):
            raise InvalidLawnMowerException('The radius of the lawn mower is not a float!')
        elif self._radius <= 0.:
            raise InvalidLawnMowerException('The radius of the lawn mower must be higher than 0!')

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
