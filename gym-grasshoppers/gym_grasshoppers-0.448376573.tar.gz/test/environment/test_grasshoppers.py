import os
from unittest import TestCase

from gym_grasshoppers.environment.grasshoppers import GrassHoppers
from gym_grasshoppers.exception.invalid_geojson_exception import InvalidGeojsonException

TEST_DIR = os.path.join(os.path.join(os.path.dirname(__file__), '..'))


class TestGrassHoppers(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._garden_grass_height = 1.1
        cls._valid_geojson_json = open(os.path.join(TEST_DIR, 'resources/valid_geojson.json'))
        cls._valid_geojson_string = cls._valid_geojson_json.read()
        cls._valid_geojson_json.close()

        cls._mower_angle = 0.
        cls._mower_height = 0.1
        cls._mower_radius = 0.25
        cls._mower_volume = 50.
        cls._mower_mulching = True

    def test_valid_environment(self):
        environment = GrassHoppers(self._garden_grass_height, self._valid_geojson_string, self._mower_angle,
                                   self._mower_height, self._mower_radius, self._mower_volume, self._mower_mulching)
        self.assertTrue(environment)

    def test_compost_heap_necessity(self):
        missing_compost_heap_geojson_json = open(os.path.join(TEST_DIR, 'resources/missing_compost_heap_geojson.json'))
        missing_compost_heap_geojson_string = missing_compost_heap_geojson_json.read()
        missing_compost_heap_geojson_json.close()
        with self.assertRaises(InvalidGeojsonException):
            GrassHoppers(self._garden_grass_height, missing_compost_heap_geojson_string, self._mower_angle,
                         self._mower_height, self._mower_radius, self._mower_volume, False)

    def test_position_starting_point(self):
        with self.assertRaises(InvalidGeojsonException):
            GrassHoppers(self._garden_grass_height, self._valid_geojson_string, self._mower_angle,
                         self._mower_height, 4., self._mower_volume, self._mower_mulching)

    # TODO: test other methods
