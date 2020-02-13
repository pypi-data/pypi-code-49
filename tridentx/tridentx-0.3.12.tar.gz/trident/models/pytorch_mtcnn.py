from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import matplotlib
import platform
if platform.system() not in ['Linux', 'Darwin'] and not platform.system().startswith('CYGWIN'):
    matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from IPython import display
import itertools
from matplotlib.collections import PolyCollection
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
import torchvision


from ..backend.common import *
from ..backend.pytorch_backend import to_numpy,to_tensor,Layer,Sequential,Combine
from ..backend.pytorch_backend import *
from ..layers.pytorch_layers import *
from ..layers.pytorch_activations import  get_activation,Identity,PRelu
from ..layers.pytorch_normalizations import get_normalization
from ..layers.pytorch_blocks import *
from ..layers.pytorch_pooling import *
from ..optims.pytorch_trainer import *
from ..data.image_common import *
from ..data.utils import download_file_from_google_drive

__all__ = ['Pnet','Rnet','Onet','Mtcnn']

_session = get_session()
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_epsilon=_session.epsilon
_trident_dir=_session.trident_dir


dirname = os.path.join(_trident_dir, 'models')
if not os.path.exists(dirname):
    try:
        os.makedirs(dirname)
    except OSError:
        # Except permission denied and potential race conditions
        # in multi-threaded environments.
        pass


p_net=Sequential(
    Conv2d((3,3),10,strides=1,auto_pad=False,use_bias=True,name='conv1'),
    PRelu(),
    MaxPool2d((2,2),strides=2,auto_pad=False),
    Conv2d((3, 3), 16, strides=1, auto_pad=False,use_bias=True,name='conv2'),
    PRelu(),
    Conv2d((3,3),32,strides=1,auto_pad=False,use_bias=True,name='conv3'),
    PRelu(),
    Combine(
        Conv2d((1,1),1,strides=1,auto_pad=False,use_bias=True,activation='sigmoid',name='conv4_1'),
        Conv2d((1,1),4,strides=1,auto_pad=False,use_bias=True,name='conv4_2'),
        Conv2d((1,1),10,strides=1,auto_pad=False,use_bias=True,name='conv4_3')))
p_net.name='pnet'


r_net=Sequential(
    Conv2d((3,3),28,strides=1,auto_pad=False,use_bias=True,name='conv1'),
    PRelu(),
    MaxPool2d((3,3),strides=2,auto_pad=False),
    Conv2d((3, 3), 48, strides=1, auto_pad=False,use_bias=True,name='conv2'),
    PRelu(),
    MaxPool2d((3,3),strides=2,auto_pad=False),
    Conv2d((2,2),64,strides=1,auto_pad=False,use_bias=True,name='conv3'),
    PRelu(),
    Flatten(),
    Dense(128,activation=None,use_bias=True,name='conv4'),
    PRelu(),
    Combine(
        Dense(1,activation='sigmoid',use_bias=True,name='conv5_1'),
        Dense(4,activation=None,use_bias=True,name='conv5_2'),
        Dense(10,activation=None,use_bias=True,name='conv5_3')))
r_net.name='rnet'


o_net=Sequential(
    Conv2d((3,3),32,strides=1,auto_pad=False,use_bias=True,name='conv1'),
    PRelu(),
    MaxPool2d((3,3),strides=2,auto_pad=False),
    Conv2d((3, 3), 64, strides=1, auto_pad=False,use_bias=True,name='conv2'),
    PRelu(),
    MaxPool2d((3,3),strides=2,auto_pad=False),
    Conv2d((3,3),64,strides=1,auto_pad=False,use_bias=True,name='conv3'),
    PRelu(),
    MaxPool2d((2, 2), strides=2,auto_pad=False),
    Conv2d((2, 2), 128, strides=1, auto_pad=False,use_bias=True,name='conv4'),
    PRelu(),
    Flatten(),
    Dense(256,activation=None,use_bias=True,name='conv5'),
    PRelu(),
    Combine(
        Dense(1,activation='sigmoid',use_bias=True,name='conv6_1'),
        Dense(4,activation=None,use_bias=True,name='conv6_2'),
        Dense(10,activation=None,use_bias=True,name='conv6_3')))
o_net.name='onet'


