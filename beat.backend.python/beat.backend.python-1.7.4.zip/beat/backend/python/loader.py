#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

###################################################################################
#                                                                                 #
# Copyright (c) 2019 Idiap Research Institute, http://www.idiap.ch/               #
# Contact: beat.support@idiap.ch                                                  #
#                                                                                 #
# Redistribution and use in source and binary forms, with or without              #
# modification, are permitted provided that the following conditions are met:     #
#                                                                                 #
# 1. Redistributions of source code must retain the above copyright notice, this  #
# list of conditions and the following disclaimer.                                #
#                                                                                 #
# 2. Redistributions in binary form must reproduce the above copyright notice,    #
# this list of conditions and the following disclaimer in the documentation       #
# and/or other materials provided with the distribution.                          #
#                                                                                 #
# 3. Neither the name of the copyright holder nor the names of its contributors   #
# may be used to endorse or promote products derived from this software without   #
# specific prior written permission.                                              #
#                                                                                 #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND #
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED   #
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE          #
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE    #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL      #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR      #
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER      #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,   #
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE   #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.            #
#                                                                                 #
###################################################################################


"""
======
loader
======

This modules implements a simple loader for Python code as well as safe
executor. Safe in this context means that if the method raises an
exception, it will catch it and return in a suitable form to the caller.
"""

import sys
import six
import imp


# ----------------------------------------------------------


def load_module(name, path, uses):
    """Loads the Python file as module, returns  a proper Python module


    Parameters:

      name (str): The name of the Python module to create. Must be a valid
        Python symbol name

      path (str): The full path of the Python file to load the module contents
        from

      uses (dict): A mapping which indicates the name of the library to load
        (as a module for the current library) and the full-path and use
        mappings of such modules.


    Returns:

      :std:term:`module`: A valid Python module you can use in an Algorithm or
          Library.
    """

    retval = imp.new_module(name)

    # loads used modules
    for k, v in uses.items():
        retval.__dict__[k] = load_module(k, v['path'], v['uses'])

    # execute the module code on the context of previously import modules
    exec(compile(open(path, "rb").read(), path, 'exec'), retval.__dict__)

    return retval


# ----------------------------------------------------------


def run(obj, method, exc=None, *args, **kwargs):
    """Runs a method on the object and protects its execution

    In case an exception is raised, it is caught and transformed into the
    exception class the user passed.

    Parameters:

      obj (object): The python object in which execute the method

      method (str): The method name to execute on the object

      exc (:std:term:`class`, Optional): The class to use as base exception
        when translating the exception from the user code. If you set it to
        ``None``, then just re-throws the user raised exception.

      *args: Arguments to the object method, passed unchanged

      **kwargs: Arguments to the object method, passed unchanged

    Returns:

      object: whatever ``obj.method()`` is bound to return.

    """

    try:
        if method == '__new__':
            return obj(*args, **kwargs)

        return getattr(obj, method)(*args, **kwargs)
    except Exception:
        if exc is not None:
            type, value, traceback = sys.exc_info()
            six.reraise(exc, exc(value), traceback)
        else:
            raise  # just re-raise the user exception
