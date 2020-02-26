# -----------------------------------------------------------------------------
#
# This file is the copyrighted property of Tableau Software and is protected
# by registered patents and other applicable U.S. and international laws and
# regulations.
#
# Unlicensed use of the contents of this file is prohibited. Please refer to
# the NOTICES.txt file for further details.
#
# -----------------------------------------------------------------------------
import os
import sys

from pathlib import Path

MICROSECONDS_PER_SECOND = 1000000
MICROSECONDS_PER_DAY = 24 * 60 * 60 * MICROSECONDS_PER_SECOND

PLAT_WINDOWS = 'win32'
PLAT_LINUX = 'linux'
PLAT_OSX = 'osx'

if sys.platform.startswith(PLAT_WINDOWS):
    PLATFORM = PLAT_WINDOWS
elif sys.platform.startswith(PLAT_LINUX):
    PLATFORM = PLAT_LINUX
elif sys.platform.startswith('darwin'):
    PLATFORM = PLAT_OSX
else:
    raise RuntimeError('Unknown platform {}'.format(sys.platform))


def _get_packaged_native_bin_dir() -> Path:
    return Path(os.path.dirname(__file__)).parent / 'bin'


def _get_hyperd_filename():
    return 'hyperd.exe' if PLATFORM == PLAT_WINDOWS else 'hyperd'


def _get_tableauhyperapi_lib_filename():
    if PLATFORM == PLAT_WINDOWS:
        return 'tableauhyperapi.dll'
    elif PLATFORM == PLAT_LINUX:
        return 'libtableauhyperapi.so'
    elif PLATFORM == PLAT_OSX:
        return 'libtableauhyperapi.dylib'
    else:
        raise RuntimeError('Unknown platform {}'.format(PLATFORM))


def _find_dir_with_binary(binary, env_var, subdir, error_message) -> Path:
    path = _get_packaged_native_bin_dir()
    if subdir is not None:
        path = path / subdir
    if path.exists() and (path / binary).exists():
        return path

    env_var_value = os.environ.get(env_var)
    if env_var_value:
        path = Path(env_var_value)
        if path.exists() and (path / binary).exists():
            return path

    raise RuntimeError(error_message + str(path))


def _find_hyper_api_dir() -> Path:
    # We expect hyper-api binary to be inside tableauhyperapi/bin, but that can be overridden, so for instance
    # one may run code directly from the source folder.
    return _find_dir_with_binary(_get_tableauhyperapi_lib_filename(), 'HYPER_API_PATH', None,
                                 '{} library not found. Could not find the Hyper API directory'
                                 .format(_get_tableauhyperapi_lib_filename()))


def find_hyper_api_dll():
    return _find_hyper_api_dir() / _get_tableauhyperapi_lib_filename()


def check_precondition(condition, error_message, error_class=None):
    if not condition:
        if not error_class:
            error_class = ValueError
        raise error_class(error_message)


def less_than_for_pairs_first_optional(pair1, pair2):
    # name with fewer components compares less
    if not pair1[0]:
        if pair2[0]:
            return True
        else:
            return pair1[1] < pair2[1]
    elif not pair2[0]:
        return False

    return pair1 < pair2


def c_modulus(x, y):
    """ C-style modulus operation (different treatment of negative numbers) """
    return x % y if x >= 0 else x % (-y)


def c_divide(x, y):
    """ C-style division operation (different treatment of negative numbers) """
    return x // y if x >= 0 else -(-x // y)
