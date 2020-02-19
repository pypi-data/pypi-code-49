"""
Package for proxy objects. Proxies are objects which act like other
objects, but can be converted to and from JSON, and subscribe to a
schema which is enforced during programmatic use as well as conversion.
"""
from ._ArrayProxy import ArrayProxy
from ._MapProxy import MapProxy
