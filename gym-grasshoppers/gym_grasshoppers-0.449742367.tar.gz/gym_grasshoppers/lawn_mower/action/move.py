import math
import gym_grasshoppers.util.utils as utils

from typing import Tuple
from gym_grasshoppers.exception.invalid_action_exception import InvalidActionException
from gym_grasshoppers.garden.garden import Garden
from gym_grasshoppers.lawn_mower.action.action import Action
from gym_grasshoppers.lawn_mower.lawn_mower import LawnMower
from shapely.geometry import LineString


class Move(Action):
    """This class is part of the Command Pattern for lawn mower actions and represents the action Move."""

    def __init__(self, lawn_mower: LawnMower, distance: float, garden: Garden) -> None:
        super().__init__(lawn_mower)

        self._total_distance = distance
        if self._total_distance is None:
            raise InvalidActionException('The distance that the lawn mower has to cover is missing!')
        elif not isinstance(self._total_distance, float):
            raise InvalidActionException('The distance that the lawn mower has to cover is not a float!')
        elif self._total_distance <= 0:
            raise InvalidActionException('The distance that the lawn mower has to cover must be higher than 0!')

        self._garden = garden

    def execute(self) -> None:
        """This method is used to move the lawn mower over the garden and mow the grass."""
        current_distance = 0.
        while current_distance < self._total_distance:
            mowed_path = LineString([(self._lawn_mower.position.x, self._lawn_mower.position.y),
                                     self.__calculate_new_position()]).buffer(
                utils.calculate_scaled_radius(self._lawn_mower.position.x, self._lawn_mower.radius))
            if not self._garden.grass.exterior.intersects(mowed_path):
                obstacle_intersection = False
                for obstacle in self._garden.obstacles:
                    if obstacle.exterior.intersects(mowed_path):
                        obstacle_intersection = True
                if not obstacle_intersection:
                    self._garden.extend_mowed_path(mowed_path)
                    self._lawn_mower.position = self.__calculate_new_position()
            current_distance += self._lawn_mower.radius

    def __calculate_new_position(self) -> Tuple[float, float]:
        """This method is used to calculate the new position of the lawn mower."""
        angle_radians = math.radians(self._lawn_mower.angle)
        latitude_radians = math.radians(self._lawn_mower.position.y)
        longitude_radians = math.radians(self._lawn_mower.position.x)
        latitude_degrees = math.degrees(
            math.asin(math.sin(latitude_radians) * math.cos(self._lawn_mower.radius / utils.EARTH_RADIUS) +
                      math.cos(latitude_radians) * math.sin(self._lawn_mower.radius / utils.EARTH_RADIUS) *
                      math.cos(angle_radians)))
        longitude_degrees = math.degrees(
            longitude_radians + math.atan2(math.sin(angle_radians) * math.sin(self._lawn_mower.radius / utils.EARTH_RADIUS) *
                                           math.cos(latitude_radians), math.cos(self._lawn_mower.radius / utils.EARTH_RADIUS) -
                                           math.sin(latitude_radians) * math.sin(latitude_degrees)))
        return longitude_degrees, latitude_degrees
