from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import six
import os
import random
import re
import numpy as np
import math
from skimage import exposure
from skimage import morphology
from skimage import color
from skimage import  transform,exposure
from skimage.filters import *
from ..backend.common import *
from itertools import repeat

__all__ = ['read_image','read_mask','save_image','save_mask','image2array','array2image','mask2array','array2mask','list_pictures','normalize','unnormalize','random_crop','resize','rescale','add_noise','gray_scale','to_rgb','auto_level','random_invert_color',
           'image_backend_adaptive','reverse_image_backend_adaptive','random_adjust_hue', 'random_channel_shift', 'random_cutout','random_center_crop','adjust_gamma','random_adjust_gamma','adjust_contast','random_adjust_contast','clahe','erosion_then_dilation','image_erosion','image_dilation','adaptive_binarization']


_session=get_session()
_backend=_session.backend
_image_backend=_session.image_backend

if _image_backend=='opencv':
    from ..backend.opencv_backend import *
else:
    from ..backend.pillow_backend import *


read_image=read_image
read_mask=read_mask
save_image=save_image
save_mask=save_mask
image2array=image2array
array2image=array2image
mask2array=mask2array
array2mask=array2mask



def list_pictures(directory, ext='jpg|jpeg|bmp|png|ppm'):
    return [os.path.join(root, f)
            for root, _, files in os.walk(directory) for f in files
            if re.match(r'([\w]+\.(?:' + ext + '))', f)]

def check_same_size(*images):
    result=True
    height, width = images[0].shape[:2]
    #check same isze
    for img in images:
        hh, ww = images[0].shape[:2]
        if hh==height and ww==width:
            pass
        else:
            result=False
    return True


def random_augmentation(func):
    def wrapper(prob=0,*args, **kwargs):
        if random.random()<=prob:
            return func(*args, **kwargs)

    return wrapper








def add_noise(intensity=0.1):
    def img_op(image:np.ndarray):
        rr=random.randint(0,10)
        orig_min=image.min()
        orig_max=image.max()
        noise = np.random.standard_normal(image.shape) *(intensity*(orig_max-orig_min))
        if rr % 2 == 0:
            noise = np.random.uniform(-1,1,image.shape) *(intensity*(orig_max-orig_min))
        image=np.clip(image+noise,orig_min,orig_max)
        return image
    return img_op

def normalize(mean,std):
    def img_op(image:np.ndarray):
        norm_mean = mean
        norm_std = std
        if isinstance(norm_mean,(float,int)) and image.ndim==3:
            norm_mean=np.array([norm_mean,norm_mean,norm_mean])
            norm_mean=np.expand_dims(norm_mean,-2)
            norm_mean = np.expand_dims(norm_mean, -2)
        if isinstance(norm_std, (float, int)) and image.ndim==3:
            norm_std = np.array([norm_std,norm_std,norm_std])
            norm_std = np.expand_dims(norm_std, -2)
            norm_std = np.expand_dims(norm_std, -2)
        if  image.ndim==3:
            return (image-norm_mean)/norm_std
        elif image.ndim==2:
            if isinstance(norm_mean, (float, int)) and isinstance(norm_std, (float, int)):
                return (image - norm_mean) / norm_std
        return image

    img_op.mean=mean
    img_op.std=std
    return img_op

def unnormalize(mean,std):
    def img_op(image:np.ndarray):
        image=reverse_image_backend_adaptive(image)
        norm_mean = mean
        norm_std = std
        if isinstance(norm_mean,tuple):
            norm_mean=list(norm_mean)

        if isinstance(norm_std,tuple):
            norm_std=list(norm_std)

        if isinstance(norm_mean,(float,int))  and isinstance(norm_std, (float, int)) and image.ndim==3:
            return image *float(norm_std)+ float(norm_mean)
        elif  isinstance(norm_mean,list) and isinstance(norm_std,list) and len(norm_mean)==1 and len(norm_std)==1:
            return image *float(norm_std[0])+float(norm_mean[0])
        elif  isinstance(norm_mean,list) and isinstance(norm_std,list) and len(norm_mean)==3 and len(norm_std)==3:
            norm_mean = np.reshape(np.array(norm_mean),(1,1,3))
            norm_std = np.reshape(np.array(norm_std),(1,1,3))
            return image *norm_std+ norm_mean
        return image
    return img_op


