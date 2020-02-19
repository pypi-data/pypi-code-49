#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# License: MIT

"""
group
=========

Group: defining topological entities.
See GetDP online documentation at http://getdp.info/doc/texinfo/getdp.html#Group

.. autosummary::
   :toctree: generated/

"""


from .getdp_object import GetDPObject
from .helpers import make_args


class Group(GetDPObject):
    """Defining topological entities"""

    name = "Group"
    content = ""

    def __init__(self):
        self.comment = ""
        super().__init__(name=self.name, content=self.content, comment=self.comment)
        self.idlist = []

    def define(self, id="domain"):
        if isinstance(id, list):
            id = ", ".join([str(g) for g in id])
        c = "DefineGroup[{}".format(id)
        c += "];"
        self.content += c + "\n"
        return

    def add(self, id="domain", glist=[1], gtype="Region", comment=None, **kwargs):
        """
        Add an expression to the Group object. The default group type is ``Region``.
        """
        if id in self.idlist:
            raise ValueError("Identifier {} already in use.".format(id))
        glist = make_args(glist)

        c = "{} = {}[ {} ".format(id, gtype, glist)
        # if kwargs:
        for k, v in kwargs.items():
            if v is not None:
                c += ", " + k + " " + make_args(v)

        c += "];"
        self.content += c
        if comment:
            self.add_comment(comment, newline=False)
        self.content += "\n"
        self.idlist.append(id)
        return id

    def Region(self, *args, **kwargs):
        """ Regions in R1"""
        return self.add(*args, **kwargs, gtype="Region")

    def Global(self, *args, **kwargs):
        """
        Regions in R1 (variant of Region used with global BasisFunctions
        BF_Global and BF_dGlobal).
        """
        return self.add(*args, **kwargs, gtype="Global")

    def NodesOf(self, *args, Not=None, **kwargs):
        """ Nodes of elements of R1 (Not: but not those of R2)
        """
        return self.add(*args, **kwargs, gtype="NodesOf", Not=Not)

    def EdgesOf(self, *args, Not=None, **kwargs):
        """ Edges of elements of R1 (Not: but not those of R2)
        """
        return self.add(*args, **kwargs, gtype="EdgesOf", Not=Not)

    def FacetsOf(self, *args, Not=None, **kwargs):
        """ Facets of elements of R1 (Not: but not those of R2)
        """
        return self.add(*args, **kwargs, gtype="FacetsOf", Not=Not)

    def VolumesOf(self, *args, Not=None, **kwargs):
        """ Volumes of elements of R1 (Not: but not those of R2)
        """
        return self.add(*args, **kwargs, gtype="VolumesOf", Not=Not)

    def ElementsOf(
        self, *args, OnOneSideOf=None, OnPositiveSideOf=None, Not=None, **kwargs
    ):
        """ Elements of regions in R1

            - OnOneSideOf: only elements on one side of R2 (non-automatic, i.e., both sides if both in R1)
            - OnPositiveSideOf: only elements on positive (normal) side of R2
            - Not: but not those touching only its skin R3 (mandatory for free skins for correct separation of side layers)
        """
        return self.add(
            *args,
            **kwargs,
            gtype="ElementsOf",
            OnOneSideOf=OnOneSideOf,
            OnPositiveSideOf=OnPositiveSideOf,
            Not=Not
        )

    def GroupsOfNodesOf(self, *args, **kwargs):
        """ Groups of nodes of elements of R1 (a group is associated with each region)
        """
        return self.add(*args, **kwargs, gtype="GroupsOfNodesOf")

    def GroupsOfEdgesOf(self, *args, InSupport=None, **kwargs):
        """Groups of edges of elements of R1 (a group is associated with each region).
         < InSupport: in a support R2 being a group of type ElementOf, i.e., containing elements >.
        """
        return self.add(*args, **kwargs, gtype="GroupsOfEdgesOf", InSupport=InSupport)

    def GroupsOfEdgesOnNodesOf(self, *args, Not=None, **kwargs):
        """Groups of edges incident to nodes of elements of R1 (a group is associated with each node).
            < Not: but not those of R2) >.
        """
        return self.add(*args, **kwargs, gtype="GroupsOfEdgesOnNodesOf", Not=Not)

    def GroupOfRegionsOf(self, *args, **kwargs):
        """Single group of elements of regions in R1
         (with basis function BF_Region just one DOF is created for all elements of R1).
        """
        return self.add(*args, **kwargs, gtype="GroupOfRegionsOf")

    def EdgesOfTreeIn(self, *args, StartingOn=None, **kwargs):
        """Edges of a tree of edges of R1
            < StartingOn: a complete tree is first built on R2 >.
        """
        return self.add(*args, **kwargs, gtype="EdgesOfTreeIn", StartingOn=StartingOn)

    def FacetsOfTreeIn(self, *args, StartingOn=None, **kwargs):
        """Facets of a tree of facets of R1
            < StartingOn: a complete tree is first built on R2 >.
        """
        return self.add(*args, **kwargs, gtype="FacetsOfTreeIn", StartingOn=StartingOn)

    def DualNodesOf(self, *args, **kwargs):
        """Dual nodes of elements of R1"""
        return self.add(*args, **kwargs, gtype="DualNodesOf")

    def DualEdgesOf(self, *args, **kwargs):
        """Dual edges of elements of R1"""
        return self.add(*args, **kwargs, gtype="DualEdgesOf")

    def DualFacetsOf(self, *args, **kwargs):
        """Dual facets of elements of R1"""
        return self.add(*args, **kwargs, gtype="DualFacetsOf")

    def DualVolumesOf(self, *args, **kwargs):
        """Dual volumes of elements of R1"""
        return self.add(*args, **kwargs, gtype="DualVolumesOf")
