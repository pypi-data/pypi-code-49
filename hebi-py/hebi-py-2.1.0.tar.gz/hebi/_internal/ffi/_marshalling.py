# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#  HEBI Core python API - Copyright 2018 HEBI Robotics
#  See https://hebi.us/softwarelicense for license details
#
# -----------------------------------------------------------------------------


import math
import numpy as np
import ctypes
from ctypes import (byref, create_string_buffer)

from ..graphics import Color, color_from_int, string_to_color
from .enums import StatusSuccess
from . import ctypes_func_defs as api
from .wrappers import WeakReferenceContainer # TODO: fix import
from .. import type_utils
from ..type_utils import decode_string_buffer as decode_str # TODO: fix import
from ..type_utils import create_string_buffer_compat as create_str # TODO: fix import

from hebi._internal.ffi.ctypes_defs import HebiVector3f, HebiQuaternionf, HebiHighResAngleStruct
from hebi._internal.ffi.ctypes_utils import to_float_ptr, to_double_ptr, cast_to_float_ptr

from numpy.ctypeslib import as_array as _ctypes_to_ndarray


################################################################################
# Pretty Printers
################################################################################


def _fmt_float_array(array):
  return '[' + ', '.join(['{:.2f}'.format(i) for i in array]) + ']'


def _numbered_float_repr(c, enum_type):
  try:
    enum_name = enum_type.name
  except:
    enum_name = enum_type
  desc = 'Numbered float (Enumeration {}):\n'.format(enum_name)
  try:
    container = c._get_ref()
    return desc +\
      '  float1: {}\n'.format(_fmt_float_array(c.float1)) +\
      '  float2: {}\n'.format(_fmt_float_array(c.float2)) +\
      '  float3: {}\n'.format(_fmt_float_array(c.float3)) +\
      '  float4: {}\n'.format(_fmt_float_array(c.float4)) +\
      '  float5: {}\n'.format(_fmt_float_array(c.float5)) +\
      '  float6: {}\n'.format(_fmt_float_array(c.float6)) +\
      '  float7: {}\n'.format(_fmt_float_array(c.float7)) +\
      '  float8: {}\n'.format(_fmt_float_array(c.float8)) +\
      '  float9: {}\n'.format(_fmt_float_array(c.float9))
  except:
    return desc + '  <Group message was finalized>'


def _fmt_io_bank_pin(pins, indent=4):
  indent_str = ''.join([' '] * indent)
  pins_i = pins[0]
  pins_f = pins[1]

  pins_i_str = '[' + ', '.join(['{0:9g}'.format(entry) for entry in pins_i]) + ']'
  pins_f_str = '[' + ', '.join(['{0:9.8g}'.format(entry) for entry in pins_f]) + ']'

  return '{}Int:   {}\n'.format(indent_str, pins_i_str) +\
         '{}Float: {}'.format(indent_str, pins_f_str)


def _io_bank_repr(bank_container, bank, bank_readable):
  try:
    enum_name = bank.name
  except:
    enum_name = bank
  desc = 'IO Bank \'{}\' (Enumeration {}):\n'.format(bank_readable, enum_name)
  try:
    io_container = bank_container._get_ref()
  except:
    # Handles the case where IO Container object was finalized already 
    return desc + "  <IO Container was finalized>"

  # TODO: Maybe replace non-existent pins with `N/A` instead of `nan` or `0`?
  def get_fmt_pin(pin):
    return _fmt_io_bank_pin((io_container.get_int(bank, pin), io_container.get_float(bank, pin)))

  return desc +\
    '  Pin 1:\n{}\n'.format(get_fmt_pin(1)) +\
    '  Pin 2:\n{}\n'.format(get_fmt_pin(2)) +\
    '  Pin 3:\n{}\n'.format(get_fmt_pin(3)) +\
    '  Pin 4:\n{}\n'.format(get_fmt_pin(4)) +\
    '  Pin 5:\n{}\n'.format(get_fmt_pin(5)) +\
    '  Pin 6:\n{}\n'.format(get_fmt_pin(6)) +\
    '  Pin 7:\n{}\n'.format(get_fmt_pin(7)) +\
    '  Pin 8:\n{}\n'.format(get_fmt_pin(8))


def _io_repr(io):
  try:
    container = io._get_ref()
    return 'IO Banks: [A, B, C, D, E, F]\n' +\
      '{}\n'.format(io.a) +\
      '{}\n'.format(io.b) +\
      '{}\n'.format(io.c) +\
      '{}\n'.format(io.d) +\
      '{}\n'.format(io.e) +\
      str(io.f)
  except:
    return 'IO Banks: [A, B, C, D, E, F]\n  <Group message was finalized>'


def _led_repr(led, led_field):
  try:
    enum_name = led_field.name
  except:
    enum_name = led_field
  desc = 'LED (Enumeration {}):\n'.format(enum_name)
  try:
    container = led._get_ref()
    colors = led.color
    return desc + '  [' + ', '.join([repr(color) for color in colors]) + ']'
  except:
    return desc + '  <Group message was finalized>'


################################################################################
# Numbered Fields
################################################################################

################################################################################
# `has` creators
################################################################################


def __create_has_func(refs, bit_index, has):
  size = len(refs)

  def ret_has():
    _tls.ensure_capacity(size)
    output = _tls.c_bool_array
    has(output, refs, size, bit_index)
    return np.array(output[0:size], dtype=bool)
  return ret_has 


