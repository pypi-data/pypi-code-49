#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# License: MIT


from .getdp_object import GetDPObject, ObjectItem


class Constraint(GetDPObject):
    """ Creates a constraint object: specifying constraints on function spaces and formulations
    """

    name = "Constraint"
    content = ""

    def __init__(self):
        self.comment = ""
        self._code = ""
        self.constraints = []
        self._content = ""
        self._content0 = ""
        super().__init__(name=self.name, content=self.content, comment=self.comment)

    @property
    def content(self):
        self._content = self._content0
        for const in self.constraints:
            self._content += const.code + "\n"
        self._content = self._content[:-1]
        return self._content

    #
    @content.setter
    def content(self, value):
        self._content = value

    def add(self, Name, **kwargs):
        """Add a constraint.

        Parameters
        ----------
        Name : str
            The name of the constraint.
        Type : str
            Type of constraint.
            Valid choices are:

            - `Assign`: To assign a value (e.g., for boundary condition).

            - `Init`: To give an initial value (e.g., initial value in a time domain analysis).
            If two values are provided (with `Value [ expression, expression ]`),
            the first value can be used using the `InitSolution1` operation.
            This is mainly useful for the Newmark time-stepping scheme.

            - `AssignFromResolution`: To assign a value to be computed by a pre-resolution.

            - `InitFromResolution`: To give an initial value to be computed by a pre-resolution.

            - `Network`: To describe the node connections of branches in a network.

            - `Link`: To define links between degrees of freedom in the constrained
            region with degrees of freedom in a “reference” region,
            with some coefficient. For example, to link the degrees of freedom in
            the contrained region `Left` with the degrees of freedom in the reference
            region `Right`, located `Pi` units to the right of the region `Left` along
            the X-axis, with the coeficient -1, one could write:

            .. code::

                { Name periodic;
                  Case {
                    { Region Left; Type Link ; RegionRef Right;
                      Coefficient -1; Function Vector[X[]+Pi, Y[], Z[]] ;
                      < FunctionRef XYZ[]; >
                    }
                  }
                }

            In this example, `Function` defines the mapping that translates the geometrical elements in the region `Left`
            by `Pi` units along the X-axis, so that they correspond with the elements in the
            reference region `Right`. For this mapping to work, the meshes of
            `Left` and `Right` must be identical. (The optional `FunctionRef`
            function allows to transform the reference region, useful e.g.
            to avoid generating overlapping meshes for rotational links.)

            - `LinkCplx`: To define complex-valued links between degrees of freedom.
            The syntax is the same as for constraints of type `Link`, but `Coeficient`
            can be complex.


        Returns
        -------
        object
            An :obj:`ObjectItem` instance.

        """
        self._content = self._content0
        bc = ObjectItem(Name, **kwargs)
        self.constraints.append(bc)
        return bc

    def assign(self, Name):
        return self.add(Name, Type="Assign")
