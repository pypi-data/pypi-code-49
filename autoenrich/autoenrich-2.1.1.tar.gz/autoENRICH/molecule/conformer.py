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

import numpy as np
import glob
from .nmrmol import nmrmol

class conformer(nmrmol):

	def __init__(self, molid, path=''):
		nmrmol.__init__(self, path=path, molid=molid)

		# store location of conf search xyz file
		self.xyz_file = 'None'

		# store location and status of optimisation files
		self.opt_in = 'None'
		self.opt_log = 'None'
		self.opt_status = 'None'

		# store location and status of NMR files
		self.nmr_in = 'None'
		self.nmr_log = 'None'
		self.nmr_status = 'None'

		self.energy = 404.404
		self.pop = 404.404




###
