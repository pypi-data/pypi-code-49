#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 NetEase.com, Inc. All Rights Reserved.
# Copyright 2019, The NSH Recommendation Project, The User Persona Group, The Fuxi AI Lab.
"""
性能分析

Authors: shangyue(shangyue@corp.netease.com)
Phone:13214168056
Date: 2019/12/18

"""

import cProfile
import pstats
import os
from PIL import Image
import matplotlib.pyplot as plt


# 性能分析装饰器定义
def do_cprofile(filename):
    """
    Decorator for function profiling.
    """
    def wrapper(func):
        def profiled_func(*args, **kwargs):
            # Flag for do profiling or not.
            DO_PROF = True
            if DO_PROF:
                profile = cProfile.Profile()
                profile.enable()
                result = func(*args, **kwargs)
                profile.disable()
                # Sort stat by internal time.
                sortby = "tottime"
                ps = pstats.Stats(profile).sort_stats(sortby)
                ps.dump_stats(filename)
                picname = filename.replace('prof', 'png')
                os.system("gprof2dot -f pstats -c pink {} | dot -Tpng -o {}".format(filename, picname))
                img = Image.open(picname)
                plt.imshow(img)
                plt.show()
            else:
                result = func(*args, **kwargs)
            return result
        return profiled_func
    return wrapper

# 性能分析结果
def ana_cprofile(filepath):
    p = pstats.Stats(filepath)
    p.strip_dirs().sort_stats('cumtime').print_stats(10, 1.0, '.*')

if __name__ == '__main__':
    filepath = './mkm_rum.prof'
    ana_cprofile(filepath)


