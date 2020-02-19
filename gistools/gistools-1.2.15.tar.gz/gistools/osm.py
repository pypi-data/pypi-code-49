# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:36:11 2019

@author: MichaelEK
"""
import numpy as np
import pandas as pd
import geopandas as gpd
from scipy.spatial import cKDTree
from gistools import vector
import copy

try:
    import overpass
    import osm2geojson
except:
    print('Install overpass and osm2geojson for osm module functions')

#############################################
### Parameters

op_endpoint = 'https://overpass-api.de/api/interpreter'


#############################################
### Functions


def get_nearest_waterways(gdf_from, id_col, max_distance=500, waterway_type='all'):
    """
    Function to get the nearest waterways and associated nodes at some max distance from the OSM overpass server. Can specify the waterway type as either 'natural' or 'all'. The higher the max distance the slower the server query.

    Parameters
    ----------
    gdf_from : GeoDataFrame
        Locations of the sites where you want to find the nearest waterway nodes.
    id_col : str
        The column name of the site ID for gdf_from.
    max_distance : int
        The maximum search distance.
    waterway_type : str
        Either 'nautral' or 'all'

    Returns
    -------
    GeoDataFrame
        of the sites and associated waterys and nodes.
    """
    if waterway_type == 'all':
        q_base = """(way['waterway'~'(river|stream|drain|canal|tidal_channel|ditch)'](around:{dis}, {lat}, {lon});
    node(around:{dis}, {lat}, {lon})(w);)"""
    elif waterway_type == 'natural':
        q_base = "(way['waterway'~'(river|stream|tidal_channel)'](around:{dis}, {lat}, {lon}); node(around:{dis}, {lat}, {lon})(w);)"
    else:
        raise ValueError('waterway_type must be either natural or all.')

    from1 = gdf_from[[id_col, 'geometry']].copy()

    pts1 = from1.to_crs(4326)

    from1['x'] = from1.geometry.x
    from1['y'] = from1.geometry.y
    from1['lon'] = pts1.geometry.x
    from1['lat'] = pts1.geometry.y

    api = overpass.API(endpoint=op_endpoint)

    print('Overpass endpoint is: ' + op_endpoint)

    res_list = []
    for index, p in from1.iterrows():
#        print(p[id_col])
        q1 = q_base.format(dis=max_distance, lat=p.lat, lon=p.lon)

        response = api.get(q1, responseformat='json')

        nodes1 = [n for n in response['elements'] if n['type'] == 'node']
        pd_nodes = pd.DataFrame.from_records(nodes1)
        if pd_nodes.empty:
            print('No node was found during the query for ' + id_col + ': ' + str(p[id_col]))
            continue
        gpd_nodes1 = gpd.GeoDataFrame(pd_nodes, geometry=gpd.points_from_xy(pd_nodes['lon'], pd_nodes['lat']), crs=4326)
        gpd_nodes2 = gpd_nodes1.to_crs(from1.crs)

        nodes2 = list(zip(gpd_nodes2.geometry.x, gpd_nodes2.geometry.y))

        btree = cKDTree(nodes2)
        dist, idx = btree.query([p.x, p.y], k=1, distance_upper_bound=max_distance)

        best1 = gpd_nodes2.iloc[[idx]].copy()
        best1['distance'] = round(dist, 2)
        best1[id_col] = p[id_col]

        ways1 = [n for n in response['elements'] if n['type'] == 'way']
        [s['tags'].update({'name': 'No name'}) for s in ways1 if not 'name' in s['tags']]
        this_way = [{'waterway_id': w['id'], 'waterway_name': w['tags']['name']} for w in ways1 if best1['id'].iloc[0] in w['nodes'][1:]][0]
        best1['waterway_id'] = this_way['waterway_id']
        best1['waterway_name'] = this_way['waterway_name']

        res_list.append(best1)

    res1 = pd.concat(res_list, sort=False).reset_index(drop=True)
    return res1


def get_waterways(osm_nodes_from, waterway_type='all'):
    """
    Function to get all the waterways connected by the node IDs derived from the get_nearest_waterways function from the OSM overpass server. Can specify the waterway type as either 'natural' or 'all'.

    Parameters
    ----------
    osm_nodes_from : GeoDataFrame
        Output GeoDataFrame from the get_nearest_waterways function with waterway nodes.
    waterway_type : str
        Either 'nautral' or 'all'.

    Returns
    -------
    Two Dicts
        of waterways and nodes.
    """
    q_node_base = "node({node});"

    if waterway_type == 'all':
        q_other_base = """complete {(way['waterway'](<);
                            (>;);
                            way['natural'='water'](<);
                            (>;););}"""
    elif waterway_type == 'natural':
        q_other_base = """complete {(way['waterway'~'(river|stream|tidal_channel)'](<);
                            (>;);
                            way['natural'='water'](<);
                            (>;););}"""
    else:
        raise ValueError('waterway_type must be either natural or all.')

    api = overpass.API(endpoint=op_endpoint)

    waterways = []
    nodes = {}

    for index, p in osm_nodes_from.iterrows():
        w_check = True
        for w in waterways:
            if p.waterway_id in w[1].keys():
                w[0].update({p.id: p.waterway_id})
                w_check = False
                break
        if w_check:
            print(p)
            q_node = q_node_base.format(node=p.id)
            q1 = q_node + q_other_base

            response = api.get(q1, responseformat='json')
            ww1 = {ww['id']: ww for ww in response['elements'] if (ww['type'] == 'way')}
            lst1 = [{p.id: p.waterway_id}, ww1]
            waterways.append(lst1)
            n1 = {n['id']: n for n in response['elements'] if n['type'] == 'node'}
            nodes.update(n1)

    return waterways, nodes


def waterway_delineation(waterways, site_delineate=False, only_waterways=True):
    """
    Function to delineate the waterways above each of the sites/nodes originally derived by the get_nearest_waterways function. Optional to delineate all the way up the waterway network or between the sites.

    Parameters
    ----------
    osm_nodes_from : GeoDataFrame
        Output GeoDataFrame from the get_nearest_waterways function with waterway nodes.
    waterways : dict
        First output dict from the get_waterways function.
    site_delineate : bool
        Whether the waterway network should be dileated all the way to the top (False) or only in between the sites (True).

    Returns
    -------
    Dict
        of each site/node each continaing the associated waterways and nodes.
    """
    site_delin = {}
    for w in waterways:
        ways = w[1]
        for node, node_way in w[0].items():
            new_wws = copy.deepcopy(ways)

            site_ww = {node_way: ways[node_way].copy()}
            site_ww_nodes1 = site_ww[node_way]['nodes']
            site_node_index = site_ww_nodes1.index(node)+1
            if (site_node_index + 1) == len(site_ww_nodes1):
                site_ww_nodes = site_ww_nodes1
            else:
                site_ww_nodes = site_ww_nodes1[:site_node_index]

            site_ww[node_way]['nodes'] = site_ww_nodes

            ww_last = {}
            for i, ww in new_wws.items():
                if 'waterway' in ww['tags']:
                    ww_last.update({i: [ww['nodes'][-1]]})
                else:
                    ww_last.update({i: ww['nodes']})

            if len(site_ww_nodes1) == site_node_index:
                big_set = set(site_ww_nodes[:-1])
            else:
                big_set = set(site_ww_nodes)

            set_len = len(big_set)

            bigger_set = big_set.copy()

            while set_len > 0:
                index1 = [i for i, ww in ww_last.items() if np.in1d(ww, list(big_set)).any()]
                new_ww = {i: new_wws[i] for i in index1}
                site_ww.update({i: new_ww[i] for i in index1})
                bigger_set.update(big_set)
                temp_set = set()
                [temp_set.update(set(new_ww[i]['nodes'][:-1])) for i in index1]

                big_set = temp_set.difference(bigger_set)

                set_len = len(big_set)

            if only_waterways:
                site_ww1 = {i: s for i, s in site_ww.items() if 'waterway' in s['tags']}
                site_ww2 = {i: s for i, s in site_ww1.items() if s['tags']['waterway'] in ['river', 'stream', 'drain', 'canal', 'ditch']}
            else:
                site_ww2 = site_ww

            site_delin.update({node: site_ww2})

        if site_delineate:
            for node1, node_way1 in w[0].items():
#                print('origin ' + str(node1))
                sw1 = site_delin[node1]
                for node2, node_way2 in w[0].items():
                    if node2 != node1:
#                        print('removal ' + str(node2))
                        if node_way2 in sw1.keys():
                            sw2 = site_delin[node2]
                            way1 = sw1[node_way2]['nodes']
                            if (node2 in way1) and (node_way2 in sw2):
                                other_way_ids = list(sw2.keys())
                                other_way2 = sw2[node_way2]['nodes']
                                if (len(other_way2)+1) < len(way1):
                                    new_way1 = way1[(way1.index(node2)):]
                                    site_delin[node1][node_way2]['nodes'] = new_way1
                                    other_way_ids.remove(node_way2)
                                [site_delin[node1].pop(w, None) for w in other_way_ids]

    return site_delin


def to_osm(site_delin, nodes):
    """
    Function to convert the output of the waterway_delineation function to a dict of dict in the OSM dict structure (for futher processing).

    Parameters
    ----------
    site_delin : dict
        Output of the waterway_delineation function.
    nodes : dict
        Second output of the get_waterways function.

    Returns
    -------
    Dict
        dict of dict in the OSM dict structure.
    """
    time1 = pd.Timestamp.now().isoformat()

    osm_delin = {}

    for id1, ww in site_delin.items():
        big_set = set()
        [big_set.update(set(v['nodes'])) for v in ww.values()]
        lotsanodes = [n for i, n in nodes.items() if i in big_set]
        lotsaways = [l for i, l in ww.items()]

        lots = []
        lots.extend(lotsanodes)
        lots.extend(lotsaways)

        dict1 = {'timestamp': time1, 'elements': lots}
        osm_delin.update({id1: dict1})

    return osm_delin


def to_gdf(osm_delin):
    """
    Function to convert the output of the to_osm function to a GeoDataFrame of the waterways associated with the sites/nodes.

    Parameters
    ----------
    osm_delin : dict
        Output of the to_osm function.

    Returns
    -------
    GeoDataFrame
    """
    shape1 = []

    for id1, osm1 in osm_delin.items():
        s1 = osm2geojson.json2shapes(osm1)
        [s['properties']['tags'].update({'name': 'No name'}) for s in s1 if not 'name' in s['properties']['tags']]
        l1 = [[id1, s['properties']['id'], s['properties']['tags']['name'], s['properties']['tags']['waterway'], s['shape']] for s in s1]
        shape1.extend(l1)

    df1 = pd.DataFrame(shape1, columns=['start_node', 'way_id', 'name', 'waterway', 'geometry'])
#    gdf1 = gpd.GeoDataFrame(df1, crs=4326, geometry='geometry').dissolve(['start_node', 'way_id']).reset_index()
    gdf1 = gpd.GeoDataFrame(df1, crs='epsg:4326', geometry='geometry')
    gdf2 = gdf1[gdf1.geom_type == 'LineString'].copy()

    return gdf2


def to_nx():
    """
    To be completed...convert to networkx. Look at osmnx...
    """


def pts_to_waterway_delineation(gdf_from, id_col, max_distance=500, waterway_type='all', site_delineate=False):
    """
    Function to fully perform the OSM waterway delineation process.

    Parameters
    ----------
    Parameters
    ----------
    gdf_from : GeoDataFrame
        Locations of the sites where you want to find the nearest waterway nodes.
    id_col : str
        The column name of the site ID for gdf_from.
    max_distance : int
        The maximum search distance.
    waterway_type : str
        Either 'nautral' or 'all'
    site_delineate : bool
        Whether the waterway network should be dileated all the way to the top (False) or only in between the sites (True).

    Returns
    -------
    Two GeoDataFrames
        The first is the GeoDataFrame of the nearest OSM waterway and node associated with the sites and the other is the one that contains the upstream delineated waterways.
    """
    pts1 = get_nearest_waterways(gdf_from, id_col, max_distance, waterway_type)
    waterways, nodes = get_waterways(pts1, waterway_type)
    site_delin = waterway_delineation(waterways, site_delineate)
    osm_delin = to_osm(site_delin, nodes)
    gdf1 = to_gdf(osm_delin).to_crs(pts1.crs)

    return pts1, gdf1


def get_waterways_within_boundary(poly, buffer=0, waterway_type='all'):
    """

    """
    if waterway_type == 'all':
        q_base = """way['waterway']({min_lat}, {min_lon}, {max_lat}, {max_lon});(._;>;);"""
    elif waterway_type == 'natural':
        q_base = """(way['waterway'~'(river|stream|tidal_channel)']({min_lat}, {min_lon}, {max_lat}, {max_lon});(._;>;);"""
    else:
        raise ValueError('waterway_type must be either natural or all.')

    ## Prepare the polygon
    poly1 = poly.to_crs('epsg:4326').copy()
    poly1['geometry'] = poly1.buffer(buffer)
    poly2 = poly1.unary_union
    min_lon, min_lat, max_lon, max_lat = poly2.bounds

    ## Query OSM
    q1 = q_base.format(min_lon=min_lon, min_lat=min_lat, max_lon=max_lon, max_lat=max_lat)

    api = overpass.API(endpoint=op_endpoint)

    print('Overpass endpoint is: ' + op_endpoint)

    response = api.get(q1, responseformat='json')

    ## convert to gpd
    s1 = osm2geojson.json2shapes(response)
    [s['properties']['tags'].update({'name': 'No name'}) for s in s1 if not 'name' in s['properties']['tags']]
    l1 = [[s['properties']['id'], s['properties']['tags']['name'], s['properties']['tags']['waterway'], s['shape']] for s in s1]
    df1 = pd.DataFrame(l1, columns=['way_id', 'name', 'waterway', 'geometry'])
    gdf1 = gpd.GeoDataFrame(df1, crs='epsg:4326', geometry='geometry')
    gdf2 = gdf1[gdf1.geom_type == 'LineString'].copy()

    ## Select rivers within polygon
    gdf3 = gdf2[gdf2.intersects(poly2)].to_crs(poly.crs).copy()

    ## Return
    return gdf3