def Pnet(pretrained=True,
             input_shape=(3,12,12),
             **kwargs):
    if input_shape is not None and len(input_shape)==3:
        input_shape=tuple(input_shape)
    else:
        input_shape=(3,12,12)
    pnet =ImageDetectionModel(input_shape=(3,12,12),output=p_net)
    pnet.preprocess_flow = [normalize(0, 255), image_backend_adaptive]
    if pretrained==True:
        download_file_from_google_drive('1w9ahipO8D9U1dAXMc2BewuL0UqIBYWSX',dirname,'pnet.pth')
        recovery_model=torch.load(os.path.join(dirname,'pnet.pth'))
        recovery_model.to(_device)
        pnet.model=recovery_model
    return pnet


def Rnet(pretrained=True,
             input_shape=(3,24,24),
             **kwargs):
    if input_shape is not None and len(input_shape)==3:
        input_shape=tuple(input_shape)
    else:
        input_shape=(3,24,24)
    rnet =ImageDetectionModel(input_shape=(3,24,24),output=r_net)
    rnet.preprocess_flow = [normalize(0, 255), image_backend_adaptive]
    if pretrained==True:
        download_file_from_google_drive('1CH7z133_KrcWMx9zXAblMCV8luiQ3wph',dirname,'rnet.pth')
        recovery_model=torch.load(os.path.join(dirname,'rnet.pth'))
        recovery_model.to(_device)
        rnet.model=recovery_model
    return rnet

def Onet(pretrained=True,
             input_shape=(3,48,48),
             **kwargs):
    if input_shape is not None and len(input_shape)==3:
        input_shape=tuple(input_shape)
    else:
        input_shape=(3,48,48)
    onet =ImageDetectionModel(input_shape=(3,48,48),output=o_net)
    onet.preprocess_flow = [normalize(0, 255), image_backend_adaptive]
    if pretrained==True:
        download_file_from_google_drive('1a1dAlSzJOAfIz77Ic38JMQJYWDG_b7-_',dirname,'onet.pth')
        recovery_model=torch.load(os.path.join(dirname,'onet.pth'))
        recovery_model.to(_device)
        onet.model=recovery_model
    return onet



class DetectorHead(Layer):
    def __init__(self, cellsize=12,threshould=0.6, **kwargs):
        super(DetectorHead, self).__init__(**kwargs)
        self.cellsize=cellsize
        self.threshould=threshould
        self._built =True

    def forward(self, input,**kwargs):
        boxprobs,boxregs,landscape=input
        boxprobs=boxprobs[0]
        height,width=boxprobs.shape[1:]
        if boxprobs.size(0)==2:
            boxprobs=boxprobs[1:,:,:]
        strides=2
        cell_size=12
        boxregs=boxregs[0]
        input_shape=boxprobs.size()
        grid=meshgrid(boxprobs.size(1),boxprobs.size(2))
        grid=grid.view(2,-1)
        score = boxprobs[0]
        cutoff=get_cutoff(score)

        y,x = torch.where(score> cutoff)

        boxregs = boxregs.permute(1,2,0)

        score = score[(y,x )]
        reg=boxregs[(y,x )].transpose(1,0)
        bb = torch.stack([x,y], dim=0)

        q1 = (strides * bb + 1)
        q2 =(strides * bb +cell_size - 1 + 1)

        w = q2[0, :] - q1[0, :] + 1
        h = q2[1, :] - q1[1, :] + 1


        b1 = q1[0, :] + reg[0, :] * w
        b2 = q1[1, :] + reg[1, :] * h
        b3 =q2[0, :] + reg[2, :] * w
        b4 =q2[1, :] + reg[3, :] * h

        boxs=torch.stack([b1,b2,b3,b4,score],dim=-1)
        keep =torchvision.ops.boxes.remove_small_boxes(boxs[:,:4],min_size=5)
        boxs=boxs[keep]
        print('total {0} boxes cutoff={1} '.format(len(x), cutoff))
        if boxs is None or len(boxs.size()) == 0:
            return None
        elif len(boxs.size())==1:
            boxs=boxs.unsqueeze(0)
        return boxs

