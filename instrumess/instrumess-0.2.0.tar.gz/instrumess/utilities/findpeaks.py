# %load ./../functions/detect_peaks.py
"""Detect peaks in data based on their amplitude and other features."""

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from instrumess.utilities.plot_aux import fig_new  # , save_last_fig, fig_label, interactive_legend,\


plt.rcParams.update({'font.size': 14})  # set default font size for all plots

__author__ = "Marcos Duarte, https://github.com/demotu/BMC"
__version__ = "1.0.4"
__license__ = "MIT"


def detect_peaks(y, x_pos=None, mph=None, mpd=1, threshold=0, edge='rising',
                 kpsh=False, valley=False, show=False, ax=None,
                 sort='decend',  # added by Rastko 2018-06-30
                 ):
    """Detect "peaks" in data based on their amplitude and other features.

    Parameters
    ----------
    y : 1D array_like
        data.
    mph : {None, number}, optional (default = None)
        detect peaks that are greater than minimum peak height.
    mpd : positive integer, optional (default = 1)
        detect peaks that are at least separated by minimum peak distance (in
        number of data).
    threshold : positive number, optional (default = 0)
        detect peaks (valleys) that are greater (smaller) than `threshold`
        in relation to their immediate neighbors.
    edge : {None, 'rising', 'falling', 'both'}, optional (default = 'rising')
        for a flat peak, keep only the rising edge ('rising'), only the
        falling edge ('falling'), both edges ('both'), or don't detect a
        flat peak (None).
    kpsh : bool, optional (default = False)
        keep peaks with same height even if they are closer than `mpd`.
    valley : bool, optional (default = False)
        if True (1), detect valleys (local minima) instead of peaks.
    show : bool, optional (default = False)
        if True (1), plot data in matplotlib figure.
    ax : a matplotlib.axes.Axes instance, optional (default = None).

    Returns
    -------
    ind : 1D array_like
        indeces of the peaks in `y`.

    Notes
    -----
    The detection of valleys instead of peaks is performed internally by simply
    negating the data: `ind_valleys = detect_peaks(-y)`
    
    The function can handle NaN's

    See this IPython Notebook [1]_.

    References
    ----------
    .. [1] http://nbviewer.ipython.org/github/demotu/BMC/blob/master/notebooks/DetectPeaks.ipynb

    Examples
    --------
    >>> from detect_peaks import detect_peaks
    >>> y = np.random.randn(100)
    >>> y[60:81] = np.nan
    >>> # detect all peaks and plot data
    >>> ind = detect_peaks(y, show=True)
    >>> print(ind)

    >>> y = np.sin(2*np.pi*5*np.linspace(0, 1, 200)) + np.random.randn(200)/5
    >>> # set minimum peak height = 0 and minimum peak distance = 20
    >>> detect_peaks(y, mph=0, mpd=20, show=True)

    >>> y = [0, 1, 0, 2, 0, 3, 0, 2, 0, 1, 0]
    >>> # set minimum peak distance = 2
    >>> detect_peaks(y, mpd=2, show=True)

    >>> y = np.sin(2*np.pi*5*np.linspace(0, 1, 200)) + np.random.randn(200)/5
    >>> # detection of valleys instead of peaks
    >>> detect_peaks(y, mph=0, mpd=20, valley=True, show=True)

    >>> y = [0, 1, 1, 0, 1, 1, 0]
    >>> # detect both edges
    >>> detect_peaks(y, edge='both', show=True)

    >>> y = [-2, 1, -2, 2, 1, 1, 3, 0]
    >>> # set threshold = 2
    >>> detect_peaks(y, threshold = 2, show=True)
    """
    if x_pos is not None and mpd==1:
        mpd = 0
    y = np.atleast_1d(y).astype('float64')
    if y.size < 3:
        return np.array([], dtype=int)
    if valley:
        y = -y
    # find indices of all peaks
    dy = y[1:] - y[:-1]
    # handle NaN's
    indnan = np.where(np.isnan(y))[0]
    if indnan.size:
        y[indnan] = np.inf
        dy[np.where(np.isnan(dy))[0]] = np.inf
    ine, ire, ife = np.array([[], [], []], dtype=int)
    if not edge:
        ine = np.where((np.hstack((dy, 0)) < 0) & (np.hstack((0, dy)) > 0))[0]
    else:
        if edge.lower() in ['rising', 'both']:
            ire = np.where((np.hstack((dy, 0)) <= 0) & (np.hstack((0, dy)) > 0))[0]
        if edge.lower() in ['falling', 'both']:
            ife = np.where((np.hstack((dy, 0)) < 0) & (np.hstack((0, dy)) >= 0))[0]
    ind = np.unique(np.hstack((ine, ire, ife)))
    # handle NaN's
    if ind.size and indnan.size:
        # NaN's and values close to NaN's cannot be peaks
        ind = ind[np.in1d(ind, np.unique(np.hstack((indnan, indnan-1, indnan+1))), invert=True)]
    # first and last values of y cannot be peaks
    if ind.size and ind[0] == 0:
        ind = ind[1:]
    if ind.size and ind[-1] == y.size-1:
        ind = ind[:-1]
    # remove peaks < minimum peak height
    if ind.size and mph is not None:
        ind = ind[y[ind] >= mph]
    # remove peaks - neighbors < threshold
    if ind.size and threshold > 0:
        dy = np.min(np.vstack([y[ind]-y[ind-1], y[ind]-y[ind+1]]), axis=0)
        ind = np.delete(ind, np.where(dy < threshold)[0])
    # detect small peaks closer than minimum peak distance
    if x_pos is None:
        if ind.size and (mpd > 1):
            ind = ind[np.argsort(y[ind])][::-1]  # sort ind by peak height
            idel = np.zeros(ind.size, dtype=bool)
            for i in range(ind.size):
                if not idel[i]:
                    # keep peaks with the same height if kpsh is True
                    idel = idel \
                           | (ind >= ind[i] - mpd) \
                           & (ind <= ind[i] + mpd) \
                           & (y[ind[i]] > y[ind] if kpsh else True)
                    idel[i] = 0  # Keep current peak
            # remove the small peaks and sort back the indices by their occurrence
            ind = np.sort(ind[~idel])
    else:
        if ind.size:
            ind = ind[np.argsort(y[ind])][::-1]  # sort ind by peak height
            x_pos_sort = x_pos[ind]
            idel = np.zeros(ind.size, dtype=bool)
            for i in range(ind.size):
                if not idel[i]:
                    idel = idel \
                           | (x_pos_sort >= x_pos_sort[i]-mpd) \
                           & (x_pos_sort <= x_pos_sort[i]+mpd) \
                           & (y[ind[i]] > y[ind] if kpsh else True)
                    idel[i] = 0  # Keep current peak
            # remove the small peaks and sort back the indices by their occurrence
            ind = np.sort(ind[~idel])

    if show:
        if indnan.size:
            y[indnan] = np.nan
        if valley:
            y = -y
        _plot(y, mph, mpd, threshold, edge, valley, ax, ind, x_pos=x_pos)

    if sort == 'decend':
        ind = ind[y[ind].argsort()[::-1]]
    elif sort == 'accend':
        ind = ind[y[ind].argsort()]

    return ind


