""" Hot-wire Data Reduction

    v0 :    c. sooriyakumaran 2019

This module contains functions which are useful for reducing hotwire data. It is currently set up to read time
series data in .wav format.

This module contains the following functions:

    * load_time_signal - returns the time-series voltage v. time signal as well as the sampling freq. in Hz
    * get_hw_calibration_func - returns a voltage to velocity calibration function and optionally the cal. coefficients
    * fft - returns the power spectral density of the signal in the frequency domain
    * turbulence_intensity - returns the integrated turbulence intensity from the spectrum data over a defined range
    * next_pow_2 - returns  p for 2**p >= x
    * process_hw_data_file - returns mean velocity and voltage, as well as 1sigma(u/U) and a filtered Tu

"""
# standard lirbrary
import logging
import os
import sys
import time
from dataclasses import dataclass

# third party site-packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wv

# Custome packages
from aiolos_commissioning_tools import __version__
from aiolos_code_instrumentation.timer import timer



log = logging.getLogger(__name__)

@dataclass
class HotWireProbe:
    """
    class acting as a data struct defining the hotwire probe with default vaules
    """
    id: int
    model: str = '55P11'
    make: str = 'Dantec Dynamic'
    sn: str = '90559011'
    support: str = '55H21'


@dataclass
class Anemometer:
    id: int
    type: str = 'Mini CTA'
    model: str = '54T30'
    make: str = 'Dantec Dynamic'
    sn: str = '9054T0302'
    cable: str = '4 m SN: 9006A1863'


def load_time_signal(data_file, gain=3.16228, id=0):
    """ Function for loading time-series turbulence data from files and storing data in a numpy array

    :param data_file:    <str> full or relative path to file
    :param gain:    <float> gain voltage used during measurement (conversion from counts to volts)
    :param id:      <int> data identifier to be used to keep track of data when using multiprocessing

    :return:
            fs:     <int> sampling frequency (Hz)
            t:      <1D array<float>> time (s)
            e:      <1D array<float>> signal voltage (V)

    """
    _ = timer.Timer()
    try:
        fs, raw_data = wv.read(data_file)
    except ValueError as err:
        log.error(err)
        raise
    except FileNotFoundError as err:
        log.error(err)
        raise
    except IOError as err:
        log.error(err)
        raise
    log.debug("Data loaded from %s successfully" % os.path.basename(data_file))
    log.debug("Sampling freq. = %i (Hz)" % fs)
    log.debug("No. of samples = %i" % len(raw_data))

    # apply count to volt conversion for soundbook data
    e = raw_data * gain / (2.0 ** 15)
    log.debug("Average voltage = %.4f (V)" % np.mean(e))

    # time in seconds
    t = np.ndarray(shape=e.size, dtype=float, buffer=np.zeros(shape=e.size))
    for i in range(1, t.size):
        t[i] = t[i - 1] + 1.0 / fs

    return id, fs, t, e


def get_hw_calibration_func(u_mean, e_mean, n=0.45, return_coeff=False):
    """ Determine the calibration of the hot-wire or hot-film probe
    based on the arrays containing mean velocity and voltage signals.

    :param u_mean:          <1D array<float>> mean velocity (m/s or kph)
    :param e_mean:          <1D array<float>> mean voltage (V or mV)
    :param n:               <float> Kings law exponent - default n = 0.45 where [E**2 = Eo**2 + A*u**n]
    :param return_coeff:   <bool> flag used to return the curve fit coefficients  - default = False

    :return:
            u:      function u(e) which applies the calibration and returns the velocity for a given voltage
            Eo2:    scalar <float> Kings law offest Eo**2 (V**2 or mV**2)
            A:      scalar <float> Kings law probe sensitivity A (units depend on input units)

    """
    _ = timer.Timer()
    def u(e):
        return f(e ** 2) ** (1 / n)

    # Do array sizes match?
    if not u_mean.size == e_mean.size:
        msg = "Array dimensions do not match: %i, %i" % (u_mean.size, e_mean.size)
        # log error message
        log.error(msg)
        # halt execution with Traceback
        raise ValueError(msg)

    # first oder (i.e. linear fit)
    k = 1

    # kth order fit to the data
    z = np.polyfit(e_mean ** 2, u_mean ** n, k)

    # define function f(x) = z[i] * x ** i for i = 0 to N
    # : u**n = z[0] * e**2 + z[1]
    f = np.poly1d(z)

    if return_coeff:
        # first order polynomial (i.e. linear) fit to the data: e**2 = eo**2 + a * u**n
        coefficients = np.polyfit(u_mean ** n, e_mean ** 2, 1)
        a, eo2 = coefficients[0], coefficients[1]
        return u, eo2, a
    else:
        return u


