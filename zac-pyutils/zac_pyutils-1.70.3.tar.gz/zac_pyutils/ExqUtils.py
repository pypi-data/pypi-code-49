import logging
import datetime
import itertools
import time
import sys
from collections import deque
import matplotlib.pyplot as plt


INFO = logging.INFO
WARN = logging.WARN
ERROR = logging.ERROR
DEBUG = logging.DEBUG


def parse_argv(argv):
    res_dict = {}
    for idx, item in enumerate(argv):
        if idx == 0:
            continue  # .py文件名
        # print(idx, item)
        if item.startswith("--"):
            res_dict.update({item.split("--")[1]: argv[idx+1]})
            # print("update..")
        # print(res_dict)
    return res_dict


def load_file_as_iter(path):
    with open(path, "r+") as f:
        for i in f:
            yield i


def padding(tokens_inp, pad_len=-1, pad="__PAD__"):
    return (tokens_inp + [pad] * pad_len)[:pad_len]


def padding_autoMax(tokens_list_inp, pad="__PAD__"):
    pad_len = max([len(i) for i in tokens_list_inp])
    return [(tokens + [pad] * pad_len)[:pad_len] for tokens in tokens_list_inp]


def zprint(*args):
    inp_str = " ".join([str(i) for i in args])
    new_m = "|{}| {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), inp_str)
    print(new_m)


def get_logger(log_file):
    logger = logging.Logger("logger to {}".format(log_file))
    hdlr = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(levelname)s %(lineno)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    return logger


def log2file(message, logger, level=logging.INFO, verbose=False):
    new_m = "|{}| {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message)
    logger.log(level, new_m)
    if verbose: print(new_m)


def map_on_iter(iter_item, function, chunk_size=100):
    dq = deque()
    while True:
        target = list(itertools.islice(iter_item, chunk_size))
        if len(target) > 0:
            dq.append(function(target))
        else:
            break
    return flat(list(dq))


def flat(inp_list):
    return [item for sublist in inp_list for item in sublist]


def timeit(func):
    def wraps(*args, **kwargs):
        t0 = time.time()
        res = func(*args, **kwargs)
        delta = str(round(time.time() - t0, 5) * 1000) + "ms"
        return res, delta

    return wraps


def groupby(it, key=lambda x:x):
    return itertools.groupby(sorted(it, key=key), key=key)


def pltshow(imgArr_list,info_list=None,figsize=(10,10),info_fontsize=8):
    row = int(len(imgArr_list)**0.5)
    col = len(imgArr_list)/row
    col = int(col) if int(col)==col else int(col)+1
    fig, axes = plt.subplots(row,col, figsize=figsize)
    for idx,img in enumerate(imgArr_list):
        ax=axes.flatten()[idx]
        ax.imshow(img)
        _ = ax.set_axis_off()
        info="" if info_list is None else info_list[idx]
        _ = ax.set_title(info,size=info_fontsize)