def create_float_group_has(refs, field, has, metadata):
  """
  Returns a callable which accepts 0 arguments
  """
  bit_index = metadata.float_field_bitfield_offset_ + int(field)
  return __create_has_func(refs, bit_index, has)


def create_high_res_angle_group_has(refs, field, has, metadata):
  """
  Returns a callable which accepts 0 arguments
  """
  bit_index = metadata.high_res_angle_field_bitfield_offset_ + int(field)
  return __create_has_func(refs, bit_index, has)


def create_vector3f_group_has(refs, field, has, metadata):
  """
  Returns a callable which accepts 0 arguments
  """
  bit_index = metadata.vector3f_field_bitfield_offset_ + int(field)
  return __create_has_func(refs, bit_index, has)


def create_quaternionf_group_has(refs, field, has, metadata):
  """
  Returns a callable which accepts 0 arguments
  """
  bit_index = metadata.quaternionf_field_bitfield_offset_ + int(field)
  return __create_has_func(refs, bit_index, has)


def create_uint64_group_has(refs, field, has, metadata):
  """
  Returns a callable which accepts 0 arguments
  """
  bit_index = metadata.uint64_field_bitfield_offset_ + int(field)
  return __create_has_func(refs, bit_index, has)


def create_enum_group_has(refs, field, has, metadata):
  """
  Returns a callable which accepts 0 arguments
  """
  bit_index = metadata.enum_field_bitfield_offset_ + int(field)
  return __create_has_func(refs, bit_index, has)


def create_bool_group_has(refs, field, has, metadata):
  """
  Returns a callable which accepts 0 arguments
  """
  bit_index = metadata.bool_field_bitfield_offset_ + int(field)
  return __create_has_func(refs, bit_index, has)


def create_numbered_float_group_has(refs, field, has, metadata):
  """
  Returns a callable which accepts 1 argument
  """
  relative_offset = int(metadata.numbered_float_relative_offsets_[int(field)])
  bit_index = metadata.numbered_float_field_bitfield_offset_ + relative_offset
  size = len(refs)

  def ret_has(number):
    _tls.ensure_capacity(size)
    output = _tls.c_bool_array
    has(output, refs, size, bit_index + number)
    return np.array(output[0:size], dtype=bool)
  return ret_has


def create_io_group_has(refs, has):
  """
  Returns a callable which accepts 2 arguments
  """
  size = len(refs)

  def ret_has(field, number):
    _tls.ensure_capacity(size)
    output = _tls.c_bool_array
    has(output, refs, size, number - 1, field)
    return np.array(output[0:size], dtype=bool)
  return ret_has


def create_led_group_has(refs, field, has, metadata):
  """
  Returns a callable which accepts 0 arguments
  """
  bit_index = metadata.led_field_bitfield_offset_ + int(field)
  return __create_has_func(refs, bit_index, has)


################################################################################
# `getter` creators
################################################################################


def create_numbered_float_group_getter(refs, field, getter):
  """
  Returns a callable which accepts 1 argument
  """
  size = len(refs)
  def ret_getter(number):
    _tls.ensure_capacity(size)
    output = _tls.c_float_array
    getter(output, refs, size, number - 1, field)
    return np.array(output[0:size], dtype=np.float32)
  return ret_getter


def create_io_float_group_getter(refs, getter):
  """
  Returns a callable which accepts 2 arguments
  """
  size = len(refs)
  def ret_getter(field, number):
    _tls.ensure_capacity(size)
    output = _tls.c_float_array
    getter(output, refs, size, number - 1, field)
    return np.array(output[0:size], dtype=np.float32)
  return ret_getter


def create_io_int_group_getter(refs, getter):
  """
  Returns a callable which accepts 2 arguments
  """
  size = len(refs)
  def ret_getter(field, number):
    _tls.ensure_capacity(size)
    output = _tls.c_int64_array
    getter(output, refs, size, number - 1, field)
    return np.array(output[0:size], dtype=np.int64)
  return ret_getter


def create_led_group_getter(refs, field, getter):
  """
  Returns a callable which accepts 0 arguments
  """
  size = len(refs)
  from hebi._internal.graphics import color_from_int
  def ret_getter():
    _tls.ensure_capacity(size)
    output = _tls.c_int32_array
    getter(output, refs, size, field)
    return [color_from_int(val) for val in output[0:size]]
  return ret_getter


################################################################################
# `setter` creators
################################################################################


def create_numbered_float_group_setter(refs, field, setter):
  """
  Returns a callable which accepts 2 arguments
  """
  size = len(refs)
  def ret_setter(number, value):
    if value is None:
      bfr = None
    else:
      _tls.ensure_capacity(size)
      bfr = _tls.c_float_array
      if hasattr(value, '__len__'):
        for i in range(size):
          bfr[i] = value[i]
      else:
        for i in range(size):
          bfr[i] = value

    setter(refs, bfr, size, number - 1, field)
  return ret_setter


def create_io_float_group_setter(refs, setter):
  """
  Returns a callable which accepts 3 arguments
  """
  size = len(refs)
  def ret_setter(field, number, value):
    if value is None:
      bfr = None
    else:
      _tls.ensure_capacity(size)
      bfr = _tls.c_float_array
      if hasattr(value, '__len__'):
        for i in range(size):
          bfr[i] = value[i]
      else:
        for i in range(size):
          bfr[i] = value

    setter(refs, bfr, size, number - 1, field)
  return ret_setter


