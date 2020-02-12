# Copyright (C) 2018, 2019 Columbia University Irving Medical Center,
#     New York, USA
# Copyright (C) 2019 Novo Nordisk Foundation Center for Biosustainability,
#     Technical University of Denmark

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Functions to add a given `DfbaModel` to the dynamic library."""


import os

import sympy


def WriteIndent(theFile, indentCount, text):
    """Write indent.

    Parameters
    -------
    theFile : file
        Open cpp file.
    indentCount : int
        Number of tabs to indent.
    text : string
        The line of text to write to file.

    """
    while indentCount > 0:
        text = "    " + text
        indentCount -= 1
    theFile.write(text)


def indices(nrow, reactions, reaction_id):
    """Write indices.

    Parameters
    -------
    nrow : int
        Number of rows in LP problem.
    reactions : DictList
        A DictList where the key is the reaction identifier and the value a
        `cobra.Reaction` object.
    reaction_id : string
        Identifier of the reaction to return indices for.

    Returns
    -------
    indices : list
        lpindices of forward and reverse reaction.

    """

    if reaction_id not in reactions:
        raise Exception("Error: {} is not a reaction in the model!".format(reaction_id))
    forward_index = 2 * reactions.index(reaction_id) + nrow
    reverse_index = forward_index + 1
    return [forward_index, reverse_index]


def col_indices(reactions, reaction_id):
    """Write column indices.

    Parameters
    -------
    reactions : DictList
        A `DictList` object where the key is the reaction identifier
        and the value a `cobra.Reaction` object.
    reaction_id : string
        Identifier of the reaction to return column indices for.

    Returns
    -------
    indices : list
        Column indices of forward and reverse reaction.

    """

    if reaction_id not in reactions:
        raise Exception("Error: {} is not a reaction in the model!".format(reaction_id))
    forward_index = 2 * reactions.index(reaction_id)
    reverse_index = forward_index + 1
    return [forward_index, reverse_index]


def ctrl_parm_expression(ctrl_parms, change_pnts):
    """Control paramter expression.

    Parameters
    -------
    ctrl_parms : dict
        A dict of control parameters to be included in expression.
    change_pnts : list
        Ordered list of change points from control parameters in model.

    Returns
    -------
    control_expression : string
        The control parameter expression.

    """

    if bool(ctrl_parms):  # if dict of control parameters not empty
        control_expression = ""
        ctrl_cp_idxs = {}
        # loop over control parameters, add their definitions, and track
        # individual change points
        for ctrl_parm in ctrl_parms.keys():
            control_parameter = ctrl_parms[ctrl_parm]
            control_expression += (
                "double "
                + str(control_parameter.id)
                + " = "
                + str(control_parameter.values[0])
                + ";\n\t"
            )
            ctrl_cp_idxs[ctrl_parm] = 0
        control_expression += "switch(flag){\n"
        # loop over change points
        for i in range(len(change_pnts)):
            control_expression += "\t\tcase " + str(i + 1) + ":\n"
            for ctrl_parm in ctrl_parms.keys():
                control_parameter = ctrl_parms[ctrl_parm]
                cp_idx = ctrl_cp_idxs[ctrl_parm]
                if control_parameter.change_points[cp_idx] == change_pnts[i]:
                    control_expression += (
                        "\t\t\t"
                        + str(control_parameter.id)
                        + " = "
                        + str(control_parameter.values[cp_idx + 1])
                        + ";\n"
                    )
                    if cp_idx < len(control_parameter.change_points) - 1:
                        ctrl_cp_idxs[ctrl_parm] += 1
                elif control_parameter.change_points[cp_idx] < change_pnts[i]:
                    control_expression += (
                        "\t\t\t"
                        + str(control_parameter.id)
                        + " = "
                        + str(control_parameter.values[cp_idx + 1])
                        + ";\n"
                    )
                else:
                    control_expression += (
                        "\t\t\t"
                        + str(control_parameter.id)
                        + " = "
                        + str(control_parameter.values[cp_idx])
                        + ";\n"
                    )
            control_expression += "\t\t\tbreak;\n"
        control_expression += "\t}\n"
        return control_expression
    else:
        raise Exception("The supplied dict of control parameters is empty!")


def create(directory):
    """Create library.

    Parameters
    -------
    directory : string
        Path to temporary directory containing library.

    """

    cppfilePath = os.path.join(directory, "functionlib.cpp")
    with open(cppfilePath, "w") as cppFile:
        cppFile.write("#include <stdlib.h> \n#include <cmath> \n#include <vector> \n\n")


def write_model_to_file(
    name,
    kinetic_variables,
    exchange_fluxes,
    nexc,
    nreq,
    exchange_indices,
    change_pnts,
    directory,
):
    """Write `DfbaModel` to file.

    Parameters
    -------
    name : string
        str of `DfbaModel` id
    kinetic_variables : DictList
        A `DictList` object where the key is the kinetic variable
        identifier and the value a `KineticValue` object.
    exchange_fluxes : DictList
        A `DictList` object where the key is the exchange flux
        identifier and the value an `ExchangeFLux` object.
    nexc : int
        Number of exchange fluxes.
    nreq : int
        Number of fluxes required to define ODE right-hand side.
    exchange_indics : list
        Indices of exchange fluxes.
    change_pnts : list
        Ordered list of change points from control parameters in model.
    directory: string
        Path to temporary directory containing library.

    """

    # Collect the kinetic expression
    kinetics = []
    for i in range(nreq // 2):
        kinetics.append(
            "double v{} = fluxes[{}] - fluxes[{}]; \n".format(i, 2 * i, 2 * i + 1)
        )
    kinetic_ctrl_parms = {}
    for kinetic_variable in kinetic_variables:
        if kinetic_variable.rhs_expression[1] is not None:
            for k in range(len(kinetic_variable.rhs_expression[1])):
                ctrl_parm_id = kinetic_variable.rhs_expression[1][k].id
                if ctrl_parm_id not in kinetic_ctrl_parms.keys():
                    kinetic_ctrl_parms[ctrl_parm_id] = kinetic_variable.rhs_expression[
                        1
                    ][k]
    if bool(kinetic_ctrl_parms):
        control_expression = ctrl_parm_expression(kinetic_ctrl_parms, change_pnts)
        kinetics.append(control_expression)
    counter = 0
    for kinetic_variable in kinetic_variables:
        kinetics.append(
            "rval["
            + str(counter)
            + "] = "
            + sympy.ccode(kinetic_variable.rhs_expression[0])
            + " - ypval["
            + str(counter)
            + "]; \n"
        )
        counter += 1

    # Collect exchange flux expressions
    upper_bounds = []
    lower_bounds = []
    for exchange_flux in exchange_fluxes:
        if exchange_flux.upper_bound_expression is not None:
            condition = exchange_flux.upper_bound_expression[1]
            bound = None
            ub_ctrl_parms = {}
            if exchange_flux.upper_bound_expression[0] is not None:
                bound = exchange_flux.upper_bound_expression[0]
            if exchange_flux.upper_bound_expression[2] is not None:
                for k in range(len(exchange_flux.upper_bound_expression[2])):
                    ctrl_parm_id = exchange_flux.upper_bound_expression[2][k].id
                    if ctrl_parm_id not in ub_ctrl_parms.keys():
                        ub_ctrl_parms[
                            ctrl_parm_id
                        ] = exchange_flux.upper_bound_expression[2][k]
            control_expression = ""
            if bool(ub_ctrl_parms):
                control_expression = ctrl_parm_expression(ub_ctrl_parms, change_pnts)
            if condition is not None:
                upper_bounds.append(
                    "\t\t\tif("
                    + sympy.ccode(condition)
                    + "<0.0){\n\t\t\t\treturn 0.0;\n\t\t\t}\n\t\t\telse{\n"
                    + control_expression
                    + "\n"
                    + "\t\t\t\treturn "
                    + sympy.ccode(bound)
                    + ";\n\t\t\t}\n"
                )
            else:
                upper_bounds.append(
                    "\t\t\t"
                    + control_expression
                    + "\n"
                    + "\t\t\treturn "
                    + str(bound)
                    + ";\n"
                )
        if exchange_flux.lower_bound_expression is not None:
            condition = exchange_flux.lower_bound_expression[1]
            bound = None
            lb_ctrl_parms = {}
            if exchange_flux.lower_bound_expression[0] is not None:
                bound = exchange_flux.lower_bound_expression[0]
            if exchange_flux.lower_bound_expression[2] is not None:
                for k in range(len(exchange_flux.lower_bound_expression[2])):
                    ctrl_parm_id = exchange_flux.lower_bound_expression[2][k].id
                    if ctrl_parm_id not in lb_ctrl_parms.keys():
                        lb_ctrl_parms[
                            ctrl_parm_id
                        ] = exchange_flux.lower_bound_expression[2][k]
            control_expression = ""
            if bool(lb_ctrl_parms):
                control_expression = ctrl_parm_expression(lb_ctrl_parms, change_pnts)
            if condition is not None:
                upper_bounds.append(
                    "\t\t\tif("
                    + sympy.ccode(condition)
                    + "<0.0){\n\t\t\t\treturn 0.0;\n\t\t\t}\n\t\t\telse{\n"
                    + control_expression
                    + "\n"
                    + "\t\t\t\treturn "
                    + sympy.ccode(bound)
                    + ";\n\t\t\t}\n"
                )
            else:
                upper_bounds.append(
                    "\t\t\t"
                    + control_expression
                    + "\n"
                    + "\t\t\treturn "
                    + sympy.ccode(bound)
                    + ";\n"
                )

    # Write functions to file
    cppfilePath = os.path.join(directory, "functionlib.cpp")
    with open(cppfilePath, "a") as cppFile:
        t = 0  # write the kinetics function
        WriteIndent(
            cppFile,
            t,
            'extern "C" void kinetics'
            + name
            + "(double tval, double *yval, double *ypval, double *rval, "
            + "std::vector<double> fluxes, int flag)\n",
        )
        WriteIndent(cppFile, t, "{\n")
        for i in range(len(kinetics)):
            WriteIndent(cppFile, t + 1, kinetics[i])
        WriteIndent(cppFile, t, "}\n\n")
        t = 0  # write the upper bounds function
        WriteIndent(
            cppFile,
            t,
            'extern "C" double upper_bounds'
            + name
            + "(int i, double tval, double *yval, int flag)\n",
        )
        WriteIndent(cppFile, t, "{\n")
        if len(upper_bounds) > 0:
            WriteIndent(cppFile, t + 1, "switch(i){\n")
            for i in range(nexc):
                WriteIndent(
                    cppFile, t + 2, "case " + str(exchange_indices[i]) + ": {\n",
                )
                WriteIndent(cppFile, t, upper_bounds[i])
                WriteIndent(cppFile, t + 3, "break;\n")
                WriteIndent(cppFile, t + 2, "}\n")
            WriteIndent(cppFile, t + 2, "default: {\n")
            WriteIndent(cppFile, t + 3, "exit(-1);\n")
            WriteIndent(cppFile, t + 2, "}\n")
            WriteIndent(cppFile, t + 1, "}\n")
        WriteIndent(cppFile, t + 1, "return 0.0; \n")
        WriteIndent(cppFile, t, "}\n\n")
        t = 0  # write the lower bounds function
        WriteIndent(
            cppFile,
            t,
            'extern "C" double lower_bounds'
            + name
            + "(int i, double tval, double *yval, int flag)\n",
        )
        WriteIndent(cppFile, t, "{\n")
        if len(lower_bounds) > 0:
            WriteIndent(cppFile, t + 1, "switch(i){\n")
            for i in range(nexc):
                WriteIndent(
                    cppFile, t + 2, "case " + str(exchange_indices[i]) + ": {\n",
                )
                WriteIndent(cppFile, t, lower_bounds[i])
                WriteIndent(cppFile, t + 3, "break;\n")
                WriteIndent(cppFile, t + 2, "}\n")
            WriteIndent(cppFile, t + 2, "default: {\n")
            WriteIndent(cppFile, t + 3, "exit(-1);\n")
            WriteIndent(cppFile, t + 2, "}\n")
            WriteIndent(cppFile, t + 1, "}\n")
        WriteIndent(cppFile, t + 1, "return 0.0; \n")
        WriteIndent(cppFile, t, "}\n\n")
