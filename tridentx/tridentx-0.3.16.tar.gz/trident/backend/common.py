from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import threading
import inspect
from inspect import _empty, signature
import collections
import os
from enum import Enum, unique
import sys
import linecache
import math
import shlex
import struct
import platform
import subprocess
import numpy as np
import re
from pydoc import locate
import datetime
import time
import types

__all__ = ['get_session','get_trident_dir','epsilon','set_epsilon','floatx','set_floatx','if_else','camel2snake','snake2camel','to_onehot','to_list','addindent','format_time', 'get_time_suffix', 'get_function', 'get_class', 'get_terminal_size', 'gcd', 'get_divisors', 'isprime', 'next_prime', 'prev_prime', 'nearest_prime','PrintException','unpack_singleton','enforce_singleton','OrderedDict','get_python_function_arguments','map_function_arguments','ClassfierType','PaddingMode','make_dir_if_need','ShortcutMode']

if 'TRIDENT_HOME' in os.environ:
    _trident_dir = os.environ.get('TRIDENT_HOME')
    if not os.path.exists(_trident_dir):
        try:
            os.makedirs(_trident_dir)
        except OSError:
            # Except permission denied and potential race conditions
            # in multi-threaded environments.
            pass
else:
    _trident_base_dir = os.path.expanduser('~')
    if not os.access(_trident_base_dir, os.W_OK):
        _trident_base_dir = '/tmp'
    _trident_dir = os.path.join(_trident_base_dir, '.trident')


_SESSION = threading.local()

_SESSION.trident_dir=_trident_dir


from enum import Enum, unique

@unique
class Backend(Enum):
    cntk = 'cntk'
    pytorch = 'pytorch'
    tensorflow = 'tensorflow'

@unique
class IntevalUnit(Enum):
    batch = 'batch'
    epoch = 'epoch'
    once = 'once'



np.set_printoptions(formatter={'float_kind':lambda x: '{0:.4e}'.format(x)})




def get_plateform():
    return platform.system()

def _is_c_contiguous(data):
    while isinstance(data, list):
        data = data[0]
    return data.flags.c_contiguous


def get_session():
    return _SESSION

def get_trident_dir():
    return _trident_dir

_SESSION.floatx='float32'
_SESSION.epsilon= 1e-8
# the type of float to use throughout the session.

_SESSION.backend='pytorch'
_SESSION.image_data_format='channels_first'
_SESSION.image_channel_order='bgr'



def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

def epsilon():
    """Returns the value of the fuzz factor used in numeric expressions.

    # Returns
        A float.

    # Example
    ```python
        >>> trident.get_backend.epsilon()
        1e-07
    ```
    """
    return _SESSION.epsilon


def set_epsilon(e):

    _SESSION.epsilon = float(e)


def floatx():
    """Returns the default float type, as a string.
    (e.g. 'float16', 'float32', 'float64').

    # Returns
        String, the current default float type.

    # Example
    ```python
        >>> trident.get_backend.floatx()
        'float32'
    ```
    """
    return _SESSION.floatx


def set_floatx(floatx):

    if floatx not in {'float16', 'float32', 'float64'}:
        raise ValueError('Unknown floatx type: ' + str(floatx))
    _SESSION.floatx = str(floatx)


def camel2snake(name):
    if name is None:
        return None
    else:
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake2camel(name):
    if name is None:
        return None
    else:
        return ''.join(x.capitalize() or '_' for x in name.split('_'))


def to_onehot(label,classes):
    onehot=np.zeros(classes)
    onehot[label]=1
    return onehot

def to_list(x):
    """Normalizes a list/tensor into a list.
    If a tensor is passed, we return
    a list of size 1 containing the tensor.
    # Arguments
        x: target object to be normalized.
        allow_tuple: If False and x is a tuple,
            it will be converted into a list
            with a single element (the tuple).
            Else converts the tuple to a list.
    # Returns
        A list.
    """
    if isinstance(x, list):
        return x
    elif isinstance(x, tuple):
        return [x[i] for i in range(len(x))]
    elif isinstance(x,np.ndarray):
        return x.tolist()
    elif isinstance(x,(int,float)):
        return [x]
    elif isinstance(x,type({}.keys())):
        return list(x)
    elif isinstance(x,type({}.values())):
        return list(x)
    elif isinstance(x,types.GeneratorType):
        return list(x)
    elif hasattr(x, 'tolist'):
        return x.tolist()
    else:
        try:
            return list(x)
        except:
            return x.tolist()



def if_else(a,b):
    if a is None:
        return b
    else:
        return a


def unpack_singleton(x):
    """Gets the first element if the iterable has only one value.
    Otherwise return the iterable.
    # Argument
        x: A list or tuple.
    # Returns
        The same iterable or the first element.
    """
    if len(x) == 1:
        return x[0]
    return x