def create_io_int_group_setter(refs, setter):
  """
  Returns a callable which accepts 3 arguments
  """
  size = len(refs)
  def ret_setter(field, number, value):
    if value is None:
      bfr = None
    else:
      _tls.ensure_capacity(size)
      bfr = _tls.c_int64_array
      if hasattr(value, '__len__'):
        for i in range(size):
          bfr[i] = value[i]
      else:
        for i in range(size):
          bfr[i] = value

    setter(refs, bfr, size, number - 1, field)
  return ret_setter


def create_led_group_setter(refs, field, setter):
  """
  Returns a callable which accepts 1 argument
  """
  size = len(refs)
  def ret_setter(value):
    _tls.ensure_capacity(size)
    setter(refs, value, size, field)
  return ret_setter


def create_numbered_float_single_getter(ref, field, getter):
  def ret_getter(number):
    ret = _tls.c_float
    getter(byref(ref), byref(ret), 1, number, field)
    return ret.value
  return ret_getter


################################################################################
# Classes
################################################################################


class GroupNumberedFloatFieldContainer(WeakReferenceContainer):
  """
  A read only view into a set of numbered float fields
  """

  __slots__ = ['_getter', '_has', '_field']

  def __init__(self, internal, field, getter, has):
    super(GroupNumberedFloatFieldContainer, self).__init__(internal)
    self._field = field
    self._getter = getter
    self._has = has

  def __repr__(self):
    return _numbered_float_repr(self, self._field)

  @property
  def has_float1(self):
    return self._has(1)

  @property
  def has_float2(self):
    return self._has(2)

  @property
  def has_float3(self):
    return self._has(3)

  @property
  def has_float4(self):
    return self._has(4)

  @property
  def has_float5(self):
    return self._has(5)

  @property
  def has_float6(self):
    return self._has(6)

  @property
  def has_float7(self):
    return self._has(7)

  @property
  def has_float8(self):
    return self._has(8)

  @property
  def has_float9(self):
    return self._has(9)

  @property
  def float1(self):
    return self._getter(1)

  @property
  def float2(self):
    return self._getter(2)

  @property
  def float3(self):
    return self._getter(3)

  @property
  def float4(self):
    return self._getter(4)

  @property
  def float5(self):
    return self._getter(5)

  @property
  def float6(self):
    return self._getter(6)

  @property
  def float7(self):
    return self._getter(7)

  @property
  def float8(self):
    return self._getter(8)

  @property
  def float9(self):
    return self._getter(9)


class MutableGroupNumberedFloatFieldContainer(WeakReferenceContainer):
  """
  A mutable view into a set of numbered float fields
  """

  __slots__ = ['_getter', '_has', '_setter', '_field']

  def __init__(self, internal, field, getter, has, setter):
    super(MutableGroupNumberedFloatFieldContainer, self).__init__(internal)
    self._field = field
    self._getter = getter
    self._has = has
    self._setter = setter

  def __repr__(self):
    return _numbered_float_repr(self, self._field)

  @property
  def has_float1(self):
    return self._has(1)

  @property
  def has_float2(self):
    return self._has(2)

  @property
  def has_float3(self):
    return self._has(3)

  @property
  def has_float4(self):
    return self._has(4)

  @property
  def has_float5(self):
    return self._has(5)

  @property
  def has_float6(self):
    return self._has(6)

  @property
  def has_float7(self):
    return self._has(7)

  @property
  def has_float8(self):
    return self._has(8)

  @property
  def has_float9(self):
    return self._has(9)

  @property
  def float1(self):
    return self._getter(1)

  @property
  def float2(self):
    return self._getter(2)

  @property
  def float3(self):
    return self._getter(3)

  @property
  def float4(self):
    return self._getter(4)

  @property
  def float5(self):
    return self._getter(5)

  @property
  def float6(self):
    return self._getter(6)

  @property
  def float7(self):
    return self._getter(7)

  @property
  def float8(self):
    return self._getter(8)

  @property
  def float9(self):
    return self._getter(9)

  @float1.setter
  def float1(self, value):
    self._setter(1, value)

  @float2.setter
  def float2(self, value):
    self._setter(2, value)

  @float3.setter
  def float3(self, value):
    self._setter(3, value)

  @float4.setter
  def float4(self, value):
    self._setter(4, value)

  @float5.setter
  def float5(self, value):
    self._setter(5, value)

  @float6.setter
  def float6(self, value):
    self._setter(6, value)

  @float7.setter
  def float7(self, value):
    self._setter(7, value)

  @float8.setter
  def float8(self, value):
    self._setter(8, value)

  @float9.setter
  def float9(self, value):
    self._setter(9, value)


class GroupMessageIoFieldBankContainer(WeakReferenceContainer):
  """
  Represents a read only IO bank
  """

  __slots__ = ['_bank', '_bank_readable']

  def __init__(self, bank, bank_readable, io_field_container):
    super(GroupMessageIoFieldBankContainer, self).__init__(io_field_container)
    self._bank = bank
    self._bank_readable = bank_readable.strip().upper()

  def __repr__(self):
    return _io_bank_repr(self, self._bank, self._bank_readable)

  def has_int(self, pin_number):
    """
    Note: `pin_number` indexing starts at `1`
    """
    container = self._get_ref()
    return container.has_int(self._bank, pin_number)

  def has_float(self, pin_number):
    """
    Note: `pin_number` indexing starts at `1`
    """
    container = self._get_ref()
    return container.has_float(self._bank, pin_number)

  def get_int(self, pin_number):
    """
    Note: `pin_number` indexing starts at `1`
    """
    container = self._get_ref()
    return container.get_int(self._bank, pin_number)

  def get_float(self, pin_number):
    """
    Note: `pin_number` indexing starts at `1`
    """
    container = self._get_ref()
    return container.get_float(self._bank, pin_number)


