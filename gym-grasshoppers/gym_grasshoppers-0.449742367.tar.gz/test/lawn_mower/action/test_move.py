import os
import numpy as np

from unittest import TestCase
from gym_grasshoppers.exception.invalid_action_exception import InvalidActionException
from gym_grasshoppers.garden.garden import Garden
from gym_grasshoppers.lawn_mower.action.move import Move
from gym_grasshoppers.lawn_mower.lawn_mower import LawnMower

TEST_DIR = os.path.join(os.path.join(os.path.dirname(__file__), '../..'))


class TestMove(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._standard_distance = 1.1

        valid_geojson_json = open(os.path.join(TEST_DIR, 'resources/valid_geojson.json'))
        valid_geojson_string = valid_geojson_json.read()
        valid_geojson_json.close()
        cls._garden = Garden(0.3, valid_geojson_string)
        cls._lawn_mower = LawnMower(cls._garden.starting_point.x, cls._garden.starting_point.y, 0., 0.1, 0.5, 50., True)

    def test_missing_distance(self):
        with self.assertRaises(InvalidActionException):
            Move(self._lawn_mower, None, self._garden)

    def test_distance_datatype(self):
        with self.assertRaises(InvalidActionException):
            Move(self._lawn_mower, np.array([self._standard_distance]), self._garden)

    def test_negative_distance(self):
        with self.assertRaises(InvalidActionException):
            Move(self._lawn_mower, -self._standard_distance, self._garden)

    # TODO
    def test_execute(self):
        pass

    # TODO
    def test_calculate_new_position(self):
        pass
