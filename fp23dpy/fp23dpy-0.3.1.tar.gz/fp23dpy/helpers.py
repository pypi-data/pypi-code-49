"""
Helper module with functions used by the other modules
"""
# Helper functions
import numpy as np
# import matplotlib.pyplot as plt
import os.path as osp
from skimage import filters


def is_image_file(f):
    """ Returns true for a filepath with supported image format """
    return osp.isfile(f) and ('.tif'  == f[-4:].lower() or
                              '.tiff' == f[-5:].lower() or
                              '.jpg'  == f[-4:].lower() or
                              '.png'  == f[-4:].lower())

def image_scaled(im, new_lim):
    """Scaling image to certain pixel value limits"""
    min_val = np.min(im)
    max_val = np.max(im)
    im = ((im - min_val) * np.diff(new_lim)[0] / (max_val - min_val)
              + new_lim[0])
    return im


def gaus2(shape, b, a_r, a_c=None, gamma=0):
    """Creates an image with a gaussian shape"""
    if a_c is None:
        a_c = a_r
    w = np.dstack(np.mgrid[:shape[0], :shape[1]]) - b
    w_r = w[:, :, 1] * np.cos(gamma) - w[:, :, 0] * np.sin(gamma)
    w[:, :, 1] = w[:, :, 1] * np.sin(gamma) + w[:, :, 0] * np.cos(gamma)
    w[:, :, 0] = w_r
    return (np.exp(-(np.square(w[:, :, 0]) / a_r**2
                + np.square(w[:, :, 1]) / a_c**2) / 2))

def make_carrier(shape, T, gamma=0, zero_point=[0, 0]):
    """Create a phase carrier, standard is to use a plane as carrier but a square function can also be used"""
    Y, X = np.mgrid[:shape[0], :shape[1]]
    if isinstance(T, (float, int)):
        w = np.dstack([Y - zero_point[1], X - zero_point[0]])
        R = np.array([[np.sin(gamma)],
                      [np.cos(gamma)]])
        carrier = 2 * np.pi * 1 / T * np.matmul(w, R)[:, :, 0]
    elif isinstance(T, list) and len(T) == 5:
        carrier = (T[0] +
                   T[1] * X + T[2] * Y + 
                   T[3] * X**2 + T[4] * Y**2)
    else:
        raise ValueError("T should either be a single value or a 5 element list")
    return carrier

def get_Trange(T, T_n=5):
    """Standard function to get Trange if it is not found"""
    Tlim = T / np.array([1.9, 0.7])
    Trange = np.linspace(Tlim[0], Tlim[1], T_n)
    return Trange


def square_carrier(phase):
    """Estimating a square phase carrier instead of a plane"""
    shape = phase.shape
    Y_full, X_full = np.mgrid[:shape[0], :shape[1]]
    if np.ma.isMaskedArray(phase):
        mask = phase.mask
        X = X_full[~mask]
        Y = Y_full[~mask]
        Z = phase[~mask]
    else:
        X = X_full.flatten()
        Y = Y_full.flatten()
        Z = phase.flatten()
    A = np.vstack((np.ones(X.size), X, Y, X**2, Y**2)).transpose()
    b = Z

    coeffs = np.linalg.lstsq(A, b, None)[0]
    return list(coeffs)

def get_T_from_square(T, shape):
    """Estimate a single derivative of a square phase carrier"""
    if isinstance(T, (float, int)):
        return T
    elif isinstance(T, list) and len(T) == 5:
        # return 2 * np.pi / np.sqrt(T[1]**2 + T[2]**2)
        return 2 * np.pi / np.sqrt((T[1] + 2 * T[3] * shape[1] / 2)**2 + (T[2] + 2 * T[4] * shape[0] / 2)**2)

def lpf(s, bandpass_x, bandpass_y=None, gamma=0):
    """Low pass filter of an image using the fourier transform and a gaussian filter"""
    if bandpass_y is None:
        bandpass_y = bandpass_x
    F = np.fft.fftshift(np.fft.fft2(s))
    shape = np.array(F.shape)
    gaus = gaus2(shape, shape / 2, bandpass_y, bandpass_x, gamma)
    return np.fft.ifft2(np.fft.ifftshift(F * gaus**3))

def hpf(signal, T = 12):
    """High pass filter of an image by subtracting the low pass filter of the same image"""
    k_size = 2 * int(T) + 1
    lpf_signal = filters.gaussian(signal, k_size / 4)
    return signal - lpf_signal

def ft2_helper(s, T, gamma, sigma_x, sigma_y=None): 
    """Helper function for the Fourier Transform phase demodulation method"""
    carrier = make_carrier(s.shape, T, gamma)
    sync_freq = s * np.exp(-1j * carrier)
    return lpf(sync_freq, sigma_x, sigma_y, gamma)

# def matrix_translation(m, dr, dc):
#     shape = m.shape
#     r, c = np.mgrid[:shape[0], :shape[1]]
#     nr = r - dr
#     nc = c - dc
#     valid = (nr >= 0) & (nc >= 0) & (nr < shape[0]) & (nc < shape[1])
#     wr, wc = np.where(valid)
#     tm = np.zeros(shape, dtype=m.dtype)
#     tm[valid] = m[wr - dr, wc - dc]
#     return tm

# def fundamental_frequency_peak(F):
#     shape = np.array(F.shape)
#     p = pf.find(F, 1, subpixel_accuracy=False)[0]
#     dr = int(np.round(p[0] * np.sin(p[1]) * shape[0]))
#     dc = int(np.round(p[0] * np.cos(p[1]) * shape[1]))
#     sigma = np.min(np.abs(1 / p[2:] - 1 / p[0])) * np.mean(shape) * 1.2
#     return (dr, dc, sigma)

# def combinations(x, y):
#     mesh_x, mesh_y = np.meshgrid(x, y)
#     return np.transpose(np.vstack((mesh_x.flatten(), mesh_y.flatten())))

def circleKernel(radius):
    """Create a kernel in the form of a circle"""
    xy = np.arange(-radius, radius + 1)
    x, y = np.meshgrid(xy, xy)
    return (x**2 + y**2 <= radius**2 + 0.8).astype(np.uint8)

# def ransac_carrier_estimation(threeD):
#     shape = threeD.shape
#     Y_full, X_full = np.mgrid[:shape[0], :shape[1]]
#     if np.ma.isMaskedArray(threeD):
#         mask = threeD.mask
#         X = X_full[~mask]
#         Y = Y_full[~mask]
#         Z = threeD[~mask]
#     else:
#         X = X_full.flatten()
#         Y = Y_full.flatten()
#         Z = threeD.flatten()
#     points = np.vstack((Z, np.ones(X.size), X, Y, X**2, Y**2)).transpose()
#     coeffs = cxx.ransac_ls(points, 1e-5)
# 
#     X_flat = X_full.flatten()
#     Y_flat = Y_full.flatten()
#     X2 = np.vstack((np.ones(X_flat.size), X_flat, Y_flat, X_flat**2, Y_flat**2)).transpose()
#     return np.dot(X2, coeffs).reshape(shape)