def _plot(y, mph, mpd, threshold, edge, valley, ax, ind, x_pos=None):
    """Plot results of the detect_peaks function, see its help."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print('matplotlib is not available.')
    else:
        if ax is None:
            _, ax = fig_new('detect_peaks result')

        if x_pos is None:
            ax.plot(y, 'b', lw=1)
        else:
            ax.plot(x_pos, y, 'b', lw=1)
        if ind.size:
            label = 'valley' if valley else 'peak'
            label = label + 's' if ind.size > 1 else label
            if x_pos is None:
                ax.plot(ind, y[ind], '+', mfc=None, mec='r', mew=2, ms=8,
                        label='%d %s' % (ind.size, label))
            else:
                ax.plot(x_pos[ind], y[ind], '+', mfc=None, mec='r', mew=2, ms=8,
                        label='%d %s' % (ind.size, label))
            ax.legend(loc='best', framealpha=.5, numpoints=1)
        if x_pos is None:
            ax.set_xlim(-.02*y.size, y.size*1.02-1)
        ymin, ymax = y[np.isfinite(y)].min(), y[np.isfinite(y)].max()
        yrange = ymax - ymin if ymax > ymin else 1
        ax.set_ylim(ymin - 0.1*yrange, ymax + 0.1*yrange)
        if x_pos is None:
            ax.set_xlabel('Data #', fontsize=14)
        ax.set_ylabel('Amplitude', fontsize=14)
        mode = 'Valley detection' if valley else 'Peak detection'
        ax.set_title("%s (mph=%s, mpd=%d, threshold=%s, edge='%s')"
                     % (mode, str(mph), mpd, str(threshold), edge))
        # plt.grid()
        plt.show()