class MutableGroupMessageIoFieldBankContainer(GroupMessageIoFieldBankContainer):
  """
  Represents a mutable IO Bank
  """

  def __init__(self, bank, bank_readable, io_field_container):
    super(MutableGroupMessageIoFieldBankContainer, self).__init__(bank, bank_readable, io_field_container)

  def set_int(self, pin_number, value):
    """
    Note: `pin_number` indexing starts at `1`
    """
    container = self._get_ref()
    return container.set_int(self._bank, pin_number, value)

  def set_float(self, pin_number, value):
    """
    Note: `pin_number` indexing starts at `1`
    """
    container = self._get_ref()
    return container.set_float(self._bank, pin_number, value)


class GroupMessageIoFieldContainer(WeakReferenceContainer):
  """
  Represents a read only view into IO banks
  """

  __slots__ = ['_a', '_b', '_c', '_d', '_e', '_f', '_getter_int', '_getter_float', '_has_int', '_has_float', '__weakref__']

  def __init__(self, group_message, getter_int, getter_float, has_int_func, has_float_func, enum_type, container_type=GroupMessageIoFieldBankContainer):
    super(GroupMessageIoFieldContainer, self).__init__(group_message)

    self._getter_int = getter_int
    self._getter_float = getter_float
    self._has_int = has_int_func
    self._has_float = has_float_func

    bank_a = enum_type.get_enum_value_by_int(0)
    bank_b = enum_type.get_enum_value_by_int(1)
    bank_c = enum_type.get_enum_value_by_int(2)
    bank_d = enum_type.get_enum_value_by_int(3)
    bank_e = enum_type.get_enum_value_by_int(4)
    bank_f = enum_type.get_enum_value_by_int(5)

    self._a = container_type(bank_a, 'a', self)
    self._b = container_type(bank_b, 'b', self)
    self._c = container_type(bank_c, 'c', self)
    self._d = container_type(bank_d, 'd', self)
    self._e = container_type(bank_e, 'e', self)
    self._f = container_type(bank_f, 'f', self)

  def __repr__(self):
    return _io_repr(self)

  def has_int(self, bank, pin_number):
    """
    Note: `pin_number` indexing starts at `1`
    """
    if pin_number < 1:
      raise ValueError("pin_number must be greater than 0")
    return self._has_int(bank, pin_number)

  def has_float(self, bank, pin_number):
    """
    Note: `pin_number` indexing starts at `1`
    """
    if pin_number < 1:
      raise ValueError("pin_number must be greater than 0")
    return self._has_float(bank, pin_number)

  def get_int(self, bank, pin_number):
    """
    Note: `pin_number` indexing starts at `1`
    """
    if pin_number < 1:
      raise ValueError("pin_number must be greater than 0")
    return self._getter_int(bank, pin_number)

  def get_float(self, bank, pin_number):
    """
    Note: `pin_number` indexing starts at `1`
    """
    if pin_number < 1:
      raise ValueError("pin_number must be greater than 0")
    return self._getter_float(bank, pin_number)

  @property
  def a(self):
    return self._a

  @property
  def b(self):
    return self._b

  @property
  def c(self):
    return self._c

  @property
  def d(self):
    return self._d

  @property
  def e(self):
    return self._e

  @property
  def f(self):
    return self._f


class MutableGroupMessageIoFieldContainer(GroupMessageIoFieldContainer):
  """
  Represents a mutable view into IO banks
  """

  __slots__ = ['_setter_int', '_setter_float']

  def __init__(self, group_message, getter_int, getter_float, has_int_func, has_float_func, setter_int, setter_float, enum_type):
    super(MutableGroupMessageIoFieldContainer, self).__init__(group_message, getter_int, getter_float, has_int_func, has_float_func, enum_type, MutableGroupMessageIoFieldBankContainer)

    self._setter_int = setter_int
    self._setter_float = setter_float

  def set_int(self, bank, pin_number, value):
    """
    Note: `pin_number` indexing starts at `1`
    """
    if pin_number < 1:
      raise ValueError("pin_number must be greater than 0")
    self._setter_int(bank, pin_number, value)

  def set_float(self, bank, pin_number, value):
    """
    Note: `pin_number` indexing starts at `1`
    """
    if pin_number < 1:
      raise ValueError("pin_number must be greater than 0")
    self._setter_float(bank, pin_number, value)


################################################################################
# LED Field Containers
################################################################################


def _get_led_values(colors, size):
  _tls.ensure_capacity(size)
  bfr = _tls.c_int32_array

  if type(colors) is str:
    bfr[0:size] = [int(string_to_color(colors)) for _ in range(size)]
  elif type(colors) is int:
    bfr[0:size] = [colors for _ in range(size)]
  elif isinstance(colors, Color):
    bfr[0:size] = [int(colors) for _ in range(size)]
  elif not (hasattr(colors, '__len__')):
    raise ValueError('Cannot broadcast input to array of colors')
  else:
    bfr[0:size] = [int(entry) for entry in colors]
  return bfr


class GroupMessageLEDFieldContainer(WeakReferenceContainer):

  __slots__ = ['_getter', '_field']

  def __init__(self, internal, getter, field):
    super(GroupMessageLEDFieldContainer, self).__init__(internal)
    self._getter = getter
    self._field = field

  def __repr__(self):
    return _led_repr(self, self._field)

  @property
  def color(self):
    return self._getter()


