# -*- coding: utf-8 -*-
"""
DCT feature extraction for audio wave
Created by Lai Yongquan (ranchlai@163.com)


"""

import numpy as np
import scipy
import scipy.signal
import scipy.fftpack
import matplotlib.pyplot as plt


def pad_both_sides(s,n):
    if len(s)>=n:
        return s
    if n - len(s) == 1:
        return np.concatenate([s,np.zeros((1,),s.dtype)])
    k = (n - len(s))//2
    return np.concatenate([np.zeros((k,),s.dtype),s,np.zeros((n-len(s)-k,),s.dtype)])


def dct_spectrogram(y,n_dct = 400,hop_length=200,window='hamming',
                    win_length=None,dct_type=2,
                    padding_mode='zeros'):
    
    '''compute dct spectogram of an input signal y, which is a one dimentional vector, typically a sound wave

    Parameters
    ----------
    y : np.ndarray [shape=(n,)]
    audio time series

    n_dct : int > 0 [scalar]
    DCT window size

    hop_length : int > 0 [scalar]
    hop length for short time DCT transform

    win_length : int <= n_dct [scalar]
    Each frame of audio is windowed by `window()`.
    The window will be of length `win_length` and then padded
    with zeros to match `n_dct`.

    If unspecified, defaults to ``win_length = n_dct``.

    window : string,  or np.ndarray [shape=(n_dct,)]
    - a window specification (string, tuple, or number);
      see `scipy.signal.get_window`        
    - a vector or array of length `n_dct`
    
    dct_type: int,  {0,1, 2, 3, 4} value passed to scipy.fftpack.dct, default is 2,if 0, no dct is used
    
    padding_mode : 'zeros', the parameter is not used and signal is always 
    padded with zeros to match align with n_dct

    '''
    if window is None:
        w = 1.0
    else:
        if isinstance(window,str):    
            if win_length is None or win_length > n_dct or win_length<=0:
                win_length = n_dct

            w = scipy.signal.get_window(window,win_length)    
            if win_length < n_dct:
                w = pad_both_sides(w,n_dct)
        elif isinstance(window,np.ndarray):
            if len(window) != n_dct:
                raise Exception('window array must be of the same length as n_dct')
            w = window
        else:
            raise Exception("window type shoud be a string or an numpy array")
   # w[:] = 1.0
    if dct_type==0:
        dct = lambda x : x
    else:
        dct = lambda x : scipy.fftpack.dct(x,norm='ortho',type=dct_type)
        
   
    
    if not isinstance(y,np.ndarray) or y.ndim!=1:
        raise Exception('the input signal must be 1-d array')
    
    n = len(y)    
    rem = n % n_dct
    if  rem !=0:
        y = np.concatenate([y,np.zeros(rem,)],0)
        
        
    ys = []
    for i in range(0,n-n_dct,hop_length):        
        s = y[i:i+n_dct]
        s = w*s
        ys.append(np.expand_dims(dct(s),1))
    Y = np.concatenate(ys,1)
    return Y


def idct_spectrogram(Y,hop_length=200,window='hamming',
                     win_length=None,dct_type=2,fusion='average'):
    
    '''compute inverse transform of  dct spectogram given an input dct spectrogram Y, which is a 
    two dimentional matrix.  See dct_spectrogram for forward transform

    Parameters
    ----------
    Y : np.ndarray [shape=(n_dct,n)]
    audio time series

    

    hop_length : int > 0 [scalar]
    hop length for inverse short time DCT transform, shoud be the same as that in dct_spectrogram()

    win_length : int <= n_dct [scalar]
    Each frame of audio is windowed by `window()`.
    The window will be of length `win_length` and then padded
    with zeros to match `n_dct`.
    If unspecified, defaults to ``win_length = n_dct``.
    This parameter should be the same as that in dct_spectrogram()

    window : None,string,  or np.ndarray [shape=(n_dct,)]
    - a window specification (string, tuple, or number);
      see `scipy.signal.get_window`        
    - a vector or array of length `n_dct`
    if window is None, no windowing is used
    This parameter should be the same as that in dct_spectrogram()
    
    
    dct_type: int,  {0,1, 2, 3, 4} value passed to scipy.fftpack.dct, default is 2
    This parameter should be the same as that in dct_spectrogram()
    
    
    fusion : 'average','overwrite', default is 'average'
    if 'avearge', the overlapped region of recovered signal is avearged
    if 'overwrite', the value of overlapped region is overwritten by latest value when scanning through the dct matrix

    '''    
         
    if not isinstance(Y,np.ndarray) or Y.ndim!=2:
        raise Exception('The input signal must be 2-d array')
        
    n_dct = Y.shape[0]
                    
    if window is None:
        w = 1.0
    else:
        if isinstance(window,str):    
            if win_length is None or win_length > n_dct or win_length<=0:
                win_length = n_dct
            if win_length < n_dct:
                raise Exception("win_length {} if smaller than n_dct {} for valid inverse dct spectrogram".format(win_length,n_dct))
            w = scipy.signal.get_window(window,win_length)

        elif isinstance(window,np.ndarray):
            if len(window) != n_dct:
                raise Exception('window array must be of the same length as n_dct')
            w = window
        else:
            raise Exception("window type shoud be a string or an numpy array")
    
    #w[:]=1.0
    if dct_type==0:
        idct = lambda x : x
    else:
        idct = lambda x : scipy.fftpack.idct(x,norm='ortho',type=dct_type)                           
            
    eps = 1e-8   
    y = np.zeros(hop_length*Y.shape[1]+n_dct-hop_length,dtype='float32')
    #set_trace()pip install libdct==0.0.2
    if fusion == 'average':
        counter = np.zeros_like(y)
        for i in range(Y.shape[1]):
            c = n_dct//2 + i*hop_length
            y0 = idct(Y[:,i])/w
            y[c-n_dct//2:c+n_dct//2] += y0
            counter[c-n_dct//2:c+n_dct//2] += np.ones_like(y0)
        y = y/counter  
    elif fusion == 'overwrite':
        for i in range(Y.shape[1]):
            c = n_dct//2 + i*hop_length
            y0 = idct(Y[:,i])/(w+eps)
            y[c-n_dct//2:c+n_dct//2] = y0
    else:
        raise Exception('invalid value "{}" provided of parameter fusion'.format(fusion) )
       
    return y

def show_dct(D):
    plt.imshow(np.power(D**2,0.1))
    plt.show()
