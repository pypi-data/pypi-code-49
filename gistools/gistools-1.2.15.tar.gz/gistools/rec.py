# -*- coding: utf-8 -*-
"""
Functions to delineate catchments.
"""
import numpy as np
import pandas as pd
from gistools.vector import kd_nearest
from gistools.util import load_geo_data

#####################################################
#### MFE REC streams network


def find_upstream(nzreach, rec_streams_shp):
    """
    Function to estimate all of the reaches (and nodes) upstream of specific reaches.

    Parameters
    ----------
    nzreach : list, ndarray, Series of int
        The NZ reach IDs
    rec_streams_shp : str path or GeoDataFrame
        str path to the REC streams shapefile or the equivelant GeoDataFrame.

    Returns
    -------
    DataFrame
    """
    if not isinstance(nzreach, (list, np.ndarray, pd.Series)):
        raise TypeError('nzreach must be a list, ndarray or Series.')

    ### Parameters
#    server = 'SQL2012PROD05'
#    db = 'GIS'
#    table = 'MFE_NZTM_REC'
#    cols = ['NZREACH', 'NZFNODE', 'NZTNODE']
#
#    ### Load data
    rec = load_geo_data(rec_streams_shp).drop('geometry', axis=1).copy()

    ### Run through all nzreaches
    reaches_lst = []
    for i in nzreach:
        reach1 = rec[rec.NZREACH == i]
        up1 = rec[rec.NZTNODE.isin(reach1.NZFNODE)]
        while not up1.empty:
            reach1 = pd.concat([reach1, up1])
            up1 = rec[rec.NZTNODE.isin(up1.NZFNODE)]
        reach1.loc[:, 'start'] = i
        reaches_lst.append(reach1)

    reaches = pd.concat(reaches_lst)
    reaches.set_index('start', inplace=True)
    return reaches


###############################################
### Catch delineation using the REC


def extract_catch(reaches, rec_catch_shp):
    """
    Function to extract the catchment polygons from the rec catchments layer. Appends to reaches layer.

    Parameters
    ----------
    reaches : DataFrame
        The output DataFrame from the find_upstream function.
    rec_catch_shp : str path, dict, or GeoDataFrame
        str path to the REC catchment shapefile or a GeoDataFrame.

    Returns
    -------
    GeoDataFrame
    """

    ### Parameters
#    server = 'SQL2012PROD05'
#    db = 'GIS'
#    table = 'MFE_NZTM_RECWATERSHEDCANTERBURY'
#    cols = ['NZREACH']
#
    sites = reaches.NZREACH.unique().astype('int32')
#
#    ### Extract reaches from SQL
#    catch1 = rd_sql(server, db, table, cols, where_col='NZREACH', where_val=sites, geo_col=True)
#    catch2 = catch1.dissolve('NZREACH')
    catch0 = load_geo_data(rec_catch_shp)

    catch1 = catch0[catch0.NZREACH.isin(sites)]
    catch2 = catch1.dissolve('NZREACH').reset_index()[['NZREACH', 'geometry']]

    ### Combine with original sites
    catch3 = catch2.merge(reaches.reset_index(), on='NZREACH')
    catch3.crs = catch0.crs

    return catch3


def agg_catch(rec_catch):
    """
    Simple function to aggregate rec catchments.

    Parameters
    ----------
    rec_catch : GeoDataFrame
        The output from extract_catch

    Returns
    -------
    GeoDataFrame
    """
    rec_shed = rec_catch[['start', 'geometry']].dissolve('start')
    rec_shed.index = rec_shed.index.astype('int32')
    rec_shed['area'] = rec_shed.area
    rec_shed.crs = rec_catch.crs
    return rec_shed.reset_index()


def catch_delineate(sites_shp, rec_streams_shp, rec_catch_shp, max_distance=np.inf, site_delineate='all', returns='catch'):
    """
    Catchment delineation using the REC streams and catchments.

    Parameters
    ----------
    sites_shp : str path or GeoDataFrame
        Points shapfile of the sites along the streams or the equivelant GeoDataFrame.
    rec_streams_shp : str path, GeoDataFrame
        str path to the REC streams shapefile, the equivelant GeoDataFrame, or a dict of parameters to read in an mssql table using the rd_sql function.
    rec_catch_shp : str path, GeoDataFrame
        str path to the REC catchment shapefile, the equivelant GeoDataFrame, or a dict of parameters to read in an mssql table using the rd_sql function.
    max_distance : non-negative float, optional
        Return only neighbors within this distance. This is used to prune tree searches, so if you are doing a series of nearest-neighbor queries, it may help to supply the distance to the nearest neighbor of the most recent point.
    site_delineate : 'all' or 'between'
        Whether the catchments should be dileated all the way to the top or only in between the sites.
    returns : 'catch' or 'all'
        Return only the catchment polygons or the catchments, reaches, and sites

    Returns
    -------
    GeoDataFrame
        Polygons
    """

    ### Parameters


    ### Modifications {NZREACH: {NZTNODE/NZFNODE: node # to change}}
    mods = {13053151: {'NZTNODE': 13055874}, 13048353: {'NZTNODE': 13048851}, 13048498: {'NZTNODE': 13048851}, 13048490: {'ORDER': 3}}

    ### Load data
    rec_catch = load_geo_data(rec_catch_shp)
    rec_streams = load_geo_data(rec_streams_shp)
    pts = load_geo_data(sites_shp)
    pts['geometry'] = pts.geometry.simplify(1)

    ### make mods
    for i in mods:
        rec_streams.loc[rec_streams['NZREACH'] == i, list(mods[i].keys())] = list(mods[i].values())

    ### Find closest REC segment to points
    rec_pts1 = rec_streams.copy()
    rec_pts1['geometry'] = rec_streams.centroid

    pts_seg = kd_nearest(pts, rec_pts1, 'NZREACH', max_distance=max_distance)
    nzreach = pts_seg.copy().NZREACH.unique()

    ### Find all upstream reaches
    reaches = find_upstream(nzreach, rec_streams_shp=rec_streams)

    ### Clip reaches to in-between sites if required
    if site_delineate == 'between':
        reaches1 = reaches.reset_index().copy()
        reaches2 = reaches1.loc[reaches1.NZREACH.isin(reaches1.start.unique()), ['start', 'NZREACH']]
        reaches2 = reaches2[reaches2.start != reaches2.NZREACH]

        grp1 = reaches2.groupby('start')

        for index, r in grp1:
#            print(index, r)
            r2 = reaches1[reaches1.start.isin(r.NZREACH)].NZREACH.unique()
            reaches1 = reaches1[~((reaches1.start == index) & (reaches1.NZREACH.isin(r2)))]

        reaches = reaches1.set_index('start').copy()

    ### Extract associated catchments
    rec_catch = extract_catch(reaches, rec_catch_shp=rec_catch)

    ### Aggregate individual catchments
    rec_shed = agg_catch(rec_catch)
    rec_shed.columns = ['NZREACH', 'geometry', 'area']
    rec_shed1 = rec_shed.merge(pts_seg.drop('geometry', axis=1), on='NZREACH')

    ### Return
    if returns == 'catch':
        return rec_shed1
    else:
        return rec_shed1, reaches, pts_seg
