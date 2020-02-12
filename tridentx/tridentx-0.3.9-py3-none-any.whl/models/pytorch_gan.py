from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from enum import Enum, unique
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
from torch.nn.parameter import Parameter
from torch._six import container_abcs
from itertools import repeat


from ..backend.common import *
from ..backend.pytorch_backend import to_numpy,to_tensor,Layer,Sequential
from ..layers.pytorch_layers import *
from ..layers.pytorch_activations import  get_activation,Identity,LeakyRelu
from ..layers.pytorch_normalizations import get_normalization,BatchNorm
from ..layers.pytorch_blocks import *
from ..layers.pytorch_pooling import *
from ..optims.pytorch_trainer import *
from ..data.image_common import *
from ..data.utils import download_file_from_google_drive

__all__ = ['gan_builder','UpsampleMode','BuildBlockMode']

_session = get_session()
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_epsilon=_session.epsilon
_trident_dir=_session.trident_dir


def resnet_block(num_filters=64,strides=1,activation='leaky_relu', normalization='batch',use_spectral=False,dilation=1,name=''):
    kernal=1 if strides==1 else 3
    return [ShortCut2d(Sequential(Conv2d_Block((3,3),filter_rate=0.5,strides=1,auto_pad=True,padding_mode=PaddingMode.reflection,use_spectral=use_spectral,normalization=normalization,activation=activation,use_bias=False,dilation=dilation,name=name + '_0_conv'),
                                 Conv2d_Block((1, 1), filter_rate=2 , strides=1, auto_pad=True,padding_mode=PaddingMode.reflection,use_spectral=use_spectral,normalization=normalization, activation=activation,use_bias=False,name=name + '_1_conv')),
                      Identity(),activation=activation,name=name),
            Conv2d_Block((kernal, kernal), num_filters=num_filters, strides=strides, auto_pad=True, padding_mode=PaddingMode.reflection, use_spectral=use_spectral, normalization=normalization, activation=activation, use_bias=False, name=name + '_conv')]

def bottleneck_block(num_filters=64,strides=1,reduce=4,activation='leaky_relu', normalization='batch',use_spectral=False,dilation=1,name=''):
    shortcut = Conv2d_Block((3, 3), num_filters=num_filters, strides=strides, auto_pad=True,
                                padding_mode=PaddingMode.zero, normalization=normalization, activation=None,
                                name=name + '_downsample')
    return ShortCut2d(Sequential(Conv2d_Block((1,1),filter_rate=1,strides=1,auto_pad=True,padding_mode=PaddingMode.reflection,use_spectral=use_spectral,normalization=normalization,activation=activation,use_bias=False,name=name + '_0_conv'),
                                 Conv2d_Block((3, 3), filter_rate=1/reduce , strides=strides, auto_pad=True,padding_mode=PaddingMode.reflection,use_spectral=use_spectral,normalization=normalization, activation=activation,use_bias=False,dilation=dilation,name=name + '_1_conv'),
                                 Conv2d_Block((1,1),num_filters=num_filters,strides=1,auto_pad=True,padding_mode=PaddingMode.reflection,use_spectral=use_spectral,normalization=normalization,activation=None,use_bias=False,name=name + '_2_conv')),
                      shortcut,activation=activation,name=name)


class UpsampleMode(Enum):
    pixel_shuffle = 'pixel_shuffle'
    transpose = 'transpose'
    nearest = 'nearest'
    bilinear = 'bilinear'

class BuildBlockMode(Enum):
    base = 'base'
    resnet = 'resnet'
    bottleneck = 'bottleneck'




