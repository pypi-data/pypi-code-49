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


"""Create top level imports."""


__author__ = """
David S. Tourigny, Columbia University Irving Medical Center, New York, USA
Moritz E. Beber, Novo Nordisk Foundation Center for Biocustainability, Technical University of Denmark
"""
__email__ = """
dst2156@cumc.columbia.edu
morbeb@biosustain.dtu.dk
"""
from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions


from .helpers import show_versions
from .control import ControlParameter
from .exchange import ExchangeFlux
from .variable import KineticVariable
from .model import DfbaModel
