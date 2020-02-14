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


def mol_read_type(mol):
	type_list = []
	type_array = np.zeros(len(mol.atoms), dtype=np.int32)
	Periodic_table = Get_periodic_table()
	for i in range(len(mol.atoms)):
		type = int(mol.atoms[i].atomicnum)
		type_array[i] = type
		type_list.append(Periodic_table[type])

	return type_list, type_array

def mol_getatoms(mol):
	atomnumber = len(mol.atoms)
	return atomnumber

def mol_read_xyz(mol):
	xyz_array = np.zeros((len(mol.atoms),3), dtype=np.float64)
	for i in range(len(mol.atoms)):
		xyz_array[i][0] = float(mol.atoms[i].coords[0])
		xyz_array[i][1] = float(mol.atoms[i].coords[1])
		xyz_array[i][2] = float(mol.atoms[i].coords[2])

	# Return array is zero indexed
	return xyz_array

def mol_read_dist(mol):
	xyz_array = mol_read_xyz(mol)
	atoms = mol_getatoms(mol)
	d_array = np.zeros((atoms, atoms), dtype=np.float64)
	for i in range(atoms):
		for j in range(atoms):
			d_array[i][j] = np.absolute(np.linalg.norm(xyz_array[i] - xyz_array[j]))

	return d_array