def remove_useless_boxes(boxes,image_size=None,min_size=5):
    height, width = image_size if image_size is not None else (None,None)

    x1, y1, x2, y2, score = [boxes[:, i] for i in range(5)]
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    boxes=boxes[area>min_size*min_size]
    x1, y1, x2, y2, score = [boxes[:, i] for i in range(5)]
    greater0=x1.gt(0).float() * x2.gt(0).float() * y1.gt(0).float() * y1.gt(0).float()
    boxes=boxes[greater0>0]
    x1, y1, x2, y2, score = [boxes[:, i] for i in range(5)]
    w=(x2 - x1 )
    boxes=boxes[w>1]
    x1, y1, x2, y2, score = [boxes[:, i] for i in range(5)]
    h=(y2 - y1)
    boxes = boxes[h > 1]


    return boxes


def clip_boxes_to_image(boxes, size):

    """
    Clip boxes so that they lie inside an image of size `size`.
    Arguments:
        boxes (Tensor[N, 4]): boxes in (x1, y1, x2, y2) format
        size (Tuple[height, width]): size of the image
    Returns:
        clipped_boxes (Tensor[N, 4])
    """
    height,width=size
    boxes[:,0]= boxes[:,0].clamp(min=0, max=width)
    boxes[:,1]= boxes[:,1].clamp(min=0, max=height)
    boxes[:,2]= boxes[:,2].clamp(min=0, max=width)
    boxes[:,3]= boxes[:,3].clamp(min=0, max=height)
    return boxes

def nms(boxes, threshold, mode='Union',image_size=None,min_size=5):
    """
        non max suppression

    Parameters:
    ----------
        box: numpy array n x 5
            input bbox array
        overlap_threshold: float number
            threshold of overlap
        mode: float number
            how to compute overlap ratio, 'Union' or 'Min'
    Returns:
    -------
        index array of the selected bbox
    """
    # if there are no boxes, return an empty list
    height, width=image_size


    boxes=remove_useless_boxes(boxes,image_size)
    boxes=clip_boxes_to_image(boxes,image_size)
    if len(boxes) == 0:
        return []

    # initialize the list of picked indexes
    pick = []
    box_len=len(boxes)
    # grab the coordinates of the bounding boxes
    x1, y1, x2, y2, score = [boxes[:, i] for i in range(5)]

    area = (x2 - x1 + 1) * (y2 - y1 + 1)


    sorted_index =  torch.argsort(score,descending=False)
    # keep looping while some indexes still remain in the indexes list
    adjust_bbox=[]
    while len(sorted_index) > 0:
        # grab the last index in the indexes list and add the index value to the list of picked indexes
        last = len(sorted_index) - 1
        i = sorted_index[-1]
        pick.append(int(i))
        sorted_index = sorted_index[:-1]
        if len(sorted_index)==1:
            break
        #sorted_index = sorted_index[:-1]
        xx1= torch.max(x1[i], x1[sorted_index[:last]])
        yy1 =  torch.max(y1[i], y1[sorted_index[:last]])
        xx2 =  torch.min(x2[i], x2[sorted_index[:last]])
        yy2 =  torch.min(y2[i], y2[sorted_index[:last]])
        # compute the width and height of the bounding box
        xc = ((xx1 + xx2).abs_() / 2 - (x1[sorted_index[:last]]+ x2[sorted_index[:last]]) / 2)
        yc = ((yy1 + yy2).abs_() / 2 - (y1[sorted_index[:last]] + y2[sorted_index[:last]]) / 2)

        w =(xx2 - xx1 + 1).clamp_(0)
        h = (yy2 - yy1 + 1).clamp_(0)
        inter = w * h

        xc_diff = (xc- 0.4 * w).lt(0).float()
        yc_diff =  (yc- 0.4 * h).lt(0).float()
        close_idx = xc_diff + yc_diff


        #any of happends will dedup
        IoU = inter / (area[i] + area[sorted_index[:last]] - inter)
        IoU1 = inter / area[i]
        IoU2 = inter / area[sorted_index[:last]]
        IoU[IoU1 > 0.9] = 0.9
        IoU[IoU2 > 0.9] = 0.9
        #IoU[close_idx == 2] = 0.9
        sorted_index = sorted_index[IoU <= threshold]

    if boxes is not None and len(pick)>0 :
        try:
            out=boxes[pick]
            if len(out.size())==1:
                out=out.unsqueeze(0)
                if len(out)==0:
                    return None
            return out
        except Exception as e:
            print(e)
            print('box_len',box_len)
            print('pick',len(pick))
            print('boxes',len(boxes))

    return None


