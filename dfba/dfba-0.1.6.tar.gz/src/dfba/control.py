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

"""Definition of `ControlParameter` class."""

from optlang import symbolics


class ControlParameter(symbolics.Symbol):
    """Holds information regarding a control parameter in a `DfbaModel` object.

    Attributes
    ----------
    id: string
        The identifier to associate with this control parameter.

    change_points: list
        The time points at which this control parameter changes value.

    values: list
        The values taken by this control parameter.

    """

    def __init__(self, name, change_points=None, values=None, *args, **kwargs):
        """`symbolics.Symbol` with list of change points and list of values."""
        symbolics.Symbol.__init__(self, name, *args, **kwargs)
        self._id = name
        self.set_parameters(change_points, values)

    @property
    def id(self):
        """For convenience, synonym with .name from `symbolics.Symbol`."""
        return self._id

    @property
    def change_points(self):
        """Time points at which this control parameter changes value."""
        return self._change_points

    @property
    def values(self):
        """Actual values of the control parameter."""
        return self._values

    def set_parameters(self, change_points, values):
        """Standardize input attributes."""
        if type(change_points) is not list:
            change_points = [change_points]
        if type(values) is not list:
            values = [values]
        if len(change_points) + 1 != len(values):
            raise Exception(
                "Error: change points list must one shorter than values list!"
            )
        if len(change_points) > 1:
            for i in range(len(change_points) - 1):
                if change_points[i] > change_points[i + 1]:
                    raise Exception(
                        "Error: change points must be listed" "in increasing order!"
                    )
        self._change_points = change_points
        self._values = values
