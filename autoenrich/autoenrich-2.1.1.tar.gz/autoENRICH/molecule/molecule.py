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
import pickle

from autoENRICH.conformational_search import conformational_search as conf_search
from .conformer import conformer as conformerclass
from .nmrmol import nmrmol
import glob

# global molecule object, contains everything for one auto-ENRICH run
class molecule(nmrmol):

	def __init__(self, molid, path=''):
		nmrmol.__init__(self, molid, path)

		self.conformers = []
		self.stage = 'init'

	# function to remove redundant conformers
	def remove_redundant(self, threshold=0.001):
		self.conformers = redundant_conformer_elim(self.conformers, threshold=threshold)

	# average NMR properties
	def boltzmann_average(self):
		# should there be equivalent bolzmann functions for variance ??
		self.shift = boltzmann_shift(self.conformers)
		self.coupling = boltzmann_coupling(self.conformers)
		self.variance = boltzmann_variance(self.conformers)

	# do conformational searching
	def generate_conformers(self, smiles, path='', iterations=100, RMSthresh=1, maxconfs=100, Ethresh=100000):
		xyzs, energies = conf_search.torsional_search(self, smiles, iterations=iterations, RMSthresh=RMSthresh)
		print('Initial search complete,', len(xyzs), 'conformers found')

		xyzs, energies = conf_search.select_conformers(xyzs, energies, maxconfs=maxconfs, Ethresh=Ethresh)

		for x, xyz in enumerate(xyzs):
			new_conf = conformerclass(str(x), path=path)
			new_conf.xyz = xyz
			new_conf.types = self.types
			new_conf.conn = self.conn
			new_conf.coupling_len = self.coupling_len
			new_conf.energy = energies[x]
			self.conformers.append(new_conf)

		self.stage = 'pre-opt'


###
