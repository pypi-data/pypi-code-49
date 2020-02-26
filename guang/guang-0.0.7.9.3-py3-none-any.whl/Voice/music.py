from IPython.display import Audio, display
import soundfile as sf
from librosa.display import waveplot, specshow
import numpy as np
import matplotlib.pyplot as plt

def listen(*voice, dtype='float64', samplerate=None):
    """
    voice can be numpy array + fs
    or file path
    use soundfile packege ,it provide audio data from a sound file as NumPy array."""
    if type(voice[0]) == str:
        x, fs = sf.read(voice[0], dtype=dtype, samplerate=samplerate)
    elif type(voice[0])== np.ndarray:
        if len(voice) < 2:
            raise ValueError('Invalid inputs, pls input both np.array and fs ')
        x, fs = voice[0], voice[1]
    else:
        raise ValueError('invalid input, voice can be np.array+fs or file path')

    return display(Audio(x, rate=fs))


def voiceshow(*voice, samplerate=None, dtype='float64', figsize=(10, 4)):
    """
    voice can be numpy array + fs
    or file path
    give the voice wave plot.
    """
    if type(voice[0]) == str:
        x, fs = sf.read(voice[0], dtype=dtype, samplerate=samplerate)
    elif type(voice[0])== np.ndarray:
        if len(voice) < 2:
            raise ValueError('Invalid inputs, pls input both np.array and fs ')
        x, fs = voice[0], voice[1]
    else:
        raise ValueError('invalid inputs, voice can be np.array+fs or file path')
    plt.figure(figsize=figsize)
    waveplot(x, fs)
    plt.show()

def duration(y=None,
            sr=22050,
            S=None,
            n_fft=2048,
            hop_length=512,
            center=True,
            filename=None,):
    """Compute the duration (in seconds) of an audio time series, feature matrix, or filename.
    return librosa.get_duration
    """
    return librosa.get_duration(y=y,
                                sr=sr,
                                S=S,
                                n_fft=n_fft,
                                hop_length=hop_length,
                                center=center,
                                filename=filename,)


from guang.Utils.toolsFunc import probar
