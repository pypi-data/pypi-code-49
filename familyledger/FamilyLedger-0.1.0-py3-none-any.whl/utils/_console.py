"""
A module for console utilities.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""
from tqdm import tqdm


def progress_bar(*pargs, bar_format=None, **kwargs):
    """Customizes the output of `tqdm`_ 's progress bar.
    
    The default bar format has been changed to eliminate the output of a "rate",
    i.e. the default 'it/s' (iterations per second) part of the output.
    
    Args:
        *pargs: positional arguments to pass through.
        bar_format (str): customized progress bar format.
        *kwargs: keyword arguments to pass through.

    Returns:
        :obj:`tqdm`: a customized iterable.
        
    .. _tqdm: https://github.com/tqdm/tqdm
    """
    default_bar_format = '{l_bar}{bar}'
    default_bar_format += '| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]'
    custom_bar_format = bar_format or default_bar_format
    return tqdm(*pargs, bar_format=custom_bar_format, **kwargs)
