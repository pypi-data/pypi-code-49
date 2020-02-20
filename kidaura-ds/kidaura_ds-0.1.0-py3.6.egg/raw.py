import pandas as pd
import traceback
from collections import Counter
from .db import get_conn
import numpy as np
from itertools import tee
from scipy.spatial.distance import euclidean


total_pixel = {
    1: 238,
    2: 183
}

def fetch_sid(game_no, database="kidaura_v1"):
    '''Fetch all sids using game type'''
    coll = get_conn()[f'game_{game_no}_raw']
    data = list(coll.distinct('S_Id'))
    return data


def fetch_student(sid, database='kidaura_v1'):
    '''Fetch student details'''
    coll = get_conn(database)['student']
    data = list(
        coll.aggregate([{
            '$lookup': {
                'from': 'classes',
                'localField': 'C_Id',
                'foreignField': "C_Id",
                'as': 'class'
            }
        }, {
            '$match': {
                'S_Id': {
                    '$in': [str(sid), int(sid)]
                }
            }
        }, {
            '$unwind': '$class'
        }, {
            '$lookup': {
                'from': 'schools',
                'localField': 'class.School_Id',
                'foreignField': "School_Id",
                'as': 'school'
            }
        }, {
            '$unwind': '$school'
        }, {
            '$project': {
                'S_Id': 1,
                'S_Roll_No': 1,
                'S_Name': 1,
                'DOB': 1,
                'Standard': '$class.Standard',
                'Division': '$class.Division',
                'School_Name': '$school.School_Name',
                '_id': 0
            }
        }]))
    return data[0]


def fetch_game_plays(s_id, game_no, database='kidaura_v1'):
    '''Fetch gameplays ordered by Timestamp, time, Touch Phase'''
    coll = get_conn(database)[f'game_{game_no}_raw']
    data = list(
        coll.aggregate([{
            '$match': {
                'S_Id': {
                    '$in': [str(s_id), int(s_id)]
                }
            }
        }, {
            "$addFields": {
                "_id": False,
                "sortField": {
                    "$cond": [{
                        "$eq": ["$Touch Phase", "Began"]
                    }, 1, {
                        "$cond": [{
                            "$eq": ["$Touch Phase", "Moved"]
                        }, 2, {
                            "$cond": [{
                                "$eq": ["$Touch Phase", "Stationary"]
                            }, 3, {
                                "$cond": [{
                                    "$eq": ["$Touch Phase", "Canceled"]
                                }, 4, {
                                    "$cond": [{
                                        "$eq": ["$Touch Phase", "Ended"]
                                    }, 5, 6]
                                }]
                            }]
                        }]
                    }]
                }
            }
        }, {
            '$project': {
                '_id': 0
            }
        }, {
            "$sort": {
                'Timestamp': 1,
                'Time': 1,
                'sortField': 1
            }
        }]))
    return data


def remove_header(df):
    return df.iloc[1:]


def split_game_plays_n(df):
    indexes = df[df['Touch Phase'] == "N"].index
    dfs = []
    for e, i in enumerate(indexes):
        if e == len(indexes) - 1:
            dfs.append(df.loc[i:])
        else:
            dfs.append(df.loc[i:indexes[e + 1] - 1])
    return dfs


def add_touch_ids(tdf):
    tdf = tdf.copy()
    record = {}
    touch_count = 0
    err_touch_id = []
    tdf['touch_id'] = ''
    for i, r in tdf.iterrows():
        fingure_id = r['Fingure ID']
        touch_phase = r['Touch Phase']
        if fingure_id in record:
            '''if touch has began already and it starts again'''
            if touch_phase == "Began":
                err_touch_id.append((touch_count, 1))
                touch_count += 1
                record[fingure_id] = touch_count
                print(f"Error: Touch not Ended, {touch_count}")
                tdf.loc[i, 'touch_id'] = record[fingure_id]
            elif touch_phase == "Ended" or touch_phase == "Canceled":
                tdf.loc[i, 'touch_id'] = record[fingure_id]
                del record[fingure_id]
            else:
                tdf.loc[i, 'touch_id'] = record[fingure_id]
        else:
            '''if touch has not began already and it ends or moves'''
            if touch_phase != "Began":
                print(f"Error: Touch not Began, {touch_count}")
                touch_count += 1
                err_touch_id.append((touch_count, -1))
                record[fingure_id] = touch_count
                tdf.loc[i, 'touch_id'] = record[fingure_id]
            else:
                touch_count += 1
                record[fingure_id] = touch_count
                tdf.loc[i, 'touch_id'] = record[fingure_id]
    return tdf


def find_be_error(tdf):
    tdf.is_copy = False
    record = {}
    touch_count = 0
    err_touch_id = []
    tdf['touch_id'] = ''
    for i, r in tdf.iterrows():
        fingure_id = r['Fingure ID']
        touch_phase = r['Touch Phase']
        if fingure_id in record:
            '''if touch has began already and it starts again'''
            if touch_phase == "Began":
                print("Touch Not ended")
                err_touch_id.append((touch_count, 1))
                touch_count += 1
                record[fingure_id] = touch_count
                tdf.loc[i, 'touch_id'] = record[fingure_id]
            elif touch_phase == "Ended" or touch_phase == "Canceled":
                tdf.loc[i, 'touch_id'] = record[fingure_id]
                touch_count += 1
                del record[fingure_id]
            else:
                tdf.loc[i, 'touch_id'] = record[fingure_id]
        else:
            '''if touch has not began already and it ends or moves'''
            if touch_phase != "Began":
                touch_count += 1
                print("Touch Not started")
                err_touch_id.append((touch_count, -1))
                record[fingure_id] = touch_count
                tdf.loc[i, 'touch_id'] = record[fingure_id]
            else:
                touch_count += 1
                record[fingure_id] = touch_count
                tdf.loc[i, 'touch_id'] = record[fingure_id]
    new_rows = []
    for t in set(tdf['touch_id']):
        td = tdf.query("touch_id == {}".format(t))
        b_count = td[td['Touch Phase'] == 'Began'].shape[0]
        e_count = td[td['Touch Phase'] == 'Ended'].shape[0]
        diff = b_count - e_count
        if diff < 0:
            print("Missing End {}".format(t))
            new_row = td.min()
            new_row['Touch Phase'] = "Began"
            new_rows.append(new_row)
        elif diff > 0:
            new_row = td.max()
            new_row['Touch Phase'] = "Ended"
            new_rows.append(new_row)
            print("Missing Began {}".format(t))
    return pd.DataFrame(new_rows)


def next_row(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def touch_distance(coords):
    d = 0
    for c1, c2 in next_row(coords):
        d += euclidean(c1, c2)
    return d


def add_offset(df):
    df = df.copy()
    cams = set(df['Cam Frame'])
    max_x = 0
    for c in cams:
        tf = df[df['Cam Frame'] == c]
        tf_i = tf.index
        df.loc[tf_i, 'X Co-ordinate'] = tf['X Co-ordinate'] + max_x
        max_x += tf['X Co-ordinate'].max()
    return df