class MutableGroupMessageLEDFieldContainer(GroupMessageLEDFieldContainer):
  __slots__ = ['_setter']

  def __init__(self, internal, getter, setter, field):
    super(MutableGroupMessageLEDFieldContainer, self).__init__(internal, getter, field)
    self._setter = setter

  def clear(self):
    """
    Clears all LEDs
    """
    messages = self._get_ref()
    self._setter(None)

  def __set_colors(self, colors):
    messages = self._get_ref()
    self._setter(_get_led_values(colors, messages.size))

  @property
  def color(self):
    return super(MutableGroupMessageLEDFieldContainer, self).color

  @color.setter
  def color(self, value):
    if value is None:
      self.clear()
    self.__set_colors(value)


################################################################################
# Helper Functions
################################################################################


def __check_broadcastable(group_type, field, value):
  if group_type.size > 1:
    if not field.allow_broadcast:
      raise ValueError('Cannot broadcast scalar value \'{}\' '.format(value) +
                       'to the field \'{0}\' '.format(field.name) +
                       'in all modules of the group.' +
                       '\nReason: {}'.format(field.not_broadcastable_reason))


def __check_broadcastable_field(field, value):
  if not field.allow_broadcast:
    raise ValueError('Cannot broadcast scalar value \'{}\' '.format(value) +\
                     'to the field \'{}\' '.format(field.name) +\
                     'in all modules of the group.' +\
                     '\nReason: {}'.format(field.not_broadcastable_reason))


def _do_broadcast(group_message, field, value, dtype):
  if hasattr(value, '__len__') and type(value) is not str:
    __assert_same_length(group_message, value)
    if dtype is str:
      return value
    else:
      return np.array(value, dtype=dtype)
  else: # Is scalar; each module in group will be set to this
    __check_broadcastable(group_message, field, value)
    return np.array([value] * group_message.size, dtype=dtype)


def __assert_same_length(group_message, b):
  if group_message.size != len(b):
    raise ValueError('Input array must have same size as number of modules in group message')


################################################################################
# TLS for accessors and mutators
################################################################################


import threading


class MessagesTLS_Holder:

  __slots__ = [
                # Scalars
                '_c_bool', '_c_int32', '_c_int64', '_c_uint64', '_c_size_t', '_c_float', '_c_double',
                '_c_vector3f', '_c_quaternionf', '_c_null_str', '_c_str', '_c_high_res_angle',
                "_array_size",
                # Arrays
                "_c_bool_array", "_c_int32_array", "_c_int64_array", "_c_uint64_array", "_c_size_t_array",
                "_c_float_array", "_c_double_array", "_c_vector3f_array", "_c_quaternionf_array",
                "_c_high_res_angle_array"
              ]

  def _grow_arrays(self, size):
    if size > self._array_size:
      self._c_bool_array = (ctypes.c_bool * size)()
      self._c_int32_array = (ctypes.c_int32 * size)()
      self._c_int64_array = (ctypes.c_int64 * size)()
      self._c_uint64_array = (ctypes.c_uint64 * size)()
      self._c_size_t_array = (ctypes.c_size_t * size)()
      self._c_float_array = (ctypes.c_float * size)()
      self._c_double_array = (ctypes.c_double * size)()
      self._c_vector3f_array = (HebiVector3f * size)()
      self._c_quaternionf_array = (HebiQuaternionf * size)()
      self._c_high_res_angle_array = (HebiHighResAngleStruct * size)()

  def __init__(self):
    self._c_bool = ctypes.c_bool(0)
    self._c_int32 = ctypes.c_int32(0)
    self._c_int64 = ctypes.c_int64(0)
    self._c_uint64 = ctypes.c_uint64(0)
    self._c_size_t = ctypes.c_size_t(0)
    self._c_float = ctypes.c_float(0)
    self._c_double = ctypes.c_double(0)
    self._c_vector3f = HebiVector3f()
    self._c_quaternionf = HebiQuaternionf()
    self._c_high_res_angle = HebiHighResAngleStruct()
    self._c_null_str = ctypes.c_char_p(None)
    self._c_str = create_str(512)

    self._array_size = 0
    self._grow_arrays(6)


class MessagesTLS(threading.local):
  def __init__(self):
    super(MessagesTLS, self).__init__()
    self._holder = MessagesTLS_Holder()

  def ensure_capacity(self, size):
    self._holder._grow_arrays(size)

  @property
  def c_bool(self):
    return self._holder._c_bool

  @property
  def c_int32(self):
    return self._holder._c_int32

  @property
  def c_int64(self):
    return self._holder._c_int64

  @property
  def c_uint64(self):
    return self._holder._c_uint64

  @property
  def c_size_t(self):
    return self._holder._c_size_t

  @property
  def c_float(self):
    return self._holder._c_float

  @property
  def c_double(self):
    return self._holder._c_double

  @property
  def c_vector3f(self):
    return self._holder._c_vector3f

  @property
  def c_quaternionf(self):
    return self._holder._c_quaternionf

  @property
  def c_null_str(self):
    return self._holder._c_null_str

  @property
  def c_str(self):
    return self._holder._c_str

  @property
  def c_high_res_angle(self):
    return self._holder._c_high_res_angle

  @property
  def c_bool_array(self):
    return self._holder._c_bool_array

  @property
  def c_int32_array(self):
    return self._holder._c_int32_array

  @property
  def c_int64_array(self):
    return self._holder._c_int64_array

  @property
  def c_uint64_array(self):
    return self._holder._c_uint64_array

  @property
  def c_size_t_array(self):
    return self._holder._c_size_t_array

  @property
  def c_float_array(self):
    return self._holder._c_float_array

  @property
  def c_double_array(self):
    return self._holder._c_double_array

  @property
  def c_vector3f_array(self):
    return self._holder._c_vector3f_array

  @property
  def c_quaternionf_array(self):
    return self._holder._c_quaternionf_array

  @property
  def c_high_res_angle_array(self):
    return self._holder._c_high_res_angle_array


