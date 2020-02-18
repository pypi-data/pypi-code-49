import cv2,os,glob,shutil
from PIL import Image,ImageFont,ImageDraw,ImageFilter

default_font=None

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
def draw_text(img,text,xy=(0,0),fill='black',font=None):
    font=font or default_font
    draw=ImageDraw.ImageDraw(img)
    draw.text(xy,text=text,fill=fill,font=font)
    return img

