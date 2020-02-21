from typing import List, Tuple
from shapely.geometry import Polygon, Point
from gym_grashoppers.exception.invalid_garden_exception import InvalidGardenException
import gym_grashoppers.util.utils as utils


class Garden:
    """This class is used to represent a garden."""

    def __init__(self, grass_height, geojson: str) -> None:
        super().__init__()

        self._grass_height = grass_height
        if self._grass_height is None or self._grass_height <= 0.:
            raise InvalidGardenException('The height of the grass of the garden is missing!')

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
        return utils.load_geojson(geojson)

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
