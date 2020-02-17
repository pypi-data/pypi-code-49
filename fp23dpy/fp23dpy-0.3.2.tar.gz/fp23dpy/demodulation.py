"""
Module for phase demodulation of an FP-LIF image (fringe pattern image)

The main method is demodulate which takes an image and an optional calibration as input and extract the phase from it
"""
# import matplotlib.pyplot as plt
import numpy as np
from skimage import restoration

from . import helpers as h
from . import wavelets as wl

def _possibly_masked(inArray, outArray):
    """Mask output array if inArray array is masked"""
    if np.ma.isMaskedArray(inArray):
        return np.ma.array(outArray, mask=inArray.mask, fill_value=inArray.fill_value)
    else:
        return outArray

def wavelet(s, T):
    """1D phase demodulation using wavelet"""
    c = wl.cwt(s, T)
    ridge = np.argmax(np.abs(c), axis=0)
    wrapped_phase = _possibly_masked(s, np.angle(c[ridge, np.arange(s.size)]))
    unwrapped_phase = restoration.unwrap_phase(wrapped_phase)
    return unwrapped_phase

def wave2_demodulation(s, T, gamma, wavelet):
    """Helper function for phase demodulation of image using wavelets"""
    # assert isinstance(gamma, float), "Wavelet demodulation only support gamma as float"
    shape = s.shape
    y, x = np.mgrid[:shape[0], :shape[1]]
    c = wl.cwt2(s, T, gamma, wavelet)
    if len(c.shape) == 4:
        c = c.reshape((gamma.size * T.size,) + shape)
    ridge = np.argmax(np.abs(c), axis=0)
    wrapped_phase = _possibly_masked(s, np.angle(c[ridge, y, x]))
    unwrapped_phase = restoration.unwrap_phase(wrapped_phase)

    # plt.figure()
    # plt.subplot(121)
    # plt.imshow(s, cmap='gray'), plt.title("signal")
    # plt.subplot(122)
    # plt.imshow(T[ridge], cmap='gray'), plt.title("ridge Ts")

    # plt.figure()
    # plt.subplot(121)
    # plt.imshow(wrapped_phase), plt.title("wrapped phase")
    # plt.subplot(122)
    # plt.imshow(unwrapped_phase), plt.title("unwrapped phase")
    # plt.show()
    # exit()

    return unwrapped_phase

def wavelet2(s, T, gamma):
    """Helper function for phase demodulation of image using the morlet wavelet"""
    return wave2_demodulation(s, T, gamma, 'morl')

def isowavelet2(s, T, gamma=np.pi/2):
    """Helper function for phase demodulation of image using the semi mexican hat"""
    return wave2_demodulation(s, T, gamma, 'mexh')

def ft2(s, T, gamma): 
    """Helper function for phase demodulatoin of image using the Fourier Transform method, see 
    M. Takeda and K. Mutoh, “Fourier transform profilometry for the automatic measurement of 3-d object shapes,” Appl. Opt. 22, 3977–3982 (1983).
    """
    shape = s.shape
    T = h.get_T_from_square(T, shape)
    sigma = 0.32 / T * 1.96 * np.mean(shape)
    lf_sync_freq = h.ft2_helper(s, T, gamma, sigma)
    wrapped_phase = _possibly_masked(s, np.angle(lf_sync_freq))
    unwrapped_phase = restoration.unwrap_phase(wrapped_phase)

    return unwrapped_phase

def demodulate(signal, calibration):
    """Function for demodulation using the Continuous Wavelet Transform method"""
    if len(signal.shape) == 2:
        Tstep = 1
        if 'Tlim' in calibration:
            Tlim = calibration['Tlim']
            if 3 < (Tlim[1] - Tlim[0]) / Tstep < 10:
                Trange = np.arange(Tlim[0], Tlim[1], Tstep)
        else:
            T0 = calibration['T']
            ### Use linear range in frequency instead
            Trange = T0 + np.arange(-5 * Tstep, 5 * Tstep, Tstep)
            Trange = Trange[Trange >= 2]
        
        # threeD = isowavelet2(signal, Trange, calibration['gamma'])
        phase = wavelet2(signal, Trange, calibration['gamma'])
    else:
        raise ValueError('Signal must be a single channel')
    return phase
