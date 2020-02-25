import os
from pydub import AudioSegment
from multiprocessing import Pool

def cvt2wav(orig_path, new_path, sr=16000):
    basename = os.path.basename(orig_path)
    sufname = basename.split('.')[-1]

    x = AudioSegment.from_file(orig_path, format=sufname)
    x = x.set_channels(1)
    x = x.set_frame_rate(sr)
    x = x.set_sample_width(2)
    x.export(new_path, format='wav')

# def multi_cvt2wav(PATH_orig, PATH_new, sr=16000, n_cpu=None):
#     with Pool(processes=n_cpu) as pool:
#         for i,j in zip(PATH_orig, PATH_new):
#             pool.apply_async(cvt2wav, (i, j, sr))
#         pool.join()

    
def multi_cvt2wav(PATH_orig, PATH_new, sr=16000, n_cpu=16):
    pool =Pool(processes=n_cpu)
    for i,j in zip(PATH_orig, PATH_new):
        pool.apply_async(cvt2wav, (i, j, sr))
    pool.close()
    pool.join()

if __name__ == "__main__":
    pass
