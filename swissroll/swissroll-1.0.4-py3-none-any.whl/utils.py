import numpy as np

__all__ = ["ecdf"]


def ecdf(samples):
    """Empirical Cumulative Distribution Function
    acts like a proxy for the Cumulative distribution
    function and can be used to predict the central
    tendency of a random sample.

    Parameters
    ----
    samples: array_like
             Observed Data.
    
    Returns
    -----
    x_ecdf, y_ecdf: array_like
                    Sorted samples x_ecdf and corresponding
                    quantiles y_ecdf.

    Examples
    -----
    >>> from swissroll.utils import ecdf
    >>> import numpy as np
    >>> sample = np.random.randn(1000)
    >>> x_ecdf, y_ecdf = ecdf(sample)
    """
    x_ecdf = np.sort(samples)
    y_ecdf = np.arange(1, len(x_ecdf) + 1) / len(x_ecdf)

    return x_ecdf, y_ecdf
