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
import openbabel
from autoENRICH.reference.periodic_table import Get_periodic_table

def mol_iswhole(mol):
	iswhole = True
	atoms = mol_getatoms(mol)
	for i in range(atoms):
		for j in range(atoms):
			if i == j:
				continue
			good = False

			while good == False:
				for length in range(0, atoms):
					paths = mol_find_all_paths(mol, i, j, length)
					if len(paths) > 0:
						good = True
						break
				if not good:
					iswhole = False
					return iswhole
	return iswhole

def mol_splitmol(mol):
	atoms = mol_getatoms(mol)
	structures = []
	assigned = []
	structures.append([])

	depth = 0
	while len(assigned) < atoms:

		for i in range(atoms):
			if i in assigned:
				continue

			if len(structures[depth]) == 0:
				structures[depth].append(i)
				assigned.append(i)

			for j in range(atoms):
				if j in assigned or j == i:
					continue

				for length in range(0, atoms):
					paths = mol_find_all_paths(mol, i, j, length)
					if len(paths) > 0:
						structures[depth].append(j)
						assigned.append(j)
						break
						continue

			structures.append([])
			depth += 1

	lent = 0
	for structure in structures:
		lent += len(structure)

	assert lent == atoms

	return structures
