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
==========
baseformat
==========

Base type for all data formats
"""

import struct
import numpy
import six

# This table defines what is the binary format for each supported basic type
BINCODE = {
        numpy.dtype('int8'): 'b', #signed char
        numpy.dtype('int16'): 'h', #signed short
        numpy.dtype('int32'): 'i', #signed int
        numpy.dtype('int64'): 'q', #signed long long
        numpy.dtype('uint8'): 'B', #unsigned char
        numpy.dtype('uint16'): 'H', #unsigned short
        numpy.dtype('uint32'): 'I', #unsigned int
        numpy.dtype('uint64'): 'Q', #unsigned long long
        numpy.dtype('float32'): 'f', #a single float
        numpy.dtype('float64'): 'd', #a single double
        numpy.dtype('complex64'): 'f', #two floats (real, imag)
        numpy.dtype('complex128'): 'd', #two doubles (real, imag)
        numpy.dtype('bool'): '?', #C99 Bool_
        }

ENDIANNESS = '<' #little-endian
SIZE = 'Q' #64-bit unsigned
STRING = ENDIANNESS + SIZE + '%ds'

def setup_scalar(formatname, attrname, dtype, value, casting, add_defaults):
    """Casts the value to the the scalar type defined by dtype

    Parameters:

      formatname (str): The name of this dataformat (e.g. ``user/format/1``).
        This value is only used for informational purposes

      attrname (str): The name of this attribute (e.g. ``value``). This value
        is only used for informational purposes

      dtype (numpy.dtype): The datatype of every element on the array

      value (:std:term:`file object`, Optional): A representation of the value.
        This object will be cast into a scalar with the dtype defined by the
        ``dtype`` parameter.

      casting (str): See :py:func:`numpy.can_cast` for a description of
        possible values for this field.

      add_defaults (bool): If we should use defaults for missing attributes. In
        case this value is set to ``True``, missing attributes are set with
        defaults, otherwise, a :py:exc:`TypeError` is raise if a missing
        attribute is found.

    Returns:

      object: the scalar or its default representation, if no value is set.

    """

    if hasattr(dtype, 'type') and issubclass(dtype.type, numpy.generic):

        if value is None:  # use the default for the type
            return dtype.type()
        else:
            if value: #  zero is classified as int64 which can't be safely casted to uint64
                if not numpy.can_cast(numpy.array(value).dtype, dtype, casting=casting):
                    raise TypeError("cannot safely cast attribute `%s' on dataformat " \
                            "`%s' with type `%s' to `%s' without precision loss" % \
                            (attrname, formatname, numpy.array(value).dtype, dtype))
            return dtype.type(value)

    elif issubclass(dtype, str):  # it is a string
        if value is None:
            return str()
        else:
            return str(value)

    else:  # it is a dataformat
        return dtype().from_dict(value, casting=casting, add_defaults=add_defaults)

class _protected_str_ndarray(numpy.ndarray):
    """Increments :py:class:`numpy.ndarray` so that item assignment is checked
    """

    def __setitem__(self, key, value):
        """First checks for conformance and then assigns"""
        if not isinstance(value, six.string_types):
            raise TypeError("string array requires string objects for " \
                    "items but you passed `%s' (%s) while setting element " \
                    "%s" % (value, type(value), key))
        return numpy.ndarray.__setitem__(self, key, value)


class _protected_ndarray(numpy.ndarray):
    """Increments :py:class:`numpy.ndarray` so that item assignment is checked
    """

    def __setitem__(self, key, value):
        """First checks for conformance and then assigns"""
        value_ = self._format_dtype()
        value_.from_dict(
                value,
                casting=self._format_casting,
                add_defaults=self._format_add_defaults,
                )
        return numpy.ndarray.__setitem__(self, key, value_)

def setup_array(formatname, attrname, shape, dtype, value, casting,
        add_defaults):
    """Casts the value to the the array type defined by (shape, dtype)


    Parameters:

      formatname (str): The name of this dataformat (e.g. ``user/format/1``).
        This value is only used for informational purposes

      attrname (str): The name of this attribute (e.g. ``value``). This value
        is only used for informational purposes

      shape (:py:class:`tuple`): The shape of the array

      dtype (numpy.dtype): The datatype of every element on the array

      value (:std:term:`file object`, Optional): A representation of the value.
        This object will be cast into a numpy array with the dtype defined by
        the ``dtype`` parameter.

      casting (str): See :py:func:`numpy.can_cast` for a description of
        possible values for this field.

      add_defaults (bool): If we should use defaults for missing attributes. In
        case this value is set to ``True``, missing attributes are set with
        defaults, otherwise, a :py:exc:`TypeError` is raise if a missing
        attribute is found.


    Returns:

      :py:class:`numpy.ndarray`: with the adequate dimensions. If a
        ``value`` is set, validates that value and returns it as a new
        :py:class:`numpy.ndarray`.

    """

    def is_empty(x):
        if isinstance(x, (numpy.ndarray,)): return not x.size
        return not x

    if is_empty(value):
        # creates an empty array that remains unchecked

        if hasattr(dtype, 'type') and issubclass(dtype.type, numpy.generic):
            retval = numpy.ndarray(shape, dtype=dtype)
        elif issubclass(dtype, str): #it is a string
            retval = numpy.ndarray(shape, dtype=object).view(_protected_str_ndarray)
            retval[~retval.astype(bool)] = ''
        else: #it is a dataformat
            retval = numpy.ndarray(shape, dtype=object).view(_protected_ndarray)
            retval._format_dtype = dtype
            retval._format_casting = 'safe'
            retval._format_add_defaults = True

    else:
        if hasattr(dtype, 'type'):
            retval = numpy.array(value, dtype=dtype)
        else:
            retval = numpy.array(value) #blindly converts data

    if retval.ndim != len(shape):
        raise TypeError("input argument for array attribute `%s' on " \
                "dataformat `%s' has %d dimensions and does not respect " \
                "what is requested in the data format (%d dimension(s))" % (
                    attrname, formatname, retval.ndim, len(shape),
                    )
                )

    for i, d in enumerate(retval.shape):
        if shape[i] and shape[i] != d:
            raise TypeError("input argument for array attribute `%s' on " \
                    "dataformat `%s' does not respect dimension " \
                    "restrictions for dimension `%d' as requested in the " \
                    "data format (%d != %d)" % (attrname, formatname, i, d, shape[i])
                    )

    if hasattr(dtype, 'type') and issubclass(dtype.type, numpy.generic):
        if not numpy.can_cast(retval.dtype, dtype, casting=casting):
            raise TypeError("cannot safely cast array attribute `%s' " \
                    "on dataformat `%s' with type `%s' to `%s' without precision " \
                    "loss" % (attrname, formatname, retval.dtype, dtype))
        return retval.astype(dtype)

    elif issubclass(dtype, str): #it is a string
        return numpy.array(retval, dtype=object).view(_protected_str_ndarray)

    # it is a dataformat
    def constructor(x):
        """Creates a data format base on the information provided by x"""

        return dtype().from_dict(x, casting=casting, add_defaults=add_defaults)

    retval = numpy.frompyfunc(constructor, 1, 1)(retval).view(_protected_ndarray)
    retval._format_dtype = dtype
    retval._format_casting = 'safe'
    retval._format_add_defaults = True
    return retval

def pack_array(dtype, value, fd):
    """Binary-encodes the array at ``value`` into the file descriptor ``fd``

    Parameters:

      dtype (numpy.dtype): The datatype of the array (taken from the format
        descriptor)

      value (:std:term:`file object`, Optional): The :py:class:`numpy.ndarray`
        representing the value to be encoded

      fd (:std:term:`file object`): The file where to encode the input

    """

    # prefix array with its shape
    shape_format = ENDIANNESS + str(len(value.shape)) + SIZE
    fd.write(struct.pack(shape_format, *value.shape))

    if hasattr(dtype, 'type') and issubclass(dtype.type, numpy.generic):

        # N.B.: this bit of code is optimized to reduce memory usage
        # if it is not C-style (row order) and memory contiguous, make a copy
        value = numpy.require(value, requirements='C')  # C_CONTIGUOUS
        # makes sure endianness is respected, will copy otherwise
        value = value.astype(ENDIANNESS + value.dtype.str[1:], copy=False)
        fd.write(value.tostring())

    elif issubclass(dtype, str):  # it is a string
        for item in value.flat:
            encoded = item.encode('utf-8')
            length = len(encoded)
            fd.write(struct.pack(STRING % length, length, encoded))

    else:  # it is a dataformat
        for o in value.flat:
            o.pack_into(fd)


def pack_scalar(dtype, value, fd):
    """Binary-encodes the scalar at ``value`` into the file descriptor ``fd``

    Parameters:

      dtype (numpy.dtype): The datatype of the scalar (taken from the format
        descriptor)

      value (:std:term:`object`, Optional): An object representing the value to
        be encoded

      fd (:std:term:`file object`): The file where to encode the input

    """

    if hasattr(dtype, 'type') and issubclass(dtype.type, numpy.generic):
        if issubclass(dtype.type, numpy.complexfloating):
            fd.write(struct.pack(ENDIANNESS + '2' + BINCODE[dtype],
                value.real, value.imag))
        else:
            fd.write(struct.pack(ENDIANNESS + BINCODE[dtype], value))

    elif issubclass(dtype, str):  # it is a string
        encoded = value.encode('utf-8')
        length = len(encoded)
        fd.write(struct.pack(STRING % length, length, encoded))

    else:  # it is a dataformat
        value.pack_into(fd)


def read_some(format, fd):
    """Reads some of the data from the file descriptor ``fd``"""
    return struct.unpack(format, fd.read(struct.calcsize(format)))


def read_string(fd):
    """Reads the next string from the file descriptor ``fd``"""
    string_format = '%ds' % read_some(ENDIANNESS + SIZE, fd)
    retval = read_some(string_format, fd)
    if not isinstance(retval[0], str):
        return (retval[0].decode('utf8'),)
    return retval


def unpack_array(shape, dtype, fd):
    """Unpacks the following data array.

    Returns the unpacked array as a :py:class:`numpy.ndarray` object. No checks
    are performed by this function as we believe that the binary stream matches
    perfectly the data type.

    Parameters:

      shape (:py:class:`tuple`): The shape of the array

      dtype (numpy.dtype): The datatype of every element on the array

      fd (:std:term:`file object`): The file where to encode the input

    Returns:

      :py:class:`numpy.ndarray`: advances readout of ``fd``.

    """

    # reads the actual array shape: remember, the declaration may have zeros
    shape_ = read_some(ENDIANNESS + str(len(shape)) + 'Q', fd)

    if hasattr(dtype, 'type') and issubclass(dtype.type, numpy.generic):
        # N.B.: this bit of code is optimized to reduce memory usage
        data_format = ENDIANNESS + dtype.str[1:]
        count = numpy.prod(shape_)
        to_read = numpy.asscalar(dtype.itemsize*count)
        a = numpy.fromstring(fd.read(to_read), dtype=data_format, count=count)
        return a.reshape(shape_)

    elif issubclass(dtype, str):  # it is a string
        a = [read_string(fd) for k in six.moves.range(numpy.prod(shape_))]
        return numpy.array(a).reshape(shape_)

    else:  # it is a dataformat
        a = []
        for k in six.moves.range(numpy.prod(shape_)):
            a_ = dtype()
            a_.unpack_from(fd)
            a.append(a_)
        return numpy.array(a).reshape(shape_)


def unpack_scalar(dtype, fd):
    """Unpacks the following scalar.

    Returns the unpacked scalar. No checks are performed by this function as we
    believe that the binary stream matches perfectly the data type.

    Parameters:

      dtype (numpy.dtype): The datatype of every element on the array

      fd (:std:term:`file object`): The file where to encode the input

    Returns:

      object: which among other options, can be a numpy scalar (``int8``,
        ``float32``, ``bool_``, etc) or a string (``str``). Advances readout of
        ``fd``.

    """

    if hasattr(dtype, 'type') and issubclass(dtype.type, numpy.generic):

        if issubclass(dtype.type, numpy.complexfloating):  # complex
            data_format = ENDIANNESS + '2' + BINCODE[dtype]
            a = read_some(data_format, fd)
            return dtype.type(complex(a[0], a[1]))

        else:
            data_format = ENDIANNESS + BINCODE[dtype]
            a = read_some(data_format, fd)
            return dtype.type(a[0])

    elif issubclass(dtype, str):  # it is a string
        return read_string(fd)[0]

    else:  # it is a dataformat
        a = dtype()
        a.unpack_from(fd)
        return a


class baseformat(object):
    """All dataformats are represented, in Python, by a derived class of this one

    Construction is, by default, set to using a unsafe data type conversion.
    For an 'safe' converter, use :py:meth:`baseformat.from_dict`, where you
    can, optionally, set the casting style (see :py:func:`numpy.can_cast` for
    details on the values this parameter can assume).

    Parameters part of the declared type which are not set, are filled in with
    defaults. Similarly to the ``casting`` parameter, use
    :py:meth:`baseformat.from_dict` to be able to adjust this behaviour.
    """

    def __init__(self, **kwargs):

        self.from_dict(kwargs, casting='unsafe', add_defaults=True)

    def from_dict(self, data, casting='safe', add_defaults=False):
        """Same as initializing the object, but with a less strict type casting

        Construction is, by default, set to using a **unsafe** data type
        conversion. See :py:func:`numpy.can_cast` for details on the values
        this parameter can assume).

        Parameters:

          data (:py:class:`dict`, Optional): A dictionary representing the data
            input, matching the keywords defined at the resolved format. A
            value of ``None``, if passed, effectively results in the same as
            passing an empty dictionary ``{}``.

          casting (str): See :py:func:`numpy.can_cast` for a description of
            possible values for this field. By default, it is set to
            ``'safe'``.
            Use the constructor to get a default ``'unsafe'`` behaviour.

          add_defaults (bool): If we should use defaults for missing
            attributes. Incase this value is set to `True`, missing attributes
            are set with defaults, otherwise, a :py:exc:`TypeError` is raise if
            a missing attribute is found.

        """

        if data is None: data = {}

        user_attributes = set([k for k in data.keys() if k != "__type__"])
        declared_attributes = set(self._format.keys())

        if not add_defaults:
            # in this case, the user must provide all attributes
            if user_attributes != declared_attributes:
                undeclared_attributes = declared_attributes - user_attributes
                raise AttributeError("missing attributes (%s) for dataformat " \
                        "`%s' which require `%s'" % (
                            ', '.join(undeclared_attributes),
                            self._name,
                            ', '.join(declared_attributes),
                            ),
                        )
            iterate_attributes = user_attributes

        else:  # then, the user passed attributes must be a subset
            if not user_attributes.issubset(declared_attributes):
                unknown_attributes = user_attributes - declared_attributes
                raise AttributeError("unexpected attribute (%s) for dataformat " \
                        "`%s' which require `%s'" % (
                            ', '.join(unknown_attributes),
                            self._name,
                            ', '.join(declared_attributes),
                            ),
                        )
            iterate_attributes = declared_attributes

        for k in iterate_attributes:
            self._setattr(k, data.get(k), casting, add_defaults)

        return self

    def as_dict(self):
        """Returns the data in a dictionary representations"""

        retval = dict()

        for key in self._format:

            v = getattr(self, key)

            if isinstance(self._format[key], list):
                dtype = getattr(self.__class__, key)[-1]
                if (hasattr(dtype, 'type') and issubclass(dtype.type, numpy.generic)) \
                        or dtype is str:
                    retval[key] = v
                else:  # it is an array of dataformat objects
                    retval[key] = numpy.frompyfunc(lambda x: x.as_dict(), 1, 1)(v)
                retval[key] = retval[key].tolist()

            else:
                retval[key] = v if not hasattr(v, 'as_dict') else v.as_dict()

        return retval

    def pack_into(self, fd):
        """Creates a binary representation of this object into a file.

        This method will make the object pickle itself on the file descritor
        ``fd``. If you'd like to write the contents of this file into a string,
        use the :py:data:`six.BytesIO`.
        """

        for key in sorted(self._format.keys()):
            dtype = getattr(self.__class__, key)
            value = getattr(self, key)
            if isinstance(dtype, list): pack_array(dtype[-1], value, fd)
            else: pack_scalar(dtype, value, fd)

    def pack(self):
        """Creates a binary representation of this object as a string
        representation. It uses, :py:meth:`baseformat.pack_into` to encode the
        string.
        """

        fd = six.BytesIO()
        self.pack_into(fd)
        retval = fd.getvalue()
        fd.close()
        return retval

    def unpack_from(self, fd):
        """Loads a binary representation of this object

        We don't run any extra checks as an unpack operation is only supposed
        to be carried out once the type compatibility has been established.
        """

        for key in sorted(self._format.keys()):

            # get the data type for this object
            dtype = getattr(self.__class__, key)

            if isinstance(dtype, list):
                value = unpack_array(dtype[:-1], dtype[-1], fd)
            else:
                value = unpack_scalar(dtype, fd)

            object.__setattr__(self, key, value)

        return self


    def unpack(self, s):
        """Loads a binary representation of this object from a string

        Effectively, this method just calls :py:meth:`baseformat.unpack_from`
        with a :py:data:`six.BytesIO` wrapped around the input string.
        """

        return self.unpack_from(six.BytesIO(s))


    def isclose(self, other, *args, **kwargs):
        """Tests for closeness in the numerical sense.

        Values such as integers, booleans and strings are checked for an
        **exact** match. Parameters with floating-point components such as
        32-bit floats and complex values should be close enough given the input
        parameterization.

        Parameters for floating-point checks are those for
        :py:func:`numpy.isclose`. Check its help page for more details.

        Returns:

          bool: indicates if the other object is close enough to this one.

        """

        if not isinstance(other, self.__class__): return False

        for key in sorted(self._format.keys()):

            # get the data type for this object
            dtype = getattr(self.__class__, key)
            this = getattr(self, key)
            that = getattr(other, key)

            if isinstance(dtype, list):
                dtype = dtype[-1]
                if hasattr(dtype, 'type'):  # numpy array
                    # note: avoid numpy.all(numpy.isclose()) for arrays
                    # see bug https://github.com/numpy/numpy/issues/2280
                    if not numpy.allclose(this, that, *args, **kwargs):
                        return False
                elif issubclass(dtype, six.string_types):  # simple string
                    if not numpy.all(this == that): return False
                else: #baseformat
                    isclose = numpy.frompyfunc(lambda x,y: x.isclose(y, *args, **kwargs), 2, 1)
                    if not numpy.all(isclose(this, that)): return False

            else:
                if hasattr(dtype, 'type'):  # numpy scalar
                    if not numpy.isclose(this, that, *args, **kwargs): return False
                elif issubclass(dtype, six.string_types):  # simple string
                    if this != that: return False
                else:  # baseformat
                    if not this.isclose(that, *args, **kwargs): return False

        # if you survived to this point, the objects are close
        return True

    def __str__(self):
        """Stringified representation for this object, uses :py:meth:`as_dict`.
        """

        return str(self.as_dict())

    def copy(self):
        """Returns a copy of itself, completely independent"""

        return self.__class__(**self.as_dict())

    def _setattr(self, key, value, casting, add_defaults):
        """Set an attribute, with validation"""

        dtype = getattr(self.__class__, key)
        if isinstance(dtype, list):
            value = setup_array(self._name, key, dtype[:-1], dtype[-1], value,
                    casting=casting, add_defaults=add_defaults)
        else:
            value = setup_scalar(self._name, key, dtype, value,
                    casting=casting, add_defaults=add_defaults)

        return object.__setattr__(self, key, value)

    def __setattr__(self, key, value):
        """Set an attribute, with validation"""

        return self._setattr(key, value, 'safe', False)
