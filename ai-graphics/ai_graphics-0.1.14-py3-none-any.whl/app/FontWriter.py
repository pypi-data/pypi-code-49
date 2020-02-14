"""
Name : FontWriter.py
Author  : Cash
Contact : tkggpdc2007@163.com
Time    : 2020-01-08 10:52
Desc:
"""

import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

__all__ = ['write_text']


def write_line(image, text, position, font_size, font_color, font_path):
    """
    写入一行文本
    :param image: PIL image
    :param text:
    :param position:
    :param font_size:
    :param font_color:
    :param font_path:
    :return:
    """
    if not os.path.exists(font_path):
        return image

    my_font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(image)
    # 文本长度
    tend = len(text)
    x_pos, y_pos = position
    frame_size = image.size
    while True:
        # 文本的尺寸
        text_size = draw.textsize(text[:tend], font=my_font)
        if text_size[0] < frame_size[0] - x_pos or text_size[0] == 0:
            break
        else:
            # 文本太长，调整文本长度
            tend -= 1

    txt = text[:tend]
    draw.text(position, txt, font=my_font, fill=font_color)

    return image, tend


def write_text(image, text, position, font_size, font_color, font_path):
    """
    写入多行文本
    :param image: numpy data
    :param text: the text that want to write
    :param position: the position that want to write
    :param font_size: the font size
    :param font_color: the font color
    :param font_path: the font path
    :return:
    """
    text_list = text.split("\n")
    t_begin, line = 0, 0
    img = Image.fromarray(image)
    for txt in text_list:
        while True:
            x_pos = position[0]
            y_pos = position[1] + line * font_size
            img, t_end = write_line(img, txt, (x_pos, y_pos), font_size, font_color, font_path)
            if t_end == 0:
                break
            else:
                txt = txt[t_end:]
                t_begin = t_begin + t_end
                line += 1
    return np.array(img)

