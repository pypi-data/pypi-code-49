import os
import numpy as np

from unittest import TestCase
from shapely.geometry import LineString, Point, shape
from gym_grasshoppers.exception.invalid_garden_exception import InvalidGardenException
from gym_grasshoppers.exception.invalid_geojson_exception import InvalidGeojsonException
from gym_grasshoppers.garden.garden import Garden

TEST_DIR = os.path.join(os.path.join(os.path.dirname(__file__), '..'))


class TestGarden(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._standard_garden_grass_height = 1.1

        valid_geojson_json = open(os.path.join(TEST_DIR, 'resources/valid_geojson.json'))
        cls._valid_geojson_string = valid_geojson_json.read()
        valid_geojson_json.close()

    def test_valid_garden(self):
        garden = Garden(self._standard_garden_grass_height, self._valid_geojson_string)
        self.assertTrue(garden)

    def test_missing_grass_height(self):
        with self.assertRaises(InvalidGardenException):
            Garden(None, self._valid_geojson_string)

    def test_grass_height_datatype(self):
        with self.assertRaises(InvalidGardenException):
            Garden(np.array([self._standard_garden_grass_height]), self._valid_geojson_string)

    def test_negative_grass_height(self):
        with self.assertRaises(InvalidGardenException):
            Garden(-self._standard_garden_grass_height, self._valid_geojson_string)

    def test_missing_geojson(self):
        with self.assertRaises(InvalidGardenException):
            Garden(self._standard_garden_grass_height, '')

    def test_invalid_format_geojson(self):
        invalid_geojson_json = open(os.path.join(TEST_DIR, 'resources/invalid_format_geojson.json'))
        invalid_geojson_string = invalid_geojson_json.read()
        invalid_geojson_json.close()
        with self.assertRaises(InvalidGeojsonException):
            Garden(self._standard_garden_grass_height, invalid_geojson_string)

    def test_missing_grass_geojson(self):
        missing_grass_geojson_json = open(os.path.join(TEST_DIR, 'resources/missing_grass_geojson.json'))
        missing_grass_geojson_string = missing_grass_geojson_json.read()
        missing_grass_geojson_json.close()
        with self.assertRaises(InvalidGeojsonException):
            Garden(self._standard_garden_grass_height, missing_grass_geojson_string)

    def test_multiple_grass_geojson(self):
        multiple_grass_geojson_json = open(os.path.join(TEST_DIR, 'resources/multiple_grass_geojson.json'))
        multiple_grass_geojson_string = multiple_grass_geojson_json.read()
        multiple_grass_geojson_json.close()
        with self.assertRaises(InvalidGeojsonException):
            Garden(self._standard_garden_grass_height, multiple_grass_geojson_string)

    def test_outside_obstacle_geojson(self):
        outside_obstacle_geojson_json = open(os.path.join(TEST_DIR, 'resources/outside_obstacle_geojson.json'))
        outside_obstacle_geojson_string = outside_obstacle_geojson_json.read()
        outside_obstacle_geojson_json.close()
        with self.assertRaises(InvalidGeojsonException):
            Garden(self._standard_garden_grass_height, outside_obstacle_geojson_string)

    def test_outside_starting_point_geojson(self):
        outside_starting_point_geojson_json = open(os.path.join(TEST_DIR, 'resources/outside_starting_point_geojson.json'))
        outside_starting_point_geojson_string = outside_starting_point_geojson_json.read()
        outside_starting_point_geojson_json.close()
        with self.assertRaises(InvalidGeojsonException):
            Garden(self._standard_garden_grass_height, outside_starting_point_geojson_string)

    def test_missing_starting_point_geojson(self):
        missing_starting_point_geojson_json = open(os.path.join(TEST_DIR, 'resources/missing_starting_point_geojson.json'))
        missing_starting_point_geojson_string = missing_starting_point_geojson_json.read()
        missing_starting_point_geojson_json.close()
        with self.assertRaises(InvalidGeojsonException):
            Garden(self._standard_garden_grass_height, missing_starting_point_geojson_string)

    def test_multiple_starting_points_geojson(self):
        multiple_starting_points_geojson_json = open(os.path.join(TEST_DIR, 'resources/multiple_starting_points_geojson.json'))
        multiple_starting_points_geojson_string = multiple_starting_points_geojson_json.read()
        multiple_starting_points_geojson_json.close()
        with self.assertRaises(InvalidGeojsonException):
            Garden(self._standard_garden_grass_height, multiple_starting_points_geojson_string)

    def test_outside_compost_heap_geojson(self):
        outside_compost_heap_geojson_json = open(os.path.join(TEST_DIR, 'resources/outside_compost_heap_geojson.json'))
        outside_compost_heap_geojson_string = outside_compost_heap_geojson_json.read()
        outside_compost_heap_geojson_json.close()
        with self.assertRaises(InvalidGeojsonException):
            Garden(self._standard_garden_grass_height, outside_compost_heap_geojson_string)

    def test_multiple_compost_heaps_geojson(self):
        multiple_compost_heaps_geojson_json = open(os.path.join(TEST_DIR, 'resources/multiple_compost_heaps_geojson.json'))
        multiple_compost_heaps_geojson_string = multiple_compost_heaps_geojson_json.read()
        multiple_compost_heaps_geojson_json.close()
        with self.assertRaises(InvalidGeojsonException):
            Garden(self._standard_garden_grass_height, multiple_compost_heaps_geojson_string)

    def test_extend_mowed_path(self):
        garden = Garden(self._standard_garden_grass_height, self._valid_geojson_string)
        garden.extend_mowed_path(shape(LineString([Point(0, 0), Point(1, 1)]).buffer(1)))
        area_first_mowed_path = garden.mowed_path.area
        garden.extend_mowed_path(shape(LineString([Point(0, 1), Point(1, 2)]).buffer(1)))
        area_second_mowed_path = garden.mowed_path.area
        self.assertGreater(area_second_mowed_path, area_first_mowed_path)

    def test_calculate_dimensions(self):
        garden = Garden(self._standard_garden_grass_height, self._valid_geojson_string)
        self.assertEqual(garden.minimum_x, 4.069246058049719)
        self.assertEqual(garden.maximum_x, 4.070713520050049)
        self.assertEqual(garden.minimum_y, 51.2092480501759)
        self.assertEqual(garden.maximum_y, 51.21020806267038)

    def test_reset(self):
        garden = Garden(self._standard_garden_grass_height, self._valid_geojson_string)
        garden.extend_mowed_path(shape(LineString([Point(0, 0), Point(1, 1)])))
        garden.reset()
        self.assertIsNone(garden.mowed_path)
