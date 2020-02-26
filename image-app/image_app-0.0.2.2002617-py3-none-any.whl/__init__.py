name = "image_app"
version_info = (0, 0, 2, 2002617)
__version__ = ".".join([str(v) for v in version_info])
__description__ = '图片处理'

__all__ = ["load_smooth_area", 'cv2pil', 'pil2cv']

from PIL import Image
import cv2
import numpy as np


def load_smooth_area(arr_img):
    from .SmoothAreaProvider import SmoothAreaProvider
    return SmoothAreaProvider().get_image_rects(arr_img)


def cv2pil(arr_img):
    img = Image.fromarray(cv2.cvtColor(arr_img, cv2.COLOR_BGR2RGB))
    # img.show()
    return img


def pil2cv(img):
    assert isinstance(img, Image.Image)
    arr_img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    # cv2.imshow("OpenCV", arr_img)
    # cv2.waitKey()
    return arr_img
