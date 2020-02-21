import numpy
import pyproj
import shapely
import shapely.wkt
import shapely.ops

from h3 import h3


def rectangular_cells(bounds, n, m):
    """
    Creates an iterator that returns the specified number of rectangular grid
    cell centers in each dimension within the provided bounds.
    :param tuple(tuple) bounds: The bounds used as border for the returned grid
        cells given as (xmin, ymin, xmax, ymax).
    :param int n: Number of grid cells in x dimension.
    :param int m: Number of grid cells in y dimension.
    :return: Iterator that yields grid cell centers.
    :rtype: Iterator(shapely.geometry.Point)
    """
    xmin, ymin, xmax, ymax = bounds
    radius_x = (xmax - xmin) / (2 * n)
    radius_y = (ymax - ymin) / (2 * m)
    for y in numpy.linspace(ymin + radius_y, ymax - radius_y, m):
        for x in numpy.linspace(xmin + radius_x, xmax - radius_x, n):
            center = shapely.geometry.Point(x, y)
            yield center


def create_grid(polygon, n=10, m=10, wkt=True):
    """
    Creates an iterator that yields rectangular grid cells at the specified
    number in each dimension and within the provided rectangular bounds of the
    given polygon.

    .. note:: The `polygon` can not be a MULTIPOLYGON (because holes are not
    supported).

    :param str polygon: Polygon in WKT format containing the area of interest
        (without holes) from which the bounds are computed.
    :param int n: Number of grid cell centers in the x dimension of the bounds.
    :param int m: Number of grid cell centers in the y dimension of the bounds.
    :param bool wkt: Should the final output be returned as a WKT formatted
        point? If False, returns a shapely.geometry.Point object, else a string.
    :return: Grid cell centers in the specified format.
    :rtype: Iterator(shapely.geometry.Point or str)
    """
    bounds = shapely.wkt.loads(polygon).bounds

    for center in rectangular_cells(bounds, n, m):
        if wkt:
            center = str(center)
        yield center


def h3_polyfill_buffer(polygon, resolution, buffer=False,
                       source_crs='epsg:4326', dest_crs='epsg:4839'):
    """
    Get hexagons for a given wkt region

    This function works as a wrapper for the h3 polyfill function, extending
    its functionality by adding a buffer around the provided polygon if
    `buffer` is set to `True`. Adding a buffer guarantees that h3 polyfill will
    return a non empty list of hexagons. Otherwise, if the resolution of the
    hexagons is larger than certain areas of the polygon, polyfill returns an
    empty list.
    The size of the buffer will be set to the edge length of the specified
    hexagon resolution.

    .. note:: The `polygon` can not be a MULTIPOLYGON (because holes are not
    supported).

    :param str polygon: Polygon in WKT format containing the area of interest
        from which the bounds are computed. `polygon` is restricted to
        'POLYGON' WKTs. Other geometries are not supported!
        Example: 'POLYGON ((long lat, long lat))'
    :param int resolution: The hexagon resolution to use (0-15)
    :param buffer: Determines if the function will buffer the polygon (
        `buffer=True`) or not (`buffer=False`). Default: `buffer=False`. If
        `buffer=True`, the buffer size will be the edge length of the specified
        hexagon resolution.
    :param str source_crs: Source CRS of the polygon
    :param str dest_crs: Destination CRS used to calculate the buffer. Must
        be metric, measured in meter. Will not be checked!
    :return: Set of hex addresses
    """
    polygon_geom = polygon_str_to_geom(polygon)
    if buffer:
        buffer_size = h3.edge_length(resolution, 'm')
        polygon_geom = extract_buffer_exterior_polygon(
            polygon_geom,
            buffer_size,
            source_crs,
            dest_crs
        )
    hexagons = h3_polyfill_on_geometry(polygon_geom, resolution)
    return hexagons


