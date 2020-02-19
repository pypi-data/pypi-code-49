import numpy as np
import os
import shutil
import sys

def path(string):
    platform = sys.platform.lower()
    if 'linux' in platform:
        return string.replace('\\','/')
    elif 'win' in platform:
        return string.replace('/','\\')
    else:
        return string


def broadcast(func):
    '''
        example:
        @broadcast
        def f(x):
            # A function that can map only a single element
            if x==1 or x==0:
                return x
            else:
                return f(x-1)+f(x-2)
            
        >> f([2,4,10])
        >> array([1, 3, 832040], dtype=object)
    '''
    def wrap(*args, **kwargs):
        '''
        Takes an arbitrary Python function and returns a NumPy ufunc
        Can be used, for example, to add broadcasting to a built-in Python function
        return: only one out, 
        type:numpy object

        '''
        nin, nout = len(args)+len(kwargs), 1
        return np.frompyfunc(func,nin, nout)(*args, **kwargs)
    return wrap

# :Enables the dictionary to be dot operated
class _Dict_enhance(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self 

def dict_dotable(dic):
    '''
    : input: a dictionary
    : output: an enhanced dictionary
    Example:
        enhance_dic = dict_dotable(dic)
    then, you can operate an enhanced dictionary like this:
        enhance_dic.key1.key2. ...
    '''
    dic = _Dict_enhance(dic)
    for i in dic:
        if type(dic[i]) == dict:
            dic[i] = dict_dotable(dic[i])
    return dic

# define a constant like C language.
class Cons:
    '''
    `object.__setattr__(self, name, value)`
    this built-in function will called when assigning values to properties of the class
    
    `object.__dict__` holds all writable attributes in object, 
    key as variable name and value as variable value.
    '''
    def __setattr__(self, name,value):
        if hasattr(self,name):
            raise ValueError('Constant value can\'t be changed')
        else:
            self.__dict__[name] = value

def rm(path):
    '''remove path
    '''
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        else:
            print(f'{path} is  illegal !')

def index_char(L=1000):
    '''
    Get the index of all characters.
    use chr() 
    '''
    index_token = {}
    token = []
    for i in range(L):
        character = chr(i)
        index_token[i] = character
        token.append(character)
    token_index=dict(zip(token, range(L))) # token_index[idx] is equal to ord(idx)
    return index_token, token_index