def get_cutoff(score):
    score = to_numpy(score).reshape(-1)
    bins = np.arange(0, 1, 0.05)
    cnt_, bins_ = np.histogram(score, bins)
    cnt_ = np.cumsum(cnt_) / np.sum(cnt_)
    grads = cnt_[1:] - cnt_[:-1]
    grads1 = grads[1:] - grads[:-1]
    high=np.argmax(grads)
    grads1=grads1[high+1:]
    if len(grads1)==0:
        return bins[high-1]
    low=np.argmin(grads1)
    # if bins[high+1+low+1]<0.4:
    #     return  math.sqrt(bins[high+1+low]*0.5)

    return bins[high+1+low+1]


class Mtcnn(ImageDetectionModel):
    def __init__(self, pretrained=True,  **kwargs):
        pnet = ImageDetectionModel(input_shape=(3, 12, 12), output=p_net).model
        self.rnet = ImageDetectionModel(input_shape=(3, 24, 24), output=r_net).model
        self.onet = ImageDetectionModel(input_shape=(3, 48, 48), output=o_net).model
        if pretrained == True:
            pnet = Pnet().model
            self.rnet = Rnet().model
            self.onet = Onet().model

        pnet.add_module('pnet_detector',DetectorHead(cellsize=12,threshould=0.6))

        super(Mtcnn, self).__init__(input_shape=(3,224,224),output=pnet)
        self.pnet=pnet
        self.model=pnet
        self.preprocess_flow =[normalize(0,255)]
        self.minsize=5
        self.detection_threshould= [0.6, 0.5, 0.5]


    def get_image_pyrimid(self,img,minsize=5,factor= 0.709):
        min_face_area = (minsize, minsize)
        h = img.shape[0]
        w = img.shape[1]
        minl = np.amin([h, w])
        m = 12.0 / minsize
        minl = minl * m
        # create scale pyramid
        scales = []
        images = []
        factor_count = 0
        while minl >= 12:
            scales += [m * np.power(factor, factor_count)]
            scaled_img = rescale(scales[-1])(img.copy())
            if img is not None:
                for func in self.preprocess_flow:
                    if inspect.isfunction(func):
                        scaled_img=func(scaled_img)
            images.append(image_backend_adaptive(scaled_img))
            minl = minl * factor
            factor_count += 1
        return images, scales

    #adjust bbox like square
    def rerec(self,bboxA,img_shape):
        """Convert bboxA to square."""

        h = bboxA[:, 3] - bboxA[:, 1]
        w = bboxA[:, 2] - bboxA[:, 0]
        max_len = np.maximum(w, h)


        bboxA[:, 0] = bboxA[:, 0] -0.5*(max_len-w)
        bboxA[:, 1] = bboxA[:, 1] -0.5*(max_len-h)
        bboxA[:, 2] = bboxA[:, 0]+max_len
        bboxA[:, 3] =bboxA[:,  1]+max_len
        return bboxA


    def infer_single_image(self,img):
        if self.model.built:
            self.model.to(self.device)
            self.model.eval()
            img=image2array(img)
            if img.shape[-1]==4:
                img=img[:,:,:3]

            imgs,scales=self.get_image_pyrimid(img)
            boxes_list=[]
            for i in range(len(scales)):
                scaled_img=imgs[i]
                boxes=self.pnet(to_tensor(np.expand_dims(scaled_img, 0)))
                if boxes is not None and len(boxes)>0:
                    scale=scales[i]
                    box=boxes[:,:4]/scale
                    score=boxes[:,4:]
                    boxes = torch.cat([box.round_(), score], dim=1)
                    if len(boxes) > 0:
                        boxes_list.append(boxes)

            #######################################
            #########pnet finish
            #######################################
            if len(boxes_list) > 0:
                boxes=to_tensor(torch.cat(boxes_list, dim=0))

                print('total {0} boxes in pnet in all scale '.format(len(boxes)))

                boxes =nms(boxes, threshold=0.5,image_size=(img.shape[0],img.shape[1]),min_size=self.minsize)
                print('total {0} boxes after nms '.format(len(boxes)))
                score = to_numpy(boxes[:, 4]).reshape(-1)
                if boxes is not None:
                    #prepare rnet input
                    boxes_np = to_numpy(boxes)
                    boxes_np = self.rerec(boxes_np, img.shape)
                    new_arr = np.zeros((boxes_np.shape[0], 3, 24, 24))

                    for k in range(boxes_np.shape[0]):
                        box = boxes_np[k]
                        crop_img = img.copy()[int(box[1]):int(box[3]), int(box[0]):int(box[2]), :]
                        if crop_img.shape[0] > 0 and crop_img.shape[1] > 0:
                            new_arr[k] = resize((24, 24))(crop_img / 255.0).transpose([2, 0, 1])
                        else:
                            print(box)

                    new_arr = to_tensor(new_arr)
                    r_out1, r_out2, r_out3 = self.rnet(new_arr)
                    print(r_out1.min(), r_out1.max())
                    boxes[:, 0] = boxes[:, 0] + r_out2[:,0] *(boxes[:,2]-boxes[:,0])
                    boxes[:, 1] = boxes[:, 1] + r_out2[:, 1] *(boxes[:,3]-boxes[:,1])
                    boxes[:, 2] = boxes[:, 2] + r_out2[:, 2] *(boxes[:,2]-boxes[:,0])
                    boxes[:, 3] = boxes[:, 3] + r_out2[:, 3] *(boxes[:,3]-boxes[:,1])
                    boxes[:, 4] = r_out1[:, 0]
                    #boxes[:, 4]=(r_out1[:,0]* boxes[:, 4]).sqrt_()

                    score = to_numpy(boxes[:, 4]).reshape(-1)
                    cutoff=get_cutoff(score)
                    print('rnet   max:{0} min:{1}  mean:{2}'.format(score.min(), score.max(), score.mean()))

                    boxes = boxes[score > cutoff]
                    print('total {0} boxes in rnet cutoff={1} '.format(len(boxes),cutoff))

                    #######################################
                    #########rnet finish
                    #######################################

                    boxes=nms(boxes,  threshold=0.6,image_size=(img.shape[0],img.shape[1]),min_size=self.minsize)
                    print('total {0} boxes after nms '.format(len(boxes)))
                    boxes_np=to_numpy(boxes)
                    boxes = clip_boxes_to_image(boxes, (img.shape[0], img.shape[1]))
                    boxes_np=self.rerec(boxes_np,img.shape)
                    new_arr=np.zeros((boxes_np.shape[0],3,48,48))


                    for k in range(boxes_np.shape[0]):
                        box=boxes_np[k]
                        crop_img=img.copy()[int(box[1]):int(box[3]),int(box[0]):int(box[2]),:]
                        if crop_img.shape[0]>0 and crop_img.shape[1]>0:
                            new_arr[k]=resize((48,48))(crop_img/255.0).transpose([2,0,1])
                        else:
                            print(box)

                    new_arr=to_tensor(new_arr)
                    o_out1, o_out2,o_out3  = self.onet(new_arr)
                    print(o_out1.min(),o_out1.max())
                    boxes[:, 0] = boxes[:, 0] +o_out2[:,0]*(boxes[:,2]-boxes[:,0])
                    boxes[:, 1] = boxes[:, 1]  +o_out2[:,1]*(boxes[:,3]-boxes[:,1])
                    boxes[:, 2] = boxes[:, 2]  +o_out2[:,2]*(boxes[:,2]-boxes[:,0])
                    boxes[:, 3] = boxes[:, 3]  +o_out2[:,3]*(boxes[:,3]-boxes[:,1])

                    boxes[:, 4]=o_out1[:,0]

                    landmarks_x = boxes[:, 0]  + o_out3[:,0::2] * (boxes[:, 2] - boxes[:, 0] )
                    landmarks_y = boxes[:, 1]  + o_out3[:,1::2] * (boxes[:, 3] - boxes[:, 1] )

                    boxes=torch.cat([boxes,landmarks_x,landmarks_y],dim=-1)

                    score=boxes[:,4]
                    cutoff=get_cutoff(score)
                    boxes=boxes[score>cutoff+0.1]
                    print('total {0} boxes in onet  cutoff={1} '.format(len(boxes),cutoff+0.1))
                    #######################################
                    #########onet finish
                    #######################################
                    boxes=nms(boxes, threshold=0.5,image_size=(img.shape[0],img.shape[1]),min_size=self.minsize)
                    print('total {0} boxes after final nms '.format(len(boxes)))
                    return boxes
            else:
                return None
            #idx=int(np.argmax(result,-1)[0])

        else:
            raise  ValueError('the model is not built yet.')
    def generate_bboxes(self,*outputs,threshould=0.5,scale=1):
        raise NotImplementedError
    def nms(self,bboxes):
        raise NotImplementedError