def h3_polyfill_bbox(polygon, resolution):
    """
    Get hexagons for a given wkt region

    This function works as a wrapper for the h3 polyfill function. Instead of
    using the provided polygon, we first extract the bounding box, build a
    new polygon, and apply the polyfill function on the bounding box polygon.
    Using the bounding box yields a more complete coverage for wiggling
    polygons.
    Otherwise, if the resolution of the hexagons is larger than
    certain areas of the polygon, polyfill returns an empty list.

    .. note:: The `polygon` can not be a MULTIPOLYGON (because holes are not
    supported).

    :param str polygon: Polygon in WKT format containing the area of interest
        from which the bounds are computed. `polygon` is restricted to
        'POLYGON' WKTs. Other geometries are not supported!
        Example: 'POLYGON ((long lat, long lat))'
    :param int resolution: The hexagon resolution to use (0-15)
    :return: Set of hex addresses
    """
    polygon_geom = polygon_str_to_geom(polygon)
    polygon_bbox_geom = extract_bbox_polygon(polygon_geom)
    hexagons = h3_polyfill_on_geometry(polygon_bbox_geom, resolution)
    return hexagons


def polygon_str_to_geom(polygon):
    """
    Convert WKT encoded polygon string into shapely geometry polygon object.

    :param str polygon: Polygon in WKT format containing the area of interest
        from which the bounds are computed. `polygon` is restricted to
        'POLYGON' WKTs. Other geometries are not supported!
        Example: 'POLYGON ((long lat, long lat))'
    :return: Shapely geometry Polygon object
    """
    polygon = polygon.strip()
    check_polygon_wkt(polygon)
    polygon_geom = shapely.wkt.loads(polygon)
    return polygon_geom


def check_polygon_wkt(polygon):
    """
    Checks if the provided wkt encoded polygon string starts with POLYGON

    :param str polygon: Polygon in WKT format containing the area of interest
        from which the bounds are computed. `polygon` is restricted to
        'POLYGON' WKTs. Other geometries are not supported!
        Example: 'POLYGON ((long lat, long lat))'
    :return: None
    :raise: ValueError
    """
    if not polygon.startswith('POLYGON'):
        raise ValueError("polygon string must start with POLYGON; got string "
                         "starting with {}".format(polygon[0:10]))


def extract_bbox_polygon(polygon):
    """
    Return the bounding box of the provided polygon as new polygon object

    :param shapely.geometry.Polygon polygon: Shapely geometry polygon object
    :return: Shapely geometry Polygon object
    """
    min_lon, min_lat, max_lon, max_lat = polygon.bounds
    lon_list = [min_lon, max_lon, max_lon, min_lon]
    lat_list = [max_lat, max_lat, min_lat, min_lat]
    polygon_bbox_geom = shapely.geometry.Polygon(zip(lon_list, lat_list))
    return polygon_bbox_geom


def extract_buffer_exterior_polygon(polygon, buffer_size,
                                    source_crs='epsg:4326',
                                    dest_crs='epsg:4839'):
    """
    Create a buffer around the given polygon and return it.

    :param shapely.geometry.Polygon polygon: Shapely geometry polygon object
    :param int buffer_size: Size of the buffer in meters
    :param str source_crs: Source CRS of the polygon
    :param str dest_crs: Destination CRS used to calculate the buffer. Must
        be metric, measured in meter. Will not be checked!
    :return:
    """
    # transform to metric crs
    # https://gis.stackexchange.com/questions/127427/transforming-shapely
    # -polygon-and-multipolygon-objects
    projection = pyproj.Transformer.from_proj(
        pyproj.Proj(init=source_crs),
        pyproj.Proj(init=dest_crs)
    )
    polygon_geom = shapely.ops.transform(projection.transform, polygon)
    # add buffer
    # https://gis.stackexchange.com/questions/97963/how-to-surround-a-polygon
    # -object-with-a-corridor-of-specified-width/97964
    polygon_geom = shapely.geometry.Polygon(polygon_geom.buffer(
        distance=buffer_size).exterior)
    # transform back to origin crs
    projection = pyproj.Transformer.from_proj(
        pyproj.Proj(init=dest_crs),
        pyproj.Proj(init=source_crs)
    )
    polygon = shapely.ops.transform(projection.transform, polygon_geom)
    return polygon


def h3_polyfill_on_geometry(polygon, resolution):
    """
    Transforms the shapely polygon object to geojson and applies the
    h3.polyfill function on it.

    :param shapely.geometry.Polygon polygon: Shapely geometry polygon object
    :param int resolution: The hexagon resolution to use (0-15)
    :return: Set of hex addresses
    """
    polygon_geojson = shapely.geometry.mapping(polygon)
    hexagons = list(h3.polyfill(geo_json=polygon_geojson,
                                res=resolution,
                                geo_json_conformant=True))
    return hexagons
