#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# License: MIT


from .getdp_object import Base_, GetDPObject
from .helpers import _comment, make_args


class Quantity(Base_):
    def __init__(self, *args, **kwargs):
        super().__init__("Quantity", *args, **kwargs)


class EquationTerm(object):
    def __init__(self, term_type, term_equation, comment=None, **kwargs):
        self.comment = ""
        self.term_type = term_type
        self.term_equation = term_equation
        self.code = ""
        c = term_type + " { " + "[ {} ];".format(term_equation)
        for k, v in kwargs.items():
            self.__setattr__(k, v)
            c += " " + k + " " + make_args(v, sep=",") + ";"
        c += " } "
        if self.comment:
            c += _comment(comment)
        self.code += c


class Equation(object):
    def __init__(self, comment=None, **kwargs):
        self.comment = ""
        self.code = ""
        self.items = []
        for k, v in kwargs.items():
            self.__setattr__(k, v)
        c = "Equation { "
        if self.comment:
            c += _comment(comment)
        c += " \n        }"
        self.code += c

    def add(self, *args, **kwargs):
        item = EquationTerm(*args, **kwargs)
        s = self.code
        n = 10
        self.code = s[:-n] + "\n       " + item.code + s[-n:]
        self.items.append(item)
        return item


class FormulationItem(object):
    def __init__(self, Name, Type, comment=None, **kwargs):
        """Item in Integration.

        Parameters
        ----------
        Name : str
            The name of the integration item.
        comment : str
            An optional comment.
        Criterion : str
            Error criterion for adaptative methods.
        """
        self.Name = Name
        self.Type = Type
        self.comment = ""
        self._code = ""
        self.items = []
        c = "{" + " Name {}; Type {}".format(Name, Type)
        for k, v in kwargs.items():
            self.__setattr__(k, v)
            c += "; " + k + " " + make_args(v, sep=",")
        c += "; "
        if self.comment:
            c += _comment(comment)
        c += "\n}"
        self._code += c
        self._code0 = self._code

    @property
    def code(self):
        s = self._code0
        for case in self.items:
            self._code = s[:-2] + "\n     " + case.code + s[-2:]
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    def add_quantity(self, *args, **kwargs):
        """Add a case and append it to :obj:`cases` list.

        Returns
        -------
        object
            An :obj:`IntegrationItemCase` instance

        """
        self._code0 = self.code
        case = Quantity(*args, **kwargs)
        self.items.append(case)
        return case

    def add_equation(self, *args, **kwargs):
        """Add a case and append it to :obj:`cases` list.

        Returns
        -------
        object
            An :obj:`IntegrationItemCase` instance

        """
        self._code0 = self.code
        case = Equation(*args, **kwargs)
        self.items.append(case)
        return case


class Formulation(GetDPObject):
    """Building equations"""

    name = "Formulation"
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
        for const in self.items:
            self._content += const.code + "\n"
        self._content = self._content[:-1]
        return self._content

    #
    @content.setter
    def content(self, value):
        self._content = value

    def add(self, Name, Type, **kwargs):
        self._content = self._content0
        o = FormulationItem(Name, Type, **kwargs)
        self.items.append(o)
        return o

    #
