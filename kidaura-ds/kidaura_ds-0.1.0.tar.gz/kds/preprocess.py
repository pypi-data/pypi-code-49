import pandas as pd
import boto3
import json
from scipy.spatial.distance import euclidean
import numpy as np
from scipy import stats
from .util import read_json_s3, next_row
from sympy.geometry import Polygon, Point2D



class Attributes(object):
    def __init__(self, s_id, game_id, game_play_id, datetime, data):
        self.s_id = s_id
        self.game_id = game_id
        self.game_play_id = game_play_id
        self.datetime = datetime
        self.data = data
        self.attributes = []

    def create_dict(self, keys, default):
        if default == list:
            return {k: [] for k in keys}
        else:
            return {k: default for k in keys}
            

    def create_attr_dict(self):
        kinematics_params = ['velocity', 'acc', 'jerk', 'deacc']
        descriptive = ['mean', 'median', 'std', 'min', 'max', 'range']

        self.kine_attrs = [
            f'{i}_{j}' for i in kinematics_params for j in descriptive]

        self.list_attrs = ['drag_distance', 'drag_duration',
                           'press_duration', 'touch_delay', 'drag_duration',
                           'drag_area', 'drag_width', 'drag_height',
                           'movement_unit', 'deacc_time', 'deacc_time_mu', 'peak_velocity', 'peak_velocity_mu']

        self.num_attr = ['drag_count', 'press_count', 'tap_count',
                         'longest_drag_duration', 'longest_drag_distance', 'longest_drag_velocity_mean',
                         'longest_drag_velocity_median', 'longest_drag_velocity_std', 'longest_drag_velocity_min',
                         'longest_drag_velocity_max', 'tap_count_cont', 'total_time', 'outside_distance', 'total_distance']

        self.list_coloring_attr = [
            'bmi', 'longest_drag_bmi', 'colors_used', 'completion_ratio']

        self.attributes = self.create_dict(self.kine_attrs, list)
        self.attributes.update(self.create_dict(self.list_attrs, list))
        self.attributes.update(self.create_dict(self.num_attr, 0))
        if self.game_id == 1:
            self.attributes.update(self.create_dict(
                self.list_coloring_attr, list))

    def calc_distance(self, df, x='x', y='y', time='time'):
        distance = 0
        df['distance'] = distance
        for (i1, r1), (i2, r2) in next_row(df.iterrows()):
            distance += euclidean(r1[[x, y]], r2[[x, y]])
            df.loc[i2, 'distance'] = distance
        df['distance'] = df['distance']

    def calc_velocity(self, df, distance='distance', time='time'):
        magnitude = 0
        df['velocity'] = magnitude
        for (i1, r1), (i2, r2) in next_row(df.iterrows()):
            try:
                magnitude = (r2[distance] - r1[distance]) / \
                    (r2[time] - r1[time])
            except ZeroDivisionError:
                magnitude = 0
            df.loc[i2, 'velocity'] = magnitude

    def calc_acceleration(self, df, velocity='velocity', time='time'):
        magnitude = 0
        df['acceleration'] = magnitude
        for (i1, r1), (i2, r2) in next_row(df.iterrows()):
            try:
                magnitude = (r2[velocity] - r1[velocity]) / \
                    (r2[time] - r1[time])
            except ZeroDivisionError:
                magnitude = 0
            df.loc[i2, 'acceleration'] = magnitude

    def calc_jerk(self, df, acceleration='acceleration', time='time'):
        magnitude = 0
        df['jerk'] = magnitude
        for (i1, r1), (i2, r2) in next_row(df.iterrows()):
            try:
                magnitude = (r2[acceleration] - r1[acceleration]
                             ) / (r2[time] - r1[time])
            except ZeroDivisionError:
                magnitude = 0
            df.loc[i2, 'jerk'] = magnitude

    def classify_touch(self, df):
        touch_phases = sorted(set(df['touchPhase']))
        touch_phases = [phase_id[0] for phase_id in touch_phases]
        if touch_phases == sorted(['B', 'E']):
            return 'Tap'
        elif touch_phases == sorted(['B', 'M', 'E']) \
                or touch_phases == sorted(['B', 'M', 'S', 'E']):
            return 'Drag'
        elif touch_phases == sorted(['B', 'S', 'E']):
            return 'Press'
        elif 'C' in touch_phases:
            return 'Canceled'
        return None

    def prospective_attrs(self, df):
        time = []
        peak_velocities = []
        mus = df[df['deacc'] < 0].index
        for p1, p2 in next_row(mus):
            peak_id = df.loc[p1:p2]['velocity'].idxmax()
            peak_velocities.append(df.loc[peak_id, 'velocity'])
            time.append(df.loc[p2]['time'] - df.loc[peak_id]['time'])

        if len(peak_velocities) > 0:

            return {
                'movement_unit': len(mus),
                'deacc_time': stats.tmean(time),
                'deacc_time_mu': time[0],
                'peak_velocity': stats.tmean(peak_velocities),
                'peak_velocity_mu': peak_velocities[0]
            }
        else:
            raise Exception("No enough point")

    def boundary_maintenance_index(self, zones):
        outside_count = 0
        outside_freq = 0
        inside_count = 0
        inside_freq = 0
        prev_zone = None
        for z in zones:
            if z[0] == 'o':
                outside_count += 1
            else:
                inside_count += 1
            if prev_zone is not None:
                if z != prev_zone and prev_zone == 'outside':
                    outside_freq += 1
                elif z != prev_zone and z == 'outside':
                    inside_freq += 1
            prev_zone = z
        total_count = outside_count + inside_count

        bmi = (outside_count/total_count) ** (1+outside_freq) + \
            (inside_count/total_count) ** (1+inside_freq)
        return bmi

    def swipe_distance(self, df):
        total_distance = 0
        outside_distance = 0
        for (i1, c1), (i2, c2) in next_row(df.iterrows()):
            ed = 0
            x1, y1 = c1[['x', 'y']]
            x2, y2 = c2[['x', 'y']]

            if (c1['zone'] in ['outside']) and c2['zone'] in ['outside']:
                ed = euclidean((x1, y1), (x2, y2))
            elif c1['zone'] == 'outside' and c2['zone'] != 'outside':
                xm = (x1 + x2) / 2
                ym = (y1 + y2) / 2
                ed = euclidean((xm, ym), (x1, y1))
            elif c1['zone'] != 'outside' and c2['zone'] == 'outside':
                xm = (x1 + x2) / 2
                ym = (y1 + y2) / 2
                ed = euclidean((x2, y2), (xm, ym))

            total_distance += euclidean((x1, y1), (x2, y2))
            outside_distance += ed
        return {
            'outside_distance': outside_distance,
            'total_distance': total_distance
        }

    def run_derivation(self):
        self.create_attr_dict()

        colors_used = set()
        prev_time = self.data['startTime']
        end_time = None
        prev_touch_type = None
        for touch_id in self.data['touchData']:
            df = pd.DataFrame(self.data['touchData'][touch_id])
            self.calc_distance(df)
            self.calc_velocity(df)
            self.calc_acceleration(df)
            self.calc_jerk(df)
            df['acc'] = df['acceleration'].where(df['acceleration'] > 0, 0)
            df['deacc'] = df['acceleration'].where(df['acceleration'] < 0, 0)
            touch_type = self.classify_touch(df)
            longest_time = 0
            if touch_type == 'Drag':
                # dervice kinematics
                for k in self.kine_attrs:
                    k_prefix, ops = k.split('_')
                    if ops == 'mean':
                        self.attributes[k].append(df[k_prefix].mean())
                    elif ops == 'median':
                        self.attributes[k].append(df[k_prefix].median())
                    elif ops == 'std':
                        self.attributes[k].append(df[k_prefix].std())
                    elif ops == 'min':
                        self.attributes[k].append(df[k_prefix].min())
                    elif ops == 'max':
                        self.attributes[k].append(df[k_prefix].max())
                    elif ops == 'range':
                        self.attributes[k].append(
                            df[k_prefix].max() - df[k_prefix].min())

                # per drag distance
                drag_distance = df.iloc[-1]['distance'] - \
                    df.iloc[0]['distance']
                self.attributes['drag_distance'].append(drag_distance)

                # derive prospective kinematics
                try:
                    pros_kine = self.prospective_attrs(df)
                    for k in pros_kine:
                        self.attributes[k].append(pros_kine[k])
                except:
                    pass

                # drag count
                self.attributes['drag_count'] += 1

                # area, width and height
                drag_polygon = Polygon(*np.array(df[['x', 'y']]))

                try:
                    self.attributes['drag_area'].append(
                        abs(float(drag_polygon.area)))
                    bounds_x_min, bounds_y_min, bounds_x_max, bounds_y_max = drag_polygon.bounds
                    self.attributes['drag_width'].append(
                        float(bounds_x_max - bounds_x_min))
                    self.attributes['drag_height'].append(
                        float(bounds_y_max - bounds_y_min))
                except Exception as e:
                    print("Not a polygon")

                # duration
                drag_duration = df.iloc[-1]['time'] - df.iloc[0]['time']
                self.attributes['drag_duration'].append(drag_duration)

                # longest drag features
                if longest_time < drag_duration:

                    self.attributes['longest_drag_duration'] = drag_duration
                    self.attributes['longest_drag_distance'] = drag_distance
                    self.attributes['longest_drag_velocity_mean'] = df['velocity'].mean()
                    self.attributes['longest_drag_velocity_median'] = df['velocity'].median()
                    self.attributes['longest_drag_velocity_std'] = df['velocity'].std()
                    self.attributes['longest_drag_velocity_min'] = df['velocity'].min()
                    self.attributes['longest_drag_velocity_max'] = df['velocity'].max()

                    if self.game_id == 1:
                        self.attributes['longest_drag_bmi'] = self.boundary_maintenance_index(df['zone'])

                # boundary maintainance index
                if self.game_id == 1:
                    self.attributes['bmi'].append(
                        self.boundary_maintenance_index(df['zone']))

            elif touch_type == 'Tap':
                self.attributes['tap_count'] += 1
                if prev_touch_type == 'Tap':
                    self.attributes['tap_count_cont'] += 1

            elif touch_type == 'Press':
                # press count
                self.attributes['press_count'] += 1

                # press duration
                press_duration = df.iloc[-1]['time'] - df.iloc[0]['time']
                self.attributes['press_duration'].append(press_duration)

            # response attrs
            if df.iloc[0]['time'] > prev_time:
                self.attributes['touch_delay'].append(
                    df.iloc[0]['time'] - prev_time)
                prev_time = df.iloc[-1]['time']

            # meta attributes game wise
            if self.game_id == 1:
                for c in set(df['color']):
                    colors_used.add(c)
                self.attributes['colors_used'] = len(colors_used)
                self.attributes['completion_ratio'] = df['completionPerc'].max()

            dist = self.swipe_distance(df)
            for k in dist:
                self.attributes[k] += dist[k]

            prev_touch_type = touch_type
            end_time = df.iloc[-1]['time']
            self.data['touchData'][touch_id] = df.to_dict('records')

        self.attributes['total_time'] = end_time - data['startTime']

    @property
    def final_attributes(self):
        f_attrs = self.attributes
        for k in f_attrs:
            if type(f_attrs[k]) == list:
                f_attrs[k] = stats.tmean(f_attrs[k])
        return f_attrs


class ParseFile(object):
    def __init__(self, file_name):
        try:
            raw_str = file_name.replace('.json', '')
            s_id, game_play_id, date_time = raw_str.split('_')
            date_time = f'{date_time[:2]}-{date_time[2:4]}-{date_time[4:6]}{date_time[6:]}'
            self.__dict__.update(locals())
        except:
            raise Exception("File Name cannot be parsed")
        

if __name__ == "__main__":
    file_name = '1000_0_02132019 12:19:05.json'
    data = read_json_s3('kidaura',  f'screenplay/raw/coloring/{file_name}')
    file_meta = ParseFile(file_name)
    attrs = Attributes(s_id=file_meta.s_id,
                       game_id=1,
                       game_play_id=file_meta.game_play_id,
                       datetime=file_meta.date_time,
                       data=data)
    attrs.run_derivation()
    print(attrs.final_attributes)
