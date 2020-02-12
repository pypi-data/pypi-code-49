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

"""Definition of `ExchangeFlux` class."""


from optlang import symbolics


class ExchangeFlux(symbolics.Symbol):
    """Class for holding information for an exchange flux in a `DfbaModel` object.

    Attributes
    ----------
    id: string
        The identifier to associate with this exchange flux.

    lower_bound_expression: optlang.symbolics expression
        The symbolic expression for calculating the lower bound of this
        exchange flux.

    upper_bound_expression: optlang.symbolics expression
        The Symbolic expression for calculating the upper bound of this
        exchange flux.

    """

    def __init__(self, name, *args, **kwargs):
        """`symbolics.Symbol` with lower and upper bounds to be added."""
        symbolics.Symbol.__init__(self, name, *args, **kwargs)
        self._id = name
        self.lower_bound_expression = None
        self.upper_bound_expression = None

    @property
    def id(self):
        """For convenience, synonym with .name from `symbolics.Symbol`."""
        return self._id

    @property
    def lower_bound_expression(self):
        """Relate the exchange rate to some symbolic expression."""
        return self._lower_bound_expression

    @property
    def upper_bound_expression(self):
        """Relate the exchange rate to some symbolic expression."""
        return self._upper_bound_expression

    @lower_bound_expression.setter
    def lower_bound_expression(self, expression):
        self._lower_bound_expression = expression

    @upper_bound_expression.setter
    def upper_bound_expression(self, expression):
        self._upper_bound_expression = expression
