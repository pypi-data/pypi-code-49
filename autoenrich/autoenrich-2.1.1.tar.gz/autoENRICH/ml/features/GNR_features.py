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

from autoENRICH.util.flag_handler.hdl_targetflag import flag_to_target
import numpy as np

# Make 'dummy features' for a given target, used to get list of references
def get_dummy_features(mols, targetflag='CCS'):
	# Input:
	#	mols: list of autoENRICH nmrmol objects
	#	targetflag: flag corresponding to nmr parameter (string)

	# Returns:
	#	x: empty list (where features would normally go)
	#	y: 1D list of NMR parameters
	#	r: 1D list of NMR parameter references (molid, atom(1, atom2))

	target = flag_to_target(targetflag)

	x = []
	y = []
	r = []

	for mol in mols:
		if len(target) == 1:
			for i in range(len(mol.types)):
				if mol.types[i] == target[0]:
					y.append(mol.shift[i])
					r.append([mol.molid, i])

		if len(target) == 3:
			for i in range(len(mol.types)):
				for j in range(len(mol.types)):
					if i == j:
						continue

					if not ( mol.types[i] == target[1] and mol.types[j] == target[2] ):
						continue

					if mol.coupling_len[i][j] != target[0]:
						continue

					y.append(mol.coupling[i][j])
					r.append([mol.molid, i, j])

	return x, y, r