_tls = MessagesTLS()


################################################################################
# Accessors
################################################################################


def __get_flag_group(refs, field, getter):
  size = len(refs)
  _tls.ensure_capacity(size)
  bfr = _tls.c_bool_array
  getter(bfr, refs, size, field)
  return np.array(bfr[0:size], dtype=np.bool)


def __get_bool_group(refs, field, getter):
  size = len(refs)
  _tls.ensure_capacity(size)
  bfr = _tls.c_bool_array
  getter(bfr, refs, size, field)
  return np.array(bfr[0:size], dtype=np.bool)


def __get_enum_group(refs, field, getter):
  size = len(refs)
  _tls.ensure_capacity(size)
  bfr = _tls.c_int32_array
  getter(bfr, refs, size, field)
  return np.array(bfr[0:size], dtype=np.int32)


def __get_float_group(refs, field, getter):
  size = len(refs)
  _tls.ensure_capacity(size)
  bfr = _tls.c_float_array
  getter(bfr, refs, size, field)
  return np.array(bfr[0:size], dtype=np.float32)


def __get_highresangle_group(refs, field, getter):
  size = len(refs)
  _tls.ensure_capacity(size)
  bfr = _tls.c_double_array
  getter(bfr, refs, size, field)
  return np.array(bfr[0:size], dtype=np.float64)


def __get_vector3f_group(refs, field, getter):
  size = len(refs)
  _tls.ensure_capacity(size)
  bfr = _tls.c_vector3f_array
  getter(bfr, refs, size, field)
  return _ctypes_to_ndarray(cast_to_float_ptr(bfr), (size, 3))


def __get_quaternionf_group(refs, field, getter):
  size = len(refs)
  _tls.ensure_capacity(size)
  bfr = _tls.c_quaternionf_array
  getter(bfr, refs, size, field)
  return _ctypes_to_ndarray(cast_to_float_ptr(bfr), (size, 4))


def __get_uint64_group(refs, field, getter):
  size = len(refs)
  _tls.ensure_capacity(size)
  bfr = _tls.c_uint64_array
  getter(bfr, refs, size, field)
  return np.array(bfr[0:size], dtype=np.uint64)


def __get_scalar_field_single(message, field, ret, getter):
  getter(byref(ret), message, 1, field)
  return ret.value


def __get_vector3f_single(message, field, ret, getter):
  ret = byref(ret)
  getter(ret, message, 1, field)
  #return ret.value
  return _ctypes_to_ndarray(cast_to_float_ptr(ret), (3,))


def __get_quaternionf_single(message, field, ret, getter):
  ret = byref(ret)
  getter(ret, message, 1, field)
  #return ret.value
  return _ctypes_to_ndarray(cast_to_float_ptr(ret), (4,))


def __get_string_group(message_list, field, output, getter):
  alloc_size_c = _tls.c_size_t
  alloc_size = 0
  null_str = _tls.c_null_str

  for i, message in enumerate(message_list.modules):
    res = getter(message, field, null_str, byref(alloc_size_c))
    alloc_size = max(alloc_size, alloc_size_c.value + 1)

  if alloc_size > len(_tls.c_str):
    string_buffer = create_str(alloc_size)
  else:
    string_buffer = _tls.c_str

  for i, message in enumerate(message_list.modules):
    alloc_size_c.value = alloc_size
    if getter(message, field, string_buffer, byref(alloc_size_c)) == StatusSuccess:
      output[i] = decode_str(string_buffer.value)
    else:
      output[i] = None
  return output


def __get_string_single(message, field, getter):
  alloc_size_c = _tls.c_size_t
  null_str = _tls.c_null_str

  getter(message, field, null_str, byref(alloc_size_c))
  alloc_size = alloc_size_c.value + 1

  if alloc_size > len(_tls.c_str):
    string_buffer = create_str(alloc_size)
  else:
    string_buffer = _tls.c_str

  alloc_size_c.value = alloc_size
  ret = None
  if getter(message, field, string_buffer, byref(alloc_size_c)) == StatusSuccess:
    ret = decode_str(string_buffer.value)
  return ret


################################################################################
# Mutators
################################################################################


def __set_flag_group(refs, field, value, setter):
  size = len(refs)
  _tls.ensure_capacity(size)
  if value is None:
    bfr = None
  else:
    bfr = _tls.c_bool_array
    if hasattr(value, '__len__'):
      for i in range(size):
        bfr[i] = value[i]
    else:
      for i in range(size):
        bfr[i] = value
  setter(refs, bfr, size, field)


def __set_bool_group(refs, field, value, setter):
  size = len(refs)
  _tls.ensure_capacity(size)
  if value is None:
    bfr = None
  else:
    bfr = _tls.c_bool_array
    if hasattr(value, '__len__'):
      for i in range(size):
        bfr[i] = value[i]
    else:
      for i in range(size):
        bfr[i] = value
  setter(refs, bfr, size, field)


