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

from autoENRICH.reference.periodic_table import Get_periodic_table

def labelmaker(i, j, mol):
	Periodic_table = Get_periodic_table()
	lent = mol.coupling_len[i][j]
	label = str(lent) + str('J')
	if mol.types[int(i)] >= mol.types[int(j)]:
		label = label + str(Periodic_table[mol.types[int(i)]]) + str(Periodic_table[mol.types[int(j)]])
	else:
		label = label + str(Periodic_table[mol.types[int(j)]]) + str(Periodic_table[mol.types[int(i)]])

	return label
