
from __future__ import division
from __future__ import print_function
import importlib
import math
import os
import inspect
import numpy as np
from collections import *
from functools import partial
import uuid
from copy import copy, deepcopy
from collections import deque
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import init

from torch._six import container_abcs
from itertools import repeat


from ..backend.common import *
from ..backend.pytorch_backend import to_numpy,to_tensor,Layer,Sequential,Input,summary
from ..layers.pytorch_layers import *
from ..layers.pytorch_activations import  get_activation,Identity,Relu
from ..layers.pytorch_normalizations import get_normalization,BatchNorm2d
from ..layers.pytorch_blocks import *
from ..layers.pytorch_pooling import *
from ..optims.pytorch_trainer import *
from ..data.image_common import *
from ..data.utils import download_model_from_google_drive


__all__ = []

_session = get_session()
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_epsilon=_session.epsilon
_trident_dir=_session.trident_dir
_backend = _session.backend

dirname = os.path.join(_trident_dir, 'models')
if not os.path.exists(dirname):
    try:
        os.makedirs(dirname)
    except OSError:
        # Except permission denied and potential race conditions
        # in multi-threaded environments.
        pass




def DeepLabHead(classes=20, atrous_rates=(6, 12, 18),num_filters=256):
    return Sequential(
        ASPP(atrous_rates,num_filters=num_filters),
        Conv2d_Block((3,3),num_filters,auto_pad=True,use_bias=False,activation='relu',normalization='batch'),
        Conv2d((1,1),num_filters=classes,strides=1,auto_pad=True,activation='sigmoid',name='classifier')
        )



def ASPPPooling(num_filters,size):
    return Sequential(AdaptiveAvgPool2d((1,1)),
                      Conv2d_Block((1,1),num_filters,strides=1,use_bias=False,activation='relu',normalization='batch'),
                      Upsampling2d(size=(size[-2], size[-1]),mode='bilinear', align_corners=False))



class ASPP(Layer):
    def __init__(self, atrous_rates,num_filters=256):
        super(ASPP, self).__init__()
        self.num_filters=num_filters
        self.convs = ShortCut2d( mode=ShortcutMode.concate)
        self.convs.add_module('conv1',Conv2d_Block((1,1),num_filters=num_filters,strides=1,use_bias=False,activation='relu',normalization='batch'))


        rate1, rate2, rate3 = tuple(atrous_rates)

        self.convs.add_module('aspp_dilation1',Conv2d_Block((1,1),num_filters=num_filters,strides=1,use_bias=False,activation='relu',normalization='batch',dilation=rate1))
        self.convs.add_module('aspp_dilation2',Conv2d_Block((1,1),num_filters=num_filters,strides=1,use_bias=False,activation='relu',normalization='batch',dilation=rate2))
        self.convs.add_module('aspp_dilation3',Conv2d_Block((1,1),num_filters=num_filters,strides=1,use_bias=False,activation='relu',normalization='batch',dilation=rate3))

        self.project =Conv2d_Block( (1,1),num_filters,strides=1,use_bias=False, bias=False,activation='relu',normalization='batch',dilation=1,dropout_rate=0.5)

    def build(self, input_shape):
        if self._built == False :
            self.convs.add_module('aspp_pooling',ASPPPooling(self.num_filters, to_list(input_shape[-2:])))
            self.to(self.device)
            self._built = True

    def forward(self, *x):
        x = enforce_singleton(x)
        x=self.convs(x)
        x=self.project(x)
        return x



def DeeplabV3(backbond,
             input_shape=(3,224,224),
             classes=10,
             **kwargs):
    input_shape=tuple(input_shape)
    deeplab=Sequential(name='deeplabv3')

    deeplab.add_module('backbond',backbond)
    deeplab.add_module('classifier', DeepLabHead(classes=classes,num_filters=128))
    deeplab.add_module('upsample', Upsampling2d(scale_factor=16, mode='bilinear', align_corners=False))
    model = ImageSegmentationModel(input_shape=input_shape, output=deeplab)
    return model

