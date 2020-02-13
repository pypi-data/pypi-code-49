# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#  HEBI Core python API - Copyright 2018 HEBI Robotics
#  See https://hebi.us/softwarelicense for license details
#
# -----------------------------------------------------------------------------


from ctypes import byref, cast, c_ubyte, c_char_p, c_void_p, c_size_t, POINTER

from .group import GroupDelegate, Group
from .type_utils import (create_string_buffer_compat, decode_string_buffer, to_mac_address)
from .ffi.enums import StatusSuccess
from .ffi import ctypes_func_defs as api
from .ffi.wrappers import UnmanagedObject
from .ffi.ctypes_defs import HebiMacAddress


################################################################################
# Mac Address
################################################################################


class MacAddress(object):
  """
  A simple wrapper class for internal C-API HebiMacAddress objects to allow
  interfacing with API calls that use MAC addresses.
  """

  __slots__ = ['_obj']

  def __init__(self, a, b, c, d, e, f):
    obj = HebiMacAddress()
    obj.bytes_[0:6] = [a, b, c, d, e, f]

    self._obj = obj

  def __repr__(self):
    return self.__human_readable()

  def __str__(self):
    return self.__human_readable()

  def __getitem__(self, item):
    return self._obj.bytes_[item]

  def __human_readable(self):
    b0 = "%0.2X" % self._obj.bytes_[0]
    b1 = "%0.2X" % self._obj.bytes_[1]
    b2 = "%0.2X" % self._obj.bytes_[2]
    b3 = "%0.2X" % self._obj.bytes_[3]
    b4 = "%0.2X" % self._obj.bytes_[4]
    b5 = "%0.2X" % self._obj.bytes_[5]
    return '{0}:{1}:{2}:{3}:{4}:{5}'.format(b0, b1, b2, b3, b4, b5)

  @property
  def _as_parameter_(self):
    return self._obj

  @property
  def raw_bytes(self):
    """
    An unsigned byte buffer view of the object (ctypes c_ubyte array).
    Use this if you need a serialized format of this object, or if you
    are marshalling data to an external C API, etc.
    """
    return self._obj.bytes_


################################################################################
# Lookup Entries
################################################################################


class Entry(object):
  """
  Represents a HEBI module. This is used by the Lookup class.
  """

  __slots__ = ['_family', '_mac_address', '_name']

  def __init__(self, name, family, mac_address):
    self._name = name
    self._family = family
    self._mac_address = mac_address

  def __repr__(self):
    return self.__human_readable()

  def __str__(self):
    return self.__human_readable()

  def __human_readable(self):
    return 'Family: {} Name: {} Mac Address: {}'.format(self._family, self._name, self._mac_address)

  @property
  def name(self):
    """
    :return: The name of the module.
    :rtype:  str
    """
    return self._name

  @property
  def family(self):
    """
    :return: The family to which this module belongs.
    :rtype:  str
    """
    return self._family

  @property
  def mac_address(self):
    """
    :return: The immutable MAC address of the module.
    :rtype:  str
    """
    return self._mac_address


class EntryList(UnmanagedObject):
  """
  A list of module entries. This is used by the :class:`~hebi.Lookup` class
  and is returned by :attr:`~hebi.Lookup.entrylist`.
  """
  __slots__ = ['_elements', '_iterator', '_size']

  def __init__(self, internal):
    super(EntryList, self).__init__(internal, on_delete=api.hebiLookupEntryListRelease)
    bypass_debug_printing = True
    if bypass_debug_printing: #with bypass_debug_printing:
      # In debug mode, this tries to call repr(self) before everything is initialized,
      # which makes Python complain. So scope to bypass debug printing.
      # If debug mode is not enabled, this does not change any behavior.
      self._size = api.hebiLookupEntryListGetSize(self)
      elements = list()
      for i in range(self._size):
        elements.append(self.__get_entry(i))
      self._elements = elements
      self._iterator = iter(elements)

  def __iter__(self):
    return self

  def __length_hint__(self):
    return self._iterator.__length_hint__()

  def __next__(self):
    try:
      return next(self._iterator)
    except StopIteration:
      # PEP 479 forbids the implicit propagation of StopIteration
      raise StopIteration

  def __repr__(self):
    return self.__human_readable()

  def __str__(self):
    return str([str(entry) for entry in self._elements])

  def __human_readable(self):
    modules = list()
    for entry in self._elements:
      modules.append(entry)
    from .utils import lookup_table_string
    return lookup_table_string(modules)

  def __get_entry(self, index):
    required_size = c_size_t(0)
    if (api.hebiLookupEntryListGetName(self, index, c_char_p(None), byref(required_size)) != StatusSuccess):
      return None

    c_buffer = create_string_buffer_compat(required_size.value)
    if (api.hebiLookupEntryListGetName(self, index, c_buffer, byref(required_size)) != StatusSuccess):
      return None

    name = decode_string_buffer(c_buffer, 'utf-8')
    if (api.hebiLookupEntryListGetFamily(self._internal, index, c_char_p(None), byref(required_size)) != StatusSuccess):
      return None

    c_buffer = create_string_buffer_compat(required_size.value)
    if (api.hebiLookupEntryListGetFamily(self._internal, index, c_buffer, byref(required_size)) != StatusSuccess):
      return None

    family = decode_string_buffer(c_buffer, 'utf-8')
    tmp_buffer = HebiMacAddress()
    if (api.hebiLookupEntryListGetMacAddress(self._internal, index, byref(tmp_buffer)) != StatusSuccess):
      return None

    return Entry(name, family, MacAddress(*tmp_buffer.bytes_))

  def __getitem__(self, index):
    return self.__get_entry(index)


