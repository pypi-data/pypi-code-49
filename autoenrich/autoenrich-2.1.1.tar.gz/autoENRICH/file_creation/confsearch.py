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


# Write file to perform conformational search
def make_confsearch_script(scriptname, pickle_file, smiles, path='', iterations=2000,
							RMSthresh=10.0, maxconfs=10, Ethresh=999.99):
	# Input:
	# scriptname : name of script to produce
	# pickle_file: pickle file containing molecule (relative to 'path')
	# smiles: smiles string representing molecule
	# aE_dir: directory containing
	# path: path to molecule folder
	# iterations: number of iterations for torsional angle search
	# RMSthresh: RMS threshold for torsional angle search
	# maxconfs: Maximum number of conformers to produce
	# Ethresh: Energy threshold above which conformers are discarded

	# Returns: None

	strings = []
	# produce script to do conformational search
	strings.append('import sys')
	strings.append("import autoENRICH')")
	strings.append('import pickle')
	strings.append('from file_creation.structure_formats import xyz')
	strings.append("file = '{0:<10s}'".format(pickle_file.split('/')[-1]))
	strings.append("molecule = pickle.load(open(file, 'rb'))")
	strings.append("molecule.generate_conformers('{smiles:<10s}', path='{path:<10s}', iterations={its:<10d}".format(smiles=smiles,
																												path=path,
																												its=iterations))
	strings.append(", RMSthresh={RMS:<10f}, maxconfs={maxconfs:<10d}, Ethresh={Ethresh:<10f})".format(RMS=RMSthresh,
																									maxconfs=maxconfs,
																									Ethresh=Ethresh))
	strings.append("for conformer in molecule.conformers:")
	strings.append("\txyz_file = 'conf_search/' +  conformer.molid + '.xyz'")
	strings.append("\txyz.nmrmol_to_xyz(molecule, xyz_file)")
	strings.append("pickle.dump(molecule, open(file, 'wb'))")

	# print script to file
	with open(path + scriptname, 'w') as f:
		for string in strings:
			print(string, file=f)
