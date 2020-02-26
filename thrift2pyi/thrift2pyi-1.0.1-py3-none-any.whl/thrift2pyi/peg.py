# coding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re

from pypeg2 import blank, name, attr, Namespace, maybe_some, endl, List, optional, csl

Type = re.compile(r"[\w.\[\]]")
Value = re.compile(r"[\w\-'.\"\{\}]*")

cls = "# noinspection PyPep8Naming, PyShadowingNames", endl, "class "


class Annotation(object):
    grammar = blank, name(), ":", attr("type", Type)


class Annotations(Namespace):
    grammar = maybe_some(Annotation, endl)


class Parameter(object):
    grammar = attr("annotation", Annotation), "=", attr("default", Value)


class Parameters(List):
    grammar = optional(csl(Parameter))


class Init(object):
    grammar = blank, "def __init__(self, ", attr("params", Parameters), ") -> None:", endl, "  ...", endl


class Struct(object):
    grammar = cls, name(), "(object):", endl, attr("annotations", Annotations), attr("init", Init), endl, \
              "_Thrift2Pyi_", name(), "=", name(), endl


class Structs(List):
    grammar = maybe_some(Struct)


class Union(object):
    grammar = cls, name(), "(object):", endl, attr("annotations", Annotations), attr("init", Init), endl, \
              "_Thrift2Pyi_", name(), "=", name(), endl


class Unions(List):
    grammar = maybe_some(Struct)


class Exc(object):
    grammar = cls, name(), "(TException):", endl, attr("annotations", Annotations), attr("init", Init), endl, \
              "_Thrift2Pyi_", name(), "=", name(), endl


class Exceptions(List):
    grammar = maybe_some(Exc)


class Method(object):
    grammar = blank, "def ", name(), "(self, ", attr("params", Parameters), ") ->", attr("response", Type), \
              ":", endl, "  ...", endl


class Methods(Namespace):
    grammar = maybe_some(Method)


class Service(object):
    grammar = cls, name(), "(object):", endl, attr("methods", Methods), endl


class Services(List):
    grammar = maybe_some(Service)


class Modules(List):
    grammar = optional(csl(re.compile(r"[\w_*]+")))


class Import(object):
    grammar = "from", blank, attr("name", re.compile(r"[\w.]*")), blank, "import", \
              blank, attr("modules", Modules), endl


class Imports(Namespace):
    grammar = maybe_some(Import)


class KeyValue(object):
    grammar = blank, name(), "=", attr("value", Value), endl


class KeyValues(List):
    grammar = maybe_some(KeyValue)


class Const(object):
    grammar = name(), "=", attr("value", Value), endl


class Consts(List):
    grammar = maybe_some(Const)


class Enum(object):
    grammar = cls, name(), "(Enum):", endl, attr("kvs", KeyValues)


class Enums(List):
    grammar = maybe_some(Enum)


class PYI(object):
    grammar = "# coding:utf-8", endl, attr("imports", Imports), endl, attr("consts", Consts), \
              attr("enums", Enums), endl, attr("structs", Structs), endl, attr("exceptions", Exceptions), \
              endl, attr("services", Services)
