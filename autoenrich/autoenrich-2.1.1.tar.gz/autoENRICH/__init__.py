# Copyright 2020 Will Gerrard
#This file is part of autoENRICH.

#autoENRICH is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#autoENRICH is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.

#You should have received a copy of the GNU Affero General Public License
#along with autoENRICH.  If not, see <https://www.gnu.org/licenses/>.

"""
autoENRICH main module
======================

Provides
	1. analysis
	2. boltzmann
	3. conformational_search
	4. file_creation
	5. file_read
	6. ml
	7. molecule
	8. preferences
	9. pybel_helpers
	10. reference
	11. top_level (command modules)
	12. util

"""

from . import analysis
from . import boltzmann
from . import conformational_search
from . import file_creation
from . import file_read
from . import ml
from . import molecule
from . import preferences
from . import pybel_helpers
from . import reference
from . import top_level
from . import util

__author__ = "Will Gerrard"
__copyright__ = "Copyright 2020"
__credits__ = ["Will Gerrard (2020) https://github.com/wg12385/autoENRICH"]
__licence__ = "GNU APGL v3+"
__version__ = "0.0.1"
__maintainer__ = "Will Gerrard"
__email__ = "will.gerrard@bristol.ac.uk"
__status__ = "Beta"
