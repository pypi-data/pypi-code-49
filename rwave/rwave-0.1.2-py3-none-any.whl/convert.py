# -*- coding: utf-8 -*-
import numpy as np
import scipy.signal
import librosa


def convert_fs(wav, fs, to_fs, to_int=True):
    ## -----*----- サンプリングレートを変換 -----*----- ##
    # wav : 変換対象の音源
    # fs  : 変換後のサンプリングレート

    converted = scipy.signal.resample(wav, int(wav.shape[0]*to_fs/fs))

    if to_int:
        converted = np.array(converted, dtype='int16')

    return (converted, to_fs)


def convert_sec(wav, fs, to_sec, to_int=True):
    ## -----*----- 秒数を変換 -----*----- ##
    # wav : 変換対象の音源
    # sec : 変換後の秒数

    converted = scipy.signal.resample(wav, int(fs*to_sec))

    if to_int:
        converted = np.array(converted, dtype='int16')

    return (converted, fs)


def to_mfcc(file, fs, n_mfcc=12):
    ## -----*----- 音声データをMFCCに変換 -----*----- ##
    x, _ = librosa.load(file, sr=fs)
    mfcc = librosa.feature.mfcc(x, sr=fs, n_mfcc=n_mfcc)

    return np.array(mfcc, dtype=np.float32)
