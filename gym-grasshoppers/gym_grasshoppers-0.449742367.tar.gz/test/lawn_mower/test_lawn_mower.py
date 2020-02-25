import os
import numpy as np

from unittest import TestCase
from gym_grasshoppers.exception.invalid_lawn_mower_exception import InvalidLawnMowerException
from gym_grasshoppers.garden.garden import Garden
from gym_grasshoppers.lawn_mower.lawn_mower import LawnMower

TEST_DIR = os.path.join(os.path.join(os.path.dirname(__file__), '..'))


class TestLawnMower(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        valid_geojson_json = open(os.path.join(TEST_DIR, 'resources/valid_geojson.json'))
        valid_geojson_string = valid_geojson_json.read()
        valid_geojson_json.close()
        cls._garden = Garden(0.3, valid_geojson_string)

        cls._angle = 0.
        cls._height = 0.1
        cls._radius = 0.25
        cls._maximum_volume = 50.
        cls._mulching = False

    def test_valid_lawn_mower(self):
        lawn_mower = LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle, self._height,
                               self._radius, self._maximum_volume, self._mulching)
        self.assertTrue(lawn_mower)

    def test_missing_angle(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, None, self._height,
                      self._radius, self._maximum_volume, self._mulching)

    def test_angle_datatype(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, np.array([self._angle]),
                      self._height, self._radius, self._maximum_volume, self._mulching)

    def test_too_low_angle(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, -181., self._height,
                      self._radius, self._maximum_volume, self._mulching)

    def test_too_high_angle(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, 181., self._height,
                      self._radius, self._maximum_volume, self._mulching)

    def test_missing_height(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle, None,
                      self._radius, self._maximum_volume, self._mulching)

    def test_height_datatype(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle,
                      np.array([self._height]), self._radius, self._maximum_volume, self._mulching)

    def test_negative_height(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle, -self._height,
                      self._radius, self._maximum_volume, self._mulching)

    def test_missing_radius(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle, self._height,
                      None, self._maximum_volume, self._mulching)

    def test_radius_datatype(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle, self._height,
                      np.array([self._radius]), self._maximum_volume, self._mulching)

    def test_negative_radius(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle, self._height,
                      -self._radius, self._maximum_volume, self._mulching)

    def test_missing_maximum_volume(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle, self._height,
                      self._radius, None, self._mulching)

    def test_maximum_volume_datatype(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle, self._height,
                      self._radius, np.array([self._maximum_volume]), self._mulching)

    def test_negative_maximum_volume(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle, self._height,
                      self._radius, -self._maximum_volume, self._mulching)

    def test_missing_mulching(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle, self._height,
                      self._radius, self._maximum_volume, None)

    def test_mulching_datatype(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle, self._height,
                      self._radius, self._maximum_volume, np.array([self._mulching]))

    def test_maximum_volume_necessity(self):
        with self.assertRaises(InvalidLawnMowerException):
            LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle, self._height,
                      self._radius, 0., self._mulching)

    def test_reset(self):
        lawn_mower = LawnMower(self._garden.starting_point.x, self._garden.starting_point.y, self._angle, self._height,
                               self._radius, self._maximum_volume, self._mulching)
        lawn_mower.angle = 20.
        lawn_mower.reset(self._garden.starting_point.x, self._garden.starting_point.y)
        self.assertEqual(lawn_mower.angle, self._angle)
