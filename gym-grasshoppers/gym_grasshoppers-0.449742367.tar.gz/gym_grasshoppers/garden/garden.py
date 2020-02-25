import json
import gym_grasshoppers.util.utils as utils

from typing import List, Tuple
from json import JSONDecodeError
from shapely.geometry import Polygon, Point, shape
from gym_grasshoppers.exception.invalid_garden_exception import InvalidGardenException
from gym_grasshoppers.exception.invalid_geojson_exception import InvalidGeojsonException


class Garden:
    """This class is used to represent a garden."""

    def __init__(self, grass_height: float, geojson: str) -> None:
        super().__init__()

        self._grass_height = grass_height
        if self._grass_height is None:
            raise InvalidGardenException('The height of the grass of the garden is missing!')
        elif not isinstance(self._grass_height, float):
            raise InvalidGardenException('The height of the grass of the garden is not a float!')
        elif self._grass_height <= 0.:
            raise InvalidGardenException('The height of the grass of the garden must be higher than 0!')

        if geojson is None or geojson == '':
            raise InvalidGardenException('The GeoJSON containing the garden is missing!')
        else:
            self._grass, self._obstacles, self._starting_point, self._compost_heap = self.__parse_garden_layers(geojson)

        self._minimum_x, self._minimum_y, self._maximum_x, self._maximum_y = self.__calculate_dimensions(self._grass)
        self._mowed_path = None

    @property
    def grass_height(self) -> float:
        return self._grass_height

    @property
    def grass(self) -> Polygon:
        return self._grass

    @property
    def obstacles(self) -> List[Polygon]:
        return self._obstacles

    @property
    def starting_point(self) -> Point:
        return self._starting_point

    @property
    def compost_heap(self) -> Point:
        return self._compost_heap

    @property
    def minimum_x(self) -> float:
        return self._minimum_x

    @property
    def minimum_y(self) -> float:
        return self._minimum_y

    @property
    def maximum_x(self) -> float:
        return self._maximum_x

    @property
    def maximum_y(self) -> float:
        return self._maximum_y

    @property
    def mowed_path(self) -> Polygon:
        return self._mowed_path

    # TODO: compost_heap -> Polygon (+ add to obstacles?)
    def __parse_garden_layers(self, geojson: str) -> Tuple[Polygon, List[Polygon], Point, Point]:
        """This method is used to load the geojson string and convert it to a useful format."""
        try:
            features = json.loads(geojson)["features"]
        except (JSONDecodeError, KeyError):
            raise InvalidGeojsonException('The format of the provided GeoJSON is not valid!')

        grass = [Polygon(shape(feature['geometry'])) for feature in features
                 if feature['properties']['type'] == 'grass']

        if len(grass) == 1:
            grass = grass[0]
        else:
            if len(grass) == 0:
                raise InvalidGeojsonException('The garden is missing some grass in the provided GeoJSON!')
            else:
                raise InvalidGeojsonException('There is more than one garden present in the provided GeoJSON!')

        obstacles = [Polygon(shape(feature['geometry'])) for feature in features
                     if feature['properties']['type'] == 'obstacle']

        for obstacle in obstacles:
            if not grass.contains(obstacle):
                raise InvalidGeojsonException('One of the obstacles falls outside the garden in the provided GeoJSON!')

        starting_point = [Point(shape(feature['geometry'])) for feature in features
                          if feature['properties']['type'] == 'starting_point']

        if len(starting_point) == 1:
            starting_point = starting_point[0]
            if not grass.contains(starting_point):
                raise InvalidGeojsonException('The starting point of the lawn mower falls outside the garden in the '
                                              'provided GeoJSON!')
        else:
            if len(starting_point) == 0:
                raise InvalidGeojsonException('The lawn mower is missing a starting point in the provided GeoJSON!')
            else:
                raise InvalidGeojsonException('There is more than one starting point present in the provided GeoJSON!')

        compost_heap = [Point(shape(feature['geometry'])) for feature in features
                        if feature['properties']['type'] == 'compost_heap']

        if len(compost_heap) == 1:
            compost_heap = compost_heap[0]
            if not grass.contains(compost_heap):
                raise InvalidGeojsonException('The compost heap falls outside the garden in the provided GeoJSON!')
        else:
            if len(compost_heap) == 0:
                compost_heap = None
            else:
                raise InvalidGeojsonException('There is more than one compost heap present in the provided GeoJSON!')

        return grass, obstacles, starting_point, compost_heap

    def __calculate_dimensions(self, garden: Polygon) -> list:
        """This method is used to calculate the dimensions of the garden."""
        return utils.get_polygon_max_dimensions(garden)

    def extend_mowed_path(self, mowed_path: Polygon) -> None:
        """This method is used to extend the mowed path of the garden."""
        if self._mowed_path is None:
            self._mowed_path = mowed_path
        else:
            self._mowed_path = self._mowed_path.union(mowed_path)

    def reset(self) -> None:
        """This method is used to reset the garden to its initial values."""
        self._mowed_path = None
