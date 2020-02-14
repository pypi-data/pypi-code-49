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

# define functions to produce QML based features
import qml.fchl
import qml.representations
from autoENRICH.util.flag_handler.hdl_targetflag import flag_to_target
import numpy as np


# all features for QML are of the shape: [n, p, r]
# where n is the number of "features", each n is a single NMR environment
# p is the number of sub environment features needed in each NMR environment
# r is the representation itself

# Make FCHL features
def get_FCHL_features(mols, targetflag='CCS', cutoff=5.0, max=400):
	# Input:
	#	mols: list of autoENRICH nmrmol objects
	#	targetflag: flag corresponding to nmr parameter (string)
	#	cutoff: distance cutoff for representation
	#	max: maximum size of molecules

	# Returns:
	#	x: 1D list of features (each item in list is a numpy array)
	#	y: 1D list of NMR parameters
	#	r: 1D list of NMR parameter references (molid, atom(1, atom2))

	# convert flag to target
	target = flag_to_target(targetflag)

	x = []
	y = []
	r = []
	# Loop through molecules to construct features
	for mol in mols:
		# Make representations using qml function
		reps = qml.fchl.generate_representation(mol.xyz, mol.types, max, cut_distance=cutoff)
		# If chemical shift target
		if len(target) == 1:
			for i in range(len(mol.types)):
				if mol.types[i] == target[0]:
					x.append([reps[i]])
					y.append(mol.shift[i])
					r.append([mol.molid, i])
		# If coupling target
		if len(target) == 3:
			for i in range(len(mol.types)):
				for j in range(len(mol.types)):
					if i == j:
						continue

					if not (mol.types[i] == target[1] and mol.types[j] == target[2]):
						continue

					if mol.coupling_len[i][j] != target[0]:
						continue

					if i > j:
						x.append([reps[j], reps[i]])
						y.append(mol.coupling[i][j])
						r.append([mol.molid, j, i])
					else:
						x.append([reps[i], reps[j]])
						y.append(mol.coupling[i][j])
						r.append([mol.molid, i, j])

	return x, y, r

# Make mbtypes for aSLATM representation
def get_aSLATM_mbtypes(mols):
	# Input:
	#	mols: list of autoENRICH nmrmol objects

	# Returns: mbtypes (list of atom type combinations)

	if len(mols) == 0:
		mbtypes = [[1],[1,1], [1,1,1], [1,1,6], [1,1,7], [1,1,8], [1,1,9], [1,6], [1,6,1], [1,6,6], [1,6,7], [1,6,8], [1,6,9], [1,7], [1,7,1], [1,7,6], [1,7,7], [1,7,8], [1,7,9], [1,8], [1,8,1], [1,8,6], [1,8,7], [1,8,8], [1,8,9], [1,9], [1,9,1], [1,9,6], [1,9,7], [1,9,8], [1,9,9], [6], [6,1], [6,1,1], [6,1,6], [6,1,7], [6,1,8], [6,1,9], [6,6], [6,6,1], [6,6,6], [6,6,7], [6,6,8], [6,6,9], [6,7], [6,7,1], [6,7,6], [6,7,7], [6,7,8], [6,7,9], [6,8], [6,8,1], [6,8,6], [6,8,7], [6,8,8], [6,8,9], [6,9], [6,9,1], [6,9,6], [6,9,7], [6,9,8], [6,9,9], [7],[7,1], [7,1,1], [7,1,6], [7,1,7], [7,1,8], [7,1,9], [7,6], [7,6,1], [7,6,6], [7,6,7], [7,6,8], [7,6,9], [7,7], [7,7,1], [7,7,6], [7,7,7], [7,7,8], [7,7,9], [7,8], [7,8,1], [7,8,6], [7,8,7], [7,8,8], [7,8,9], [7,9], [7,9,1], [7,9,6], [7,9,7], [7,9,8], [7,9,9], [8], [8,1], [8,1,1], [8,1,6], [8,1,7], [8,1,8], [8,1,9], [8,6], [8,6,1], [8,6,6], [8,6,7], [8,6,8], [8,6,9], [8,7], [8,7,1], [8,7,6], [8,7,7], [8,7,8], [8,7,9], [8,8], [8,8,1], [8,8,6], [8,8,7], [8,8,8], [8,8,9], [8,9], [8,9,1], [8,9,6], [8,9,7], [8,9,8], [8,9,9], [9], [9,1], [9,1,1], [9,1,6], [9,1,7], [9,1,8], [9,1,9], [9,6], [9,6,1], [9,6,6], [9,6,7], [9,6,8], [9,6,9], [9,7], [9,7,1], [9,7,6], [9,7,7], [9,7,8], [9,7,9], [9,8], [9,8,1], [9,8,6], [9,8,7], [9,8,8], [9,8,9], [9,9], [9,9,1], [9,9,6], [9,9,7], [9,9,8], [9,9,9]]

	else:
		nuclear_charges = []
		for tmp_mol in mols:
			nuclear_charges.append(tmp_mol.types)
		mbtypes = qml.representations.get_slatm_mbtypes(nuclear_charges)

	return mbtypes

