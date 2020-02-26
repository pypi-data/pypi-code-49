from multiprocessing import Pool, TimeoutError
import os
import librosa
from glob import glob
import soundfile as sf
import numpy as np
import warnings

def is_lt_duration(file, least_time):
    try:
        if librosa.get_duration(filename = file) < least_time:
            return 1
        else:
            return 0
    except:
        print(f'file {i} open failed, and has been ignored')
#         return None

def reduce_from_duration(filelist, least_time=1):
    '''
    return reduced list
    '''
    with Pool(processes=None) as pool:
        multi_res=[pool.apply_async(is_lt_duration, (i,least_time)) for i in filelist]
        reduce_list = [res.get() for res in multi_res]
        
    return [filelist[idx] for idx,i in enumerate(reduce_list) if i==0]

def find_no_silence(filename):
    """read the sound file, return you the voice start end voice end.
    
    Return:
        start(/s), end(/s), arg_start, arg_end
    """
    warnings.filterwarnings('ignore')
    voice, sr = sf.read(filename)
#     diff = np.diff(voice, n=2)
#     print(diff)
#     plt.plot(diff)
#     print(np.argwhere(diff>1e-4))
    argvoice = np.argwhere(np.log(voice, )>-6)
    a= argvoice/sr
    win = int(16 * sr/20000)
    for i in range(len(a)):
        if abs(np.mean(a[i:i+win])-a[i]) < 1e-3:
            start = a[i]
            arg_start = argvoice[i]
            break

    for i in range(-1, -len(a), -1):
        if abs(np.mean(a[i-win:i])-a[i]) < 1e-3:
            end = a[i-win]
            arg_end = argvoice[i-win]
            break
    
    return start[0], end[0], arg_start[0], arg_end[0]

import time
if __name__ == "__main__":
    pass
#     t1=time.time()
#     flist = glob(r"data/*")
#     l = reduce_from_duration(flist, least_time=3)
#     print(l)
#     print(time.time()- t1)
