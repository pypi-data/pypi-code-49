# -*- coding: utf-8 -*-
"""
Vector processing functions.
"""
import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas.tools import sjoin
from shapely.geometry import Point, Polygon
from gistools.util import load_geo_data
from pycrs import parse
from scipy.spatial import cKDTree

#########################################
### Functions


def kd_nearest(gdf_from, gdf_to, id_col, max_distance=np.inf):
    """
    Function to find the nearest point from gdf_from to gdf_to given an id_col in gdf_to. Uses the scipy function cKDTree.

    Parameters
    ----------
    gdf_from : GeoSeries or GeoDataFrame
        Source points.
    gdf_to : GeoDataFrame
        Points to find the nearest to gdf_from.
    id_col : str
        The ID column in gdf_to as an identifier.
    max_distance : non-negative float, optional
        Return only neighbors within this distance. This is used to prune tree searches, so if you are doing a series of nearest-neighbor queries, it may help to supply the distance to the nearest neighbor of the most recent point.

    Returns
    -------
    GeoDataFrame
    """
    new_gdf = gdf_from.copy()
    nA = np.array(list(zip(gdf_from.geometry.x, gdf_from.geometry.y)))
    nB = np.array(list(zip(gdf_to.geometry.x, gdf_to.geometry.y)))
    btree = cKDTree(nB)
    dist, idx = btree.query(nA, k=1, distance_upper_bound=max_distance)

    new_gdf['distance'] = dist.astype(int)
    new_gdf[id_col] = gdf_to.reset_index(drop=True).loc[idx, id_col].values

    return new_gdf


def sel_sites_poly(pts, poly, buffer_dis=0):
    """
    Simple function to select points within a single polygon. Optional buffer.

    Parameters
    ----------
    pts: GeoDataFrame or str
        A GeoDataFrame of points with the site names as the index. Or a shapefile with the first column as the site names.
    poly: GeoDataFrame or str
        A GeoDataFrame of polygons with the site names as the index. Or a shapefile with the first column as the site names.
    buffer_dis: int
        Distance in coordinate system units for a buffer around the polygon.

    Returns
    -------
    GeoDataFrame
        Of points.
    """

    #### Read in data
    gdf_pts = load_geo_data(pts)
    gdf_poly = load_geo_data(poly)

    #### Perform vector operations for initial processing
    ## Dissolve polygons by id
    poly2 = gdf_poly.unary_union

    ## Create buffer
    poly_buff = poly2.buffer(buffer_dis)

    ## Select only the vcn sites within the buffer
    points2 = gdf_pts[gdf_pts.within(poly_buff)]

    return points2


def pts_poly_join(pts, poly, poly_id_col):
    """
    Simple function to join the attributes of the polygon to the points. Specifically for an ID field in the polygon.

    Parameters
    ----------
    pts: GeoDataFrame
        A GeoDataFrame of points with the site names as the index.
    poly: GeoDataFrame
        A GeoDataFrame of polygons with the site names as the index.
    poly_id_col: str or list of str
        The names of the columns to join.

    Returns
    -------
    GeoDataFrame
    """
    #### Read in data
    gdf_pts = load_geo_data(pts)
    gdf_poly = load_geo_data(poly)

    if isinstance(poly_id_col, str):
        poly_id_col = [poly_id_col]
    cols = poly_id_col.copy()
    cols.extend(['geometry'])
    poly2 = gdf_poly[cols].copy()
    poly3 = poly2.dissolve(poly_id_col).reset_index()

    join1 = sjoin(gdf_pts.copy(), poly3.copy(), how='inner', op='within')
    cols = set(gdf_pts.columns)
    cols.update(set(poly3.columns))
    join1.drop([i for i in join1.columns if i not in cols], axis=1, inplace=True)

    return join1, poly3


def precip_catch_agg(sites, site_precip, id_area):
    """
    Function to aggregate time series of catchments into their all of their upstream catchments.
    """

    #    n_sites = len(sites) + len(singles)
    #    if n_sites != len(site_precip.columns):
    #        print("Site numbers between data sets are not the same!")
    output = site_precip.copy()

    id_area2 = id_area.area
    area_out = pd.concat([id_area2, id_area2], axis=1)
    area_out.columns = ['id_area', 'tot_area']
    site_precip2 = site_precip.mul(id_area2.values.flatten(), axis=1)

    for i in sites.index:
        set1 = np.insert(sites.loc[i, :].dropna().values, 0, i).astype(int)
        tot_area = int(id_area2[np.in1d(id_area2.index, set1)].sum())
        output.loc[:, i] = (site_precip2[set1].sum(axis=1) / tot_area).values
        area_out.loc[i, 'tot_area'] = tot_area

    return output.round(2), area_out.round()


