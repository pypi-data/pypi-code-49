"""
Name : InsightFace.py
Author  : Cash
Contact : tkggpdc2007@163.com
Time    : 2020-01-08 10:52
Desc:
"""

import numpy as np
from sklearn.cluster import DBSCAN
from ..libs.common import singleton
from ..libs.face_align import norm_crop
from .FaceDetector import FaceDetector
from .FaceRecognition import FaceRecognition

__all__ = ['InsightFace']


@singleton
class InsightFace:
    def __init__(self,
                 det_name='retinaface_r50_v1',
                 rec_name='arcface_r100_v1',
                 ctx_id=-1,
                 nms=0.4):

        if det_name is not None:
            self.det_model = FaceDetector(det_name, ctx_id=ctx_id, nms=nms)
        if rec_name is not None:
            self.rec_model = FaceRecognition(rec_name, ctx_id=ctx_id)

    def batch_encodings(self, images):
        """
        批量获取人脸编码信息
        :param images: a list of images each has only one face
        :return: a list of encodings
        """
        embeddings = list(np.empty((len(images), 512)))
        for i in range(len(images) - 1, -1, -1):
            bboxes, landmarks = self.face_locations(images[i])
            if len(bboxes) == 1:
                aligns = self.face_alignment(images[i], landmarks)
                embeddings[i] = self.face_encoding(aligns[0])
            else:
                del (images[i])
                del (embeddings[i])
        return embeddings

    def face_locations(self, image, thresh=0.8, scale=1.0):
        """
        获取人脸位置信息
        :param image: a numpy data with one or more faces
        :param thresh: thresh judge if is a face
        :param scale: scale the image to smaller one
        :return: a list of boxes: [[x1,y1,x2,y2]]
        """
        bboxes, landmarks = self.det_model.detect(image, threshold=thresh, scale=scale)
        return bboxes, landmarks

    @staticmethod
    def face_alignment(image, landmarks):
        """
        人脸对齐
        :param image: a numpy data
        :param landmarks: a list of one or more face key-points
        :return: a list of aligned face images
        """
        return [norm_crop(image, landmark=landmark) for landmark in landmarks]

    def face_encoding(self, image):
        """
        获取单个人脸编码
        :param image: an aligned face image
        :return: en embedding
        """
        return self.rec_model.get_embedding(image)

    @staticmethod
    def face_distance(encoding1, encoding2):
        """
        获取人脸编码的欧式距离
        :param encoding1: an encoding
        :param encoding2: an encoding to check
        :return: distance
        """
        return np.linalg.norm(encoding1 - encoding2)

    @staticmethod
    def face_cluster(encodings, min_distance=1.0):
        """
        获取人脸聚类信息，哪些人脸属于同一人脸
        :param encodings: a list of encodings
        :param min_distance: cluster distance
        :return: a list of labels, the number of clusters
        """
        number = len(encodings)
        if number <= 0:
            return [], 0
        matrix = [[np.linalg.norm(encodings[i] - encodings[j]) for j in range(number)] for i in range(number)]

        db = DBSCAN(eps=min_distance, min_samples=1, metric='precomputed')
        db.fit(matrix)
        labels = db.labels_
        num_clusters = len(set(labels)) - (1 if -1 in labels else 0)

        return labels, num_clusters
