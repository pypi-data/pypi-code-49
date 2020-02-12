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


"""Definition of `KineticVariable` class."""

from optlang import symbolics


class KineticVariable(symbolics.Symbol):
    """Class for holding information for a kinetic variable in a `DfbaModel` object.

    Attributes
    ----------
    id: string
        The identifier to associate with this kinetic variable.

    rhs_expression: optlang.symbolics expression
        The symbolic expression for calculating derivative of this kinetic
        variable wrt time.

    initital_condition: int or float
        The initial value of this kinetic variable to be used at start of
        simulation.

    """

    def __init__(self, name, initial_condition=0.0, *args, **kwargs):
        """`symbolics.Symbol` with rhs expression to be added."""
        symbolics.Symbol.__init__(self, name, *args, **kwargs)
        self._id = name
        self.initial_condition = initial_condition
        self.rhs_expression = None

    @property
    def id(self):
        """For convenience, synonym with .name from `symbolics.Symbol`."""
        return self._id

    @property
    def rhs_expression(self):
        """Relate the rhs expression to some symbolic expression."""
        return self._rhs_expression

    @property
    def initial_condition(self):
        """Relate the ininital condition to some int or float value."""
        return self._initial_condition

    @rhs_expression.setter
    def rhs_expression(self, expression):
        self._rhs_expression = expression

    @initial_condition.setter
    def initial_condition(self, value):
        if not isinstance(value, (int, float)):
            raise Exception(
                f"Error: initial condition for kinetic variable {self.id} must"
                f"be int or float!"
            )
        self._initial_condition = value
