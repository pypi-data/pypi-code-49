#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# License: MIT

"""
function
=========

Defining global and piecewise expressions

"""

from .getdp_object import GetDPObject
from .helpers import (
    _is_complex,
    _is_list,
    _is_tuple,
    make_args,
    py2getdplist,
    replace_formula,
)


class Function(GetDPObject):
    """
    Defining global and piecewise expressions

    Parameters
    ----------
    description : str (optional)
        Comment to describe the object
    """

    name = "Function"
    content = ""

    def __init__(self):
        self.comment = ""
        super().__init__(name=self.name, content=self.content, comment=self.comment)
        self.idlist = []

    def define(self, name="f"):
        if isinstance(name, list):
            name = ", ".join([str(g) for g in name])
        c = "DefineFunction[{}".format(name)
        c += "];"
        self.content += c + "\n"
        return

    def add(self, name="f", expression=None, region=None, arguments=None, comment=None):
        arguments = arguments or []
        # arguments = make_args(arguments)

        if _is_list(expression):
            c = "{} = {} ;".format(name, py2getdplist(expression))
            self.content += c
            self.content += "\n"
            return name

        if region:
            region = make_args(region)
        else:
            region = region or ""

        if not region:
            region = ""
        if _is_list(region):
            region = "{" + ",".join(region) + "}"

        if arguments:
            replacement = ["${}".format(i + 1) for i in range(len(arguments))]
            expression = replace_formula(expression, arguments, replacement)
        c = "{}[{}] = {} ".format(name, region, expression)

        c += ";"
        self.content += c
        if comment:
            self.add_comment(comment, newline=False)
        self.content += "\n"
        self.idlist.append(name)
        return name

    def add_params(self, params):
        """Add constant parameters.

        Parameters
        ----------
        params : dict
            A dictionary of parameters. The keys give the name of the parameter
            and the values can be str, float, complex, bool, or a tuple with (value, "comment")
            to add a description of the parameter
        """
        for key, value in params.items():
            comment = None
            if _is_tuple(value):
                if len(value) > 1:
                    comment = value[1]
                    value = value[0]
            self.constant(name=key, expression=value, comment=comment)

    def constant(self, name="c", expression=None, comment=None):
        if _is_complex(expression):
            expression = self.Complex(expression.real, expression.imag)

        c = "{} = {} ".format(name, expression)
        c += ";"
        self.content += c
        if comment:
            self.add_comment(comment, newline=False)
        self.content += "\n"
        self.idlist.append(name)
        return name

    ### Math functions

    def Exp(self, expression):
        """Exponential function: e^expression."""
        return "Exp[{}]".format(expression)

    def Log(self, expression):
        """Natural logarithm: ln(expression), expression>0."""
        return "Log[{}]".format(expression)

    def Log10(self, expression):
        """Base 10 logarithm: log10(expression), expression>0."""
        return "Log10[{}]".format(expression)

    def Sqrt(self, expression):
        """Square root, expression>=0."""
        return "Sqrt[{}]".format(expression)

    def Sin(self, expression):
        """Sine of expression."""
        return "Sin[{}]".format(expression)

    def Asin(self, expression):
        """Arc sine (inverse sine) of expression in [-Pi/2,Pi/2], expression in [-1,1] (real valued only)."""
        return "Asin[{}]".format(expression)

    def Cos(self, expression):
        """Cosine of expression."""
        return "Cos[{}]".format(expression)

    def Acos(self, expression):
        """Arc cosine (inverse cosine) of expression in [0,Pi], expression in [-1,1] (real valued only)."""
        return "Acos[{}]".format(expression)

    def Tan(self, expression):
        """Tangent of expression."""
        return "Tan[{}]".format(expression)

    def Atan(self, expression):
        """Arc tangent (inverse tangent) of expression in [-Pi/2,Pi/2] (real valued only)."""
        return "Atan[{}]".format(expression)

    def Atan2(self, expression):
        """Arc tangent (inverse tangent) of the first expression divided by the second, in [-Pi,Pi] (real valued only)."""
        return "Atan2[{}]".format(expression)

    def Sinh(self, expression):
        """Hyperbolic sine of expression."""
        return "Sinh[{}]".format(expression)

    def Cosh(self, expression):
        """Hyperbolic cosine of expression."""
        return "Cosh[{}]".format(expression)

    def Tanh(self, expression):
        """Hyperbolic tangent of the real valued expression."""
        return "Tanh[{}]".format(expression)

    def TanhC2(self, expression):
        """Hyperbolic tangent of a complex valued expression."""
        return "TanhC2[{}]".format(expression)

    def Fabs(self, expression):
        """Absolute value of expression (real valued only)."""
        return "Fabs[{}]".format(expression)

    def Abs(self, expression):
        """Absolute value of expression."""
        return "Abs[{}]".format(expression)

    def Floor(self, expression):
        """Rounds downwards to the nearest integer that is not greater than expression (real valued only)."""
        return "Floor[{}]".format(expression)

    def Ceil(self, expression):
        """Rounds upwards to the nearest integer that is not less than expression (real valued only)."""
        return "Ceil[{}]".format(expression)

    def Fmod(self, expression1, expression2):
        """Remainder of the division of the first expression by the second, with the sign of the first (real valued only)."""
        return "Fmod[{},{}]".format(expression1, expression2)

    def Min(self, expression1, expression2):
        "Minimum of the two (scalar) expressions (real valued only)."
        return "Min[{},{}]".format(expression1, expression2)

    def Max(self, expression1, expression2):
        "Maximum of the two (scalar) expressions (real valued only)."
        return "Max[{},{}]".format(expression1, expression2)

    def Sign(self, expression):
        """-1 for expression less than zero and 1 otherwise (real valued only)."""
        return "Sign[{}]".format(expression)

    def Jn(self, expression):
        """Returns the Bessel function of the first kind of order given by the first expression for the value of the second expression (real valued only)."""
        return "Jn[{}]".format(expression)

    def dJn(self, expression):
        """Returns the derivative of the Bessel function of the first kind of order given by the first expression for the value of the second expression (real valued only)."""
        return "dJn[{}]".format(expression)

    def Yn(self, expression):
        """Returns the Bessel function of the second kind of order given by the first expression for the value of the second expression (real valued only)."""
        return "Yn[{}]".format(expression)

    def dYn(self, expression):
        """Returns the derivative of the Bessel function of the second kind of order given by the first expression for the value of the second expression (real valued only)."""
        return "dYn[{}]".format(expression)

    ### Extended math functions

    def Cross(self, expression1, expression2):
        """Cross product of the two arguments; expression must be a vector."""
        return "Cross[{},{}]".format(expression1, expression2)

    def Hypot(self, expression1, expression2):
        """Square root of the sum of the squares of its arguments."""
        return "Hypot[{},{}]".format(expression1, expression2)

    def Norm(self, expression):
        """Absolute value if expression is a scalar; euclidian norm if expression is a vector."""
        return "Norm[{}]".format(expression)

    def SquNorm(self, expression):
        """Square norm: Norm[expression]^2."""
        return "SquNorm[{}]".format(expression)

    def Unit(self, expression):
        """Normalization: expression/Norm[expression]. Returns 0 if the norm is smaller than 1.e-30."""
        return "Unit[{}]".format(expression)

    def Transpose(self, expression):
        """Transposition; expression must be a tensor."""
        return "Transpose[{}]".format(expression)

    def Inv(self, expression):
        """Inverse of the tensor expression."""
        return "Inv[{}]".format(expression)

    def Det(self, expression):
        """Determinant of the tensor expression."""
        return "Det[{}]".format(expression)

    def Rotate(self, object_to_rotate, rot_x, rot_y, rot_z):
        """Rotation of a vector or tensor given by the first expression by the angles
        in radians given by the last three expression values around the x-, y- and z-axis."""
        return "Rotate[{},{},{},{}]".format(object_to_rotate, rot_x, rot_y, rot_z)

    def TTrace(self, tensor):
        """Trace; expression must be a tensor."""
        return "TTrace[{}]".format(tensor)

    def Cos_wt_p(self, omega, phase):
        """The first parameter represents the angular frequency and the second
        represents the phase. If the type of the current system is Real,
        F_Cos_wt_p[]{w,p} is identical to Cos[w*$Time+p]. If the type of the current
        system is Complex, it is identical to Complex[Cos[p],Sin[p]]."""
        return "Cos_wt_p[]{{{},{}}}".format(omega, phase)

    def Sin_wt_p(self, omega, phase):
        """The first parameter represents the angular frequency and the second
        represents the phase. If the type of the current system is Real,
        F_Sin_wt_p[]{w,p} is identical to Sin[w*$Time+p]. If the type of the current
        system is Complex, it is identical to Complex[Sin[p],-Cos[p]]."""
        return "Sin_wt_p[]{{{},{}}}".format(omega, phase)

    def Period(self, expression, expression_cst):
        """Fmod[expression,expression-cst] + (expression<0 ? expression-cst : 0);
        the result is always in [0,expression-cst[."""
        return "Period[{}]{{{}}}".format(expression, expression_cst)

    def Interval(self, *args):
        """Not documented yet."""
        return "Period[{},{},{}]{{{},{},{}}}".format(*args)

    ### Green functions

    def Laplace(self, dim):
        """r/2, 1/(2*Pi)*ln(1/r), 1/(4*Pi*r)."""
        return "Laplace[]{{{}}}".format(dim)

    def GradLaplace(self, dim):
        """Gradient of Laplace relative to the destination point ($X, $Y, $Z)."""
        return "GradLaplace[]{{{}}}".format(dim)

    def Helmholtz(self, dim, k0):
        """exp(j*k0*r)/(4*Pi*r), where k0 is given by the second parameter."""
        return "Helmholtz[]{{{0},{1}}}".format(dim, k0)

    def GradHelmholtz(self, dim, k0):
        """Gradient of Helmholtz relative to the destination point ($X, $Y, $Z)."""
        return "GradHelmholtz[]{{{0},{1}}}".format(dim, k0)

    ### Type manipulation functions

    def Complex(self, *args):
        """Creates a (multi-harmonic) complex expression from
        an number of real-valued expressions.
        The number of expressions in expression-list must be even. """
        a = [str(_) for _ in args]
        a = ", ".join(a)
        return "Complex[" + a + "]"

    def Re(self, z):
        """Takes the real part of a complex-valued expression."""
        return "Re[{}]".format(z)

    def Im(self, z):
        """Takes the imaginary part of a complex-valued expression."""
        return "Im[{}]".format(z)

    def Conj(self, z):
        """    Computes the conjugate of a complex-valued expression.
        """
        return "Conj[{}]".format(z)

    def Cart2Pol(self, expr):
        """
            Converts the cartesian form (reale, imaginary) of a complex-valued expression into polar form (amplitude, phase [radians]).
        """
        return "Cart2Pol[{}]".format(expr)

    def Vector(self, scalar0, scalar1, scalar2):
        """Creates a vector from 3 scalars."""
        return "Vector[{},{},{}]".format(scalar0, scalar1, scalar2)

    def Tensor(
        self,
        scalar0,
        scalar1,
        scalar2,
        scalar3,
        scalar4,
        scalar5,
        scalar6,
        scalar7,
        scalar8,
    ):

        """Creates a second-rank tensor of order 3 from 9 scalars, by row:
            [ scalar0 scalar1 scalar2 ]   [ CompXX CompXY CompXZ ]
        T = [ scalar3 scalar4 scalar5 ] = [ CompYX CompYY CompYZ ]
            [ scalar6 scalar7 scalar8 ]   [ CompZX CompZY CompZZ ]
        """
        return "Tensor[{},{},{},{},{},{},{},{},{}]".format(
            scalar0,
            scalar1,
            scalar2,
            scalar3,
            scalar4,
            scalar5,
            scalar6,
            scalar7,
            scalar8,
        )

    def TensorV(self, vector0, vector1, vector2):
        """Creates a second-rank tensor of order 3 from 3 row vectors:
            [ vector0 ]
        T = [ vector1 ]
            [ vector2 ]
        """
        return "TensorV[{},{},{}]".format(vector0, vector1, vector2)

    def TensorSym(self, scalar0, scalar1, scalar2, scalar3, scalar4, scalar5):
        """Creates a symmetrical second-rank tensor of order 3 from 6 scalars.
            [ scalar0 scalar1 scalar2 ]
        T = [ scalar1 scalar3 scalar4 ]
            [ scalar2 scalar4 scalar5 ]

        """
        return "TensorSym[{}]".format(
            scalar0, scalar1, scalar2, scalar3, scalar4, scalar5
        )

    def TensorDiag(self, scalar0, scalar1, scalar2):
        """Creates a diagonal second-rank tensor of order 3 from 3 scalars
        """
        return "TensorDiag[{},{},{}]".format(scalar0, scalar1, scalar2)

    def SquDyadicProduct(self, vector):
        """Dyadic product of the vector given by expression with itself."""
        return "SquDyadicProduct[{}]".format(vector)

    def CompX(self, vector):
        """Gets the X component of a vector."""
        return "CompX[{}]".format(vector)

    def CompY(self, vector):
        """Gets the Y component of a vector."""
        return "CompY[{}]".format(vector)

    def CompZ(self, vector):
        """Gets the Z component of a vector."""
        return "CompZ[{}]".format(vector)

    def CompXX(self, tensor):
        """Gets the XX component of a tensor."""
        return "CompXX[{}]".format(tensor)

    def CompYY(self, tensor):
        """Gets the YY component of a tensor."""
        return "CompYY[{}]".format(tensor)

    def CompZZ(self, tensor):
        """Gets the ZZ component of a tensor."""
        return "CompZZ[{}]".format(tensor)

    def CompXY(self, tensor):
        """Gets the XY component of a tensor."""
        return "CompXY[{}]".format(tensor)

    def CompYX(self, tensor):
        """Gets the YX component of a tensor."""
        return "CompYX[{}]".format(tensor)

    def CompXZ(self, tensor):
        """Gets the XZ component of a tensor."""
        return "CompXZ[{}]".format(tensor)

    def CompZX(self, tensor):
        """Gets the ZX component of a tensor."""
        return "CompZX[{}]".format(tensor)

    def CompYZ(self, tensor):
        """Gets the YZ component of a tensor."""
        return "CompYZ[{}]".format(tensor)

    def CompZY(self, tensor):
        """Gets the ZY component of a tensor."""
        return "CompZY[{}]".format(tensor)

    def Cart2Sph(self, vector):
        """Gets the tensor for transformation of vector from cartesian to spherical coordinates."""
        return "Cart2Sph[{}]".format(vector)

    def Cart2Cyl(self, vector):
        """Gets the tensor for transformation of vector from cartesian to cylindric coordinates.
        E.g. to convert a vector with (x,y,z)-components to one with (radial, tangential, axial)-components:
        Cart2Cyl[XYZ[]] * vector"""
        return "Cart2Cyl[{}]".format(vector)

    def UnitVectorX(self):
        """Creates a unit vector in x-direction."""
        return "UnitVectorX[]"

    def UnitVectorY(self):
        """Creates a unit vector in y-direction."""
        return "UnitVectorY[]"

    def UnitVectorZ(self):
        """Creates a unit vector in z-direction."""
        return "UnitVectorZ[]"

    ## Coordinate functions

    def X(self):
        """Gets the X coordinate."""
        return "X[]"

    def Y(self):
        """Gets the Y coordinate."""
        return "Y[]"

    def Z(self):
        """Gets the Z coordinate."""
        return "Z[]"

    def XYZ(self):
        """Gets X, Y and Z in a vector."""
        return "XYZ[]"

    ## Miscellaneous functions

    def Printf(self, expression):
        """Prints the value of expression when evaluated. (MPI_Printf can be use instead,
         to print the message for all MPI ranks.)
        """
        return "Printf[{}]".format(expression)

    def Rand(self, expression):
        """Returns a pseudo-random number in [0, expression]."""
        return "Rand[{}]".format(expression)

    def Normal(self):
        """Computes the normal to the element."""
        return "Normal[]"

    def NormalSource(self):
        """Computes the normal to the source element (only valid in a quantity of Integral type)."""
        return "NormalSource[]"

    def Tangent(self):
        """Computes the tangent to the element (only valid for line elements)."""
        return "Tangent[]"

    def TangentSource(self):
        """Computes the tangent to the source element (only valid in a quantity of
        Integral type and only for line elements).
        """
        return "TangentSource[]"

    def ElementVol(self):
        """Computes the element’s volume."""
        return "ElementVol[]"

    def SurfaceArea(self, expression_cst_list):
        """Computes the area of the physical surfaces in expression_cst_list
        or of the actual surface if expression_cst_list is empty.
        """
        return "SurfaceArea[]{{{}}}".format(expression_cst_list)

    def GetVolume(self):
        """Computes the volume of the actual physical group."""
        return "GetVolume[]"

    def CompElementNum(self):
        """Returns 0 if the current element and the current source element are identical."""
        return "CompElementNum[]"

    def GetNumElements(self, expression_cst_list):
        """Counts the elements of physical numbers in expression_cst_list or of the actual region if expression_cst_list is empty."""
        return "GetNumElements[]{{{}}}".format(expression_cst_list)

    def ElementNum(self):
        """Returns the tag (number) of the current element."""
        return "ElementNum[]"

    def QuadraturePointIndex(self):
        """Returns the index of the current quadrature point."""
        return "QuadraturePointIndex[]"

    def AtIndex(self, expression, expression_cst_list):
        """Returns the i-th entry of expression_cst_list. This can be used to get an
        element in a list, using an index that is computed at runtime."""
        return "AtIndex[{}]{{{}}}".format(expression, expression_cst_list)

    def InterpolationLinear(self, expression, expression_cst_list):
        """Linear interpolation of points. The number of constant expressions in expression_cst_list must be even."""
        return "InterpolationLinear[{}]{{{}}}".format(expression, expression_cst_list)

    def dInterpolationLinear(self, expression, expression_cst_list):
        """Derivative of linear interpolation of points. The number of constant expressions in expression_cst_list must be even."""
        return "dInterpolationLinear[{}]{{{}}}".format(expression, expression_cst_list)

    def InterpolationBilinear(self, expression1, expression2, expression_cst_list):
        """Bilinear interpolation of a table based on two variables."""
        return "InterpolationBilinear[{}, {}]{{{}}}".format(
            expression1, expression2, expression_cst_list
        )

    def dInterpolationBilinear(self, expression1, expression2, expression_cst_list):
        """Derivative of bilinear interpolation of a table based on two variables. The result is a vector."""
        return "dInterpolationBilinear[{}, {}]{{{}}}".format(
            expression1, expression2, expression_cst_list
        )

    def InterpolationAkima(self, expression, expression_cst_list):
        """Akima interpolation of points. The number of constant expressions in expression_cst_list must be even."""
        return "InterpolationAkima[{}]{{{}}}".format(expression, expression_cst_list)

    def dInterpolationAkima(self, expression, expression_cst_list):
        """Derivative of Akima interpolation of points. The number of constant expressions in expression_cst_list must be even.
        """
        return "dInterpolationAkima[{}]{{{}}}".format(expression, expression_cst_list)

    def Order(self, quantity):
        """Returns the interpolation order of the quantity."""
        return "Order[{}]".format(quantity)

    def Field(self, expression, expression_cst_list=None):
        """Evaluate the last one of the fields (“views”) loaded with GmshRead (see Types for Resolution),
        at the point expression. Common usage is thus Field[XYZ[]].
        If 'expression_cst_list' is not empty, this evaluates all the fields corresponding to the tags in the list,
        and sum all the values. A field having no value at the given position does
        not produce an error: its contribution to the sum is simply zero.
        """
        if expression_cst_list:
            return "Field[{}]{{{}}}".format(expression, expression_cst_list)
        else:
            return "Field[{}]".format(expression)

    def ScalarField(
        self, expression, expression_cst_list, timestep=0, elmt_interp=True
    ):
        """Idem, but consider only real-valued scalar fields.
        A second optional argument is the value of the time step.
        A third optional argument is a boolean flag to indicate that the interpolation should
        be performed (if possible) in the same element as the current element.
        """
        return "ScalarField[{0}, {2}, {3}]{{{1}}}".format(
            expression, expression_cst_list, timestep, int(elmt_interp)
        )

    def VectorField(
        self, expression, expression_cst_list, timestep=0, elmt_interp=True
    ):
        """Idem, but consider only real-valued vector fields. Optional arguments are treated in the same way as for ScalarField.
        """
        return "VectorField[{0}, {2}, {3}]{{{1}}}".format(
            expression, expression_cst_list, timestep, int(elmt_interp)
        )

    def TensorField(
        self, expression, expression_cst_list, timestep=0, elmt_interp=True
    ):
        """Idem, but consider only real-valued tensor fields. Optional arguments are treated in the same way as for ScalarField.
        """
        return "TensorField[{0}, {2}, {3}]{{{1}}}".format(
            expression, expression_cst_list, timestep, int(elmt_interp)
        )

    def ComplexScalarField(
        self, expression, expression_cst_list, timestep=0, elmt_interp=True
    ):
        """Idem, but consider only complex-valued scalar fields. Optional arguments are treated in the same way as for ScalarField.
        """
        return "ComplexScalarField[{0}, {2}, {3}]{{{1}}}".format(
            expression, expression_cst_list, timestep, int(elmt_interp)
        )

    def ComplexVectorField(
        self, expression, expression_cst_list, timestep=0, elmt_interp=True
    ):
        """Idem, but consider only complex-valued vector fields. Optional arguments are treated in the same way as for ScalarField.
        """
        return "ComplexVectorField[{0}, {2}, {3}]{{{1}}}".format(
            expression, expression_cst_list, timestep, int(elmt_interp)
        )

    def ComplexTensorField(
        self, expression, expression_cst_list, timestep=0, elmt_interp=True
    ):
        """Idem, but consider only complex-valued tensor fields. Optional arguments are treated in the same way as for ScalarField.
        """
        return "ComplexTensorField[{0}, {2}, {3}]{{{1}}}".format(
            expression, expression_cst_list, timestep, int(elmt_interp)
        )

    def GetCpuTime(self):
        """Returns current CPU time, in seconds (total amount of time spent executing in user mode since GetDP was started).
        """
        return "GetCpuTime[]"

    def GetWallClockTime(self):
        """Returns the current wall clock time, in seconds (total wall clock time since GetDP was started)."""
        return "GetWallClockTime[]"

    def GetMemory(self):
        """Returns the current memory usage, in megabytes (maximum resident set size)."""
        return "GetMemory[]"

    def SetNumberRunTime(self, expression, char_expression):
        """Sets the char-expression ONELAB variable at run-time to expression."""
        return 'SetNumberRunTime[{}]{{"{}"}}'.format(expression, char_expression)

    def GetNumberRunTime(self, char_expression, expression=None):
        """Gets the value of the char-expression ONELAB variable at run-time.
        If the optional expression is provided, it is used as a default value if ONELAB is not available.
        """
        return 'GetNumberRunTime[{}]{{"{}"}}'.format(expression, char_expression)

    def SetVariable(self, expression, variable_id):
        """Sets the value of the runtime variable $variable-id to the value of the
        first expression, and returns this value.
        If optional expressions are provided, they are appended to the variable name, separated by _."""
        if hasattr(expression, "__len__") and len(expression) > 1:
            e1 = ""
            for _ in expression:
                e1 += str(_) + ","
            expression = e1[:-1]
        return "SetVariable[{}]{{${}}}".format(expression, variable_id)

    def GetVariable(self, expression, variable_id):
        """Gets the value of the runtime variable $variable-id.
        If the optional expressions are provided, they are appended to the variable name,
        separated by _."""
        if hasattr(expression, "__len__") and len(expression) > 1:
            e1 = ""
            for _ in expression:
                e1 += str(_) + ","
            expression = e1[:-1]
        return "GetVariable[{}]{{${}}}".format(expression, variable_id)

    def ValueFromIndex(self, expression_cst_list):
        """Treats expression_cst_list as a map of (entity, value) pairs.
        Useful to specify nodal or element-wise constraints, where entity
        is the node (mesh vertex) or element number (tag)."""
        return "ValueFromIndex[]{{{}}}".format(expression_cst_list)

    def VectorFromIndex(self, expression_cst_list):
        """Same ValueFromIndex, but with 3 scalar values per entity."""
        return "VectorFromIndex[]{{{}}}".format(expression_cst_list)

    def ValueFromTable(self, expression, char_expression):
        """Accesses the map char-expression created by a NodeTable or
        ElementTable PostOperation. If the map is not available (e.g. in pre-processing),
        or if the entity is not found in the map, use expression as default value.
        Useful to specify nodal or element-wise constraints, where entity is the
        node (mesh vertex) or element number (tag)."""
        return 'ValueFromTable[{}]{{"{}"}}'.format(expression, char_expression)
