#
# Classes representing key/value configuration dictionaries and files.
#
from __future__ import absolute_import, unicode_literals

import io
import itertools
import functools
import os
import re
try:
    from UserDict import DictMixin
except ImportError:
    from collections import MutableMapping as DictMixin
import collections

from dgpy.utils  import parse_key_value_from_fo


@functools.total_ordering
class ConfigDict(DictMixin):
    """Dictionary variant for classes based on key/value items, with following additional features:
    1. allow both access object[key] and object.key
    2. if the optional %ATTR_MAP and %OPTIONAL_ATTR are present, perform validation:
      - ATTR_MAP maps <key> -> func(string) for each permitted key.
      - OPTIONAL_ATTR is a set of optional keys. If present, it must be a subset of ATTR_MAP.keys()
    """
    def __init__(self, config, allow_whitespace=False):  # pylint: disable=too-many-branches
        """Initialize self from @config.
        @config:           key/value representation, one of
                           a) dictionary type ('dict' or 'OrderedDict') or
                           b) list of (key, value) pairs
                           c) iterable producing a list of type (b)
        @allow_whitespace: allow values to have trailing/leading whitespace
        """
        if hasattr(self, 'ATTR_MAP'):
            if not isinstance(config, dict):
                config = dict(config)

            have = set(config.keys())
            may_have = set(self.ATTR_MAP.keys())
            unknown_keys = have - may_have
            if unknown_keys:
                raise KeyError("unsupported %s configuration key(s): %s" % (self.__class__.__name__,
                                                                            ', '.join(map(repr, unknown_keys))))

            if hasattr(self, 'OPTIONAL_ATTR'):
                if not self.OPTIONAL_ATTR.issubset(may_have):
                    raise KeyError("Invalid OPTIONAL_ATTR %s" % ', '.join(self.OPTIONAL_ATTR - may_have))

                missing_keys = may_have - self.OPTIONAL_ATTR - have
                if missing_keys:
                    raise KeyError("missing %s configuration key(s): %s" % (self.__class__.__name__,
                                                                            ', '.join(map(repr, missing_keys))))

            # Order of %ATTR_MAP overrides the order in @config
            init_items = [(k, config[k]) for k in self.ATTR_MAP.keys() if k in config]
            for k, v in init_items:
                if v and not self.ATTR_MAP[k](v): # Empty values are O.K.
                    raise ValueError("invalid entry '%s = %r" % (k, v))

        elif isinstance(config, dict):
            init_items = [(k, config[k]) for k in sorted(config.keys())]
        else:
            init_items = list(config)  # Permit generator expressions as argument.

        self.__dict = collections.OrderedDict(init_items)

        if not allow_whitespace:
            for k, v in self.__dict.items():
                if re.search(r'(^\s+|\s+$)', v):
                    raise ValueError("whitespace in configuration: %s = %r" % (k, v))

    def __hash__(self):
        """Hash value is the ordered representation of wrapped key/value pairs.
        This implementation ignores additional attributes added in subclasses, i.e.
        subclasses must override this function if items are to be added to sets, dictionaries etc.
        """
        return hash(repr(self.__dict))

    def __eq__(self, other):
        return self.__class__ == other.__class__ and hash(self) == hash(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return hash(self) < hash(other)

    def __len__(self):  # Required for MutableMapping
        return len(self.__dict)

    def __iter__(self):  # Required for MutableMapping
        return iter(self.__dict)

    def __getitem__(self, item):  # Required for MutableMapping
        return self.__dict.__getitem__(item)

    def __setitem__(self, item, value):  # Required for MutableMapping
        return self.__dict.__setitem__(item, value)

    def __delitem__(self, item):  # Required for MutableMapping
        return self.__dict.__delitem__(item)

    def __getattr__(self, name):
        # The following case happens because we call getattr in __init__ (for subclasses having ATTR_MAP):
        if name == '_ConfigDict__dict':
            raise AttributeError(name)
        if name in self.__dict:               # Allow access as self.<name>
            return self.__dict[name]
        return getattr(self.__dict, name)     # Fallback: delegate to wrapped dictionary (superclass)

    def __str__(self):
        """Print dictionary items first, then any additional attributes."""
        return "%s(%s)" % (self.__class__.__name__, ', '.join('%s=%r' % e for e in itertools.chain(
            iter(self.__dict.items()),
            ((f, getattr(self, f)) for f in self.__dict__  if not f.endswith('__dict'))
        )))


class ConfFile(ConfigDict):  # pylint: disable=too-few-public-methods
    """Utility class for key/value-based configuration files.
    Initializes from key/value file or from @keyvals dictionary.
    """
    def __init__(self, path, *keyvals):
        """
        @path:    full/absolute path of configuration file
        @keyvals: initial (key, val) pairs for this file
        """
        if keyvals:
            dict_ = collections.OrderedDict(keyvals)
        elif os.path.exists(path):
            dict_ = parse_key_value_from_fo(io.open(path, 'rt'))
        else:
            dict_ = {}

        # Handle shell variable references using '$var'.
        for k, v in dict_.items():
            m = re.match(r'\s*\$(\S+)', v)
            if m:
                ref = m.group(1)
                if ref in dict_:
                    dict_[k] = dict_[ref]
                else:
                    raise SyntaxError("Mismatched reference %s=%s in %s" % (k, v, path))

        ConfigDict.__init__(self, dict_)
        self.path = path

def syntropy_value(v):
    """Utility method to sanitize values into Syntropy strings."""
    if isinstance(v, type(None)):
        return "<none>"
    if isinstance(v, bool):
        return str(v).lower()
    if isinstance(v, (int, float)):
        return str(v)
    return v

if __name__ == '__main__':
    pass
