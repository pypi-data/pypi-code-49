import cv2
from PIL import Image
import numpy as np
import os,shutil,glob
import collections
from .utils import crop_by_ratio,pilimg,cv2img
from wpkit.fsutil import remove_fsitem
def main():
    img=cv2.imread('images/3.jpg')
    color=get_color(img)
    print(color)
    pass

def make_color_classify_dataset(data_dir,out_dir,func=None,partial_area=None):
    func=func or get_color
    fs=glob.glob(data_dir+'/*.jpg')
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)
    for i,f in enumerate(fs):
        img=cv2.imread(f)
        if partial_area:
            pim=pilimg(img)
            pim=crop_by_ratio(pim,partial_area)
            img=cv2img(pim)
        color=func(img)
        cls_dir=out_dir+'/'+color
        if not os.path.exists(cls_dir):
            os.makedirs(cls_dir)
        f2=cls_dir+'/'+os.path.basename(f)
        shutil.copy(f,f2)
        print(i,f,color)





def recognize_dominant_color(img,generate_info_img=False):

    color=get_color(img,generate_info=generate_info_img)
    return color
def _finetune_result(sums):
    sums = [(c, num) for c, num in sums.items()]
    sums.sort(key=lambda x: x[1], reverse=True)
    first,second=sums[:2]
    if first[0]=='black':
        if first[1]>=second[1]*3:
            return first[0]
        else:
            return second[0]
    else:
        return first[0]

def get_color(frame,generate_info=False,return_sums=False):
    if isinstance(frame,str):
        assert os.path.isfile(frame)
        frame=cv2.imread(frame)
    from .utils import pilimg,cv2img
    frame=cv2img(frame)
    # print('go in get_color')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maxsum = -100
    color = None
    color_dict = getColorList()
    sums={}
    for d in color_dict:
        mask = cv2.inRange(hsv, color_dict[d][0], color_dict[d][1])
        if generate_info:
            if not os.path.exists(generate_info):os.makedirs(generate_info)
            cv2.imwrite(generate_info+'/'+d + '.jpg', mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        binary = cv2.dilate(binary, None, iterations=2)
        cnts, hiera = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        sum = 0
        for c in cnts:
            sum += cv2.contourArea(c)
        sums[d]=sum
        if sum > maxsum:
            maxsum = sum
            color = d
    color=_finetune_result(sums)
    if return_sums:
        return color,sums
    return color

class Colors:
    black = '黑色'
    white = '白色'
    red = '红色'
    red2 =red
    orange='橘红色'
    yellow='黄色'
    blue='蓝色'
    cyan='青蓝色'
    green='绿色'
    purple='紫色'
color_eng2zh={
    'black':Colors.black,
    'white':Colors.white,
    'red':Colors.red,
    'red2':Colors.red2,
    'orange':Colors.orange,
    'yellow':Colors.yellow,
    'blue':Colors.blue,
    'cyan':Colors.cyan,
    'green':Colors.green,
    'purple':Colors.purple
}
def getColorList():
    dict = collections.defaultdict(list)

    # 黑色
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 46])
    color_list = []
    color_list.append(lower_black)
    color_list.append(upper_black)
    dict['black'] = color_list

    # #灰色
    # lower_gray = np.array([0, 0, 46])
    # upper_gray = np.array([180, 43, 220])
    # color_list = []
    # color_list.append(lower_gray)
    # color_list.append(upper_gray)
    # dict['gray']=color_list

    # 白色
    lower_white = np.array([0, 0, 221])
    upper_white = np.array([180, 30, 255])
    color_list = []
    color_list.append(lower_white)
    color_list.append(upper_white)
    dict['white'] = color_list

    # 红色
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red'] = color_list

    # 红色2
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red2'] = color_list

    # 橙色
    lower_orange = np.array([11, 43, 46])
    upper_orange = np.array([25, 255, 255])
    color_list = []
    color_list.append(lower_orange)
    color_list.append(upper_orange)
    dict['orange'] = color_list

    # 黄色
    lower_yellow = np.array([26, 43, 46])
    upper_yellow = np.array([34, 255, 255])
    color_list = []
    color_list.append(lower_yellow)
    color_list.append(upper_yellow)
    dict['yellow'] = color_list

    # 绿色
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    color_list = []
    color_list.append(lower_green)
    color_list.append(upper_green)
    dict['green'] = color_list

    # 青色
    lower_cyan = np.array([78, 43, 46])
    upper_cyan = np.array([99, 255, 255])
    color_list = []
    color_list.append(lower_cyan)
    color_list.append(upper_cyan)
    dict['cyan'] = color_list

    # 蓝色
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])
    color_list = []
    color_list.append(lower_blue)
    color_list.append(upper_blue)
    dict['blue'] = color_list

    # 紫色
    lower_purple = np.array([125, 43, 46])
    upper_purple = np.array([155, 255, 255])
    color_list = []
    color_list.append(lower_purple)
    color_list.append(upper_purple)
    dict['purple'] = color_list

    return dict
def test_get_color():
    color_dict = getColorList()
    print(color_dict)

    num = len(color_dict)
    print('num=', num)

    for d in color_dict:
        print('key=', d)
        print('value=', color_dict[d][1])
if __name__ == '__main__':
    main()