def __set_enum_group(refs, field, value, setter):
  size = len(refs)
  _tls.ensure_capacity(size)
  if value is None:
    bfr = None
  else:
    bfr = _tls.c_int32_array
    if hasattr(value, '__len__'):
      for i in range(size):
        bfr[i] = value[i]
    else:
      for i in range(size):
        bfr[i] = value
  setter(refs, bfr, size, field)


def __set_float_group(refs, field, value, setter):
  size = len(refs)
  _tls.ensure_capacity(size)
  if value is None:
    bfr = None
  else:
    bfr = _tls.c_float_array
    if hasattr(value, '__len__'):
      for i in range(size):
        bfr[i] = value[i]
    else:
      for i in range(size):
        bfr[i] = value
  setter(refs, bfr, size, field)


def __set_highresangle_group(refs, field, value, setter):
  size = len(refs)
  _tls.ensure_capacity(size)
  if value is None:
    bfr = None
  else:
    bfr = _tls.c_double_array
    if hasattr(value, '__len__'):
      for i in range(size):
        bfr[i] = value[i]
    else:
      for i in range(size):
        bfr[i] = value
  setter(refs, bfr, size, field)


def __set_vector3f_group(refs, field, value, setter):
  size = len(refs)
  _tls.ensure_capacity(size)
  if value is None:
    bfr = None
  else:
    bfr = _tls.c_vector3f_array
    if hasattr(value, '__len__'):
      for i in range(size):
        bfr[i] = value[i]
    else:
      for i in range(size):
        bfr[i] = value
  setter(refs, bfr, size, field)


def __set_quaternionf_group(refs, field, value, setter):
  size = len(refs)
  _tls.ensure_capacity(size)
  if value is None:
    bfr = None
  else:
    bfr = _tls.c_quaternionf_array
    if hasattr(value, '__len__'):
      for i in range(size):
        bfr[i] = value[i]
    else:
      for i in range(size):
        bfr[i] = value
  setter(refs, bfr, size, field)


def __set_uint64_group(refs, field, value, setter):
  size = len(refs)
  _tls.ensure_capacity(size)
  if value is None:
    bfr = None
  else:
    bfr = _tls.c_uint64_array
    if hasattr(value, '__len__'):
      for i in range(size):
        bfr[i] = value[i]
    else:
      for i in range(size):
        bfr[i] = value
  setter(refs, bfr, size, field)


def __set_field_single(ref, field, value, value_ctype, setter):
  if value is not None:
    value_ctype.value = value
    setter(byref(ref), byref(value_ctype), 1, field)
  else:
    setter(byref(ref), None, 1, field)


def __set_string_group(message_list, field, value, setter):
  alloc_size_c = _tls.c_size_t
  if value is not None:
    value = _do_broadcast(message_list, field, value, str)

    for i, message in enumerate(message_list.modules):
      val = value[i]
      alloc_size = len(val) + 1
      # TODO: use tls string buffer and copy val into it instead
      string_buffer = create_str(val, size=alloc_size)
      alloc_size_c.value = alloc_size
      setter(message, field, string_buffer, byref(alloc_size_c))
  else:
    for i, message in enumerate(message_list.modules):
      setter(message, field, None, None)


def __set_string_single(message, field, value, setter):
  if value is not None:
    alloc_size_c = _tls.c_size_t
    alloc_size = len(value) + 1
    # TODO: use tls string buffer and copy val into it instead
    string_buffer = create_str(value, size=alloc_size)
    alloc_size_c.value = alloc_size
    setter(message, field, string_buffer, byref(alloc_size_c))
  else:
    setter(message, field, None, None)

################################################################################
# Command
################################################################################


get_command_flag = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_bool, api.hwCommandGetFlag)
get_command_bool = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_bool, api.hwCommandGetBool)
get_command_enum = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_int32, api.hwCommandGetEnum)
get_command_float = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_float, api.hwCommandGetFloat)
get_command_highresangle = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_double, api.hwCommandGetHighResAngle)
get_command_string = lambda msg, field: __get_string_single(msg, field, api.hebiCommandGetString)

set_command_flag = lambda msg, field, value: __set_field_single(msg, field, value, _tls.c_bool, api.hwCommandSetFlag)
set_command_bool = lambda msg, field, value: __set_field_single(msg, field, value, _tls.c_bool, api.hwCommandSetBool)
set_command_enum = lambda msg, field, value: __set_field_single(msg, field, value, _tls.c_int32, api.hwCommandSetEnum)
set_command_float = lambda msg, field, value: __set_field_single(msg, field, value, _tls.c_float, api.hwCommandSetFloat)
set_command_highresangle = lambda msg, field, value: __set_field_single(msg, field, value, _tls.c_double, api.hwCommandSetHighResAngle)
set_command_string = lambda msg, field, value: __set_string_single(msg, field, value, api.hebiCommandSetString)

get_group_command_flag = lambda msg, field: __get_flag_group(msg, field, api.hwCommandGetFlag)
get_group_command_bool = lambda msg, field: __get_bool_group(msg, field, api.hwCommandGetBool)
get_group_command_enum = lambda msg, field: __get_enum_group(msg, field, api.hwCommandGetEnum)
get_group_command_float = lambda msg, field: __get_float_group(msg, field, api.hwCommandGetFloat)
get_group_command_highresangle = lambda msg, field: __get_highresangle_group(msg, field, api.hwCommandGetHighResAngle)
get_group_command_string = lambda msg, field, output: __get_string_group(msg, field, output, api.hebiCommandGetString)

