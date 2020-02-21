import math
import json
import matplotlib.pyplot as plt
import pyproj

from functools import partial
from typing import Dict, List, Tuple

from gym.envs.classic_control import rendering
from gym.envs.classic_control.rendering import FilledPolygon, PolyLine
from shapely.ops import transform
from shapely.geometry import GeometryCollection, shape, Point, Polygon


"""This module is used as a collection of helper methods."""

EARTH_RADIUS = 6372800


def calculate_distance(lat_long_coordinate_1: Tuple, lat_long_coordinate_2: Tuple) -> float:
    """This method is used to calculate the distance between two coordinates."""
    latitude_1, longitude_1 = lat_long_coordinate_1
    latitude_2, longitude_2 = lat_long_coordinate_2
    geod = pyproj.Geod(ellps='WGS84')
    # geod.inv returns forward [0] and backward [1] azimuths and distance [2]
    return geod.inv(longitude_1, latitude_1, longitude_2, latitude_2)[2]


def plot_points(points: GeometryCollection, color: str = 'red') -> None:
    """This method is used to show a collection of points."""
    for geometry in points.geoms:
        x, y = geometry.coords.xy
        plt.plot([x], [y], marker='o', markersize=3, color=color)


# TODO: only for testing purpose in this project?

def load_geojson(path: str) -> Dict:
    """This method is used to load the geojson file and convert it to a useful format."""
    try:
        with open(path) as file:
            features = json.load(file)["features"]
    except FileNotFoundError:
        print('We could not find the file on the provided path (\'{}\')!'.format(path))

    grass = GeometryCollection([shape(feature['geometry']).buffer(0) for feature in features
                                if feature['properties']['type'] == 'grass'])
    if grass is None:  # TODO: error-handling!
        print('Provide some grass to get your lawn mower going!')

    obstacles = GeometryCollection([shape(feature['geometry']).buffer(0) for feature in features
                                    if feature['properties']['type'] == 'obstacle'])

    starting_point = GeometryCollection([Point(feature['geometry']['coordinates']) for feature in features
                                         if feature['properties']['type'] == 'starting_point'])
    if starting_point is None:  # TODO: error-handling!
        print('Provide a starting point for your lawn_mower!')

    # TODO: a compost heap is necessary when the lawn mower can't mulch!
    compost_heap = GeometryCollection([Point(feature['geometry']['coordinates']) for feature in features
                                       if feature['properties']['type'] == 'compost_heap'])

    return {
        'obstacles': obstacles,
        'grass': grass,
        'starting_point': starting_point,
        'compost_heap': compost_heap
    }


def get_polygon_max_dimensions(polygon: Polygon) -> List:
    """This method is used to calculate the dimensions of a polygon."""
    points = polygon.minimum_rotated_rectangle.bounds
    return points


def plot_polygon(polygon: Polygon, color: str = 'green') -> None:
    """This method is used to show a polygon."""
    x, y = polygon.exterior.xy
    plt.fill(x, y, color=color)
    for interior in polygon.interiors:
        x, y = interior.xy
        plt.fill(x, y, color='white')


def plot_point(point: Point, color: str = 'red') -> None:
    """This method is used to show a point."""
    x, y = point.coords.xy
    plt.plot([x], [y], marker='o', markersize=3, color=color)


def calculate_polygon_area(polygon: Polygon) -> float:
    """This method is used to calculate the area of a polygon."""
    polygon_aea = transform(
        partial(
            pyproj.transform,
            pyproj.Proj(init='EPSG:4326'),
            pyproj.Proj(
                proj='aea',
                lat_1=polygon.bounds[1],
                lat_2=polygon.bounds[3])),
        polygon)
    return polygon_aea.area


def calculate_scaled_radius(latitude: float, radius: float) -> float:
    """This method is used to scale the radius of the lawn mower to the scale of the garden."""
    latitude_radians = math.radians(latitude)
    new_latitude = math.degrees(
        math.asin(math.sin(latitude_radians) * math.cos(radius / EARTH_RADIUS) +
                  math.cos(latitude_radians) * math.sin(radius / EARTH_RADIUS) *
                  math.cos(0.0)))
    return abs(new_latitude - latitude)


def make_positioned_circle(radius, x, y, res=30, filled=True, rgb_color=(1., 1., 1.)):
    r, g, b = rgb_color
    points = []
    for i in range(res):
        ang = 2 * math.pi * i / res
        points.append((math.cos(ang) * radius + x, math.sin(ang) * radius + y))
    if filled:
        circle = FilledPolygon(points)
    else:
        circle = PolyLine(points, True)
    circle.set_color(r, g, b)
    return circle


def make_scaled_polygon(exterior_coords, scale_x, scale_y, garden_min_x, garden_min_y, rgb_color=(1., 1., 1.)):
    r, g, b = rgb_color
    polygon = rendering.FilledPolygon([tuple(
        scale_x * (value - garden_min_x) if count % 2 == 0 else scale_y * (
                value - garden_min_y)
        for count, value in enumerate(point)) for point in list(exterior_coords)])
    polygon.set_color(r, g, b)
    return polygon