#0: Nearest-neighbor 1: Bi-linear (default) 2: Bi-quadratic 3: Bi-cubic 4: Bi-quartic 5: Bi-quintic
def resize(size,keep_aspect=True,order=1):
    def img_op(image:np.ndarray):
        output = np.ones((size[1], size[0], 3))
        multichannel = True
        if len(image.shape) == 2:
            multichannel = False
            # output = np.ones((size[1], size[0]))
            # multichannel = False
            # counts, bins = np.histogram(image.reshape([-1]), np.arange(0, 255, 32).tolist())
            # if counts[:3].sum()/counts.sum()>0.6:
            #     output=output*0.0
            # elif counts[:2].sum() / counts.sum() < 0.3:
            #     output = output * 255
            # else:
            #     output = output * counts[-4:].sum() / counts.sum()*255.0


        if keep_aspect:
            scalex=size[0]/image.shape[1]
            scaley = size[1] / image.shape[0]

            scale=min(scalex,scaley)
            scale=(scale,scale)

            image = transform.rescale(image, scale, clip=False, anti_aliasing=True, multichannel=multichannel)
            pady = ((size[1] - image.shape[0]) // 2, (size[1] - image.shape[0]) - (size[1] - image.shape[0]) // 2)
            padx = ((size[0] - image.shape[1]) // 2, (size[0] - image.shape[1]) - (size[0] - image.shape[1]) // 2)
            all_pad = (padx, pady)
            if len(image.shape) == 2:
                all_pad = (pady,padx)
            else:
                all_pad = (pady,padx, (0, 0))

            image = np.pad(image, all_pad, 'edge')

            return image

        else:
            return  transform.resize(image, size,anti_aliasing=True,order=order)
    return img_op

def rescale(scale_factor,order=1):
    def img_op(image:np.ndarray):
        multichannel = True
        if len(image.shape) == 2:
            multichannel = False
        image = transform.rescale(image, (scale_factor,scale_factor), clip=False, anti_aliasing=True, multichannel=multichannel,order=order)
        return image
    return img_op



def invert_color():
    def img_op(image:np.ndarray):
        if np.min(image)>=0 and np.max(image)<=1:
            return 1 - image
        elif np.min(image)>=-1 and np.min(image)<0 and np.max(image)<=1:
            return 1-(image*0.5+0.5)
        else:
            return 255-image
    return img_op

def random_invert_color():
    def img_op(image:np.ndarray):
        if random.random()<0.7:
            if np.min(image)>=0 and np.max(image)<=1:
                return 1 - image
            elif np.min(image)>=-1 and np.min(image)<0 and np.max(image)<=1:
                return 1-(image*0.5+0.5)
            else:
                return 255-image
        else:
            return image
    return img_op




def gray_scale():
    def img_op(image:np.ndarray):
        if image.shape[0]==3:
            image=color.rgb2gray(image/255.0).astype(np.float32)
            if image.max()<=1:
                image=image*255.0
        return image
    return img_op

def to_rgb():
    def img_op(image:np.ndarray):
        if len(image.shape)==2:
            image=np.expand_dims(image,-1)
            image=np.concatenate([image,image,image],-1)
            return image

        elif len(image.shape)==3 :
            if image.shape[0]==3 and image.shape[0]==4:
                image = image.transpose([1, 2, 0])
            if  image.shape[-1]==4:
                image = image[:,:,:3]
        return image
    return img_op


def adjust_gamma(gamma=1):
    def img_op(image:np.ndarray):
        return exposure.adjust_gamma(image, gamma)
    return img_op

def random_adjust_gamma(gamma=(0.6,1.4)):
    gammamin,gammamax=gamma
    def img_op(image:np.ndarray):
        gamma=np.random.choice(np.arange(gammamin,gammamax,0.01))
        return exposure.adjust_gamma(image, gamma)
    return img_op


def adjust_contast(alpha=1):
    beta=0
    def img_op(image: np.ndarray):
        image = image.astype(np.float32) * alpha + beta
        image = np.clip(image,0,255).astype(np.uint8)
        return image.astype(np.float32)
    return img_op


def random_adjust_contast(scale=(0.5, 1.5)):
    beta=0
    scalemin,scalemax=scale
    def img_op(image: np.ndarray):
        alpha=random.uniform(scalemin, scalemax)
        image = image.astype(np.float32) * alpha + beta
        image = np.clip(image,0,255).astype(np.uint8)
        return image.astype(np.float32)
    return img_op


def auto_level():
    def img_op(image: np.ndarray):
        counts, bins = np.histogram(image.reshape([-1]), np.arange(0, 255, 32).tolist())
        if 0.6<counts[:1].sum()/counts.sum()<0.99:
            image[image<image.mean()//2]=0
        if 0.7<counts[-3:].sum() / counts.sum() <0.99:
            image[image>(256-(256-image.mean())//2) ] = 255

        image=image-np.clip(np.min(image,keepdims=True),0,255)
        image=np.clip(image*255/(np.max(image,keepdims=True)+1e-5),0,255)
        return image.astype(np.float32)
    return img_op

def random_adjust_hue():
    def img_op(image: np.ndarray):
        # hue is mapped to [0, 1] from [0, 360]
        # if hue_offset not in range(-180, 180):
        #     raise ValueError('Hue should be within (-180, 180)')
        # if saturation not in range(-100, 100):
        #     raise ValueError('Saturation should be within (-100, 100)')
        # if lightness not in range(-100, 100):
        #     raise ValueError('Lightness should be within (-100, 100)')
        hue_offset=random.uniform(-20,20)
        saturation=random.uniform(-50,50)
        lightness = random.uniform(-30, 30)
        image = color.rgb2hsv(image.astype('uint8'))  #.astype('uint8')
        offset = ((180 + hue_offset) % 180) / 360.0
        image[:, :, 0] = image[:, :, 0] + offset
        image[:, :, 1] = image[:, :, 1] + saturation / 200.0
        image[:, :, 2] = image[:, :, 2] + lightness / 200.0
        image = color.hsv2rgb(image) * 255.0
        return image.astype(np.float32)
    return img_op

def random_crop(w, h):
    def img_op(image:np.ndarray):
        result=np.zeros((h,w,image.shape[-1]))
        height, width = image.shape[:2]
        offset_x,offset_y=0,0
        if width>w:
            offset_x = np.random.choice(width-w)
        if height>h:
            offset_y = np.random.choice(height-h)
        crop_im=image[offset_y:offset_y+h,offset_x:offset_x+w,:]
        result[:crop_im.shape[0],:crop_im.shape[1],:]=crop_im
        return result
    return img_op


def random_center_crop(w, h, scale=(0.8, 1.2)):
    scalemin, scalemax = scale
    def img_op(image:np.ndarray):

        height, width = image.shape[:2]
        max_value=max(height, width)
        result = np.zeros((max_value, max_value, image.shape[-1]))
        i = int(round((max_value - height) / 2.))
        j = int(round((max_value - width) / 2.))
        result[i:i+height,j:j+width,:]=image

        scale = min(w/max_value, h/max_value)*np.random.choice(np.arange(scalemin,scalemax,0.01))

        image = transform.rescale(result, scale, clip=False, anti_aliasing=True, multichannel=True)
        result = np.zeros((max(image.shape[0],h), max(image.shape[1],w), image.shape[-1]))
        i = int(round((result.shape[0] - image.shape[0]) / 2.))
        j = int(round((result.shape[1] - image.shape[1]) / 2.))
        result[i:i + image.shape[0], j:j + image.shape[1], :] = image

        i = int(round((result.shape[0] -h) / 2.))
        j = int(round((result.shape[1] -w) / 2.))

        return result[i:i +h, j:j +w, :]
    return img_op



def image_backend_adaptive(image):
    if _session.backend=='tensorflow' and image.ndim in (3,4):
        image = image.astype(np.float32)
    elif _session.backend in ['pytorch','cntk'] and image.ndim ==3:
        image=np.transpose(image,[2,0,1]).astype(np.float32)
    elif _session.backend in ['pytorch','cntk'] and image.ndim ==4:
        image=np.transpose(image,[0,3,1,2]).astype(np.float32)
    elif isinstance(image,np.ndarray):
        return image.astype(np.float32)
    elif isinstance(image, list):
        return np.array(image).astype(np.float32)
    return image


def reverse_image_backend_adaptive(image):
    if _session.backend in ['pytorch','cntk'] and image.ndim ==3 and image.shape[0] in [3,4]:
        image=np.transpose(image,[1,2,0]).astype(np.float32)
    elif  _session.backend in ['pytorch','cntk'] and image.ndim ==4 and image.shape[1] in [3,4]:
        image=np.transpose(image,[0,2,3,1]).astype(np.float32)
    return image


def random_channel_shift(intensity=15):
    channel_axis = -1
    inten=intensity
    def img_op(image: np.ndarray):
        image = np.rollaxis(image, channel_axis, channel_axis)
        min_x, max_x = np.min(image), np.max(image)
        intensity = max_x / 255 * inten
        channel_images = [np.clip(x_channel + np.random.uniform(-intensity, intensity), min_x, max_x) for x_channel in image[:,:,]]
        x = np.stack(channel_images, axis=channel_axis)
        x = np.rollaxis(x, 0, channel_axis + 1)
        return x
    return img_op

def random_cutout(img, mask ):
    h, w = img.shape[:2] if _backend=='tensorflow' or len(img.shape)==2 else img.shape[1:3]
    cutx=random.choice(range(0,w//4))
    cuty = random.choice(range(0, h//4))
    offsetx=random.choice(range(0,w))
    offsety=random.choice(range(0,h))
    block=np.zeros((min(offsety+cuty,h)-offsety,min(offsetx+cutx,w)-offsetx))
    if random.randint(0, 10) % 4 == 1:
        block = np.clip(np.random.standard_normal((min(offsety+cuty,h)-offsety,min(offsetx+cutx,w)-offsetx)) * 127.5 + 127.5, 0,255)
    elif random.randint(0, 10) % 4 == 2:
        block = np.random.uniform(0,255,(min(offsety + cuty, h) - offsety, min(offsetx + cutx, w) - offsetx))
    if _backend == 'tensorflow':
        block=np.expand_dims(block,-1)
        block = np.concatenate([block, block, block], axis=-1)
        img[offsety:min(offsety + cuty, img.shape[0]), offsetx:min(offsetx + cutx, img.shape[1]), :] = block
        mask[offsety:min(offsety + cuty, mask.shape[0]), offsetx:min(offsetx + cutx, mask.shape[1])] = 0
    else:
        block = np.expand_dims(0,block)
        block = np.concatenate([block, block, block], axis=0)
        img[:,offsety:min(offsety + cuty, img.shape[0]), offsetx:min(offsetx + cutx, img.shape[1])] = block
        mask[offsety:min(offsety + cuty, mask.shape[0]), offsetx:min(offsetx + cutx, mask.shape[1])] = 0
    return img,mask

## denoise, smooth,
def clahe(clip_limit=0.1,nbins=16):
    def img_op(image: np.ndarray):

        image=image.astype(np.float32)/255.0
        if image.max()-image.min()>0.2:
            image=exposure.equalize_adapthist(image,clip_limit=clip_limit,nbins=nbins)
        return image*255.0
    return img_op

def erosion_then_dilation(filter_size=3,repeat=1):
    def img_op(image: np.ndarray):
        for i in range(repeat):
            image=morphology.erosion(image,morphology.square(filter_size))
            image = morphology.dilation(image, morphology.square(filter_size))
        return image
    return img_op

def image_erosion(filter_size=3,repeat=1):
    def img_op(image: np.ndarray):
        for i in range(repeat):
            image=morphology.erosion(image,morphology.square(filter_size))
        return image
    return img_op

def image_dilation(filter_size=3,repeat=1):
    def img_op(image: np.ndarray):
        for i in range(repeat):
            image = morphology.dilation(image, morphology.square(filter_size))
        return image
    return img_op

def adaptive_binarization(threshold_type='otsu' ):
    def img_op(image: np.ndarray):
        local_thresh=None
        blur = gaussian(image, sigma=1)
        if threshold_type=='otsu':
            local_thresh = threshold_otsu(blur)
        elif threshold_type=='minimum':
            local_thresh= threshold_minimum(blur)
        elif threshold_type=='local':
            local_thresh=threshold_local(blur, block_size=35, offset=10)
        elif threshold_type=='isodata':
            local_thresh=threshold_isodata(blur, nbins=256)
        image =(image > local_thresh).astype(np.float32)*255.0
        return image
    return img_op

# def image_smoothening():
#     def img_op(image: np.ndarray):
#         ret1, th1 = cv2.threshold(img, BINARY_THREHOLD, 255, cv2.THRESH_BINARY)
#         ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#         blur = cv2.GaussianBlur(th2, (1, 1), 0)
#         ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#         return th3

#
# def do_random_crop_rescale(image, mask, w, h):
#     height, width = image.shape[:2]
#     x,y=0,0
#     if width>w:
#         x = np.random.choice(width-w)
#     if height>h:
#         y = np.random.choice(height-h)
#     image = image[y:y+h,x:x+w]
#     mask  = mask [y:y+h,x:x+w]
#
#     #---
#     if (w,h)!=(width,height):
#         image = cv2.resize( image, dsize=(width,height), interpolation=cv2.INTER_LINEAR)
#         mask = cv2.resize( mask,  dsize=(width,height), interpolation=cv2.INTER_NEAREST)
#
#     return image, mask
#
# def do_random_crop_rotate_rescale(image, mask, w, h):
#     H,W = image.shape[:2]
#
#     #dangle = np.random.uniform(-2.5, 2.5)
#     #dscale = np.random.uniform(-0.10,0.10,2)
#     dangle = np.random.uniform(-8, 8)
#     dshift = np.random.uniform(-0.1,0.1,2)
#
#     dscale_x = np.random.uniform(-0.00075,0.00075)
#     dscale_y = np.random.uniform(-0.25,0.25)
#
#     cos = math.cos(dangle/180*math.pi)
#     sin = math.sin(dangle/180*math.pi)
#     sx,sy = 1 + dscale_x, 1+ dscale_y #1,1 #
#     tx,ty = dshift*min(H,W)
#
#     src = np.array([[-w/2,-h/2],[ w/2,-h/2],[ w/2, h/2],[-w/2, h/2]], np.float32)
#     src = src*[sx,sy]
#     x = (src*[cos,-sin]).sum(1)+W/2
#     y = (src*[sin, cos]).sum(1)+H/2
#     # x = x-x.min()
#     # y = y-y.min()
#     # x = x + (W-x.max())*tx
#     # y = y + (H-y.max())*ty
#     #
#     # if 0:
#     #     overlay=image.copy()
#     #     for i in range(4):
#     #         cv2.line(overlay, int_tuple([x[i],y[i]]), int_tuple([x[(i+1)%4],y[(i+1)%4]]), (0,0,255),5)image_show('overlay',overlay)
#     #
#
#
#     src = np.column_stack([x,y])
#     dst = np.array([[0,0],[w,0],[w,h],[0,h]])
#     s = src.astype(np.float32)
#     d = dst.astype(np.float32)
#     transform = cv2.getPerspectiveTransform(s,d)
#
#     image = cv2.warpPerspective( image, transform, (W, H),
#         flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0))
#
#     mask = cv2.warpPerspective( mask, transform, (W, H),
#         flags=cv2.INTER_NEAREST, borderMode=cv2.BORDER_CONSTANT, borderValue=(0))
#
#     return image, mask
#
# def do_random_log_contast(image, gain=[0.70, 1.30] ):
#     gain = np.random.uniform(gain[0],gain[1],1)
#     inverse = np.random.choice(2,1)
#
#     image = image.astype(np.float32)/255
#     if inverse==0:
#         image = gain*np.log(image+1)
#     else:
#         image = gain*(2**image-1)
#
#     image = np.clip(image*255,0,255).astype(np.uint8)
#     return image
#
#

#
#







