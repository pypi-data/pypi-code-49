"""
Name : Format.py
Author  : Cash
Contact : tkggpdc2007@163.com
Time    : 2020-01-08 10:52
Desc:
"""

from PIL import Image
import os


def convert_png2jpg(infile):
    """
    图像格式转换: png转jpg
    :param infile:
    :return:
    """
    outfile = os.path.splitext(infile)[0] + ".jpg"
    image = Image.open(infile)
    try:
        if len(image.split()) == 4:
            r, g, b, a = image.split()
            image = Image.merge("RGB", (r, g, b))
            image.convert('RGB').save(outfile, quality=70)
            os.remove(infile)
        else:
            image.convert('RGB').save(outfile, quality=70)
            os.remove(infile)
        return outfile
    except ValueError:
        pass


def convert_jpg2png(infile):
    """
    图像格式转换: jpg转png
    :param infile:
    :return:
    """
    pass
