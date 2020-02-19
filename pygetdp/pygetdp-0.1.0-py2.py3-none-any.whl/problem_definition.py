#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# License: MIT

import tempfile

from .__about__ import __version__
from .constraint import Constraint
from .formulation import Formulation
from .function import Function
from .functionspace import FunctionSpace
from .group import Group
from .helpers import _add_raw_code, _comment
from .integration import Integration
from .jacobian import Jacobian
from .postoperation import PostOperation
from .postprocessing import PostProcessing
from .resolution import Resolution


class Problem(object):
    def __init__(self, gmsh_major_version=None):
        super().__init__()
        self._GETDP_CODE = [
            "// This code was created by pygetdp v{}.\n".format(__version__)
        ]
        self.filename = None
        self.group = Group()
        self.function = Function()
        self.constraint = Constraint()
        self.functionspace = FunctionSpace()
        self.jacobian = Jacobian()
        self.integration = Integration()
        self.formulation = Formulation()
        self.resolution = Resolution()
        self.postprocessing = PostProcessing()
        self.postoperation = PostOperation()
        self.objects = [
            "group",
            "function",
            "constraint",
            "functionspace",
            "jacobian",
            "integration",
            "formulation",
            "resolution",
            "postprocessing",
            "postoperation",
        ]
        return

    def get_code(self):
        """Returns properly formatted GetDP code.
        """
        return "\n".join(self._GETDP_CODE)

    def add_raw_code(self, raw_code, newline=True):
        self._GETDP_CODE = [_add_raw_code(self.get_code(), raw_code, newline=newline)]

    def add_comment(self, comment, newline=True):
        self.add_raw_code(_comment(comment, newline=False), newline=newline)

    def make_file(self):
        for attr in self.objects:
            p = self.__getattribute__(attr)
            self._GETDP_CODE.append(p.code)

    def write_file(self):
        self.filename = self.filename or tempfile.mkdtemp()
        with open(self.filename, "w") as f:
            f.write(self.get_code())

    def include(self, incl_file):
        self._GETDP_CODE.append('\nInclude "{}";'.format(incl_file))
