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
import sys
from autoENRICH.file_read import orca_read, g09_read, nmredata_read, structure_read
from autoENRICH.reference.periodic_table import Get_periodic_table
import pickle


class nmrmol(object):
	"""
		nmr data file
	"""

	def __init__(self, molid, path=''):
		self.path = path

		self.molid = str(molid)
		self.types = []
		self.xyz = []
		self.conn = []

		self.shift = []
		self.shift_var = []

		self.coupling = []
		self.coupling_var = []
		self.coupling_len = []

		self.energy = -404.404


	def read_structure(self, file, type):
		old_type_array = self.types
		old_xyz_array = self.xyz
		self.xyz, self.types, self.conn, self.coupling_len = structure_read.generic_pybel_read(file, type)

		if not (np.array_equal(old_type_array, self.types) or np.array_equal(old_xyz_array, self.xyz)):
			self.shift = []
			self.shift_var = []
			self.coupling = []
			self.coupling_var = []

	def read_opt(self, file, type):
		if type == 'orca':
			#self.xyz, self.types, self.conn, self.coupling_len = orca_read.read_structure(file)
			self.energy = orca_read.read_opt(file)


	def read_nmr(self, file, type):
		if type == 'orca':
			self.xyz, self.types, self.conn, self.coupling_len = orca_read.read_structure(file)
			self.shift, self.coupling = orca_read.read_nmr(file)
		elif type == 'g09':
			self.xyz, self.types, self.conn, self.coupling_len = structure_read.generic_pybel_read(file, 'g09')
			self.shift, self.coupling = g09_read.read_nmr(file, len(self.types))
			self.shift_var = np.zeros((len(self.types)), dtype=np.float64)
			self.coupling_var = np.zeros((len(self.types), len(self.types)), dtype=np.float64)
		elif type == 'nmredata':
			self.xyz, self.types, self.conn, _ = structure_read.fast_generic_pybel_read(file, 'sdf')
			self.shift, self.shift_var, self.coupling, self.coupling_var, self.coupling_len = nmredata_read.read_nmr(file, len(self.types))
		else:
			self.xyz, self.types, self.conn, self.coupling_len = structure_read.generic_pybel_read(file, type)
			atoms = len(self.types)
			self.shift = np.zeros((atoms), dtype=np.float64)
			self.shift_var = np.zeros((atoms), dtype=np.float64)
			self.coupling = np.zeros((atoms, atoms), dtype=np.float64)
			self.coupling_var = np.zeros((atoms, atoms), dtype=np.float64)
			print('non-nmr file detected, generated dummy file'.format(type))

	def scale_shifts(self, scaling_factors={}):
		periodic_table = Get_periodic_table()
		for nucleus, factor in scaling_factors.items():
			if nucleus in ['basis_set', 'functional']:
				continue

			for i in range(len(self.shift)):
				if periodic_table[self.types[i]] == nucleus:
					self.shift[i] = (self.shift[i] - factor[1]) / float(factor[0])

	def save_pickle(file):
		pickle.dump(self, open(file, "wb"))














####