def enforce_singleton(x):
    """Gets the first element if the iterable has only one value.
    Otherwise return the iterable.
    # Argument
        x: A list or tuple.
    # Returns
        The same iterable or the first element.
    """
    if hasattr(x,'__len__'):
        return x[0]
    return x


def check_for_unexpected_keys(name, input_dict, expected_values):
    unknown = set(input_dict.keys()).difference(expected_values)
    if unknown:
        raise ValueError('Unknown entries in {} dictionary: {}. Only expected following keys: {}'.format(name, list(unknown),expected_values))

def addindent(s_, numSpaces):
    s = s_.split('\n')
    # don't do anything for single-line stuff
    if len(s) == 1:
        return s_
    first = s.pop(0)
    s = [(numSpaces * ' ') + line for line in s]
    s = '\n'.join(s)
    s = first + '\n' + s
    return s


def format_time(seconds):
    days = int(seconds / 3600/24)
    seconds = seconds - days*3600*24
    hours = int(seconds / 3600)
    seconds = seconds - hours*3600
    minutes = int(seconds / 60)
    seconds = seconds - minutes*60
    secondsf = int(seconds)
    seconds = seconds - secondsf
    millis = int(seconds*1000)

    f = ''
    i = 1
    if days > 0:
        f += str(days) + 'D'
        i += 1
    if hours > 0 and i <= 2:
        f += str(hours) + 'h'
        i += 1
    if minutes > 0 and i <= 2:
        f += str(minutes) + 'm'
        i += 1
    if secondsf > 0 and i <= 2:
        f += str(secondsf) + 's'
        i += 1
    if millis > 0 and i <= 2:
        f += str(millis) + 'ms'
        i += 1
    if f == '':
        f = '0ms'
    return f


def get_time_suffix():
    prefix = str(datetime.datetime.fromtimestamp(time.time())).replace(' ', '').replace(':', '').replace('-','').replace( '.', '')
    return prefix

def get_function(fn_or_name,module_paths= None):
    if callable(fn_or_name):
        return fn_or_name
    fn = locate(fn_or_name)
    if (fn is None) and (module_paths is not None):
        for module_path in module_paths:
            fn = locate('.'.join([module_path, fn_or_name]))
            if fn is not None:
                break
    if fn is None:
        raise ValueError( "Method not found in {}: {}".format(module_paths, fn_or_name))
    return fn  # type: ignore

def get_class(class_name, module_paths = None) :
    r"""Returns the class based on class name.
    Args:
        class_name (str): Name or full path to the class.
        module_paths (list): Paths to candidate modules to search for the
            class. This is used if the class cannot be located solely based on
            ``class_name``. The first module in the list that contains the class
            is used.
    Returns:
        The target class.

    Raises:
        ValueError: If class is not found based on :attr:`class_name` and
            :attr:`module_paths`.

    """
    class_ = locate(class_name)
    if (class_ is None) and (module_paths is not None):
        for module_path in module_paths:
            class_ = locate('.'.join([module_path, class_name]))
            if class_ is not None:
                break
    if class_ is None:
        raise ValueError(
            "Class not found in {}: {}".format(module_paths, class_name))
    return class_  # type: ignore


def get_terminal_size():
    """ getTerminalSize()
     - get width and height of console
     - works on linux,os x,windows,cygwin(windows)
     originally retrieved from:
     http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
    """
    current_os = platform.system()
    tuple_xy = None
    if current_os == 'Windows':
        tuple_xy = _get_terminal_size_windows()
        if tuple_xy is None:
            tuple_xy = _get_terminal_size_tput()  # needed for window's python in cygwin's xterm!
    if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
        tuple_xy = _get_terminal_size_linux()
    if tuple_xy is None:
        tuple_xy = (80, 25)  # default value
    return tuple_xy


