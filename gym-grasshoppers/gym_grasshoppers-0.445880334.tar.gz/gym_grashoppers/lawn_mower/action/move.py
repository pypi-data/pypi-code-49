import math
from typing import Tuple

from gym_grashoppers.garden.garden import Garden
from gym_grashoppers.lawn_mower.action.action import Action
from gym_grashoppers.lawn_mower.lawn_mower import LawnMower
from shapely.geometry import LineString
import gym_grashoppers.util.utils as utils



class Move(Action):
    """This class is part of the Command Pattern for lawn mower actions and represents the action Move."""

    def __init__(self, lawn_mower: LawnMower, distance: float, garden: Garden) -> None:
        super().__init__(lawn_mower)
        self._total_distance = distance
        self._garden = garden

    def execute(self) -> None:
        """This method is used to move the lawn mower over the garden and mow the grass."""
        current_distance = 0.
        while current_distance < self._total_distance:
            mowed_path = LineString([(self._lawn_mower.position.x, self._lawn_mower.position.y),
                                     self.__calculate_new_position()]).buffer(
                utils.calculate_scaled_radius(self._lawn_mower.position.x, self._lawn_mower.radius))
            # TODO: starting point intersects with the boundary
            if not self._garden.grass.exterior.intersects(mowed_path):
                obstacle_intersection = False
                for obstacle in self._garden.obstacles:
                    if obstacle.exterior.intersects(mowed_path):
                        obstacle_intersection = True
                if not obstacle_intersection:
                    self._garden.extend_mowed_path(mowed_path)
                    self.lawn_mower.position = self.__calculate_new_position()
            current_distance += self._lawn_mower.radius

    def __calculate_new_position(self) -> Tuple[float, float]:
        """This method is used to calculate the new position of the lawn mower."""
        angle_radians = math.radians(self.lawn_mower.angle)
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
