from typing import Dict, List
from shapely.geometry import Polygon, GeometryCollection, Point
from gym_grashoppers.util.utils import Utils


class Garden:
    """This class is used to represent a garden."""

    def __init__(self, grass_height, layers: Dict[str, GeometryCollection]) -> None:
        super().__init__()
        self._grass_height = grass_height
        self._obstacles = layers['obstacles']
        self._grass = layers['grass'][0]
        self._starting_point = layers['starting_point'][0]
        self._compost_heap = layers['compost_heap'][0]  # TODO: compost heap is not always necessary!
        self._minimum_x, self._minimum_y, self._maximum_x, self._maximum_y = self.__calculate_dimensions(self._grass)
        self._mowed_path = None

    @property
    def grass_height(self) -> float:
        return self._grass_height

    @property
    def grass(self) -> Polygon:
        return self._grass

    @property
    def obstacles(self) -> GeometryCollection:
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

    def __calculate_dimensions(self, garden: Polygon) -> list:
        """This method is used to calculate the dimensions of the garden."""
        return Utils.get_polygon_max_dimensions(garden)

    def extend_mowed_path(self, mowed_path: Polygon) -> None:
        """This method is used to extend the mowed path of the garden."""
        if self._mowed_path is None:
            self._mowed_path = mowed_path
        else:
            self._mowed_path = self._mowed_path.union(mowed_path)

    def reset(self) -> None:
        """This method is used to reset the garden to its initial values."""
        self._mowed_path = None