def gan_builder(
        noise_shape=100,
        image_width=256,
        upsample_mode=UpsampleMode.nearest,
        generator_build_block=BuildBlockMode.resnet,
        discriminator_build_block=BuildBlockMode.resnet,
        use_spectral=False,
        activation='leaky_relu',
        generator_norm='batch',
        discriminator_norm='batch',
        use_dilation=False,
        use_dropout=False,
        use_self_attention=False):

    noise_input=torch.tensor(data=np.random.normal(0, 1,size=noise_shape))

    def build_generator():
        layers=[]
        initial_size=8
        if image_width in [192,96,48]:
            initial_size=6
        elif image_width in [144,72,36]:
            initial_size = 9
        elif image_width in [160,80]:
            initial_size = 10
        layers.append(Dense(16 * initial_size * initial_size, activation=None, name='fc'))
        layers.append(BatchNorm())
        layers.append(LeakyRelu())
        layers.append(Reshape((16, initial_size, initial_size), name='reshape'))

        if upsample_mode == UpsampleMode.pixel_shuffle:
            layers.append(Conv2d_Block((3, 3), 256, strides=1, auto_pad=True, use_spectral=use_spectral,use_bias=False, activation=activation,normalization=generator_norm))
        else:
            layers.append(Conv2d_Block((3, 3), 128, strides=1, auto_pad=True,use_spectral=use_spectral, use_bias=False, activation=activation,normalization=generator_norm))

        filter =64 if upsample_mode == UpsampleMode.pixel_shuffle else 128
        current_width=initial_size
        i=0
        while current_width<image_width:
            scale = 2 if (image_width // current_width) % 2 == 0 else (image_width // current_width)

            dilation=1
            if use_dilation:
                dilation=2 if current_width>=64 else 1

            if  i>0 and upsample_mode == UpsampleMode.pixel_shuffle:
                filter = max(filter // 2, 32) if i%2==0 else filter
            elif upsample_mode != UpsampleMode.pixel_shuffle:
                filter = max(filter//2, 32)


            if upsample_mode==UpsampleMode.transpose:
                layers.append(TransConv2d_Block((3,3),filter_rate=1,strides=scale,auto_pad=True,use_spectral=use_spectral,use_bias=False,activation=activation,normalization=generator_norm,dilation=dilation,name='transconv_block{0}'.format(i)))
            else:
                layers.append(Upsampling2d(scale_factor=scale,mode=upsample_mode.value,name='{0}{1}'.format(upsample_mode.value,i)))

            if use_self_attention and current_width == initial_size * 2:
                layers.append(SelfAttention(16, name='self_attention'))

            if generator_build_block == BuildBlockMode.base :
                layers.append(Conv2d_Block((3, 3), filter, strides=1, auto_pad=True, use_spectral=use_spectral,use_bias=False, activation=activation, normalization=generator_norm,dilation=dilation,name='base_block{0}'.format(i)))
            elif generator_build_block == BuildBlockMode.resnet:
                layers.extend(resnet_block(filter,  strides=1, activation=activation, use_spectral=use_spectral,normalization=generator_norm, dilation=dilation,name='resnet_block{0}'.format(i)))
            elif generator_build_block == BuildBlockMode.bottleneck:
                layers.append( bottleneck_block(filter,  strides=1, activation=activation, use_spectral=use_spectral,normalization=generator_norm,  dilation=dilation, name='resnet_block{0}'.format(i)))

            if use_dropout and current_width==initial_size*4 :
                layers.append(Dropout(0.2))


            current_width = current_width*scale
            i=i+1
        layers.append( Conv2d((5, 5), 3, strides=1, auto_pad=True, use_bias=False, activation='tanh',name='last_layer'))
        return Sequential(layers,name='generator')


    def build_discriminator():
        layers = []
        layers.append(Conv2d((5,5), 32, strides=1, auto_pad=True, use_bias=False, activation=activation,name='first_layer'))
        layers.append(Conv2d_Block((3, 3), 64, strides=2, auto_pad=True, use_spectral=use_spectral,use_bias=False, activation=activation,normalization=discriminator_norm ,name='second_layer'))
        filter = 64
        current_width =image_width//2
        i=0
        while current_width >8:
            filter = filter * 2 if i % 2 == 1 else filter
            if discriminator_build_block == BuildBlockMode.base:
                layers.append(Conv2d_Block((3, 3), filter  , strides=2, auto_pad=True, use_spectral=use_spectral,use_bias=False, activation=activation, normalization=discriminator_norm,name='base_block{0}'.format(i)))
            elif discriminator_build_block == BuildBlockMode.resnet:
                layers.extend(resnet_block(filter , strides=2,activation=activation, use_spectral=use_spectral,normalization=discriminator_norm,name='resnet_block{0}'.format(i)))
            elif discriminator_build_block == BuildBlockMode.bottleneck:
                layers.append(bottleneck_block(filter, strides=2,reduce=2, activation=activation, use_spectral=use_spectral,normalization=discriminator_norm, name='bottleneck_block{0}'.format(i)))

            current_width = current_width//2
            i = i + 1
        if use_self_attention :
            layers.insert(-1,SelfAttention(16, name='self_attention'))
        if use_dropout and not use_self_attention:
            layers.insert(-1,Dropout(0.2))
        layers.append(Conv2d((3, 3), 1, strides=1, auto_pad=True, use_bias=False, activation=None,name='features'))
        layers.append(GlobalAvgPool2d())
        return Sequential(layers,name='discriminator')

    gen=ImageGenerationModel(input_shape=(noise_shape),output=build_generator())
    gen.model.name='generator'
    dis=ImageClassificationModel(input_shape=(3,image_width,image_width),output=build_discriminator())
    dis.model.name = 'discriminator'
    return gen,dis