def xy_to_gpd(id_col, x_col, y_col, df=None, crs=2193):
    """
    Function to convert a DataFrame with x and y coordinates to a GeoDataFrame.

    Parameters
    ----------
    df: Dataframe
        The DataFrame with the location data.
    id_col: str or list of str
        The column(s) from the dataframe to be returned. Either a one name string or a list of column names.
    xcol: str or ndarray
        Either the column name that has the x values within the df or an array of x values.
    ycol: str or ndarray
        Same as xcol except for y.
    crs: int
        The projection of the data.

    Returns
    -------
    GeoDataFrame
        Of points.
    """

    if isinstance(x_col, str):
        geometry = [Point(xy) for xy in zip(df[x_col], df[y_col])]
    else:
        geometry = [Point(xy) for xy in zip(x_col, y_col)]
    if isinstance(id_col, str) & (df is not None):
        id_data = df[id_col]
    elif isinstance(id_col, list):
        if df is not None:
            id_data = df[id_col]
        else:
            id_data = id_col
    elif isinstance(id_col, (np.ndarray, pd.Series, pd.Index)):
        id_data = id_col
    else:
        raise ValueError('id_data could not be determined')
    if isinstance(crs, int):
        crs1 = parse.from_epsg_code(crs).to_proj4()
    elif isinstance(crs, (str, dict)):
        crs1 = crs
    else:
        raise ValueError('crs must be an int, str, or dict')
    gpd1 = gpd.GeoDataFrame(id_data, geometry=geometry, crs=crs1)
    return gpd1


def point_to_poly_apply(geo, side_len):
    """
    Apply function for a GeoDataFrame to convert a point to a square polygon. Input is a shapely point. Output is a shapely polygon.

    Parameters
    ----------
    geo: Point
        A shapely point.
    side_len: int
        The side length of the square (in the units of geo).

    Returns
    -------
    Shpaely Polygon
    """

    half_side = side_len * 0.5
    l1 = Polygon([[geo.x + half_side, geo.y + half_side], [geo.x + half_side, geo.y - half_side],
                  [geo.x - half_side, geo.y - half_side], [geo.x - half_side, geo.y + half_side]])
    return l1


def points_grid_to_poly(geodataframe, id_col):
    """
    Function to convert a GeoDataFrame of evenly spaced gridded points to square polygons. Output is a GeoDataFrame of the same length as input.

    geodataframe: GeoDataFrame
        GeoDataFrame of gridded points with an id column.
    id_col: str or list of str
        The id column(s) name(s).

    Returns
    -------
    GeoDataFrame
    """
    gdf1 = geodataframe.copy()

    geo1a = pd.Series(gdf1.geometry.apply(lambda j: j.x))
    geo1b = geo1a.shift()

    side_len1 = (geo1b - geo1a).abs()
    side_len = side_len1[side_len1 > 0].min()
    gdf1['geometry'] = gdf1.apply(lambda j: point_to_poly_apply(j.geometry, side_len=side_len), axis=1)
    return gdf1


def closest_line_to_pts(pts, lines, line_site_col, max_distance=1000):
    """
    Function to determine the line closest to each point. Inputs must be GeoDataframes.

    Parameters
    ----------
    pts: GeoDataFrame
        The points input.
    lines: GeoDataFrame
        The lines input.
    line_site_col: str
        The site column from the 'lines' that should be retained at the output.
    buffer_dis: int
        The max distance from each point to search for a line. Try to use the shortest buffer_dis that will cover all of your points as a larger buffer_dis will significantly slow down the operation.

    Returns
    -------
    GeoDataFrame
    """
    ## Load data
    gdf_pts = load_geo_data(pts)
    gdf_lines = load_geo_data(lines)

    ## Process data
    pts_line_seg = gpd.GeoDataFrame()
    for i in gdf_pts.index:
        pts_seg = gdf_pts.loc[[i]]
        dis = 50
        while dis < max_distance:
            bound = pts_seg.buffer(dis).unary_union
            lines1 = gdf_lines[gdf_lines.intersects(bound)]
            if lines1.empty:
                dis = dis + 50
            else:
                break
        if lines1.empty:
            continue
        near1 = lines1.distance(gdf_pts.geometry[i]).idxmin()
        line_seg1 = lines1.loc[near1, line_site_col]
        pts_seg[line_site_col] = line_seg1
        pts_line_seg = pd.concat([pts_line_seg, pts_seg])
    #        print(i)

    ### Determine points that did not find a line
    mis_pts = gdf_pts.loc[~gdf_pts.index.isin(pts_line_seg.index)]
    if not mis_pts.empty:
        print(mis_pts)
        print('Did not find a line segment for these sites')

    return pts_line_seg


def multipoly_to_poly(geodataframe):
    """
    Function to convert a GeoDataFrame with some MultiPolygons to only polygons. Creates additional rows in the GeoDataFrame.

    Parameters
    ----------
    geodataframe: GeoDataFrame

    Returns
    -------
    GeoDataFrame
    """

    gpd2 = gpd.GeoDataFrame()
    for i in geodataframe.index:
        geom1 = geodataframe.loc[[i]]
        geom2 = geom1.loc[i, 'geometry']
        if geom2.type == 'MultiPolygon':
            polys = [j for j in geom2]
            new1 = geom1.loc[[i] * len(polys)]
            new1.loc[:, 'geometry'] = polys
        else:
            new1 = geom1.copy()
        gpd2 = pd.concat([gpd2, new1])
    return gpd2.reset_index(drop=True)

