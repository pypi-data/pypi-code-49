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

"""Definition of `DfbaModel` class."""

import logging
import tempfile

import cobra
import pandas as pd
from cobra import DictList, Object
from cobra.util import solver
from optlang import symbolics

from . import jit, library
from .dfba_utils import *  # noqa: F403


logger = logging.getLogger(__name__)

# Lines refering to the imported functions from .dbfa utils must be commented
# in-line to ignore F405 since flake8 can't understand this import
# (C++ level related)


class DfbaModel(Object):
    """Class representation for a dynamic FBA model.

    Parameters
    ----------
    cobra_object : cobra.Model
        Existing `cobra.Model` object representing FBA model.

    Attributes
    ----------
    cobra_model : cobra.Model
        Existing `cobra.Model` object containing FBA model
        (reactions, metabolites, objective).
    reactions : DictList
        A `DictList` object where the key is the reaction identifier
        and the value a `cobra.Reaction` object in cobra_model attribute.
    objectives : list
        A list containing identifiers of reactions to be used as objectives
        in lexicographic optimization (currently not supported)
    directions : list
        A list containing directions (max or min) of each objective in
        lexicographic optimization (currently not supported)
    kinetic_variables : DictList
        A `DictList` object where the key is the kinetic variable identifier
        and the value a `KineticVariable` object.
    exchange_fluxes : DictList
        A `DictList` object where the key is the reaction identifier and the
        value an `ExchangeFlux` object.
    user_data : dfba_utils.UserData
        A read only attribute containing user data of the model
        to be passed to algorithm prior to simulation.
    solver_data : dfba_utils.SolverData
        An attribute containing data for the solver to be used for
        simulation of the model.

    """

    def __init__(self, cobra_object):
        """Init method."""
        if isinstance(cobra_object, cobra.Model):
            self._id = id(self)
            self._cobra_model = cobra_object
            self._reactions = cobra_object.reactions
            self._objectives = []
            self._directions = []
            self._kinetic_variables = DictList()
            self._exchange_fluxes = DictList()
            self._user_data = UserData()  # noqa: F405
            self._solver_data = SolverData()  # noqa: F405
        else:
            raise Exception(
                "Error: must use instance of class cobra.Model " "to init DfbaModel!"
            )

    def add_objectives(self, objectives, directions):
        """Add objectives.

        Parameters
        -------
        objectives : list
            The list of reaction indetifiers to be added to the model as
            objectives for lexicographic optimization.
        directions : list
            The list of directions (max or min) of each objective to be
            added to the model for lexicographic optimization.


        """
        # TODO: currently not supported. Should it raise NotImplementedError?

        if type(objectives) is not list:
            objectives = [objectives]
        if type(directions) is not list:
            directions = [directions]
        if len(objectives) != len(directions):
            raise Exception(
                "Error: objectives list must be same length as directions list!"
            )
        self._objectives.extend(objectives)
        self._directions.extend(directions)

    def add_kinetic_variables(self, kinetic_variable_list):
        """Add kinetic variables.

        Parameters
        -------
        kinetic_variable_list : list
            The list of indetifiers of kinetic variables to be added to the
            model.

        """
        if type(kinetic_variable_list) is not list:
            kinetic_variable_list = [kinetic_variable_list]

        def existing_filter(kinetic_variable):
            if kinetic_variable.id in self.kinetic_variables:
                logger.warning(
                    f"Ignoring kinetic variable {kinetic_variable.id} since it"
                    f"already exists in the model."
                )
                return False
            return True

        pruned = DictList(filter(existing_filter, kinetic_variable_list))
        self._kinetic_variables += pruned
        DictList.sort(self._kinetic_variables)
        counter = 0
        for kinetic_variable in self._kinetic_variables:
            symbolics.Symbol.__init__(kinetic_variable, "yval[" + str(counter) + "]")
            counter += 1

    def add_exchange_fluxes(self, exchange_flux_list):
        """Add exchange fluxes.

        Parameters
        -------
        exchange_flux_list : list
            list of indetifiers of exchange fluxes to be added to the model.

        """
        if type(exchange_flux_list) is not list:
            exchange_flux_list = [exchange_flux_list]

        def existing_filter(exchange_flux):
            if exchange_flux.id not in self.reactions:
                logger.warning(
                    f"Ignoring exchange flux {exchange_flux.id} since it does"
                    f"not correspond to a reaction in the model."
                )
                return False
            if exchange_flux.id in self.exchange_fluxes:
                logger.warning(
                    f"Ignoring exchange flux {exchange_flux.id} since it"
                    f"already exists in the model."
                )
                return False
            return True

        pruned = DictList(filter(existing_filter, exchange_flux_list))
        self._exchange_fluxes += pruned
        DictList.sort(self._exchange_fluxes)
        counter = 0
        for exchange_flux in self._exchange_fluxes:
            symbolics.Symbol.__init__(exchange_flux, "v" + str(counter))
            counter += 1

    def add_initial_conditions(self, initial_conditions):
        """Add initial conditions.

        Parameters
        -------
        initial_conditions : dict
            A dict where the key is the kinetic variable identifier and
            the value an initial condition.

        """

        if type(initial_conditions) is not dict:
            raise Exception(
                "Error: initial conditions should be dict of format"
                "{kinetic_variable.id: initial condition}!"
            )

        for key in initial_conditions.keys():
            if key in self.kinetic_variables:
                self.kinetic_variables.get_by_id(
                    key
                ).initial_condition = initial_conditions[key]
            else:
                logger.warning(
                    f"Ignoring initial condition for {key} since it does not"
                    f"correspond to a kinetic variable in the model."
                )

    def add_rhs_expression(
        self, kinetic_variable_id, expression, control_parameters=None
    ):
        """Add rhs expression.

        Parameters
        -------
        kinetic_variable_id : string
            Identifier of the kinetic variable to be supplied with
            rhs expression for calculating its derivative wrt time.
        expression : optlang.symbolics expression
            The symbolic expression for calculating derivative of kinetic
            variable wrt time.
        control_parameters : list
            A list of `ControlParameter` objects (if any) appearing in the
            supplied symbolic expression.

        """

        if control_parameters is not None:
            if type(control_parameters) is not list:
                control_parameters = [control_parameters]

        if kinetic_variable_id not in self.kinetic_variables:
            raise Exception(
                "Error: {} is not a kinetic variable in model!".format(
                    kinetic_variable_id
                )
            )
        self.kinetic_variables.get_by_id(kinetic_variable_id).rhs_expression = [
            expression,
            control_parameters,
        ]

    def add_exchange_flux_lb(
        self, exchange_flux_id, expression, condition=None, control_parameters=None,
    ):
        """Add exchange flux lower bound.

        Parameters
        -------
        exchange_flux_id : string
            Indetifier of the exchange flux to be supplied with expression
            for calculating its lower bound.
        expression : optlang.symbolics expression
            The symbolic expression for calculating lower bound of exchange
            flux. Convention is that lower bounds of exchange fluxes come
            with negative sign and therefore expression should be
            non-negative,representing the magnitude of this lower bound.
        condition : optlang.symbolics expression
            The symbolic expression for non-negative condition on metabolite
            concentrations required for correct evaluation of lower bound
            expression. Numerical approximation can generate unphysical,
            negative concetration values.
        control_parameters : list
            A list of `ControlParameter` objects (if any) appearing in the
            supplied symbolic expression.

        """

        if control_parameters is not None:
            if type(control_parameters) is not list:
                control_parameters = [control_parameters]

        if exchange_flux_id not in self.exchange_fluxes:
            raise Exception(
                "Error: reaction {} is not an exchange flux in model!".format(
                    exchange_flux_id
                )
            )
        self.exchange_fluxes.get_by_id(exchange_flux_id).lower_bound_expression = [
            expression,
            condition,
            control_parameters,
        ]

    def add_exchange_flux_ub(
        self, exchange_flux_id, expression, condition=None, control_parameters=None,
    ):
        """Add exchange flux upper bound.

        Parameters
        -------
        exchange_flux_id : string
            Indetifier of the exchange flux to be supplied with expression
            for calculating its upper bound.
        expression : optlang.symbolics expression
            The symbolic expression for calculating upper bound of exchange
            flux. Convention is that upper bounds of exchange fluxes come
            with positive sign and therefore expression should be
            non-negative, representing the magnitude of this upper bound.
        condition : optlang.symbolics expression
            The symbolic expression for non-negative condition on metabolite
            concentrations required for correct evaluation of upper bound
            expression. Numerical approximation can generate unphysical,
            negative concetration values.
        control_parameters : list
            A list of `ControlParameter` objects (if any) appearing in the
            supplied symbolic expression.

        """
        if control_parameters is not None:
            if type(control_parameters) is not list:
                control_parameters = [control_parameters]

        if exchange_flux_id not in self.exchange_fluxes:
            raise Exception(
                "Error: reaction {} is not an exchange flux in model!".format(
                    exchange_flux_id
                )
            )
        self.exchange_fluxes.get_by_id(exchange_flux_id).upper_bound_expression = [
            expression,
            condition,
            control_parameters,
        ]

    def simulate(self, tstart, tstop, tout, output_fluxes=None):
        """Simulate model.

        Parameters
        -------
        tstart : float
            Initial time point to be used in simulation of the model.
        tstop : float
            Final time point to be used in simulation of the model.
        tout : float
            Output frequency to be used in simulation of the model.
        output_fluxes : list
            Optional list of reaction ids whose fluxes are to be printed to
            results along with kinetic variables.

        Returns
        -------
        tuple of 2 pd.Dataframe's
            1. time, concentrations (in `self.kinetic_variables`)
            2. time, flux trajectories (in )

        """

        print_fluxes = []
        if output_fluxes:
            for rxn in output_fluxes:
                if not self.reactions.__contains__(rxn):
                    logger.warning(
                        f"Ignoring reaction {rxn} since it does not correspond"
                        f"to a reaction in the model."
                    )
                else:
                    print_fluxes.extend([self.reactions.get_by_id(rxn)])
        else:
            output_fluxes = []

        with tempfile.TemporaryDirectory() as directory:
            logger.debug(f"The created temporary directory is {directory}")
            library.create(directory)
            self.add_to_library(tstart, tstop, tout, print_fluxes, directory)
            functionlib = jit.compile(directory)
            logger.debug(f"Function library {functionlib} compiled successfully...")
            results = simulate_dfba_model(self, functionlib)  # noqa: F405

            # Post-processing of results
            kv_ids = [kv.id for kv in self.kinetic_variables]
            header = ["time"] + kv_ids + output_fluxes
            df_results = pd.DataFrame(results, columns=header)

        return (
            df_results[["time"] + kv_ids],
            df_results[["time"] + output_fluxes],
        )

    def lp_problem(self):
        """LP problem.

        Returns
        -------
        lp_problem : Swig Object of type `glp_prob *`
            SWIGLPK object representing FBA model as pointer to GLPK problem

        """

        self.cobra_model.solver.update()
        return self.cobra_model.solver.problem
        # TODO:
        # def lp_config(self):
        """
        LP problem configuration

        Returns
        -------
        lp_problem : proxy of Swig Object of type `glp_smcp *`
            SWIGLPK object representing configuration of GLPK problem.
        """

        # self.cobra_model.solver.update()
        # return self.cobra_model.solver.configuration._smcp

    @property
    def id(self):
        """."""
        return getattr(self, "_id", None)

    @property
    def cobra_model(self):
        """."""
        return self._cobra_model

    @property
    def reactions(self):
        """."""
        return self._reactions

    @property
    def objectives(self):
        """."""
        return self._objectives

    @property
    def directions(self):
        """."""
        return self._directions

    @property
    def kinetic_variables(self):
        """."""
        return self._kinetic_variables

    @property
    def exchange_fluxes(self):
        """."""
        return self._exchange_fluxes

    @property
    def user_data(self):
        """."""
        return self._user_data

    @property
    def solver_data(self):
        """."""
        return self._solver_data

    def add_to_library(self, tstart, tstop, tout, print_fluxes, directory):
        """Add model to library.

        Parameters
        -------
        tstart : float
            Initial time point to be used in simulation of the model.
        tstop : float
            Final time point to be used in simulation of the model.
        tout : float
            Length of time interval for output.
        print_fluxes : list
            List of reactions whose fluxes are to be printed to results
            along with kinetic variables.
        directory: string
                Path to temporary directory containing library.

        """

        for objective in self.objectives[:-1]:
            logger.debug(f"Adding objective to user data for model {self.id}.")
            rxn = self.reactions.index(objective)
            expression = (
                self.cobra_model.variables[2 * rxn]
                - self.cobra_model.variables[2 * rxn + 1]
            )
            constraint = self.cobra_model.problem.Constraint(
                expression, name=objective, ub=None, lb=None
            )
            solver.add_cons_vars_to_problem(self.cobra_model, constraint, sloppy=True)
        for objective in self.objectives:
            self.user_data.add_objective(
                library.col_indices(self.reactions, objective), [1, -1]
            )
        self.user_data.set_directions(self.directions)
        self.cobra_model.solver.update()
        nkin = len(self.kinetic_variables)
        initial_conditions = [tstart]
        change_pnts = []
        control_parameter = None
        for kinetic_variable in self.kinetic_variables:
            initial_conditions.extend([kinetic_variable.initial_condition])
            if kinetic_variable.rhs_expression[1] is not None:
                for k in range(len(kinetic_variable.rhs_expression[1])):
                    control_parameter = kinetic_variable.rhs_expression[1][k]
                    change_pnts.extend(control_parameter.change_points)
        nrow = len(self.cobra_model.constraints)
        required_indices = []
        for exchange_flux in self.exchange_fluxes:
            required_indices.extend(
                library.indices(nrow, self.reactions, exchange_flux.id)
            )
        nreq = len(required_indices)
        exchange_indices = []
        for exchange_flux in self.exchange_fluxes:
            lb = exchange_flux.lower_bound_expression
            ub = exchange_flux.upper_bound_expression
            if ub is not None:
                exchange_indices.append(
                    library.indices(nrow, self.reactions, exchange_flux.id)[0]
                )
                if ub[2] is not None:
                    for k in range(len(ub[2])):
                        control_parameter = ub[2][k]
                        change_pnts.extend(control_parameter.change_points)
            if lb is not None:
                exchange_indices.append(
                    library.indices(nrow, self.reactions, exchange_flux.id)[1]
                )
                if lb[2] is not None:
                    for k in range(len(lb[2])):
                        control_parameter = lb[2][k]
                        change_pnts.extend(control_parameter.change_points)
        nexc = len(exchange_indices)
        change_pnts = list(set(change_pnts))
        change_pnts = sorted(change_pnts)
        current_indices = []
        for rxn in print_fluxes:
            current_indices.extend(library.indices(nrow, self.reactions, rxn.id))
        logger.debug("Adding model {self.id} to library.")
        library.write_model_to_file(
            str(self.id),
            self.kinetic_variables,
            self.exchange_fluxes,
            nexc,
            nreq,
            exchange_indices,
            change_pnts,
            directory,
        )
        logger.debug("Setting user data for model {self.id}.")
        self.user_data.set_name(str(self.id))
        self.user_data.set_kinetic_dimensions(nkin, nexc, nreq)
        self.user_data.set_output_times(tstop, tout)
        self.user_data.set_initial_conditions(initial_conditions)
        self.user_data.set_exchange_indices(exchange_indices)
        self.user_data.set_required_indices(required_indices)
        self.user_data.set_current_indices(current_indices)
        self.user_data.set_change_points(change_pnts)
