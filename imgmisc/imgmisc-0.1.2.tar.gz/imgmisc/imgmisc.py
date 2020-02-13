# -*- coding: utf-8 -*-

"""Main module."""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 20:00:11 2018

@author: henrik
"""

import re
import os
import numpy as np
import tifffile as tiff

def get_resolution(fname):
    f = tiff.TiffFile(fname)
    if f.imagej_metadata is not None:
        try:
            z = f.imagej_metadata['spacing']
        except:
            z = 1.
        x = f.pages[0].tags['XResolution'].value[1] / f.pages[0].tags['XResolution'].value
        y = x
    elif f.lsm_metadata is not None:
        raise NotImplementedError()
    else:
        z, y, x = 1., 1., 1.
    return z, y, x



def cut(img, cuts):
    return img[
        cuts[0, 0] : cuts[0, 1], cuts[1, 0] : cuts[1, 1], cuts[2, 0] : cuts[2, 1]
    ]


def merge(lists):
    """
    Merge lists based on overlapping elements.

    Parameters
    ----------
    lists : list of lists
        Lists to be merged.

    Returns
    -------
    sets : list
        Minimal list of independent sets.

    """
    sets = [set(lst) for lst in lists if lst]
    merged = 1
    while merged:
        merged = 0
        results = []
        while sets:
            common, rest = sets[0], sets[1:]
            sets = []
            for x in rest:
                if x.isdisjoint(common):
                    sets.append(x)
                else:
                    merged = 1
                    common |= x
            results.append(common)
        sets = results
    return sets


def flatten(llist):
    """ Flatten a list of lists """
    return [item for sublist in llist for item in sublist]


def remove_empty_slices(arr, keepaxis=0):
    """ Remove empty slices (based on the total intensity) in an ndarray """
    not_empty = np.sum(arr, axis=tuple(np.delete(list(range(arr.ndim)), keepaxis))) > 0
    arr = arr[not_empty]
    return arr


def autocrop(arr, threshold=8e3, channel=-1, n=1, return_cuts=False, offset=None):

    if offset is None:
        offset = [[0, 0], [0, 0], [0, 0]]
    offset = np.array(offset)

    sumarr = arr
    if arr.ndim > 3:
        if channel == -1:
            sumarr = np.max(arr, axis=1)
        elif isinstance(channel, (list, np.ndarray, tuple)):
            sumarr = np.max(arr.take(channel, axis=1), axis=1)
        else:
            sumarr = sumarr[:, channel]

    cp = np.zeros((sumarr.ndim, 2), dtype=np.int)
    for ii in range(sumarr.ndim):
        axes = np.array([0, 1, 2])[np.array([0, 1, 2]) != ii]

        transposed = np.transpose(sumarr, (ii,) + tuple(axes))
        nabove = np.sum(
            np.reshape(transposed, (transposed.shape[0], -1)) > threshold, axis=1
        )

        first = next((e[0] for e in enumerate(nabove) if e[1] >= n), 0)
        last = len(nabove) - next(
            (e[0] for e in enumerate(nabove[::-1]) if e[1] >= n), 0
        )

        cp[ii] = first, last
    #    ranges = [range(cp[ii, 0], cp[ii, 1]) for ii in range(len(cp))]
    cp[0, 0] = np.max([0, cp[0, 0] - offset[0, 0]])
    cp[0, 1] = np.min([arr.shape[0], cp[0, 1] + offset[0, 1]])
    cp[1, 0] = np.max([0, cp[1, 0] - offset[1, 0]])
    cp[1, 1] = np.min([arr.shape[1], cp[1, 1] + offset[1, 1]])
    cp[2, 0] = np.max([0, cp[2, 0] - offset[2, 0]])
    cp[2, 1] = np.min([arr.shape[2], cp[2, 1] + offset[2, 1]])

    if arr.ndim > 3:
        arr = np.moveaxis(arr, 1, -1)
    for ii, _range in enumerate(cp):
        arr = np.swapaxes(arr, 0, ii)
        arr = arr[_range[0] : _range[1]]
        arr = np.swapaxes(arr, 0, ii)
    if arr.ndim > 3:
        arr = np.moveaxis(arr, -1, 1)

    if return_cuts:
        return arr, cp
    else:
        return arr


def mkdir(path):
    """
    Make a directory if it doesn't exist already.

    Parameters
    ----------
    path : str
        Path to directory.

    Returns
    -------
    None.

    """

    if not os.path.exists(path):
        os.makedirs(path)


def listdir(path, include=None, exclude=None, full=True, sorting=None):
    if isinstance(path, (list, np.ndarray)):
        files = flatten([listdir(ff, include, exclude, full, sorting) for ff in path])
        return np.array(files)
    else:
        files = os.listdir(path)
        files = np.array(files)

    if full:
        files = np.array([os.path.join(path, x) for x in files])

    # Include
    if isinstance(include, str):
        files = np.array([x for x in files if include in x])
    elif isinstance(include, (list, np.ndarray)):
        matches = np.array([np.array([inc in ii for ii in files]) for inc in include])
        matches = np.any(matches, axis=0)
        files = files[matches]

    # Exclude
    if isinstance(exclude, str):
        files = np.array([x for x in files if exclude not in x])
    elif isinstance(exclude, (list, np.ndarray)):
        matches = np.array([np.array([exc in ii for ii in files]) for exc in exclude])
        matches = np.logical_not(np.any(matches, axis=0))
        files = files[matches]

    if sorting == "natural":
        files = np.array(natural_sort(files))
    elif sorting == "alphabetical":
        files = np.sort(files)
    elif sorting == True:
        files = np.sort(files)

    return files


def natural_sort(l):
    """
    Sort a list alphanumerically (natural sorting).

    Parameters
    ----------
    l : list or np.ndarray
        Structure to sort.

    Returns
    -------
    list or np.ndarray
        Sorted list/array.

    """

    def convert(text):
        return int(text) if text.isdigit() else text.lower()

    def alphanum_key(key):
        return [convert(c) for c in re.split("([0-9]+)", key)]

    return sorted(l, key=alphanum_key)


def match_shape(a, t, side="both", val=0):
    """

    Parameters
    ----------
    a : np.ndarray
    t : Dimensions to pad/trim to, must be a list or tuple
    side : One of 'both', 'before', and 'after'
    val : value to pad with
    """
    try:
        if len(t) != a.ndim:
            raise TypeError(
                "t shape must have the same number of dimensions as the input"
            )
    except TypeError:
        raise TypeError("t must be array-like")

    try:
        if isinstance(val, (int, float, complex)):
            b = np.ones(t, a.dtype) * val
        elif val == "max":
            b = np.ones(t, a.dtype) * np.max(a)
        elif val == "mean":
            b = np.ones(t, a.dtype) * np.mean(a)
        elif val == "median":
            b = np.ones(t, a.dtype) * np.median(a)
        elif val == "min":
            b = np.ones(t, a.dtype) * np.min(a)
    except TypeError:
        raise TypeError("Pad value must be numeric or string")
    except ValueError:
        raise ValueError("Pad value must be scalar or valid string")

    aind = [slice(None, None)] * a.ndim
    bind = [slice(None, None)] * a.ndim

    # pad/trim comes after the array in each dimension
    if side == "after":
        for dd in range(a.ndim):
            if a.shape[dd] > t[dd]:
                aind[dd] = slice(None, t[dd])
            elif a.shape[dd] < t[dd]:
                bind[dd] = slice(None, a.shape[dd])
    # pad/trim comes before the array in each dimension
    elif side == "before":
        for dd in range(a.ndim):
            if a.shape[dd] > t[dd]:
                aind[dd] = slice(int(a.shape[dd] - t[dd]), None)
            elif a.shape[dd] < t[dd]:
                bind[dd] = slice(int(t[dd] - a.shape[dd]), None)
    # pad/trim both sides of the array in each dimension
    elif side == "both":
        for dd in range(a.ndim):
            if a.shape[dd] > t[dd]:
                diff = (a.shape[dd] - t[dd]) / 2.0
                aind[dd] = slice(int(np.floor(diff)), int(a.shape[dd] - np.ceil(diff)))
            elif a.shape[dd] < t[dd]:
                diff = (t[dd] - a.shape[dd]) / 2.0
                bind[dd] = slice(int(np.floor(diff)), int(t[dd] - np.ceil(diff)))
    else:
        raise Exception("Invalid choice of pad type: %s" % side)

    b[tuple(bind)] = a[tuple(aind)]

    return b


def intensity_projection_series_all(infiles, outname, fct=np.max, normalize="all"):
    import phenotastic.file_processing as fp
    from pystackreg import StackReg
    from skimage.transform import warp
    import tifffile as tiff

    fdata = [fp.tiffload(x).data for x in infiles]
    shapes = [x.shape for x in fdata]
    max_dim = np.max(shapes)
    nchannels = fdata[0].shape[1]
    ntp = len(fdata)

    sr = StackReg(StackReg.RIGID_BODY)
    stack = np.zeros((nchannels, max_dim * ntp, 3 * max_dim))
    for chan in range(nchannels):
        cstack = np.zeros((3, max_dim * ntp, max_dim))
        for dim in range(3):
            cdstack = np.zeros((ntp, max_dim, max_dim))
            for tp in range(len(fdata)):
                one_proj = np.max(fdata[tp][:, chan], axis=dim)
                one_proj = match_shape(one_proj, (max_dim, max_dim))
                cdstack[tp] = one_proj
            tmats = sr.register_stack(cdstack, moving_average=ntp)
            for ii in range(len(tmats)):
                cdstack[ii] = warp(cdstack[ii], tmats[ii], preserve_range=True)
            cdstack = np.vstack(cdstack)
            cstack[dim] = cdstack

        if normalize == "all":
            cstack /= np.max(cstack)
        elif normalize == "first":
            cstack /= np.max(cstack[0])

        cstack = np.hstack(cstack)
        stack[chan] = cstack

    out = np.hstack(stack)
    out = out.astype(np.float32)
    # TODO: Save as png instead
    tiff.imsave(outname, out)


def to_uint8(data, normalize=True):
    data = data.astype("float")
    if normalize:
        data = (data - np.min(data)) / (np.max(data) - np.min(data)) * 255
    else:
        data = data / np.max(data) * 255
    data = data.astype(np.uint8)
    return data


def matching_rows(array1, array2):
    return np.array(
        np.all((array1[:, None, :] == array2[None, :, :]), axis=-1).nonzero()
    ).T


def rand_cmap(
    nlabels,
    type="bright",
    first_color_black=True,
    last_color_black=False,
    verbose=False,
):
    """
    Creates a random colormap to be used together with matplotlib. Useful for segmentation tasks
    :param nlabels: Number of labels (size of colormap)
    :param type: 'bright' for strong colors, 'soft' for pastel colors
    :param first_color_black: Option to use first color as black, True or False
    :param last_color_black: Option to use last color as black, True or False
    :param verbose: Prints the number of labels and shows the colormap. True or False
    :return: colormap for matplotlib
    """
    from matplotlib.colors import LinearSegmentedColormap
    import colorsys
    import numpy as np

    if type not in ("bright", "soft"):
        print('Please choose "bright" or "soft" for type')
        return

    if verbose:
        print("Number of labels: " + str(nlabels))

    # Generate color map for bright colors, based on hsv
    if type == "bright":
        randHSVcolors = [
            (
                np.random.uniform(low=0.0, high=1),
                np.random.uniform(low=0.2, high=1),
                np.random.uniform(low=0.9, high=1),
            )
            for i in range(nlabels)
        ]

        # Convert HSV list to RGB
        randRGBcolors = []
        for HSVcolor in randHSVcolors:
            randRGBcolors.append(
                colorsys.hsv_to_rgb(HSVcolor[0], HSVcolor[1], HSVcolor[2])
            )

        if first_color_black:
            randRGBcolors[0] = [0, 0, 0]

        if last_color_black:
            randRGBcolors[-1] = [0, 0, 0]

        random_colormap = LinearSegmentedColormap.from_list(
            "new_map", randRGBcolors, N=nlabels
        )

    # Generate soft pastel colors, by limiting the RGB spectrum
    if type == "soft":
        low = 0.6
        high = 0.95
        randRGBcolors = [
            (
                np.random.uniform(low=low, high=high),
                np.random.uniform(low=low, high=high),
                np.random.uniform(low=low, high=high),
            )
            for i in range(nlabels)
        ]

        if first_color_black:
            randRGBcolors[0] = [0, 0, 0]

        if last_color_black:
            randRGBcolors[-1] = [0, 0, 0]
        random_colormap = LinearSegmentedColormap.from_list(
            "new_map", randRGBcolors, N=nlabels
        )

    # Display colorbar
    if verbose:
        from matplotlib import colors, colorbar
        from matplotlib import pyplot as plt

        fig, ax = plt.subplots(1, 1, figsize=(15, 0.5))

        bounds = np.linspace(0, nlabels, nlabels + 1)
        norm = colors.BoundaryNorm(bounds, nlabels)

        cb = colorbar.ColorbarBase(
            ax,
            cmap=random_colormap,
            norm=norm,
            spacing="proportional",
            ticks=None,
            boundaries=bounds,
            format="%1i",
            orientation=u"horizontal",
        )

    return random_colormap
