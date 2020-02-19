import cv2
from PIL import Image,ImageDraw,ImageFont
import numpy as np
from matplotlib import pyplot as plt
import os,shutil,glob

default_font=None
default_font_path=None
def set_font_path(path):
    global default_font_path
    default_font_path=path
def set_font(path,size=32):
    global default_font
    default_font=ImageFont.truetype(path,size=size)
def test_font_dir(dir,dst=None,text=None):
    fs=glob.glob(dir+'/*.ttf')+glob.glob(dir+'/*.ttc')+glob.glob(dir+'/*.otf')
    dst=dst or dir+'/test_font'
    for i,f in enumerate(fs):
        test_font(f,dst,text=text)
        print(i,f)
    print('finished.')

def test_font(path,dst='./test_font',text=None):
    img_dir=dst+'/imgs'
    log_file=dst+'/font_errors.txt'
    bad_fonts=dst+'/bad_fonts.txt'
    img=blank_rgb(size=(1024,32))
    font=ImageFont.truetype(path,size=24)
    text=text or 'Hello! 今天过得怎么样,~!#$%^&*()_+=-'
    try:
        img=draw_text(img,text=text,font=font)
    except:
        msg='Error occured when handle %s'%(path)
        print(msg)
        with open(log_file,'a',encoding='utf-8') as f:
            f.write(msg+'\n')
        with open(bad_fonts,'a',encoding='utf-8') as f:
            f.write(path+'\n')
        return
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    img.save(img_dir+'/'+os.path.basename(path)[:-3]+'.jpg')
def blank_rgb(size=(512,48),color='white'):
    img=Image.new('RGB',size,color)
    return img
def calc_pos(img_size,box_size,pos='center'):
    imw,imh=img_size
    w,h=box_size
    l=(imw-w)//2
    t=(imh-h)//2
    return l,t
def mark_img(img,text,font_path=None,font_size=None):
    imw,imh=img.size
    font_path=font_path or default_font_path
    if font_path:
        font_size=font_size or min(32,imw//len(text))
        font=ImageFont.truetype(font_path,size=font_size)
    else:
        font=None
    xy=calc_pos(img.size,(font.size*len(text),font.size))
    img=draw_text(img,text,xy=xy,fill='red',font=font)
    return img




def draw_text(img,text,xy=(0,0),fill='black',font=None):
    font=font or default_font
    draw=ImageDraw.ImageDraw(img)
    draw.text(xy,text=text,fill=fill,font=font)
    return img
def new_blank_img_as(img):
    img=Image.new('RGB',size=img.size,color='white')
    return img
def pilimshow(x,*args,**kwargs):
    x=pilimg(x)
    x.show(*args,**kwargs)
def cv2imshow(x,title='cv2 image'):
    x=cv2img(x)
    cv2.imshow(title,x)
    cv2.waitKey(0)
def pltimshow(x,*args,**kwargs):
    x=cv2img(x)
    plt.imshow(x,*args,**kwargs)
    plt.show()
def resize_to_fixed_height(img,height):
    w,h=img.size
    r=h/height
    nw=int(w/r)
    nh=int(h/r)
    img=img.resize((nw,nh))
    return img
def resize_to_fixed_width(img,width):
    w,h=img.size
    r=w/width
    nw=int(w/r)
    nh=int(h/r)
    img=img.resize((nw,nh))
    return img
def resize_by_scale(img,scale):
    w, h = img.size
    r = scale
    nw = int(w * r)
    nh = int(h * r)
    img = img.resize((nw, nh))
    return img
def limit_size(img,limits):
    w,h=img.size
    mw,mh=limits
    rw=w/mw
    rh=h/mh
    r=max(rw,rh)
    if r<=1:
        return img
    nw=int(w/r)
    nh=int(h/r)
    img=img.resize((nw,nh))
    return img
def draw_boxes(img,boxes,copy=False,*args,**kwargs):
    if copy:
        img=img.copy()
    for box in boxes:img=draw_box(img,box,copy=False,*args,**kwargs)
    return img
def draw_box(img,box,copy=True,width=5,outline='red',fill=None):
    box=tuple(box)
    if copy:
        img=img.copy()
    draw=ImageDraw.Draw(img)
    draw.rectangle((box[:2],box[2:]),width=width,outline=outline,fill=fill)
    return img
def draw_textboxes(img,textboxes,copy=False,font_size=32):
    if copy:
        img=img.copy()
    for textbox in textboxes:
        img=draw_textbox(img,textbox,copy=False,font_size=font_size)
    return img

def draw_textbox(img,textbox,copy=True,font_size=None):
    import os
    font_size=font_size or 32
    box,text=textbox
    if copy:
        img=img.copy()
    draw = ImageDraw.Draw(img)
    font=ImageFont.truetype(os.path.dirname(__file__)+'/msyh.ttf',size=font_size)
    draw.text(box[:2],text=text,fill='black',font=font)
    return img
def crop_boxes(img,boxes):
    imgs=[]
    for box in boxes:
        im=crop(img,box)
        imgs.append(im)
    return imgs
def iter_boxes(img,boxes,do):
    reses=[]
    for box in boxes:
        im=crop(img,box)
        res=do(im)
        reses.append(res)
    return reses
def cv2img(img):
    if isinstance(img,Image.Image):
        # print(img)
        # print(type(img))
        # img=np.array(img).astype(np.float)
        img=np.array(img)
        if len(img.shape)==3:img=img[:,:,::-1]
        return img
    # return np.array(img).astype(np.float)
    return img
npimg=cv2img
def pilimg(img):
    if isinstance(img,Image.Image):return img
    if isinstance(img,np.ndarray):
        if len(img.shape)==3:img=img[:,:,::-1]
    return Image.fromarray(np.array(img).astype(np.uint8))
def crop(img,bbox):
    return img.crop(bbox)
def crop_by_ratio(img,rbox):
    w,h=img.size
    box=tuple([int(x) for x in (rbox[0]*w,rbox[1]*h,rbox[2]*w,rbox[3]*h)])
    return img.crop(box)