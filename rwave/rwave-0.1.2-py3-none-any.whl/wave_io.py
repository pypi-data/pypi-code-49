# -*- coding: utf-8 -*-
import numpy as np
import scipy.io.wavfile
import os


def read_wave(wavfile, is_nomalize=False):
    ## -----*----- .wavファイルの読み込み -----*----- ##
    fs, wav = scipy.io.wavfile.read(wavfile)
    if is_nomalize:
        wav = nomalize(wav)

    return (wav, fs)


def write_wave(wavfile, wav, fs):
    ## -----*----- .wavファイルに書き込み -----*----- ##
    if not os.path.dirname(wavfile) == '':
        os.makedirs(os.path.dirname(wavfile), exist_ok=True)
    if os.path.exists(wavfile):
        os.remove(wavfile)
    scipy.io.wavfile.write(wavfile, fs, wav)


def nomalize(x, axis=None):
    ## -----*----- 0~1に正規化 -----*----- ##
    min = x.min(axis=axis, keepdims=True)
    max = x.max(axis=axis, keepdims=True)
    if not (max - min) == 0:
        result = (x - min) / (max - min)
    else:
        result = x

    return result
