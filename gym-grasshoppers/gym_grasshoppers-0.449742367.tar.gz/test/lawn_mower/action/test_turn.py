import os
import numpy as np

from unittest import TestCase
from gym_grasshoppers.exception.invalid_action_exception import InvalidActionException
from gym_grasshoppers.garden.garden import Garden
from gym_grasshoppers.lawn_mower.action.turn import Turn
from gym_grasshoppers.lawn_mower.lawn_mower import LawnMower

TEST_DIR = os.path.join(os.path.join(os.path.dirname(__file__), '../..'))


class TestTurn(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._standard_angle = 1.1

        valid_geojson_json = open(os.path.join(TEST_DIR,'resources/valid_geojson.json'))
        valid_geojson_string = valid_geojson_json.read()
        valid_geojson_json.close()
        garden = Garden(0.3, valid_geojson_string)
        cls._lawn_mower = LawnMower(garden.starting_point.x, garden.starting_point.y, 0., 0.1, 0.5, 50., False)

    def test_missing_angle(self):
        with self.assertRaises(InvalidActionException):
            Turn(self._lawn_mower, None)

    def test_angle_datatype(self):
        with self.assertRaises(InvalidActionException):
            Turn(self._lawn_mower, np.array([self._standard_angle]))

    def test_too_low_angle(self):
        with self.assertRaises(InvalidActionException):
            Turn(self._lawn_mower, -181.)

    def test_too_high_angle(self):
        with self.assertRaises(InvalidActionException):
            Turn(self._lawn_mower, 181.)

    def test_execute(self):
        new_angle = self._standard_angle
        Turn(self._lawn_mower, new_angle).execute()
        self.assertEqual(self._lawn_mower.angle, new_angle)
