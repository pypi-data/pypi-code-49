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
Copyright 2014-2020 Sylvain Meignier and Anthony Larcher
"""

from .clustering.hac_bic import HAC_BIC
from .clustering.hac_clr import HAC_CLR
from  .clustering.hac_iv import hac_iv, hac_iv_it

from .clustering.hac_utils import argmin
from .clustering.hac_utils import argmax
from .clustering.hac_utils import roll
from .clustering.hac_utils import stat_server_remove
from .clustering.hac_utils import scores_remove
from .clustering.hac_utils import scores2distance
from .clustering.hac_utils import stat_server_merge
from .clustering.hac_utils import bic_square_root

from .clustering.cc_iv import ConnectedComponent

from .model_iv import ModelIV

from .diar import Diar
from .segmentation import sanity_check
from .segmentation import bic_linear
from .segmentation import div_gauss

from .viterbi import Viterbi

from .scoring import DER


__author__ = "Sylvain Meignier and Anthony Larcher"
__copyright__ = "Copyright 2014-20120 Sylvain Meignier and Anthony Larcher"
__license__ = "LGPL"
__maintainer__ = "Sylvain Meignier"
__email__ = "sylvain.meignierr@univ-lemans.fr"
__status__ = "Production"
__docformat__ = 'reStructuredText'
__version__ = "0.1.4.3"
