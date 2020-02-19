#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# License: MIT


import inspect
from functools import wraps

from pygetdp.getdp_object import Base_, GetDPObject
from pygetdp.helpers import _comment, _is_list, make_args, py2getdplist


def myself():
    return inspect.stack()[1][3]


def add_code(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        s = func(self, *args, **kwargs)
        self.code = self.code[:-2] + s + "; " + self.code[-2:]
        return s

    return wrapper


class Operation(Base_):
    def __init__(self, *args, **kwargs):
        self.loops = []
        self._code0 = ""
        super().__init__("Operation", *args, **kwargs)
        # self._code0 = super().code

    @add_code
    def Generate(self, system_id):
        """Generate the system of equations system_id."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def Solve(self, system_id):
        """Solve the system of equations system_id."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def SolveAgain(self, system_id):
        """Save as Solve, but reuses the preconditionner when called multiple times."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def SetGlobalSolverOptions(self, char_expression):
        """Set global PETSc solver options (with the same syntax as PETSc options specified on the command line, e.g. '-ksp_type gmres -pc_type ilu')."""
        return "{}['{}']".format(myself(), char_expression)

    @add_code
    def GenerateJac(self, system_id):
        """Generate the system of equations system_id using a jacobian matrix (of which the unknowns are corrections dx of the current solution x)."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def SolveJac(self, system_id):
        """Solve the system of equations system_id using a jacobian matrix (of which the unknowns are corrections dx of the current solution x). Then, Increment the solution (x=x+dx) and compute the relative error dx/x."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def GenerateSeparate(self, system_id):
        """Generate matrices separately for DtDtDof, DtDof and NoDt terms in system_id.
        The separate matrices can be used with the Update operation (for efficient time
        domain analysis of linear PDEs with constant coefficients), or with the EigenSolve
        operation (for solving generalized eigenvalue problems)."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def GenerateOnly(self, system_id, expression_cst_list):
        """Not documented yet."""
        return "{}[{}, {}]".format(
            myself(), system_id, py2getdplist(expression_cst_list)
        )

    @add_code
    def GenerateOnlyJac(self, system_id, expression_cst_list):
        """Not documented yet."""
        return "{}[{}, {}]".format(
            myself(), system_id, py2getdplist(expression_cst_list)
        )

    @add_code
    def GenerateGroup(self):
        """Not documented yet"""
        return "{}[]".format(myself())

    @add_code
    def GenerateRightHandSdeGroup(self):
        """Not documeted yet"""
        return "{}[]".format(myself())

    @add_code
    def Update(self, system_id, expression=None):
        """Update the system of equations system_id (built from sub-matrices
        generated separately with GenerateSeparate)
        - if expression=None: with the TimeFunction(s) provided in Assign constraints.
        - if expression is given: with expression.
        This assumes that the problem is
        linear, that the matrix coefficients are independent of time, and that
        all sources are imposed using Assign constraints."""
        if expression:
            return "{}[{}, {}]".format(myself(), system_id, expression)
        else:
            return "{}[{}]".format(myself(), system_id)

    @add_code
    def UpdateConstraint(self, system_id, group_id, constraint_type):
        """Recompute the constraint of type constraint_type acting on group_id during processing."""
        return "{}[{}, {}, {}]".format(myself(), system_id, group_id, constraint_type)

    @add_code
    def GetResidual(self, system_id, variable_id):
        """Compute the residual r = b - A x and store its L2 norm in the run-time variable $variable_id."""
        return "{}[{}, {}]".format(myself(), system_id, variable_id)

    @add_code
    def GetNormSolution(self, system_id, variable_id):
        """Compute the norm of the solutionand store its L2 norm in the run-time variable $variable_id."""
        return "{}[{}, {}]".format(myself(), system_id, variable_id)

    @add_code
    def GetNormRightHandSide(self, system_id, variable_id):
        """Compute the norm of the right-hand-side and store its L2 norm in the run-time variable $variable_id."""
        return "{}[{}, {}]".format(myself(), system_id, variable_id)

    @add_code
    def GetNormResidual(self, system_id, variable_id):
        """Compute the norm of the residual and store its L2 norm in the run-time variable $variable_id."""
        return "{}[{}, {}]".format(myself(), system_id, variable_id)

    @add_code
    def GetNormIncrement(self, system_id, variable_id):
        """Compute the norm of the increment and store its L2 norm in the run-time variable $variable_id."""
        return "{}[{}, {}]".format(myself(), system_id, variable_id)

    @add_code
    def SwapSolutionAndResidual(self, system_id):
        """Swap the solution x and residual r vectors."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def SwapSolutionAndRightHandSide(self, system_id):
        """Swap the solution x and right-hand-side b vectors."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def InitSolution(self, system_id):
        """Creates a new solution vector, adds it to the solution vector list for system_id, and initializes the solution. The values in the vector are initialized to the values given in a Constraint of Init type (if two values are given in Init, the second value is used). If no constraint is provided, the values are initialized to zero if the solution vector is the first in the solution list; otherwise the values are initialized using the previous solution in the list."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def InitSolution1(self, system_id):
        """Same as InitSolution, but uses the first value given in the Init constraints."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def CreateSolution(self, system_id, expression_cst=None):
        """If expression_cst is not given, creates a new solution vector,
        adds it to the solution vector list
        for system_id, and initializes the solution to zero.
        If expression_cst is given, initialize the solution by copying
        the expression_cst to the solution in the solution list."""
        if expression_cst:
            return "{}[{}, {}]".format(myself(), system_id, expression_cst)
        else:
            return "{}[{}]".format(myself(), system_id)

    @add_code
    def Apply(self, system_id):
        """x <- Ax"""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def SetSolutionAsRightHandSide(self, system_id):
        """b <- x"""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def SetRightHandSideAsSolution(self, system_id):
        """x <- b"""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def Residual(self, system_id):
        """res <- b - Ax"""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def CopySolution(self, system_id, expression, reverse=False):
        """Copy the current solution x into a vector or into a list named
        expression. If reverse is True, copy the vector or the
        list named expression into the current solution x"""
        if _is_list(expression):
            expression = "{}()".format(expression[0])
        else:
            expression = "'{}'".format(expression)
        if reverse:
            return "{}[{}, {}]".format(myself(), expression, system_id)
        else:
            return "{}[{}, {}]".format(myself(), system_id, expression)

    @add_code
    def CopyRightHandSide(self, system_id, expression, reverse=False):
        """"Copy the current right-hand side b into a vector or into a list named
        expression. If reverse is True, copy the vector or the
        list named expression into the current right-hand side b"""
        if _is_list(expression):
            expression = "{}()".format(expression[0])
        else:
            expression = "'{}'".format(expression)
        if reverse:
            return "{}[{}, {}]".format(myself(), expression, system_id)
        else:
            return "{}[{}, {}]".format(myself(), system_id, expression)

    @add_code
    def CopyResidual(self, system_id, expression, reverse=False):
        """"Copy the current residual into a vector or into a list named
        expression. If reverse is True, copy the vector or the
        list named expression into the current residual"""
        if _is_list(expression):
            expression = "{}()".format(expression[0])
        else:
            expression = "'{}'".format(expression)
        if reverse:
            return "{}[{}, {}]".format(myself(), expression, system_id)
        else:
            return "{}[{}, {}]".format(myself(), system_id, expression)

    @add_code
    def SaveSolution(self, system_id):
        """Save the solution of the system of equations system_id."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def SaveSolutions(self, system_id):
        """Save all the solutions available for the system of equations system_id. This should be used with algorithms that generate more than one solution at once, e.g., EigenSolve or FourierTransform."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def RemoveLastSolution(self, system_id):
        """Removes the last solution (i.e. associated with the last time step) associated with system system_id."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def TransferSolution(self, system_id):
        """Transfer the solution of system system_id, as an Assign constraint, to the system of equations defined with a DestinationSystem command. This is used with the AssignFromResolution constraint type (see Types for Constraint)."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def TransferInitSolution(self, system_id):
        """Transfer the solution of system system_id, as an Init constraint, to the system of equations defined with a DestinationSystem command. This is used with the InitFromResolution constraint type (see Types for Constraint)."""
        return "{}[{}]".format(myself(), system_id)

    @add_code
    def Evaluate(self, expression_list):
        """Evaluate the expression(s)."""
        if not _is_list(expression_list):
            expression_list = list([expression_list])
        s = ", ".join([str(_) for _ in expression_list])
        return "{}[{}]".format(myself(), s)

    @add_code
    def SetTime(self, expression):
        """Change the current time."""
        return "{}[{}]".format(myself(), expression)

    @add_code
    def SetTimeStep(self, expression):
        """Change the current time step number (1, 2, 3, ...)"""
        return "{}[{}]".format(myself(), expression)

    @add_code
    def SetDTime(self, expression):
        """Change the current time step value (dt)."""
        return "{}[{}]".format(myself(), expression)

    @add_code
    def SetFrequency(self, system_id, expression):
        """Change the frequency of system system_id."""
        "{}[{}, {}]".format(myself(), system_id, expression)

    @add_code
    def SystemCommand(self, expression_char):
        """Execute the system command given by expression_char."""
        return "{}['{}']".format(myself(), expression_char)

    @add_code
    def Error(self, expression_char):
        """Output error message expression_char."""
        return "{}['{}']".format(myself(), expression_char)

    @add_code
    def Test(self, expression, resolution_op_1, resolution_op_2=None):
        """If expression is true (nonzero), perform the operations in resolution_op_1.
        If the argument resolution_op_2 is given, if expression is true (nonzero),
        perform the operations in the first resolution_op_1,
        else perform the operations in the second resolution_op_2."""
        if resolution_op_2:
            return "{}[{} {{{}}} {{{}}}]".format(
                myself(), expression, resolution_op_1, resolution_op_2
            )
        else:
            return "{}[{} {{{}}}]".format(myself(), expression, resolution_op_1)

    @add_code
    def While(self, expression, resolution_op):
        """While expression is true (nonzero), perform the operations in resolution-op."""
        return "{}[{} {{{}}}]".format(myself(), expression, resolution_op)

    @add_code
    def Break(self):
        """Aborts an iterative loop, a time loop or a While loop."""
        return "{}[]".format(myself())

    @add_code
    def Sleep(self, expression):
        """Sleeps for expression seconds."""
        return "{}[{}]".format(myself(), expression)

    @add_code
    def SetExtrapolationOrder(self, expression_cst):
        """Chooses the extrapolation order to compute the initialization
        of the solution vector in time loops. Default is 0."""
        return "{}[{}]".format(myself(), expression_cst)

    @add_code
    def PrintExpr(self, expression_list, File=None, Format=None):
        """Print the expressions listed in expression-list. If Format is given,
        use it to format the (scalar) expressions like `Printf`."""
        if Format and File:
            return "{}[{}, File {}, Format {}]".format(
                "Print", py2getdplist(expression_list), File, Format
            )
        else:
            return "{}[{}]".format("Print", py2getdplist(expression_list))

    @add_code
    def PrintSys(self, system_id, File=None, dof_list=None, TimeStep=None):
        """Print the system system_id. If the dof_list is given,
        print only the values of the degrees of freedom given in that list.
        If the TimeStep option is present, limit the printing to the selected time steps."""
        kwargs = locals()
        del kwargs["self"]
        del kwargs["system_id"]
        s = "{}[{}".format("Print", system_id)
        for k, v in kwargs.items():
            if v is not None:
                if k == "dof_list":
                    s += ", {}".format(py2getdplist(v))
                else:
                    s += ", {} {}".format(k, v)
        s += "]"
        return s

    @add_code
    def EigenSolve(self, system_id, neig, shift_re, shift_im, filter=None):
        """Eigenvalue/eigenvector computation using Arpack or SLEPc. The parameters
        are: the system (which has to be generated with GenerateSeparate[]), the number
        of eigenvalues/eigenvectors to compute and the real and imaginary spectral
        shift (around which to look for eigenvalues). The last optional argument
        allows to filter which eigenvalue/eigenvector pairs will be saved.
        For example, ($EigenvalueReal > 0) would only keep pairs corresponding
        to eigenvalues with a striclty positive real part."""
        if filter:
            return "{}[{}, {}, {}, {}, {}]".format(
                myself(), system_id, neig, shift_re, shift_im, filter
            )
        else:
            return "{}[{}, {}, {}, {}]".format(
                myself(), system_id, neig, shift_re, shift_im
            )

    # @add_code
    # def Lanczos(self, system_id, expression_cst, { expression_cst_list } , expression_cst]):
    #     """Eigenvalue/eigenvector computation using the Lanczos algorithm. The parameters are:
    #     the system (which has to be generated with GenerateSeparate[]), the size of the Lanczos space,
    #     the indices of the eigenvalues/eigenvectors to store, the spectral shift.
    #     This routine is deprecated: use EigenSolve instead."""
    #     return ""

    @add_code
    def FourierTransform(self, system_id, system_id_dest, freq_list):
        """On-the-fly (incremental) computation of a Fourier transform.
        The parameters are: the (time domain) system, the destination system
        in which the result of the Fourier tranform is to be saved (it should be
        declared with Type Complex) and the list of frequencies to consider.
        The computation is an approximation that assumes that the time step is
        constant; it is not an actual Discrete Fourier Transform (the number
        of samples is unknown a priori)."""
        return "{}[{},{},{}]".format(
            myself(), system_id, system_id_dest, py2getdplist(freq_list)
        )

    @add_code
    def IterativeLinearSolver(self):
        """Generic iterativelinear solver. To be documented."""
        raise NotImplementedError("To be implemented")
        return

    @add_code
    def PostOperation(self, post_operation_id):
        """Perform the specified PostOperation."""
        return "{}[{}]".format(myself(), post_operation_id)

    @add_code
    def GmshRead(self, filename, tag=None):
        """When GetDP is linked with the Gmsh library, read a file using Gmsh.
        This file can be in any format recognized by Gmsh.
        If the file contains one or multiple post-processing fields,
        these fields will be evaluated using the built-in Field[],
        ScalarField[], VectorField[], etc., functions (see Miscellaneous functions).
        (Note that GmshOpen and GmshMerge can be used instead of GmshRead to
        force Gmsh to do classical “open” and “merge” operations, instead of
        trying to “be intelligent” when reading post-processing datasets, i.e.,
        creating new models on the fly if necessary.)
        If the tag is not empty
        field is forced to be stored with the given tag.
        The tag can be used to retrieve the given field with the built-in Field[],
        ScalarField[], VectorField[], etc., functions (see Miscellaneous functions).
        """
        if tag:
            return "{}['{}']".format(myself(), filename)
        else:
            return "{}['{}', {}]".format(myself(), filename, tag)

    @add_code
    def GmshWrite(self, filename, field):
        """Writes the a Gmsh field to disk. (The format is guessed from the file extension.)"""
        return "{}['{}', {}]".format(myself(), filename, field)

    @add_code
    def GmshClearAll(self):
        """Clears all Gmsh data (loaded with GmshRead and friends)."""
        return "{}[]".format(myself())

    @add_code
    def DeleteFile(self, filename):
        """Delete a file."""
        return "{}['{}']".format(myself(), filename)

    @add_code
    def RenameFile(self, filename, field):
        """Rename a file."""
        return "{}['{}', '{}']".format(myself(), filename, field)

    @add_code
    def CreateDirectory(self, dirmane):
        """Create a directory."""
        return "{}['{}']".format(myself(), dirmane)

    @add_code
    def MPI_SetCommSelf(self):
        """Changes MPI communicator to self."""
        return "{}[]".format(myself())

    @add_code
    def MPI_SetCommWorld(self):
        """Changes MPI communicator to world."""
        return "{}[]".format(myself())

    @add_code
    def MPI_Barrier(self):
        """MPI barrier (blocks until all processes have reached this call)."""
        return "{}[]".format(myself())

    @add_code
    def MPI_BroadcastFields(self, file_list=None):
        """Broadcast all fields over MPI (except those listed in the list)."""
        if list:
            return "{}[{}]".format(myself(), py2getdplist(file_list))
        else:
            return "{}[]".format(myself())

    @add_code
    def MPI_BroadcastVariables(self):
        """    Broadcast all runtime variables over MPI."""
        return "{}[]".format(myself())

    def add_time_loop_theta(self, *args, **kwargs):
        self._code0 = self.code
        tl = TimeLoopTheta(*args, **kwargs)
        self.loops.append(tl)
        return tl

    def add_time_loop_newmark(self, *args, **kwargs):
        self._code0 = self.code
        tl = TimeLoopNewmark(*args, **kwargs)
        self.loops.append(tl)
        return tl

    def add_iterative_loop(self, *args, **kwargs):
        self._code0 = self.code
        tl = IterativeLoop(*args, **kwargs)
        self.loops.append(tl)
        return tl

    @property
    def code(self):
        s = self._code0
        itemcode = "       "
        for item in self.loops:
            if item is not None:
                itemcode += item.code + "\n       "
                self._code = "   " + s[:-1] + "\n" + itemcode + s[-1:]
        self._code = self._code[:-1] + self._code[-1:]
        return self._code

    @code.setter
    def code(self, value):
        self._code = value


class SystemItem(object):
    def __init__(self, Name, NameOfFormulation, comment=None, **kwargs):
        self.comment = ""
        self.Name = Name
        self.NameOfFormulation = NameOfFormulation
        self.code = ""
        c = " { " + "Name {}; NameOfFormulation {};".format(Name, NameOfFormulation)
        for k, v in kwargs.items():
            self.__setattr__(k, v)
            c += " " + k + " " + make_args(v, sep=",") + ";"
        c += " } "
        if self.comment:
            c += _comment(comment)
        self.code += c


class System(object):
    def __init__(self, comment=None, **kwargs):
        self.comment = ""
        self.code = ""
        self.items = []
        for k, v in kwargs.items():
            self.__setattr__(k, v)
        c = "System { "
        if self.comment:
            c += _comment(comment)
        c += " \n        }"
        self.code += c

    def add(self, *args, **kwargs):
        item = SystemItem(*args, **kwargs)
        s = self.code
        n = 10
        self.code = s[:-n] + "\n       " + item.code + s[-n:]
        self.items.append(item)
        return item


class ResolutionItem(object):
    def __init__(self, Name, comment=None, **kwargs):
        """Item in Resolution.

        Parameters
        ----------
        Name : str
            The name of the Resolution item.
        comment : str
            An optional comment.
        Hidden : str
            Optional. Used with `SendToServer`, selects the visibility of the exchanged value.
        """
        self.Name = Name
        self.comment = ""
        self._code = ""
        self.items = []
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
        for case in self.items:
            self._code = s[:-2] + "\n     " + case.code + s[-2:]
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    def add_operation(self, *args, **kwargs):
        self._code0 = self.code
        case = Operation(*args, **kwargs)
        self.items.append(case)
        return case

    def add_system(self, *args, **kwargs):
        self._code0 = self.code
        case = System(*args, **kwargs)
        self.items.append(case)
        return case


class Resolution(GetDPObject):
    """Solving systems of equations"""

    name = "Resolution"
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
        self._content = self._content0
        o = ResolutionItem(Name, **kwargs)
        self.items.append(o)
        return o


class TimeLoopTheta(Operation):
    def __init__(self, t0=0, tend=1, step=0.1, theta=1, *args, **kwargs):
        """Time loop of a theta scheme. The parameters are: the initial time,
        the end time, the time step and the theta parameter (e.g., 1 for implicit
        Euler, 0.5 for Crank-Nicholson).
        Warning: GetDP automatically handles time-dependent constraints when
        they are provided using the TimeFunction mechanism in an Assign-type
        Constraint (see Constraint). However, GetDP cannot automatically
        transform general time-dependent source terms in weak formulations
        (time-dependent functions written in a Integral term). Such source
        terms will be correctly treated only for implicit Euler, as the expression
        in the Integral term is evaluated at the current time step. For other schemes,
        the source term should be written explicitly, by splitting it in two
        (theta f_n+1 + (1-theta) f_n), making use of the AtAnteriorTimeStep[]
        for the second part, and specifying NeverDt in the Integral term."""
        super().__init__(*args, **kwargs)
        self.code = (
            "TimeLoopTheta[{}, {}, {}, {}]".format(t0, tend, step, theta)
            + "{\n        }"
        )


class TimeLoopNewmark(Operation):
    def __init__(self, t0=0, tend=1, step=0.1, beta=1, gamma=1, *args, **kwargs):
        """Time loop of a Newmark scheme. The parameters are: the initial time,
        the end time, the time step, the beta and the gamma parameter.
        Warning: same restrictions apply for time-dependent functions in the
        weak formulations as for TimeLoopTheta."""
        super().__init__(*args, **kwargs)
        self.code = (
            "TimeLoopNewmark[{}, {}, {}, {}, {}]".format(t0, tend, step, beta, gamma)
            + "{\n        }"
        )


class TimeLoopAdaptive(Operation):
    """Time loop with variable time steps. The step size is adjusted according the local truncation error (LTE) of the specified Systems/PostOperations via a predictor-corrector method.
    The parameters are: start time, end time, initial time step, min. time step, max. time step, integration method, list of breakpoints (time points to be hit). The LTE calculation can be based on all DOFs of a system and/or on a PostOperation result. The parameters here are: System/PostOperation for LTE assessment, relative LTE tolerance, absolute LTE tolerance, norm-type for LTE calculation.
    Possible choices for integration-method are: Euler, Trapezoidal, Gear_2, Gear_3, Gear_4, Gear_5, Gear_6. The Gear methods correspond to backward differentiation formulas of order 2..6.
    Possible choices for norm-type: L1Norm, MeanL1Norm, L2Norm, MeanL2Norm, LinfNorm.
    MeanL1Norm and MeanL2Norm correspond to L1Norm and L2Norm divided by the number of degrees of freedom, respectively.
    The first resolution-op is executed every time step. The second one is only executed if the actual time step is accepted (LTE is in the specified range). E.g. SaveSolution[] is usually placed in the 2nd resolution-op.
    """

    #
    # [expression_cst,exprssion-cst,expression_cst,expression_cst, expression_cst,integration-method,<expression_cst_list>,System { {system_id,epression-cst,expression_cst,norm-type} ... } |):
    # PostOperation { {post-operation_id,expression_cst,expression_cst,norm-type} ... } ]
    # { resolution-op }
    # { resolution-op }

    def __init__(self, *args, **kwargs):
        raise NotImplementedError("To be implemented")


class IterativeLoop(Operation):
    """Iterative loop for nonlinear analysis. The parameters are: the maximum number of iterations
    (if no convergence), the relaxation factor (multiplies the iterative correction dx)
    and the relative error to achieve. The optional parameter is a flag for testing purposes."""

    def __init__(
        self, maxit=10, rel_fact=0.1, err_rel=1e-6, test_flag=None, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        if test_flag:
            self.code = (
                "IterativeLoop[{}, {}, {}, {}]".format(
                    maxit, rel_fact, err_rel, int(test_flag)
                )
                + "{\n        }"
            )
        else:
            self.code = (
                "IterativeLoop[{}, {}, {}]".format(maxit, rel_fact, err_rel)
                + "{\n        }"
            )


# def IterativeLoopN(self,
#
#     [expression_cst,exression,System { {system-idexpression_cst,expression_cst, assessed-object norm-type} ... } |):
#     PostOperation { {post-operation_id,expression_cst,expression_cst, norm-type} ... } ]
#     { resolution-op }
#
#     Similar to IterativeLoop[] but allows to specify in detail the tolerances and the type of norm to be calculated for convergence assessment.
#     The parameters are: the maximum number of iterations (if no convergence), the relaxation factor (multiplies the iterative correction dx). The convergence assessment can be based on all DOFs of a system and/or on a PostOperation result. The parameters here are: System/PostOperation for convergence assessment, relative tolerance, absolute tolerance, assessed object (only applicable for a specified system), norm-type for error calculation.
#     Possible choices for assessed-object: Solution, Residual, RecalcResidual. Residual assesses the residual from the last iteration whereas RecalcResidual calculates the residual once again after each iteration. This means that with Residual usually one extra iteration is performed, but RecalcResidual causes higher computational effort per iteration. Assessing the residual can only be used for Newton’s method.
#     Possible choices for norm-type: L1Norm, MeanL1Norm, L2Norm, MeanL2Norm, LinfNorm.
#     MeanL1Norm and MeanL2Norm correspond to L1Norm and L2Norm divided by the number of degrees of freedom, respectively.
