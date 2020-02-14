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


# Print molecule properties to csv file
def print_mol_csv(outname, refs, typerefs, values, labels):
	# Input:
	# outname: name of output file
	# refs: molecular property references (m x k)	m = number of properties,
	#												k = number of atoms in reference + 1,
	#												ref[y, z] = (molid, atomid1, atomid2, atomid3, . . . )
	# typerefs: atom types corresponding to the atom ids in refs (m x k)
	#												ref[y, z] = (molid, atomtype1, atomtype2, atomtype3, . . . )
	# values: molecular properties (n, m, k)
	# labels: Labels for molecule sets

	# Returns: None

	# start empty line array (to print at the end)
	lines = []
	# get periodic table array
	p_table = Get_periodic_table()
	# Get number of molecule sets
	sets = len(refs[0])
	# Get first part of header string (molecule set labels for mol IDs)
	idstring = ""
	for x in range(len(refs[0])):
		idstring = idstring + "{label:<s}MOLID,".format(label=labels[x])
	# Get second part of header string (atom references)
	refstring = ""
	for y in range(1, len(refs[0][0])):
		refstring = refstring + "{atom:<s},{type:<s},".format(atom='Atom',
											type='Type',)
	# Get third part of header string (molecule set labels for values)
	valstring = ""
	for z in range(len(values[0])):
		valstring = valstring + "{label:<s}VALUE,".format(label=labels[z])
	# Add header string
	lines.append(idstring+refstring+valstring)
	# Loop through property references
	for i in range(len(refs)):
		# Get molid string
		idstring = ""
		for x in range(len(refs[i])):
			idstring = idstring + "{id:<s},".format(id=refs[i][x][0])
		# Get atomic ref string (atomid, atomtype) x number of atom references
		refstring = ""
		for y in range(1, len(refs[0][0])):
			refstring = refstring + "{atom:<s},{type:<s},".format(atom=str(refs[i][0][y]),
												type=p_table[typerefs[i][0][y-1]])
		# Get value string (value1, value2, . . .)
		valstring = ""
		for z in range(len(values[i])):
			valstring = valstring + "{value:<.4f},".format(value=values[i][z])
		# Construct line and add to list
		lines.append(idstring+refstring+valstring)

	# Print all lines to file
	with open(outname, 'w') as f:
		for line in lines:
			print(line, file=f)
