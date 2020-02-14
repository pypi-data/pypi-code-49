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

# Write an nmrmol object to an xyz file
def nmrmol_to_xyz(mol, outname, num=-404):
	periodic_table = Get_periodic_table()
	with open(outname, 'w') as f:
		print(len(mol.types), file=f)
		if num == -404:
			print(mol.molid, file=f)
		else:
			string = "{0:<10d}\t{1:<20s}".format(num, mol.molid)
			print(string, file=f)

		for i in range(len(mol.types)):
			string = "{i:<10s}\t{x:<10.6f}\t{y:<10.6f}\t{z:<10.6f}".format(i=periodic_table[mol.types[i]],
																			x=mol.xyz[i][0],
																			y=mol.xyz[i][1],
																			z=mol.xyz[i][2])
			print(string, file=f)