def fft(y, fs, nsets=8, overlap=0.250):
    _ = timer.Timer()
    """ Fast Fourier transform function which returns the psd for positive frequencies.

    :param y:       <1D array<float>> time series data
    :param fs:      <int> sampling frequency
    :param nsets:   <int> number of windows
    :param overlap: <float> percentage of overlap between windows (0.0 <= overlap < 1.0)
    :return:
            psd:    <1D array<float>> power spectral density ([fft units]**2 / hz)
            f:      <1D array<float>> frequency range (Hz)
    """

    n = y.size  # number of data points in time series data

    # are the arguments within the allowable range
    # if not 0.0 <= overlap < 1.0:
    # defaults = lib.get_defaults(fft)
    # log.warning("cannot have %i %% overlap - set to default value (%i %%)." %
    #             (int(overlap*100), int(defaults['overlap']*100)))
    # overlap = defaults['overlap']

    nn = int(n / (1 - overlap))  # number of data point including repeated points in overlap
    p = next_pow_2(nn // nsets)

    if nn // nsets - 2 ** p == 0:
        nfft = int(2 ** p)
    else:
        p = p - 1
        nfft = int(2 ** p)  # number of data points per frame

    log.debug("No. Sample = %i" % n)
    log.debug("No. Windows = %i" % nsets)
    log.debug("Overlap = %i %%" % (overlap * 100))
    log.debug("Window size: 2**%i = %i" % (p, nfft))

    # number of points in overlap region
    m = int(nfft * overlap)

    # frequency range from 0 to Nyquist criterion of fs/2
    f = fs / 2.0 * np.linspace(0, 1, nfft // 2 + 1)
    df = f[1] - f[0]
    log.debug("Resolution in the frequency domain: %.4f Hz" % df)

    # set up 2D array for the windows
    psd_frame = np.ndarray(shape=(nsets, nfft // 2 + 1))

    for subset in range(nsets):
        # window the signal data
        data_frame = y[subset * (nfft - m):subset * (nfft - m) + nfft]
        # compute the fft
        fft_frame = np.fft.fft(data_frame)

        """ From NumPy.fft documentation:
            A_k =  \sum_{m=0}^{n-1} a_m \exp\left\{-2\pi i{mk \over n}\right\} k = 0,\ldots,n-1.
        If A = fft(a, n), then A[0] contains the zero-frequency term (the sum of the signal), which is always purely 
        real for real inputs. Then A[1:n/2] contains the positive-frequency terms, and A[n/2+1:] contains the negative-
        frequency terms, in order of decreasingly negative frequency. For an even number of input points, A[n/2] 
        represents both positive and negative Nyquist frequency, and is also purely real for real input. For an odd 
        number of input points, A[(n-1)/2] contains the largest positive frequency, while A[(n+1)/2] contains the 
        largest negative frequency """

        # only the positive frequencies are important (Nyquist freq. at nfft/2).
        fft_frame = fft_frame[0:nfft // 2 + 1]

        # compute power spectral density
        psd_frame[subset] = np.abs(fft_frame) ** 2.0 / (fs * nfft)

        # since half the frequencies are dropped, multiply by 2.0 to preserve total signal energy (DC and Nyquist freq.
        # are not repeated). nfft will always be even since nfft = 2**p
        psd_frame[subset][1:nfft // 2] = psd_frame[subset][1:nfft // 2] * 2.0

    psd = np.ndarray(shape=(nfft // 2 + 1,))

    for i in range(0, nfft // 2 + 1):
        psd[i] = np.mean([psd_frame[x][i] for x in range(nsets)])

    return psd, f


def turbulence_intensity(u_psd, f, low_freq=0.0, high_freq=10 ** 9):
    """ Calculate the overall turbulence intensity from the power spectral density in the
    frequency domain

    :param u_psd:       <1D array<float>> psd of the velocity signal (m/(s*Hz))
    :param f:           <1D array<float>> frequency range (Hz)
    :param low_freq:    <float> high-pass filter frequency (Hz)
    :param high_freq:   <float> low-pass filter frequency (Hz)
    :return:
            tu:         <float> turbulence intensity = sqrt(sum(psd*df))
            f:          <1D array<float>> truncated frequency range (Hz)
    """
    _ = timer.Timer()
    df = f[2] - f[1]
    rng = np.where((f >= low_freq) & (f <= high_freq))
    sum_u_df = 0.0
    for u in u_psd[rng]:
        sum_u_df += u * df
    tu = np.sqrt(sum_u_df)
    log.debug("Filtered from %.3f Hz to %.1f kHz" % (f[rng][0], f[rng][-1] / 1000))
    log.debug("Turbulence intensity = %.2f %%" % (tu * 100))
    return tu, f[rng]


def next_pow_2(x):
    """
    :param x:
    :return:    p for 2**p >= x
    """
    _ = timer.Timer()
    p = np.ceil(np.log2(x))
    log.debug("Next power of 2 for %i samples is %i (2**%i = %i)" % (x, p, p, 2 ** p))
    return p


def process_hw_data_file(data_filename, calibration_data_filename, run_id,
                         gain=3.16228, n=0.45, nsets=8, overlap=0.25, low_freq=0, high_freq=10 ** 9):
    """
    wrapper funciton which takes in a hotwire data file, and probe calibration data and returns the mean
    velocity, as well as 1sigma(u/U) and a filtered turbulence intensity

    :param run_id                       <int> run id used to keep track of data during parallel processing
    :param data_filename:               <str> time series data file (eg *.wav)
    :param calibration_data_filename:   <str> contains mean U and e for the calibration runs in two columns
    :param gain:                        <float> gain voltage used during measurement (conversion from counts to volts)
    :param n:                           <float> Kings law exponent - default n = 0.45 where [E**2 = Eo**2 + A*u**n]
    :param nsets:                       <int> number of windows
    :param overlap:                     <float> percentage of overlap between windows (0.0 <= overlap < 1.0)
    :param low_freq:                    <float> high-pass filter frequency (Hz)
    :param high_freq:                   <float> low-pass filter frequency (Hz)
    :return:
    """
    _ = timer.Timer()
    # check for a calibration file (else make one)
    try:
        u_cal, e_cal = np.loadtxt(calibration_data_filename, delimiter=',', unpack=True)
        log.debug('Calibration file %s exists!', os.path.basename(calibration_data_filename))
    except (ValueError, IOError, FileNotFoundError) as err:
        log.warning(err)
        log.warning('Cannont read %s' % os.path.basename(calibration_data_filename))
        raise
    else:
        # determine calibration function
        u_fit = get_hw_calibration_func(u_cal, e_cal, n=n, return_coeff=False)

        id, fs, t, e = load_time_signal(data_filename, gain=gain, id=run_id)
        u = u_fit(e)
        e_mean = np.mean(e, dtype=np.float64)
        u_mean = np.mean(u, dtype=np.float64)

        u_U = u / u_mean

        u_psd, f = fft(u_U, fs, nsets=nsets, overlap=overlap)

        tu, f_filt = turbulence_intensity(u_psd, f, low_freq=low_freq, high_freq=high_freq)

        log.debug('U = %.2f (m/s) e = %.2f (V), 1sigma(u/U) = %.2f %%, tu (%.2f Hz - %.2f kHz) = %.4f %% ' %
                  (u_mean, e_mean, np.std(u_U) * 100., f_filt[0], f_filt[-1] / 1000., tu * 100.))

        return run_id, u_mean, np.std(u_U), tu, f_filt[0], f_filt[-1]


def main():
    """ Main function to call when this module is executed directly on a list of input data files"""
    log.setLevel(logging.DEBUG)
    fmt = logging.Formatter('%(asctime)s <%(levelname)s> [%(module)s.%(funcName)s]: %(message)s')
    strm_handler = logging.StreamHandler()
    strm_handler.setLevel(logging.DEBUG)
    strm_handler.setFormatter(fmt)

    file_handler = logging.FileHandler('debugging-errors.log', 'a')
    file_handler.setLevel(logging.WARN)
    file_handler.setFormatter(fmt)

    log.addHandler(strm_handler)
    log.addHandler(file_handler)

    log.debug("running module %s -v%s with test case(s) %s" %
              (os.path.basename(sys.argv[0]), __version__, [os.path.basename(arg) for arg in sys.argv[1:]]))

    probe = HotWireProbe(id=1)
    aneometer = Anemometer(id=1)

    log.debug('Default %s ' % probe.__repr__())
    log.debug('Default %s ' % aneometer.__repr__())
    plt.figure(figsize=(10,5))
    for id, fname in enumerate(sys.argv[1:]):
        try:
            id, fs, t, e = load_time_signal(fname, id=id)
        except (ValueError, IOError) as err:
            log.error("Could not open %s" % fname)
            log.error(err)
        else:
            psd, f = fft(e, fs)
            e_rms = np.sqrt(0.5 * np.sum(psd[1:]))
            eo2 = 1.28
            n = 0.45
            tu = 2 * np.mean(e) * e_rms / ((np.mean(e) ** 2 - eo2) * n)
            log.debug('Tu = %.2f %% from rms voltage, guessed eo**2 = %.2f, and n = %.2f' % (tu * 100., eo2, n))
            turbulence_intensity(psd, f, low_freq=f[1], high_freq=f[-1])
            plt.gcf()
            plt.loglog(f, np.sqrt(psd), linewidth=0.5, label=os.path.basename(fname))
    plt.xlabel(r'Frequency, $f$ $\left(Hz\right)$')
    plt.ylabel(r'$\sqrt{psd}$')
    plt.legend(loc=1)




if __name__ == "__main__":
    start_time = time.time()
    main()
    print("\n[completed in %.2f seconds]" % (time.time() - start_time))
    plt.show()
    input('Press <Enter> to exit')
