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
import cffi

from .lib_h import LIB_H
from .util import find_hyper_api_dll


ffi = cffi.FFI()
ffi.cdef(LIB_H)
# ffi does not support unions, so we fake hyper_error_field_value
ffi.cdef('''
    typedef struct {
        int discriminator;
        void *value;
    } py_hyper_error_field_value;
    hyper_error_t* hyper_error_get_field(
        const hyper_error_t* error, hyper_error_field_key key, py_hyper_error_field_value* value);
    hyper_error_t* hyper_error_set_field(
        hyper_error_t* error, hyper_error_field_key field, py_hyper_error_field_value value);
''')
# define a struct with correct layout for INTERVAL
ffi.cdef('''
    typedef struct {
        int64_t microseconds;
        int32_t days;
        int32_t months;
    } py_interval;
''')
lib = ffi.dlopen(str(find_hyper_api_dll()))
