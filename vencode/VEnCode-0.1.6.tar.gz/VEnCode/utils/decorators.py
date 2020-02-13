#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
decorators.py: Utility functions for Decorating other functions.
"""
import os
from functools import wraps


def profile_func(filename=None):
    """
    Function that makes decorators. It is used to pass down arguments to decorators if needed.

    Use like this: @profile_func("filename.profile"). Note, you can provide no arg at all.

    These decorators create a file "..._func.profile" containing the rundown of a cProfile call on that function.
    The file can then be parsed by pstats module or visually by the snakevis module.

    BE CAREFUL! profiling adds overhead time in your functions. Better not use in final products, only in testing.
    """

    def prof_func(f):
        """
        The actual decorator wrapped around the function (f).
        :param f: The function to decorate.
        :return: the wrapper function.
        """

        @wraps(f)
        def profiled_func(*args, **kwargs):
            """
            The actual wrapper function.
            :param args: args to pass down to function.
            :param kwargs: key args to pass down to function.
            :return: the cProfiler run.
            """
            import cProfile
            import logging
            logging.info('Profiling function {}'.format(f.__name__))
            directory = os.path.join(os.pardir, "Profiling")
            if not os.path.exists(directory):
                os.makedirs(directory)
            file = os.path.join(directory, filename or "{}_func.profile".format(f.__name__))
            try:
                profiler = cProfile.Profile()
                retval = profiler.runcall(f, *args, **kwargs)
                profiler.dump_stats(file)
            except IOError:
                logging.exception(_("Could not open profile file '%(filename)s'") % {"filename": filename})
            return retval

        return profiled_func

    return prof_func
