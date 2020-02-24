import os
from unittest import TestCase

from gym_grasshoppers.garden.garden import Garden
from gym_grasshoppers.lawn_mower.lawn_mower import LawnMower

TEST_DIR = os.path.join(os.path.join(os.path.dirname(__file__), '../..'))


class TestEmpty(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        valid_geojson_json = open(os.path.join(TEST_DIR, 'resources/valid_geojson.json'))
        valid_geojson_string = valid_geojson_json.read()
        valid_geojson_json.close()
        garden = Garden(0.3, valid_geojson_string)
        cls._lawn_mower = LawnMower(garden.starting_point.x, garden.starting_point.y, 0., 0.1, 0.5, 50., False)

    # TODO
    def test_execute(self):
        pass
