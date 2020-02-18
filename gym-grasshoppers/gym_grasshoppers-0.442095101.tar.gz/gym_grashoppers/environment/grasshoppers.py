import gym
import numpy as np
import math
import matplotlib.pyplot as plt

from gym_grashoppers.lawn_mower.action.move import Move
from gym_grashoppers.lawn_mower.action.turn import Turn
from gym_grashoppers.lawn_mower.lawn_mower import LawnMower
from gym_grashoppers.util.utils import Utils
from shapely.geometry import GeometryCollection, LineString
from gym_grashoppers.garden.garden import Garden
from typing import Tuple, Dict


class GrassHoppers(gym.Env):
    """This is the grasshoppers environment for the OpenAI gym."""
    metadata = {'render.modes': ['human']}
    _MINIMUM_ANGLE = -180.
    _MAXIMUM_ANGLE = 180.
    _MINIMUM_DISTANCE = 0.
    _MAXIMUM_DISTANCE = math.inf
    _MINIMUM_SPEED = 0
    _MAXIMUM_SPEED = 1

    def __init__(self, garden_grass_height, garden_layers: Dict[str, GeometryCollection], mower_angle: float,
                 mower_radius: float, mower_volume: float, mower_mulching: bool) -> None:
        super().__init__()

        self._garden = Garden(garden_grass_height, garden_layers)
        self._lawn_mower = LawnMower(self._garden.starting_point.x, self._garden.starting_point.y,
                                     mower_angle, mower_radius, mower_volume, mower_mulching)

        self._observation_space = gym.spaces.Box(low=np.array([self._garden.minimum_x,
                                                               self._garden.minimum_y,
                                                               self._MINIMUM_ANGLE,
                                                               self._MINIMUM_SPEED]),
                                                 high=np.array([self._garden.maximum_x,
                                                                self._garden.maximum_y,
                                                                self._MAXIMUM_ANGLE,
                                                                self._MAXIMUM_SPEED]),
                                                 dtype=np.float16)
        self._action_space = gym.spaces.Box(low=np.array([self._MINIMUM_ANGLE, self._MINIMUM_DISTANCE]),
                                            high=np.array([self._MAXIMUM_ANGLE, self._MAXIMUM_DISTANCE]),
                                            dtype=np.float16)
        self._state = self.reset()
        self.viewer = None
        
        
    def step(self, action: Tuple[float, float]) -> Tuple[np.array, float, bool, dict]:
        """This method is used to execute one step in the environment."""
        angle = action[0]
        distance = action[1]

        Turn(self._lawn_mower, angle).execute()
        Move(self._lawn_mower, distance, self._garden).execute()

        reward = self.__calculate_reward(distance)

        self._lawn_mower.current_volume = \
            Utils.calculate_polygon_area(self._garden.mowed_path) * self._garden.grass_height

        self._state = np.array([self._lawn_mower.position.x, self._lawn_mower.position.y,
                                self._lawn_mower.angle, self._lawn_mower.current_volume])
        return self._state, reward, self.__is_done(), {}

    def reset(self) -> np.array:
        """This method is used to reset the environment, including the lawn mower and the garden."""
        self._garden.reset()
        self._lawn_mower.reset(self._garden.starting_point.x, self._garden.starting_point.y)
        return np.array([self._lawn_mower.position.x, self._lawn_mower.position.y,
                         self._lawn_mower.angle, self._lawn_mower.current_volume])

    def render(self, mode='human') -> None:
        """This method is used to show the environment."""
        screen_width = 600
        screen_height = 600
        garden_width = self._garden.maximum_x - self._garden.minimum_x
        garden_height = self._garden.maximum_y - self._garden.minimum_y
        scale_x = screen_width / garden_width
        scale_y = screen_height / garden_height

        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)

            # render grass
            grass = Utils.make_scaled_polygon(self._garden.grass.exterior.coords, scale_x, scale_y,
                                              self._garden.minimum_x, self._garden.minimum_y, (0, 0.5, 0))
            self.viewer.add_geom(grass)

            # render obstacles
            obstacles = [Utils.make_scaled_polygon(obstacle.exterior.coords, scale_x, scale_y, self._garden.minimum_x,
                                                   self._garden.minimum_y, (1, 1, 1)) for obstacle in
                         list(self._garden.obstacles)]
            for obstacle in obstacles:
                self.viewer.add_geom(obstacle)

            # render mowed path
            if self._garden.mowed_path is not None:
                mowed_path = Utils.make_scaled_polygon(self._garden.mowed_path.exterior.coords, scale_x, scale_y,
                                                       self._garden.minimum_x,
                                                       self._garden.minimum_y, (1, 1, 1))
                self.viewer.add_geom(mowed_path)

            # render starting point
            starting_point = Utils.make_positioned_circle(
                Utils.calculate_scaled_radius(self._lawn_mower.position.y, self._lawn_mower.radius) * scale_y,
                (self._garden.starting_point.x - self._garden.minimum_x) * scale_x,
                (self._garden.starting_point.y - self._garden.minimum_y) * scale_y, rgb_color=(0, 0, 1))
            self.viewer.add_geom(starting_point)

            # render compost heap
            compost_heap = Utils.make_positioned_circle(
                Utils.calculate_scaled_radius(self._lawn_mower.position.y, self._lawn_mower.radius) * scale_y,
                (self._garden.compost_heap.x - self._garden.minimum_x) * scale_x,
                (self._garden.compost_heap.y - self._garden.minimum_y) * scale_y, rgb_color=(0.5, 0.2, 0))
            self.viewer.add_geom(compost_heap)

            # render mower
            mower = Utils.make_positioned_circle(
                Utils.calculate_scaled_radius(self._lawn_mower.position.y, self._lawn_mower.radius) * scale_y,
                (self._lawn_mower.position.x - self._garden.minimum_x) * scale_x,
                (self._lawn_mower.position.y - self._garden.minimum_y) * scale_y, rgb_color=(1, 0, 0))
            self.viewer.add_geom(mower)

        self.viewer.render()

    # TODO: this needs to be refined!
    def __calculate_reward(self, distance: float) -> float:
        """This method is used to calculate the reward."""
        return (Utils.calculate_polygon_area(self._garden.mowed_path) *
                self._garden.grass_height) - self._lawn_mower.current_volume - distance

    # TODO: this needs to be refined!
    def __is_done(self) -> bool:
        """This method is used to check whether the garden is fully/enough mowed."""
        current_mowable_area = Utils.calculate_polygon_area(self._garden.grass.boundary
                                                            .buffer(self._lawn_mower.radius)
                                                            .difference(self._garden.grass))
        for obstacle in self._garden.obstacles:
            current_mowable_area -= Utils.calculate_polygon_area(obstacle.union(obstacle.boundary
                                                                                .buffer(self._lawn_mower.radius)))
        current_mowable_area -= Utils.calculate_polygon_area(self._garden.mowed_path)
        return current_mowable_area != 0

