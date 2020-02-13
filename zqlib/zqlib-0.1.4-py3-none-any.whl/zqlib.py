#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 qiang.zhou <qiang.zhou@Macbook>
#
# Distributed under terms of the MIT license.

"""
Common used functions.
"""

# 2020-01-09: imgs have been read as a TxHxW array
def imgs2vid(imgs, output_fn="test.avi", fps=5):
    import cv2
    import numpy as np
    _, height, width = imgs.shape
    video_handler = cv2.VideoWriter(output_fn, cv2.VideoWriter_fourcc(*"MJPG"), fps, (width, height), isColor=False)
    for img in imgs:
        img = np.uint8(img)
        video_handler.write(img)
    cv2.destroyAllWindows()
    video_handler.release()



