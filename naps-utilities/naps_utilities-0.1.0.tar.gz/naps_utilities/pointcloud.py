# Nécessaires pour la lecture/écriture de fichiers
import os
import json
import pickle

#Les données sont stockées sous forme de numpy ndarray
import numpy as np

#Nécessaire pour la conversion vers/depuis ROS2
from builtin_interfaces.msg import Time
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import PointField
from std_msgs.msg import Header
from array import array

class Pointcloud():
    def __init__(self, ros_msg=None, keep_ring=True, matrix=None, procrastinate=False):
        # PoinCloud Metadata
        self.metadata = {'header': None,
                         'height': None,
                         'width': None,
                         'fields': None,
                         'is_bigendian': None,
                         'point_step': None,
                         'row_step': None,
                         'is_dense': None,
                         'keep_ring': None,
                         'is_populated': False,
                         'procrastinated': True,}
        # Pointcloud DATA
        self.points = None
        self.rings = None
        self.matrix = matrix

        if ros_msg is not None:
            self.from_msg(ros_msg)
            if not procrastinate:
                self.filter()
                self.transform(matrix)

    def from_msg(self, msg):
        #Données conservées "telles quelles"

        self.metadata['height'] = msg.height
        self.metadata['width'] = msg.width

        self.metadata['is_bigendian'] = msg.is_bigendian
        self.metadata['point_step'] = msg.point_step
        self.metadata['row_step'] = msg.row_step

        self.metadata['is_dense'] = msg.is_dense

        def from_header(header):
            return {'time': {'sec': header.stamp.sec, 'nanosec': header.stamp.nanosec},
               'frame_id': header.frame_id}
        self.metadata['header'] = from_header(msg.header)

        def from_pointfields(fields):
            return [{'name': field.name,
                'offset': field.offset,
                'datatype': field.datatype,
                'count': field.count}
               for field in fields]

        self.metadata['fields'] = from_pointfields(msg.fields)

        # Données converties
        self.metadata['nb_points'] = msg.height * msg.width

        data = np.reshape(msg.data, (-1, self.metadata['point_step']))

        self.points = np.ndarray(
            (self.metadata['nb_points'], 4), dtype=np.float32,
            buffer=np.ascontiguousarray(data[:, :16]))

        if self.metadata['keep_ring']:
            self.metadata['rings'] = np.zeros(
                self.metadata['nb_points'], dtype=np.uint16)

            pointcloud['rings'] = np.ndarray(
                (self.metadata['nb_points']), dtype=np.uint16,
                buffer=np.ascontiguousarray(data[:, 16:]))

        if not self.metadata['keep_ring']:
            self.metadata['fields'] = [field for field in self.metadata['fields'] if field['name'] != 'ring']
            self.metadata['point_step'] = 16
            self.metadata['row_step'] = self.metadata['point_step'] * len(self.metadata['fields'])
            self.metadata['is_populated'] = True

    def to_msg(self):
        msg = PointCloud2()
        #Données conservées "telles quelles"

        msg.height = self.metadata['height']
        msg.width = self.metadata['width']

        msg.is_bigendian = self.metadata['is_bigendian']
        msg.point_step = self.metadata['point_step']
        msg.row_step = self.metadata['row_step']

        msg.is_dense = self.metadata['is_dense']

        def to_header(header_data):
            return Header(stamp=Time(
                sec=header_data['time']['sec'],
                nanosec=header_data['time']['nanosec']),
                     frame_id=header_data['frame_id'])
        msg.header = to_header(self.metadata['header'])

        def to_pointfields(pointfields_data):
            return [PointField(name=field['name'],
                          offset=field['offset'],
                          datatype=field['datatype'],
                          count=field['count']) for field in pointfields_data]
        msg.fields = to_pointfields(self.metadata['fields'])

        if self.metadata['keep_ring']:
            msg.data = array('B', np.concatenate(
            (self.points.view(dtype=np.uint8),
             self.rings.reshape((self.metadata['nb_points'], -1)).view(dtype=np.uint8)),
            axis=1).ravel().tolist())

        else:
            msg.data = array('B', self.points.view(dtype=np.uint8).ravel().tolist())
        return msg

    def filter(self, threshold=10):
        if self.metadata['keep_ring']:
            concat = np.concatenate((self.points, self.rings.reshape((len(points), 1))), axis=1)
            concat = concat[np.logical_and(
                np.logical_not(np.isnan(concat).any(axis=1)),
                concat[:,3]>=threshold)]
            self.points = np.ascontiguousarray(concat[:,:4], dtype=np.float32)
            self.rings = np.ascontiguousarray(concat[:,4:], dtype=np.uint16)

        else:
            self.points = self.points[np.logical_and(
                np.logical_not(np.isnan(self.points).any(axis=1)),
                self.points[:,3]>=threshold)]
        self.metadata['nb_points'] = len(self.points)
        self.metadata['height'] = 1
        self.metadata['width'] = self.metadata['nb_points']

    def transform(self, matrix):
        self.points[:,:3] = np.transpose(
            matrix @ np.concatenate((self.points[:,:3].transpose(),
                                     np.ones((1, self.metadata['nb_points'])))))[:,:3]
        self.matrix = matrix
        self.metadata['procrastinated'] = False

    def update(self, pointcloud):
        if self.metadata['keep_ring']:
            if pointcloud.metadata['keep_ring']:
                self.rings = np.ascontiguousarray(np.concatenate((self.rings, pointcloud.rings)))
            else:
                return False
        self.points = np.ascontiguousarray(np.concatenate((self.points, pointcloud.points)))
        self.metadata['nb_points'] = len(self.points)
        self.metadata['height'] = 1
        self.metadata['width'] = self.metadata['nb_points']
        return True

    def save(self, path):
        save_path = os.path.expanduser(path)
        with open('{}_meta.json'.format(save_path), 'w') as outfile:
            json.dump(self.metadata, outfile, indent=4)

        np.savez_compressed('{}_data'.format(save_path), points=self.points, rings=self.rings, matrix=self.matrix)