################################################################################
# Lookup and delegates
################################################################################


class LookupDelegate(UnmanagedObject):
  """
  Delegate for Lookup
  """

  __slots__ = []

  __singleton = None
  __singleton_lock = None

  @staticmethod
  def get_singleton():
    LookupDelegate.__singleton_lock.acquire()
    if LookupDelegate.__singleton is None:
      LookupDelegate.__singleton = LookupDelegate()
    LookupDelegate.__singleton_lock.release()
    return LookupDelegate.__singleton


  def __parse_to(self, timeout_ms):
    if timeout_ms is None:
      # FIXME: don't import here. We have to ATM because there would be cyclic dependencies otherwise
      from .. import Lookup
      return Lookup.DEFAULT_TIMEOUT_MS
    else:
      try:
        return int(timeout_ms)
      except:
        raise ValueError('timeout_ms must be a number')

  def __init__(self):
    super(LookupDelegate, self).__init__(api.hebiLookupCreate(None, 0), on_delete=api.hebiLookupRelease)

  @property
  def entrylist(self):
    list = api.hebiCreateLookupEntryList(self)
    if list:
      return EntryList(list)
    else:
      return None

  @property
  def lookup_frequency(self):
    return api.hebiLookupGetLookupFrequencyHz(self)

  @lookup_frequency.setter
  def lookup_frequency(self, freq):
    api.hebiLookupSetLookupFrequencyHz(self, freq)

  def get_group_from_names(self, families, names, timeout_ms=None):
    timeout_ms = self.__parse_to(timeout_ms)
    families_length = len(families)
    names_length = len(names)

    families_buffer = (c_char_p * families_length)()
    families_buffer_list = [ None ] * families_length
    names_buffer = (c_char_p * names_length)()
    names_buffer_list = [ None ] * names_length

    for i, family in enumerate(families):
      family_length = len(family)+1
      families_buffer_list[i] = create_string_buffer_compat(family, family_length)

    for i, name in enumerate(names):
      name_length = len(name)+1
      names_buffer_list[i] = create_string_buffer_compat(name, name_length)

    for i in range(families_length):
      families_buffer[i] = cast(families_buffer_list[i], c_char_p)

    for i in range(names_length):
      names_buffer[i] = cast(names_buffer_list[i], c_char_p)

    c_char_pp = POINTER(c_char_p)
    group = c_void_p(api.hebiGroupCreateFromNames(self,
                                              cast(byref(families_buffer), c_char_pp),
                                              families_length,
                                              cast(byref(names_buffer), c_char_pp),
                                              names_length,
                                              timeout_ms))

    if group:
      return Group(GroupDelegate(group))
    return None

  def get_group_from_macs(self, addresses, timeout_ms=None):
    timeout_ms = self.__parse_to(timeout_ms)
    addresses_length = len(addresses)
    addresses_list = [None] * addresses_length

    for i, address in enumerate(addresses):
      addresses_list[i] = to_mac_address(address)

    addresses_list_c = (c_void_p * addresses_length)()
    for i in range(addresses_length):
      addresses_list_c[i] = cast(addresses_list[i].raw_bytes, c_void_p)

    group = c_void_p(api.hebiGroupCreateFromMacs(self, byref(addresses_list_c),
                                             addresses_length, timeout_ms))

    if group:
      return Group(GroupDelegate(group))
    return None

  def get_group_from_family(self, family, timeout_ms=None):
    timeout_ms = self.__parse_to(timeout_ms)
    family_buffer = create_string_buffer_compat(family, len(family)+1)
    group = c_void_p(api.hebiGroupCreateFromFamily(self, family_buffer, timeout_ms))

    if (group):
      return Group(GroupDelegate(group))
    return None

  def get_connected_group_from_name(self, family, name, timeout_ms=None):
    timeout_ms = self.__parse_to(timeout_ms)
    family_buffer = create_string_buffer_compat(family, len(family)+1)
    name_buffer = create_string_buffer_compat(name, len(name)+1)
    group = c_void_p(api.hebiGroupCreateConnectedFromName(self, family_buffer,
                                                      name_buffer, timeout_ms))

    if group:
      return Group(GroupDelegate(group))
    return None

  def get_connected_group_from_mac(self, address, timeout_ms=None):
    timeout_ms = self.__parse_to(timeout_ms)
    mac_address = to_mac_address(address)
    group = c_void_p(api.hebiGroupCreateConnectedFromMac(self, mac_address.raw_bytes,
                                                     timeout_ms))

    if group:
      return Group(GroupDelegate(group))
    return None


from threading import Lock
LookupDelegate._LookupDelegate__singleton_lock = Lock()
del Lock
