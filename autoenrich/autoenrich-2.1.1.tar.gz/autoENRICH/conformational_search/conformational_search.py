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

import sys
from rdkit import Chem
from rdkit.Chem import AllChem
import pybel as pyb
import numpy as np

# raw mass generation of xyz coordinates based on torsional angle searching
def torsional_search(smiles, iterations=100000, RMSthresh=1):
	# Input:
	# smiles: smiles string representing the molecule (string)
	# iterations: number of ETRKG iterations (integer)
	# RMSthresh: RMS threshold for ETRKG search (how different new conformers need to be) (float)

	# Returns: xyzs (list (conformers) of lists (atoms) of xyz coordinates), energies (list of conformer MMFF94s energies)

	xyzs = []
	energies = []
	# read mol into RDkit from smiles string
	rdmol = Chem.MolFromSmiles(smiles)
	# rdkit is an absolute piece of c**p, so it wont read in hydrogens, it has to add them itself
	rdmol = Chem.AddHs(rdmol)
	# Do conformational search by ETRKG
	# Riniker, S.; Landrum, G. A. “Better Informed Distance Geometry: Using What We Know To Improve Conformation Generation” J. Chem. Inf. Comp. Sci. 55:2562-74 (2015)
	ids = AllChem.EmbedMultipleConfs(rdmol,
								  clearConfs=True,
								  numConfs=iterations,
								  pruneRmsThresh=RMSthresh)
	# align conformers, not strictly neccesary but should make visualisation more convenient later on
	AllChem.AlignMolConformers(rdmol)
	# Optimise conformers by MMFF, returns success states (ignored atm) and energies
	rd_es = AllChem.MMFFOptimizeMoleculeConfs(rdmol, mmffVariant='MMFF94s')
	# Record energies in list
	for e in rd_es:
		energies.append(e[1])

	# Get list of conformer IDs
	confIds = [x.GetId() for x in rdmol.GetConformers()]
	# Define empty array for lists of coordinates
	xyzs = []
	# Loop through conformers
	for id in confIds:
		xyz = []
		# Loop over length of molecule (defined by size of mol type array)
		for t in range(len(rdmol.getatoms())):
			# append atom coordinates
			xyz.append([float(rdmol.GetConformer(id).GetAtomPosition(t)[0]),
						float(rdmol.GetConformer(id).GetAtomPosition(t)[1]),
						float(rdmol.GetConformer(id).GetAtomPosition(t)[2])])
		xyzs.append(xyz)

	return xyzs, energies


# select conformers based on coverage of the chemical space
def select_conformers(xyzs, energies, maxconfs=100, Ethresh=100000):
	# Input:
	# xyzs: list of lists of xyz coordinates from torsional search (n x m) n=number of conformers, m=number of atoms
	# energies: list of energies (n)
	# maxconfs: maximum number of conformers to return (int)
	# Ethresh: Energy threshold above which conformers will be automatically discarded (float)

	# Returns: xyzs (list (conformers) of lists (atoms) of xyz coordinates), energies (list of conformer MMFF94s energies)

	remove = []
	# Mark for removal all conformers with energy over threshold
	for i in range(len(energies)):
		if energies[i] > Ethresh:
			remove.append(i)
	# Remove marked conformers
	print('Removing', len(remove), 'conformers because MMFF energy too high')
	for id in sorted(remove, reverse=True):
		del energies[remove]
		del xyzs[remove]

	# If still too many conformers
	if len(xyzs) > maxconfs:
		# Run geomtry based conformer removal
		remove = select_over_space(xyzs, to_remove=len(xyzs)-maxconfs)
		# Remove marked conformers selected by geometric similarity
		print('Removing', len(remove), 'conformers due to similarity to other conformers')
		for id in sorted(remove, reverse=True):
			del energies[id]
			del xyzs[id]
	# Return xyz coords and energies of selected conformers
	return xyzs, energies

# xyz based selection of most similar structures
def select_over_space(xyzs, to_remove):
	#Input:
	# xyzs: list of lists of xyz coordinates from torsional search (n x m) n=number of conformers, m=number of atoms
	# to_remove: number of conformers to be removed

	# Returns: list of conformer ids to remove

	dist = np.zeros((len(xyzs),len(xyzs)), dtype=np.float64)
	remove = []
	# loop over all conformer/conformer pairs
	for aa, a in enumerate(xyzs):
		for bb, b in enumerate(xyzs):
			if aa == bb:
				continue
			# Get distance between conformers geometrically
			# Technically this is a thing called the frobeius distance/norm
			dist[aa][bb] = np.linalg.norm(np.asarray(a)-np.asarray(b))

	# Keep looping until enough conformers are marked for removal
	while len(remove) < to_remove:
		id = 0
		lowest_dist = 9999999999999999
		# Loop over conformers
		for i in range(dist.shape[0]):
			# Get sum of distances to all other conformers for conformer i
			sumdist = np.sum(dist[i])
			# Store lowest distance and conformer id
			if sumdist <= lowest_dist and i not in remove:
				id = i
				lowest_dist = sumdist
		# add least geometrically different conformer to removal list
		remove.append(id)
	# Return Ids to remove
	return remove









###
