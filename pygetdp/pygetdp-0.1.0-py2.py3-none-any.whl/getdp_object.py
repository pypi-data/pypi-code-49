#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# License: MIT


from .helpers import _add_raw_code, _comment, make_args


class GetDPObject(object):
    """
    Base Getdp object


    """

    def __init__(self, name="Group", content="", comment=None):
        """Short summary.

        Parameters
        ----------
        name : str
            Name of the object.
        content : str
            Content of the object.
        comment : str
            A comment.

        """
        self.name = name
        self.content = content
        self.comment = comment
        self.indent = " " * 4  # len(self.name)
        return

    @property
    def code(self):
        code_ = []
        code_.append("{}{{".format(self.name))
        [code_.append(_) for _ in self.content.splitlines()]
        code_.append("}")
        code_ = ("\n" + self.indent).join(code_) + "\n"
        if self.comment:
            code_ = _comment(self.comment) + "\n" + code_
        return code_

    def add_raw_code(self, raw_code, newline=True):
        self.content = _add_raw_code(self.content, raw_code, newline=newline)

    def add_comment(self, comment, newline=True):
        self.add_raw_code(_comment(comment, newline=False), newline=newline)


class SimpleItem(object):
    def __init__(self, comment=None, **kwargs):
        self.comment = ""
        self.code = ""
        c = " { "
        for k, v in kwargs.items():
            self.__setattr__(k, v)
            c += " " + k + " " + make_args(v, sep=",") + ";"
        c += " } "
        if self.comment:
            c += _comment(comment)
        self.code += c


class Base_(object):
    def __init__(self, header, comment=None, **kwargs):
        self.comment = ""
        self.code = ""
        self.items = []
        for k, v in kwargs.items():
            self.__setattr__(k, v)
        c = header + " { "
        if self.comment:
            c += _comment(comment)
        c += " \n        }"
        self.code += c
        self._code0 = self.code

    def __len__(self):
        return len(self.items)

    def add(self, *args, **kwargs):
        item = SimpleItem(*args, **kwargs)
        s = self.code
        n = 10
        self.code = s[:-n] + "\n       " + item.code + s[-n:]
        self.items.append(item)


class ObjectItem(object):
    def __init__(self, Name, comment=None, **kwargs):
        self.Name = Name
        self.comment = ""
        self._code = ""
        self.cases = []
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
        for case in self.cases:
            self._code = s[:-2] + "\n     " + case.code + s[-2:]
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    def add(self, *args, **kwargs):
        self._code0 = self.code
        case = Case_(*args, **kwargs)
        self.cases.append(case)
        return case


class CaseItem_(SimpleItem):
    def __init__(self, Region, comment=None, *args, **kwargs):
        self.Region = Region
        super().__init__(*args, **kwargs)
        self.code = "{" + " Region {};".format(Region) + self.code[3:]


class Case_(object):
    def __init__(self, Name=None, comment=None, **kwargs):
        self.Name = Name
        self.comment = ""
        self.code = ""
        self.case_items = []
        for k, v in kwargs.items():
            self.__setattr__(k, v)
        case_name = Name or ""
        c = "Case {} ".format(case_name)
        c += "{ "
        if self.comment:
            c += _comment(comment)
        c += " \n     }"
        self.code += c

    def add(self, *args, **kwargs):
        case_item = CaseItem_(*args, **kwargs)
        s = self.code
        n = 7
        self.code = s[:-n] + "\n       " + case_item.code + s[-n:]
        self.case_items.append(case_item)
