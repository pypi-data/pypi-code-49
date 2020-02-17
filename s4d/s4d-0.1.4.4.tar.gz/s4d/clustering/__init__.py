# -*- coding: utf-8 -*-
#
# This file is part of s4d.
#
# s4d is a python package for speaker diarization.
# Home page: http://www-lium.univ-lemans.fr/s4d/
#
# s4d is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# s4d is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with s4d.  If not, see <http://www.gnu.org/licenses/>.


"""
Copyright 2014-2020 Sylvain Meignier
"""

from .gauss import GaussFull
from .hac_utils import bic_square_root
from .hac_bic import HAC_BIC

from .hac_utils import argmin
from .hac_utils import argmax
from .hac_utils import roll
from .hac_utils import stat_server_remove
from .hac_utils import scores_remove
from .hac_utils import scores2distance
from .hac_utils import stat_server_merge
from .hac_utils import bic_square_root