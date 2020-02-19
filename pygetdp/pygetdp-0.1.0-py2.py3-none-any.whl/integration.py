#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# License: MIT


from .getdp_object import GetDPObject, SimpleItem
from .helpers import _comment, make_args


class CaseLevel2(object):
    def __init__(self, GeoElement="", NumberOfPoints=0, comment=None):
        self.comment = ""
        self.code = ""
        self.items = []
        c = "Case  "
        c += "{ "
        if self.comment:
            c += _comment(comment)
        c += " \n      }"
        self.code += c

    def add(self, GeoElement="", NumberOfPoints=0):
        """Add an item and append it to :obj:`items` list.

        Parameters
        ----------
        GeoElement : str
            Element type, valid choices are:
            - `Line`: Line (2 nodes, 1 edge, 1 volume) (#1).
            - `Triangle`: Triangle (3 nodes, 3 edges, 1 facet, 1 volume) (#2).
            - `Quadrangle`: Quadrangle (4 nodes, 4 edges, 1 facet, 1 volume) (#3).
            - `Tetrahedron`: Tetrahedron (4 nodes, 6 edges, 4 facets, 1 volume) (#4).
            - `Hexahedron`: Hexahedron (8 nodes, 12 edges, 6 facets, 1 volume) (#5).
            - `Prism`: Prism (6 nodes, 9 edges, 5 facets, 1 volume) (#6).
            - `Pyramid`: Pyramid (5 nodes, 8 edges, 5 facets, 1 volume) (#7).
            - `Point`: Point (1 node) (#15).

        NumberOfPoints : int
            Number of points.

        Note
        ----
        `n` in (`#n`) is the type number of the element (see Input file format
        http://getdp.info/doc/texinfo/getdp.html#Input-file-format).


        Returns
        -------
        object
            An :obj:`SimpleItem` instance

        """
        case_item = SimpleItem(GeoElement=GeoElement, NumberOfPoints=NumberOfPoints)
        s = self.code
        n = 9
        self.code = s[:-n] + "\n       " + case_item.code + s[-n:]
        self.items.append(case_item)


class IntegrationItemCaseItem(object):
    def __init__(self, Type="Gauss", comment=None):
        """Item in Integration item case.

        Parameters
        ----------
        Type : str
            The type  of integration. Valid choices are:
                - "Gauss": Numerical Gauss integration.
                - "GaussLegendre": Numerical Gauss integration obtained by application of a
                multiplicative rule on the one-dimensional Gauss integration.
        comment : str
            An optional comment.
        """
        self.Type = Type
        self.comment = ""
        self.code = ""
        self.cases = []

        c = "{ " + " Type {} ;".format(Type)
        if self.comment:
            c += _comment(comment)
        c += " \n}"
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

    def add(self, GeoElement="", NumberOfPoints=0):
        """Add a case and append it to :obj:`cases` list.

        Returns
        -------
        object
            An :obj:`CaseLevel2` instance

        """
        case_item = CaseLevel2(GeoElement=GeoElement, NumberOfPoints=NumberOfPoints)
        s = self.code
        n = 7
        self.code = s[:-n] + "\n       " + case_item.code + s[-n:]
        self.cases.append(case_item)
        return case_item


class IntegrationItemCase(object):
    def __init__(self):
        """Case in Integration item.

        Parameters
        ----------
        comment : str
            An optional comment.

        """
        self.comment = ""
        self.code = ""
        self.items = []

        c = "Case { "
        if self.comment:
            c += _comment(self.comment)
        c += " \n}"
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

    def add(self, Type):
        """Add an item to this case and append it to :obj:`items` list.

        Returns
        -------
        object
            An :obj:`IntegrationItemCaseItem` instance

        """
        item = IntegrationItemCaseItem(Type)
        s = self.code
        n = 7
        self.code = s[:-n] + "\n       " + item.code + s[-n:]
        self.items.append(item)
        return item


class IntegrationItem(object):
    def __init__(self, Name, comment=None, **kwargs):
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

    def add(self):
        """Add a case and append it to :obj:`cases` list.

        Returns
        -------
        object
            An :obj:`IntegrationItemCase` instance

        """
        self._code0 = self.code
        case = IntegrationItemCase()
        self.cases.append(case)
        return case


class Integration(GetDPObject):
    """
    Defining integration methods.
    """

    name = "Integration"
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

    def add(self, Name, **kwargs):
        """Add an item to the :obj:`Integration` object and append it to :obj:`items` list.

        Returns
        -------
        object
            An :obj:`IntegrationItem` instance

        """
        self._content = self._content0
        bc = IntegrationItem(Name, **kwargs)
        self.items.append(bc)
        return bc


##
