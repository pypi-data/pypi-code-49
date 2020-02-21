import collections
import typing

import numpy as np
from equilibrator_api import Q_, R, default_T
from scipy import stats


RT = R * default_T

CELL_VOL_PER_DW = Q_(
    "2.7 milliliter / gram"
)  # cell dry weight, [Winkler and Wilson, 1966, http://www.jbc.org/content/241/10/2200.full.pdf+html]

ECF_DEFAULTS = {
    "flux_unit": "mM/s",
    "version": "3",  # options are: 1, 2, 3, or 4
    "kcat_source": "gmean",  # options are: 'fwd' or 'gmean'
    "denominator": "CM",  # options are: 'S', 'SP', '1S', '1SP', or 'CM'
    "regularization": "volume",  # options are: None, 'volume', or 'quadratic'
    "standard_concentration": "1 M",  # must be explicit in order to avoid
    # confusion with other scripts that
    # use different conventions (e.g. 1 mM)
}
str2bool = lambda x: x not in [0, "false", "False"]


def CastToColumnVector(v):
    """
        casts any numeric list of floats to a 2D-matrix with 1 column,
        and rows corresponding to the length of the list

        if the input is a NumPy array or matrix, it will be reshaped to
    """
    if type(v) in [np.ndarray, np.matrix]:
        return np.array(
            np.reshape(v, (np.prod(v.shape), 1)), dtype=float, ndmin=2
        )
    if isinstance(v, collections.Iterable):
        return np.array(list(v), dtype=float, ndmin=2).T
    else:
        raise ValueError(
            "Can only cast lists or numpy arrays, not " + str(type(v))
        )


def QuantitiesToColumnVector(l: typing.Iterable[Q_], unit: str = ""):
    """
        Returns a float column vector, after converting all values to
        the provided unit.
    """
    return np.array(
        [x.m_as(unit) if not np.isnan(x) else np.nan for x in l],
        dtype=float,
        ndmin=2,
    ).T


def PlotCorrelation(ax, x, y, labels, mask=None, scale="log", grid=True):
    """
        scale - if 'log' indicates that the regression should be done on the
                logscale data.
    """
    x = CastToColumnVector(x)
    y = CastToColumnVector(y)

    if mask is None:
        mask = (np.nan_to_num(x) > 0) & (np.nan_to_num(y) > 0)

    ax.grid(grid)
    if scale == "log":
        ax.set_xscale("log")
        ax.set_yscale("log")
        logx = np.log10(x[mask])
        logy = np.log10(y[mask])
        slope, intercept, r_value, p_value, std_err = stats.linregress(
            logx.flat, logy.flat
        )
        rmse = np.sqrt(np.power(logx - logy, 2).mean())
    else:
        ax.set_xscale("linear")
        ax.set_yscale("linear")
        slope, intercept, r_value, p_value, std_err = stats.linregress(
            x[mask].flat, y[mask].flat
        )
        rmse = np.sqrt(np.power(x[mask] - y[mask], 2).mean())
    ax.plot(x[mask], y[mask], ".", markersize=15, color="red", alpha=0.5)
    ax.plot(x[~mask], y[~mask], ".", markersize=15, color="blue", alpha=0.5)

    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    ax.set_xlim(min(xmin, ymin), max(xmax, ymax))
    ax.set_ylim(min(xmin, ymin), max(xmax, ymax))
    ax.plot(
        [0, 1], [0, 1], ":", color="black", alpha=0.4, transform=ax.transAxes
    )

    boxtext = "RMSE = %.2f\n$r^2$ = %.2f\n(p = %.1e)" % (
        rmse,
        r_value ** 2,
        p_value,
    )

    ax.text(
        0.05,
        0.95,
        boxtext,
        verticalalignment="top",
        horizontalalignment="left",
        transform=ax.transAxes,
        color="black",
        fontsize=10,
        bbox={"facecolor": "white", "alpha": 0.5, "pad": 10},
    )

    for l, x_i, y_i, m in zip(labels, x, y, mask):
        if m:
            ax.text(x_i, y_i, l, alpha=1.0)
        elif np.isfinite(x_i) and np.isfinite(y_i):
            if scale == "linear" or (x_i > 0 and y_i > 0):
                ax.text(x_i, y_i, l, alpha=0.4)