def _get_terminal_size_windows():
    try:
        from ctypes import windll, create_string_buffer
        # stdin handle is -10
        # stdout handle is -11
        # stderr handle is -12
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res and res!=0:
            (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh",
                                                                                                  csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
        else:
            import tkinter as tk
            root = tk.Tk()
            sizex,sizey=root.winfo_screenwidth() // 8, root.winfo_screenheight() // 8
            root.destroy()
            return sizex,sizey
    except Exception as e:
        print(e)
        pass


def _get_terminal_size_tput():
    # get terminal width
    # src: http://stackoverflow.com/questions/263890/how-do-i-find-the-width-height-of-a-terminal-window
    try:
        cols = int(subprocess.check_call(shlex.split('tput cols')))
        rows = int(subprocess.check_call(shlex.split('tput lines')))
        return (cols, rows)
    except:
        pass


def _get_terminal_size_linux():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            return cr
        except:
            pass

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            return None
    return int(cr[1]), int(cr[0])


def gcd(x, y):
    gcds = []
    gcd = 1
    if x % y == 0:
        gcds.append(int(y))
    for k in range(int(y // 2)+1, 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            gcds.append(int(k))
    return gcds


def get_divisors(n):
    return [d for d in range(2, n // 2+1) if n % d == 0]


def isprime(n):
    if n>=9:
        divisors = [d for d in range(2, int(math.sqrt(n))) if n % d == 0]
        return all(n % od != 0 for od in divisors if od != n)
    elif n in [1,2,3,5,7]:
        return True
    else:
        return False

def next_prime(n):
    pos=n+1
    while True:
        if isprime(pos):
            return pos
        pos+=1


def prev_prime(n):
    pos=n-1
    while True:
        if  isprime(pos):
            return pos
        pos-=1


def nearest_prime(n):
    nextp=next_prime(n)
    prevp=prev_prime(n)
    if abs(nextp-n)<abs(prevp-n):
        return nextp
    else:
        return nextp




def get_python_function_arguments(f):
    '''
    Helper to get the parameter names and annotations of a Python function.
    '''
    # Note that we only return non-optional arguments (we assume that any optional args are not specified).
    # This allows to, e.g., accept max(a, b, *more, name='') as a binary function
    import sys
    param_specs = inspect.getfullargspec(f)
    annotations = param_specs.annotations
    arg_names = param_specs.args
    defaults = param_specs.defaults # "if this tuple has n elements, they correspond to the last n elements listed in args"
    if defaults:
        arg_names = arg_names[:-len(defaults)] # we allow Function(functions with default arguments), but those args will always have default values since CNTK Functions do not support this
    return (arg_names, annotations)



def map_function_arguments(params, params_dict, *args, **kwargs):
    '''
    Helper to determine the argument map for use with various call operations.
    Returns a dictionary from parameters to whatever arguments are passed.
    Accepted are both positional and keyword arguments.
    This mimics Python's argument interpretation, except that keyword arguments are not optional.
    This does not require the arguments to be Variables or Functions. It is also called by train_minibatch() and @Signature.
    '''
    # start with positional arguments
    arg_map = dict(zip(params, args))

    # now look up keyword arguments
    if len(kwargs) != 0:
        for name, arg in kwargs.items():  # keyword args are matched by name
            if name not in params_dict:
                raise TypeError("got an unexpected keyword argument '%s'" % name)
            param = params_dict[name]
            if param in arg_map:
                raise SyntaxError("got multiple values for argument '%s'" % name)
            arg_map[param] = arg # add kw argument to dict
    assert len(arg_map) == len(params)

    return arg_map



# def map_if_possible(obj_to_map, *args, **kwargs):
#     if inspect.isfunction(obj_to_map):

def make_dir_if_need(path):
    path=os.path.normpath(path)
    folder,file=os.path.split(path)
    if folder=='':
        folder, file = os.path.split(file)
    if '.' not in file and len(file)>=1:
        folder=os.path.join(folder,file)
        file=''
    if len(folder)>0 and not os.path.exists(folder):
        try:
            os.makedirs(folder)
        except Exception as e:
            PrintException()
            sys.stderr.write('folder:{0} is not valid path'.format(folder))
    return os.path.join(folder,file)


class OrderedDict(collections.OrderedDict):
    def __init__(self):
        super(OrderedDict,self).__init__()

    @property
    def key_list(self):
        return list(super().keys())

    def keys(self):
        return super().keys()

    @property
    def value_list(self):
        return list(super().values())
    def values(self):
        return super().values()

    @property
    def item_list(self):
        return list(super().items())
    def items(self):
        return super().items()


class ClassfierType(Enum):
    dense = 'dense'
    global_avgpool = 'global_avgpool'
    centroid='centroid'


class PaddingMode(Enum):
    zero = 'constant'
    reflection = 'reflect'
    replicate='replicate'
    circular='circular'



class Color(Enum):
    rgb = 'rgb'
    bgr = 'bgr'
    gray='gray'
    rgba='rgba'



class ShortcutMode(Enum):
    add = 'add'
    dot = 'dot'
    concate='concate'



def get_argument_maps(self, default_map, func):
    r"""Extracts the signature of the `func`. Then it returns the list of arguments that
    are present in the object and need to be mapped and passed to the `func` when calling it.
    Args:
        default_map (dict): The keys of this dictionary override the function signature.
        func (function): Function whose argument map is to be generated.
    Returns:
        List of arguments that need to be fed into the function. It contains all the positional
        arguments and keyword arguments that are stored in the object. If any of the required
        arguments are not present an error is thrown.
    """
    sig = signature(func)
    arg_map = {}
    for sig_param in sig.parameters.values():
        arg = sig_param.name
        arg_name = arg
        if arg in default_map:
            arg_name = default_map[arg]
        if sig_param.default is not _empty:
            if arg_name in self.__dict__:
                arg_map.update({arg: arg_name})
        else:
            if arg_name not in self.__dict__ and arg != "kwargs" and arg != "args":
                raise Exception("Argument : {} not present.".format(arg_name))
            else:
                arg_map.update({arg: arg_name})
    return arg_map







