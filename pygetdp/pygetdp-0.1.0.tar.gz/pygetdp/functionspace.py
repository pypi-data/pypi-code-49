#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# License: MIT

"""
functionspace
==============

Building function spaces
See GetDP online documentation at http://getdp.info/doc/texinfo/getdp.html#FunctionSpace
"""


from .getdp_object import Base_, GetDPObject
from .helpers import _comment, make_args


class BasisFunction(Base_):
    def __init__(self, *args, **kwargs):
        super().__init__("BasisFunction", *args, **kwargs)


class Constraint(Base_):
    def __init__(self, *args, **kwargs):
        super().__init__("Constraint", *args, **kwargs)


class GlobalQuantity(Base_):
    def __init__(self, *args, **kwargs):
        super().__init__("GlobalQuantity", *args, **kwargs)


class FunctionSpaceItem(object):
    def __init__(self, Name, comment=None, **kwargs):
        self.Name = Name
        self.comment = ""
        self._code = ""
        self.bf = BasisFunction()
        self.globalq = GlobalQuantity()
        self.constraint = Constraint()
        c = "{" + " Name {}".format(Name)
        for k, v in kwargs.items():
            self.__setattr__(k, v)
            c += "; " + k + " " + make_args(v, sep=",")
        c += "; "
        if self.comment:
            c += _comment(comment)
        c += "}"
        self._code += c
        self._code0 = self._code

    @property
    def code(self):
        s = self._code0
        itemcode = "       "
        for item in [self.bf, self.globalq, self.constraint]:
            if len(item) > 0:
                itemcode += item.code + "\n       "
                self._code = "   " + s[:-1] + "\n" + itemcode + s[-1:]
        self._code = self._code[:-5] + self._code[-1:]
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    def add_basis_function(self, *args, **kwargs):
        self._code = self._code0
        self.bf.add(*args, **kwargs)
        return self.bf

    def add_global_quantity(self, *args, **kwargs):
        self._code = self._code0
        self.globalq.add(*args, **kwargs)
        return self.globalq

    def add_constraint(self, *args, **kwargs):
        self._code = self._code0
        self.constraint.add(*args, **kwargs)
        return self.constraint


class FunctionSpace(GetDPObject):
    """
    Building function spaces
    """

    name = "FunctionSpace"
    content = ""

    def __init__(self):
        self.comment = ""
        self._code = ""
        self.items = []
        self._content = ""
        self._content0 = ""
        super().__init__(name=self.name, content=self.content, comment=self.comment)

    @property
    def content(self):
        self._content = self._content0
        for s in self.items:
            self._content += s.code + "\n"
        # self._content = self._content[:-1]
        return self._content

    #
    @content.setter
    def content(self, value):
        self._content = value

    def add(self, Name, **kwargs):
        self._content = self._content0
        fsi = FunctionSpaceItem(Name, **kwargs)
        self.items.append(fsi)
        return fsi
