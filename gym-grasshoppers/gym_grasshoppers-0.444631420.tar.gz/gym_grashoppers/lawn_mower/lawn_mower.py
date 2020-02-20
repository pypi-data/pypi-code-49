from typing import Tuple
from shapely.geometry import Point
import gym_grashoppers.util.utils as utils


class LawnMower:
    """This class is used to represent a lawn mower."""
    _INITIAL_VOLUME = 0.
    _INITIAL_ANGLE = 0.

    def __init__(self, x: float, y: float, angle: float, radius: float, maximum_volume: float, mulching: bool) -> None:
        super().__init__()
        self._position = Point(x, y)
        self._initial_angle = self._INITIAL_ANGLE
        self._angle = angle
        self._current_volume = self._INITIAL_VOLUME
        self._maximum_volume = maximum_volume
        self._mulching = mulching
        self._radius = radius

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
        self._angle = self._INITIAL_ANGLE
        self._current_volume = self._INITIAL_VOLUME