set_group_command_flag = lambda msg, field, value: __set_flag_group(msg, field, value, api.hwCommandSetFlag)
set_group_command_bool = lambda msg, field, value: __set_bool_group(msg, field, value, api.hwCommandSetBool)
set_group_command_enum = lambda msg, field, value: __set_enum_group(msg, field, value, api.hwCommandSetEnum)
set_group_command_float = lambda msg, field, value: __set_float_group(msg, field, value, api.hwCommandSetFloat)
set_group_command_highresangle = lambda msg, field, value: __set_highresangle_group(msg, field, value, api.hwCommandSetHighResAngle)
set_group_command_string = lambda msg, field, value: __set_string_group(msg, field, value, api.hebiCommandSetString)


################################################################################
# Feedback
################################################################################


get_feedback_vector3f = lambda msg, field: __get_vector3f_single(msg, field, _tls.c_vector3f, api.hwFeedbackGetVector3f)
get_feedback_quaternionf = lambda msg, field: __get_quaternionf_single(msg, field, _tls.c_quaternionf, api.hwFeedbackGetQuaternionf)
get_feedback_uint64 = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_uint64, api.hwFeedbackGetUInt64)
get_feedback_enum = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_int, api.hwFeedbackGetEnum)
get_feedback_float = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_float, api.hwFeedbackGetFloat)
get_feedback_highresangle = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_double, api.hwFeedbackGetHighResAngle)

get_group_feedback_vector3f = lambda msg, field: __get_vector3f_group(msg, field, api.hwFeedbackGetVector3f)
get_group_feedback_quaternionf = lambda msg, field: __get_quaternionf_group(msg, field, api.hwFeedbackGetQuaternionf)
get_group_feedback_uint64 = lambda msg, field: __get_uint64_group(msg, field, api.hwFeedbackGetUInt64)
get_group_feedback_enum = lambda msg, field: __get_enum_group(msg, field, api.hwFeedbackGetEnum)
get_group_feedback_float = lambda msg, field: __get_float_group(msg, field, api.hwFeedbackGetFloat)
get_group_feedback_highresangle = lambda msg, field: __get_highresangle_group(msg, field, api.hwFeedbackGetHighResAngle)


def get_group_feedback_float_into(refs, field, output):
  size = len(refs)
  bfr = to_float_ptr(output)
  api.hwFeedbackGetFloat(bfr, refs, size, field)


def get_group_feedback_highresangle_into(refs, field, output):
  size = len(refs)
  bfr = to_double_ptr(output)
  api.hwFeedbackGetHighResAngle(bfr, refs, size, field)


################################################################################
# Info
################################################################################


get_info_flag = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_bool, api.hwInfoGetFlag)
get_info_bool = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_bool, api.hwInfoGetBool)
get_info_enum = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_int, api.hwInfoGetEnum)
get_info_float = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_float, api.hwInfoGetFloat)
get_info_highresangle = lambda msg, field: __get_scalar_field_single(msg, field, _tls.c_double, api.hwInfoGetHighResAngle)
get_info_string = lambda msg, field: __get_string_single(msg, field, api.hebiInfoGetString)


get_group_info_flag = lambda msg, field: __get_flag_group(msg, field, api.hwInfoGetFlag)
get_group_info_enum = lambda msg, field: __get_enum_group(msg, field, api.hwInfoGetEnum)
get_group_info_bool = lambda msg, field: __get_bool_group(msg, field, api.hwInfoGetBool)
get_group_info_float = lambda msg, field: __get_float_group(msg, field, api.hwInfoGetFloat)
get_group_info_highresangle = lambda msg, field: __get_highresangle_group(msg, field, api.hwInfoGetHighResAngle)
get_group_info_string = lambda msg, field, output: __get_string_group(msg, field, output, api.hebiInfoGetString)


################################################################################
# Parsers
################################################################################


def __map_input_setter_delegate(group_message, values, setter, setter_field):
  mapped_values = [None] * group_message.size
  str_map = setter_field.substrates

  try:
    if type(values) is str:
      val = str_map[values.lower()]
      for i in range(0, group_message.size):
        mapped_values[i] = val
    else:
      for i, entry in enumerate(values):
        mapped_values[i] = str_map[entry.lower()]
  except KeyError as key:
    print('{} is not a valid string parameter.'.format(key))
    print('Valid string parameters: {0}'.format("'" + "', '".join(setter_field.substrates.keys()) + "'"))
    raise key
  setter(group_message, setter_field, mapped_values)


def setter_input_parser_delegate(group_message, values, setter, setter_field):
  """
  Maps strings (case insensitive) to a non-string type.
  Only used for fields which are not of type string

  This function assumes that `setter_field` has an attribute called `substrates`
  which returns a dictionary with :type str: keys and values of the type which
  the function `setter` expects
  """
  if not hasattr(setter_field, 'substrates'):
    raise RuntimeError('Field {} has no substrates map field'.format(setter_field))
  if hasattr(values, '__len__') and type(values) is not str:  # Is "array-like" according to numpy
    for entry in values:
      if type(entry) is not str:
        # By default, delegate to regular `setter` routine
        setter(group_message, setter_field, values)
        return
    __map_input_setter_delegate(group_message, values, setter, setter_field)
  elif type(values) == str:
    __map_input_setter_delegate(group_message, values, setter, setter_field)
  else:
    setter(group_message, setter_field, values)
