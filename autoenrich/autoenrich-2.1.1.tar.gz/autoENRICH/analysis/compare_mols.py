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

from autoENRICH.util.flag_handler.hdl_targetflag import target_to_flag
import numpy as np

# Attempts to determine if the molecules are the same molecule
def mol_isequal(mol1, mol2, print=False):
	# input:
	# mol1: autoENRICH nmrmol object (molecule 1)
	# mol2: autoENRICH nmrmol object (molecule 2)
	# print: True/False , whether to print information about bad matches

	# Returns: True/False

	# First simple check: same number of atoms
	if len(mol1.types) != len(mol2.types):
		if print:
			print('Molecules are different sizes')
		return False
	atoms = len(mol1.types)

	# Check for same chemical formula
	counts1 = np.zeros(1000, dtype=np.int32)
	counts2 = np.zeros(1000, dtype=np.int32)
	for i in range(atoms):
		counts1[mol1.types[i]] += 1
		counts2[mol2.types[i]] += 1
	Fail = False
	for i in range(1000):
		if counts1[i] == 0 and counts2[i] == 0:
			continue
		if counts1[i] != counts2[i]:
			Fail = True
	if Fail:
		if print:
			print('Molecules have different compositions')
		return False

	# Check for same connectivity
	# Done by checking both have the same number of each coupling type: 1JCH, 3JNH, . . .
	cpl_dict1 = {}
	cpl_dict2 = {}
	for i in range(atoms):
		for j in range(atoms):
			if mol1.conn[i][j] != 0:
				flag1 = target_to_flag([mol1.coupling_len[i][j], mol1.types[i], mol1.types[j]])
				flag2 = target_to_flag([mol2.coupling_len[i][j], mol2.types[i], mol2.types[j]])

				if flag1 not in cpl_dict1.keys():
					cpl_dict1[flag1] = 0
				if flag2 not in cpl_dict2.keys():
					cpl_dict2[flag2] = 0

				cpl_dict1[flag1] = cpl_dict1[flag1] + 1
				cpl_dict2[flag2] = cpl_dict2[flag2] + 1
	if cpl_dict1 != cpl_dict2:
		if print:
			print('Connectivity is different')
			return False

	# Return true if no checks fail
	return True


















###
