"""
Copyright 2013 Steven Diamond

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from cvxpy.constraints import (Equality, ExpCone, Inequality,
                               SOC, Zero, NonPos, PSD)
from cvxpy.cvxcore.python import canonInterface
from cvxpy.expressions.variable import Variable
from cvxpy.problems.objective import Minimize
from cvxpy.reductions import InverseData, Solution, cvx_attr2constr
from cvxpy.reductions.matrix_stuffing import extract_mip_idx, MatrixStuffing
from cvxpy.reductions.utilities import (are_args_affine,
                                        group_constraints,
                                        lower_equality,
                                        lower_inequality)
import cvxpy.settings as s
from cvxpy.utilities.coeff_extractor import CoeffExtractor
import numpy as np
import scipy.sparse as sp


# TODO(akshayka): unit tests
class ParamConeProg(object):
    """Represents a parameterized cone program

    minimize   c'x  + d
    subject to cone_constr1(A_1*x + b_1, ...)
               ...
               cone_constrK(A_i*x + b_i, ...)


    The constant offsets d and b are the last column of c and A.
    """
    def __init__(self, c, x, A,
                 variables,
                 var_id_to_col,
                 constraints,
                 parameters,
                 param_id_to_col,
                 formatted=False):
        self.c = c
        self.x = x
        self.A = A
        self._A_mapping_nonzero = None
        self.constraints = constraints
        self.constr_size = sum([c.size for c in constraints])
        self.parameters = parameters
        self.param_id_to_col = param_id_to_col
        self.id_to_param = {p.id: p for p in self.parameters}
        self.param_id_to_size = {p.id: p.size for p in self.parameters}
        self.total_param_size = sum([p.size for p in self.parameters])
        # TODO technically part of inverse data.
        self.variables = variables
        self.var_id_to_col = var_id_to_col
        self.id_to_var = {v.id: v for v in self.variables}
        # whether this param cone prog has been formatted for a solver
        self.formatted = formatted

    def is_mixed_integer(self):
        return self.x.attributes['boolean'] or \
            self.x.attributes['integer']

    def apply_parameters(self, id_to_param_value=None, zero_offset=False,
                         keep_zeros=False):
        """Returns A, b after applying parameters (and reshaping).

        Args:
          id_to_param_value: (optional) dict mapping parameter ids to values
          zero_offset: (optional) if True, zero out the constant offset in the
                       parameter vector
          keep_zeros: (optional) if True, store explicit zeros in A where
                        parameters are affected
        """
        def param_value(idx):
            return (np.array(self.id_to_param[idx].value) if id_to_param_value
                    is None else id_to_param_value[idx])
        param_vec = canonInterface.get_parameter_vector(
            self.total_param_size,
            self.param_id_to_col,
            self.param_id_to_size,
            param_value,
            zero_offset=zero_offset)
        c, d = canonInterface.get_matrix_and_offset_from_tensor(
            self.c, param_vec, self.x.size)
        c = c.toarray().flatten()
        if keep_zeros and self._A_mapping_nonzero is None:
            self._A_mapping_nonzero = canonInterface.A_mapping_nonzero_rows(
                self.A, self.x.size)
        A, b = canonInterface.get_matrix_and_offset_from_tensor(
            self.A, param_vec, self.x.size,
            nonzero_rows=self._A_mapping_nonzero)
        return c, d, A, np.atleast_1d(b)

    def apply_param_jac(self, delc, delA, delb, active_params=None):
        """Multiplies by Jacobian of parameter mapping.

        Assumes delA is sparse.

        Returns:
            A dictionary param.id -> dparam
        """
        if active_params is None:
            active_params = {p.id for p in self.parameters}

        del_param_vec = delc @ self.c[:-1]
        flatdelA = delA.reshape((np.prod(delA.shape), 1), order='F')
        delAb = sp.vstack([flatdelA, sp.csc_matrix(delb[:, None])])
        del_param_vec += np.squeeze((delAb.T @ self.A).A)
        del_param_vec = np.squeeze(del_param_vec)

        param_id_to_delta_param = {}
        for param_id, col in self.param_id_to_col.items():
            if param_id in active_params:
                param = self.id_to_param[param_id]
                delta = del_param_vec[col:col + param.size]
                param_id_to_delta_param[param_id] = np.reshape(
                    delta, param.shape, order='F')
        return param_id_to_delta_param

    def split_solution(self, sltn, active_vars=None):
        """Splits the solution into individual variables.
        """
        if active_vars is None:
            active_vars = [v.id for v in self.variables]
        # var id to solution.
        sltn_dict = {}
        for var_id, col in self.var_id_to_col.items():
            if var_id in active_vars:
                var = self.id_to_var[var_id]
                value = sltn[col:var.size+col]
                if var.attributes_were_lowered():
                    orig_var = var.variable_of_provenance()
                    value = cvx_attr2constr.recover_value_for_variable(
                        orig_var, value, project=False)
                    sltn_dict[orig_var.id] = np.reshape(
                        value, orig_var.shape, order='F')
                else:
                    sltn_dict[var_id] = np.reshape(
                        value, var.shape, order='F')
        return sltn_dict

    def split_adjoint(self, del_vars=None):
        """Adjoint of split_solution.
        """
        var_vec = np.zeros(self.x.size)
        for var_id, delta in del_vars.items():
            var = self.id_to_var[var_id]
            col = self.var_id_to_col[var_id]
            if var.attributes_were_lowered():
                orig_var = var.variable_of_provenance()
                if cvx_attr2constr.attributes_present(
                        [orig_var], cvx_attr2constr.SYMMETRIC_ATTRIBUTES):
                    delta = delta + delta.T - np.diag(np.diag(delta))
                delta = cvx_attr2constr.lower_value(orig_var, delta)
            var_vec[col:col + var.size] = delta.flatten(order='F')
        return var_vec


class ConeMatrixStuffing(MatrixStuffing):
    """Construct matrices for linear cone problems.

    Linear cone problems are assumed to have a linear objective and cone
    constraints which may have zero or more arguments, all of which must be
    affine.
    """
    CONSTRAINTS = 'ordered_constraints'

    def accepts(self, problem):
        return (type(problem.objective) == Minimize
                and problem.objective.expr.is_affine()
                and not cvx_attr2constr.convex_attributes(problem.variables())
                and are_args_affine(problem.constraints)
                and problem.is_dpp())

    def stuffed_objective(self, problem, extractor):
        # Extract to c.T * x + r; c is represented by a ma
        c = extractor.affine(problem.objective.expr)

        boolean, integer = extract_mip_idx(problem.variables())
        x = Variable(extractor.x_length, boolean=boolean, integer=integer)

        return c, x

    def apply(self, problem):
        inverse_data = InverseData(problem)
        # Form the constraints
        extractor = CoeffExtractor(inverse_data)
        params_to_objective, flattened_variable = self.stuffed_objective(
            problem, extractor)
        # Lower equality and inequality to Zero and NonPos.
        cons = []
        for con in problem.constraints:
            if isinstance(con, Equality):
                con = lower_equality(con)
            elif isinstance(con, Inequality):
                con = lower_inequality(con)
            elif isinstance(con, SOC) and con.axis == 1:
                con = SOC(con.args[0], con.args[1].T, axis=0,
                          constr_id=con.constr_id)
            cons.append(con)
        # Reorder constraints to Zero, NonPos, SOC, PSD, EXP.
        constr_map = group_constraints(cons)
        ordered_cons = constr_map[Zero] + constr_map[NonPos] + \
            constr_map[SOC] + constr_map[PSD] + constr_map[ExpCone]
        inverse_data.cons_id_map = {con.id: con.id for con in ordered_cons}

        inverse_data.constraints = ordered_cons
        # Batch expressions together, then split apart.
        expr_list = [arg for c in ordered_cons for arg in c.args]
        params_to_problem_data = extractor.affine(expr_list)

        inverse_data.minimize = type(problem.objective) == Minimize
        new_prob = ParamConeProg(params_to_objective,
                                 flattened_variable,
                                 params_to_problem_data,
                                 problem.variables(),
                                 inverse_data.var_offsets,
                                 ordered_cons,
                                 problem.parameters(),
                                 inverse_data.param_id_map)
        return new_prob, inverse_data

    def invert(self, solution, inverse_data):
        """Retrieves a solution to the original problem"""
        var_map = inverse_data.var_offsets
        con_map = inverse_data.cons_id_map
        # Flip sign of opt val if maximize.
        opt_val = solution.opt_val
        if solution.status not in s.ERROR and not inverse_data.minimize:
            opt_val = -solution.opt_val

        primal_vars, dual_vars = {}, {}
        if solution.status not in s.SOLUTION_PRESENT:
            return Solution(solution.status, opt_val, primal_vars, dual_vars,
                            solution.attr)

        # Split vectorized variable into components.
        x_opt = list(solution.primal_vars.values())[0]
        for var_id, offset in var_map.items():
            shape = inverse_data.var_shapes[var_id]
            size = np.prod(shape, dtype=int)
            primal_vars[var_id] = np.reshape(x_opt[offset:offset+size], shape,
                                             order='F')

        # Remap dual variables if dual exists (problem is convex).
        if solution.dual_vars is not None:
            for old_con, new_con in con_map.items():
                con_obj = inverse_data.id2cons[old_con]
                shape = con_obj.shape
                # TODO rationalize Exponential.
                if shape == () or isinstance(con_obj, (ExpCone, SOC)):
                    dual_vars[old_con] = solution.dual_vars[new_con]
                else:
                    dual_vars[old_con] = np.reshape(
                        solution.dual_vars[new_con],
                        shape,
                        order='F'
                    )

        return Solution(solution.status, opt_val, primal_vars, dual_vars,
                        solution.attr)
