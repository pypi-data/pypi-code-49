"""
Name : FaceRecognition.py
Author  : Cash
Contact : tkggpdc2007@163.com
Time    : 2020-01-08 10:52
Desc:
"""

from __future__ import division
import mxnet as mx
import numpy as np
import cv2
from ..libs.model_store import get_model_file
from ..libs.common import singleton

__all__ = ['FaceRecognition']


@singleton
class FaceRecognition:
    def __init__(self, model_name="arcface_r100_v1", ctx_id=-1):
        self.param_file = get_model_file(model_name)
        self.image_size = (112, 112)
        if ctx_id >= 0:
            self.ctx = mx.gpu(ctx_id)
        else:
            self.ctx = mx.cpu()
        self._load_model()

    def _load_model(self):
        pos = self.param_file.rfind('-')
        prefix = self.param_file[0:pos]
        pos2 = self.param_file.rfind('.')
        epoch = int(self.param_file[pos + 1:pos2])
        sym, arg_params, aux_params = mx.model.load_checkpoint(prefix, epoch)
        all_layers = sym.get_internals()
        sym = all_layers['fc1_output']

        model = mx.mod.Module(symbol=sym, context=self.ctx, label_names=None)
        data_shape = (1, 3) + self.image_size
        model.bind(data_shapes=[('data', data_shape)])
        model.set_params(arg_params, aux_params)

        data = mx.nd.zeros(shape=data_shape, ctx=self.ctx)
        db = mx.io.DataBatch(data=(data,))
        model.forward(db, is_train=False)
        embedding = model.get_outputs()[0].asnumpy()
        self.model = model

    def get_embedding(self, img):
        data = np.zeros((img.shape[0], img.shape[1], 3))
        if len(img.shape) == 2:
            img = img.reshape(img.shape[0], img.shape[1], 1)
            for i in range(3):
                data[:, :, i] = img[:, :, 0]
        else:
            for i in range(3):
                data[:, :, i] = img[:, :, i]

        data = np.transpose(data, (2, 0, 1))
        data = np.expand_dims(data, axis=0)
        data = mx.nd.array(data, ctx=self.ctx)
        db = mx.io.DataBatch(data=(data,))
        self.model.forward(db, is_train=False)
        embedding = self.model.get_outputs()[0].asnumpy().flatten()
        embedding_norm = np.linalg.norm(embedding)
        normed_embedding = embedding / embedding_norm
        return normed_embedding

