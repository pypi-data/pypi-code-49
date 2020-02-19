#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# License: MIT


from .getdp_object import Base_, GetDPObject
from .helpers import _comment, make_args


class PrintItem(object):
    def __init__(self, quantity, comment=None, **kwargs):
        self.comment = ""
        self.code = ""
        c = " Print [ {},".format(quantity)
        append = False
        for k, v in kwargs.items():
            if k == "append":
                append = v
        for k, v in kwargs.items():
            self.__setattr__(k, v)
            if k == "File":
                v = '"{}"'.format(v)
                if append:
                    v = " > " + v

            if k != "append":
                c += " " + k + " " + make_args(v, sep=",") + ","
        c = c[:-1]
        c += " ]; "
        if self.comment:
            c += _comment(comment)
        self.code += c


class POBase_(Base_):
    def add(self, quantity, *args, **kwargs):
        item = PrintItem(quantity, *args, **kwargs)
        s = self.code
        n = 10
        self.code = s[:-n] + "\n       " + item.code + s[-n:]
        self.items.append(item)


class PostopItem(object):
    def __init__(self, Name, comment=None, **kwargs):
        self.Name = Name
        self.comment = ""
        self._code = ""
        self.item = []
        c = "{" + " Name {}".format(Name)
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
        for case in self.item:
            self._code = s[:-2] + "\n     " + case.code + s[-2:]
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    def add(self, *args, **kwargs):
        self._code0 = self.code
        case = POBase_("Operation", *args, **kwargs)
        self.item.append(case)
        return case


class PostOperation(GetDPObject):
    """Exporting results"""

    name = "PostOperation"
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
        for item in self.items:
            self._content += item.code + "\n"
        self._content = self._content[:-1]
        return self._content

    #
    @content.setter
    def content(self, value):
        self._content = value

    def add(self, Name, NameOfPostProcessing, **kwargs):
        """Add a postprocessing.
        """
        self._content = self._content0
        postpro = PostopItem(Name, NameOfPostProcessing=NameOfPostProcessing, **kwargs)
        self.items.append(postpro)
        return postpro
