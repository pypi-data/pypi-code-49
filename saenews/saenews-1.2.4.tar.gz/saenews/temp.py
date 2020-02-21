def add_border(input_image, output_image, border, border_color='black'):
    img = Image.open(input_image) 
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill=border_color)
    else:
        raise RuntimeError('Border is not an integer or tuple!')
    bimg.save(output_image)
    print (output_image)

def put_quote(border_dim=0.2,border_dims=(0,0,0,0), *args, **kwargs):
    bottom_factor = border_dim
    in_img = input_file_orig
    img = Image.open(in_img)
    W,H = img.size
    a = border_dims
    border_len = (round(a[0]*W),round(a[1]*H),round(a[2]*W),round(a[3]*H))
    add_border(in_img,
               output_image='bordered.jpg',
               border=border_len)
    quote(input_file='bordered.jpg', *args,**kwargs)
    
    
    

from PIL import Image, ImageFont, ImageDraw
import cv2
import datetime
from saenews.sae3 import *
import os
from saenews.utils import quote, put_quote


title = "Arise, Awake, stop not till the goal is reached."
tag_line = "(Kathopanishad)"
input_file_orig = "SV.jpg"
in_img = input_file_orig

put_quote(input_file_orig=input_file_orig,
border_dim=0.2,border_dims= (0, 0, 0,0.15), title=title,tag_line='', cord = (0.1,0.886), border_color='red', text_font = '', cap_text_font = '', cap_width=0.055, cap_cord=(0.7,0.866),focus='false')