# Make aSLATM features
def get_aSLATM_features(mols, targetflag='CCS', cutoff=5.0, max=400, mbtypes=[]):
	# Input:
	#	mols: list of autoENRICH nmrmol objects
	#	targetflag: flag corresponding to nmr parameter (string)
	#	cutoff: distance cutoff for representation
	#	max: maximum size of molecules
	#	mbtypes: list of all possible atoms, pairs and triplets

	# Returns:
	#	x: 1D list of features (each item in list is a numpy array)
	#	y: 1D list of NMR parameters
	#	r: 1D list of NMR parameter references (molid, atom(1, atom2))

	# convert flag to target
	target = flag_to_target(targetflag)

	x = []
	y = []
	r = []

	# If no mbtypes given, get default ones
	if len(mbtypes) == 0:
		mbtypes = get_aSLATM_mbtypes([])

	# loop through molecules to construct features
	for mol in mols:
		# Basic assertions
		assert mol.xyz.shape[1] == 3
		assert mol.xyz.shape[0] == mol.types.shape[0]
		# Get representations from qml function
		reps = qml.representations.generate_slatm(mol.xyz, mol.types, mbtypes, rcut=cutoff)
		# Convert features to numpy array (no idea why its a list in the first place)
		reps = np.asarray(reps)
		# if chemical shift target
		if len(target) == 1:
			for i in range(len(mol.types)):
				if mol.types[i] == target[0]:
					x.append([reps[i]])
					y.append(mol.shift[i])
					r.append([mol.molid, i])
		# If coupling target
		if len(target) == 3:
			for i in range(len(mol.types)):
				for j in range(len(mol.types)):
					if i == j:
						continue
					if not ( mol.types[i] == target[1] and mol.types[j] == target[2] ):
						continue

					if mol.coupling_len[i][j] != target[0]:
						continue

					if i > j:
						x.append([reps[j], reps[i]])
						y.append(mol.coupling[i][j])
						r.append([mol.molid, j, i])
					else:
						x.append([reps[i], reps[j]])
						y.append(mol.coupling[i][j])
						r.append([mol.molid, i, j])

	return x, y, r


def get_CMAT_features(mols, targetflag='CCS', cutoff=5.0, max=100,
				central_decay=-1, interaction_cutoff =1e6, interaction_decay=-1):
	# Input:
	#	mols: list of autoENRICH nmrmol objects
	#	targetflag: flag corresponding to nmr parameter (string)
	#	cutoff: distance cutoff for representation
	#	max: maximum size of molecules
	#	central_decay: representation parameter
	#	interaction_cutoff: representation parameter
	#	interaction_decay: representation parameter

	# Returns:
	#	x: 1D list of features (each item in list is a numpy array)
	#	y: 1D list of NMR parameters
	#	r: 1D list of NMR parameter references (molid, atom(1, atom2))

	# Convert flag to target
	target = flag_to_target(targetflag)

	x = []
	y = []
	r = []
	'''
	for mol in mols:
		if len(mol.types) > max:
			max = len(mol.types)
	'''
	# Loop through molecules to make features
	for mol in mols:
		# Get representations from qml function
		reps = qml.representations.generate_atomic_coulomb_matrix(mol.types, mol.xyz, size = max, central_cutoff = cutoff)
		# If chemical shift target
		if len(target) == 1:
			for i in range(len(mol.types)):
				if mol.types[i] == int(target[0]):
					x.append([reps[i]])
					y.append(mol.shift[i])
					r.append([mol.molid, i])
		# If coupling target
		if len(target) == 3:
			for i in range(len(mol.types)):
				for j in range(len(mol.types)):
					if i == j:
						continue

					if not ( mol.types[i] == target[1] and mol.types[j] == target[2] ):
						continue

					if mol.coupling_len[i][j] != target[0]:
						continue

					if i > j:
						x.append([reps[j], reps[i]])
						y.append(mol.coupling[i][j])
						r.append([mol.molid, j, i])
					else:
						x.append([reps[i], reps[j]])
						y.append(mol.coupling[i][j])
						r.append([mol.molid, i, j])

	return x, y, r

# Get ACSF features
def get_ACSF_features(mols, targetflag='CCS', cutoff=5.0, max=400, elements=[], nRs2=3, nRs3=3, nTs=3, eta2=1,
									eta3=1, zeta=1, acut=5, bin_min=0.8):
	# Input:
	#	mols: list of autoENRICH nmrmol objects
	#	targetflag: flag corresponding to nmr parameter (string)
	#	cutoff: distance cutoff for representation
	#	max: maximum size of molecules
	#	elements: list of possible atom types
	# 	various feature parameters

	# Returns:
	#	x: 1D list of features (each item in list is a numpy array)
	#	y: 1D list of NMR parameters
	#	r: 1D list of NMR parameter references (molid, atom(1, atom2))

	# Convert flag to target
	target = flag_to_target(targetflag)

	x = []
	y = []
	r = []
	# Adjust max size if needed
	for tmp_mol in mols:
		if len(tmp_mol.types) > max:
			max = len(tmp_mol.types)
	# loop through mols to make features
	for mol in mols:
		# Get representations from qml function
		reps = qml.representations.generate_acsf(mol.types, mol.xyz, elements=[1, 6, 7, 8, 9, 14, 15, 16, 17, 35],
												nRs2=int(nRs2), nRs3=int(nRs3),
												nTs=int(nTs), eta2=eta2, eta3=eta3, zeta=zeta, rcut=cutoff, acut=acut,
												bin_min=0.0, gradients=False)
												#pad=1010)
		# If chemical shift target
		if len(target) == 1:
			for i in range(len(mol.types)):
				if mol.types[i] == target[0]:
					x.append([reps[i]])
					y.append(mol.shift[i])
					r.append([mol.molid, i])
		# If coupling target
		if len(target) == 3:
			for i in range(len(mol.types)):
				for j in range(len(mol.types)):
					if i == j:
						continue
					if not ( mol.types[i] == target[1] and mol.types[j] == target[2] ):
						continue

					if mol.coupling_len[i][j] != target[0]:
						continue

					if i > j:
						x.append([reps[j], reps[i]])
						y.append(mol.coupling[i][j])
						r.append([mol.molid, j, i])
					else:
						x.append([reps[i], reps[j]])
						y.append(mol.coupling[i][j])
						r.append([mol.molid, i, j])

	return x, y, r
