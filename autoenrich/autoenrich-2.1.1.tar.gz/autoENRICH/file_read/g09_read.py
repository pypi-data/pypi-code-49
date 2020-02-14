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

# Get status of gaussian optimisation file
def get_opt_status(file):
	# Input:
	#	file: filename

	# Returns: status (string), successful, failed, or not submitted

	status = 'unknown'
	try:
		# Read through file looking for SUCCESS or ERROR
		with open(filename, 'r') as f:
			for line in f:
				if 'SUCCESS' in line:
					status = 'successful'
				if 'ERROR' in line:
					status = 'failed'
	except:
		status = 'not submitted'

	return status

# Get status of gaussian nmr file
def get_nmr_status(file):
		# Input:
		#	file: filename

		# Returns: status (string), successful, failed, or not submitted
	status = 'unknown'
	with open(filename, 'r') as f:
		# Read through file looking for SUCCESS or ERROR
		for line in f:
			if 'SUCCESS' in line:
				status = 'successful'
			if 'ERROR' in line:
				status = 'failed'
	return status

# Get energy from optimisation file
def read_opt(file):
	# Input:
	#	file: filename

	# Returns: energy

	# NEEDS TO BE WRITTEN

	return energy

# Get functional and basis set from gaussian log file
def read_functional(file):
	# Input:
	# file: filename

	# Returns: functional, basisset

	functional = ''
	basisset = ''
	with open(file, 'r') as f:
		for line in f:
			# assumes nmrcommand of format:
			# #T nmr(stuff)functional/basisset stuff...
			if '#T nmr' in line:
				try:
					items = line.split()
					nmrcommand = items[2]
					functional = nmrcommand.split('/')[0]
					basisset = nmrcommand.split('/')[1]

					break
				except Exception as e:
					print(line, items)
					print(e)

	return functional, basisset

# Get NMR parameters from gaussian log file
def read_nmr(file, atomnumber):
	# Input:
	#	file: filename
	#	atomnumber: number of atoms in molecule

	# Returns: shift_array (1D numpy array), couplings (2D numpy array)

	# Define empty array for shifts
	shift_array = np.zeros(atomnumber, dtype=np.float64)
	switch = False
	# Go through file to find magnetic shielding tensors
	with open(file, 'r') as f_handle:
		for line in f_handle:
			# If tensor label is found, activate switch
			if "SCF GIAO Magnetic shielding tensor (ppm)" in line:
				switch = True
			# This label comes at the end of the tensor section, so deactivate switch
			if "Fermi Contact" in line:
				switch = False

			if switch:
				# Find isotropic tensor lines
				if "Isotropic" in line:
					items = line.split()
					try:
						num = int(items[0])
					except:
						continue
					# Isotropic shielding tensor is the 5th item (0, 1, 2, 3, '4')
					shift_array[num-1] = float(items[4])

	# Define empty array for couplings
	couplings = np.zeros((atomnumber, atomnumber), dtype=float)
	# Go through file to find coupling constants
	with open(file, 'r') as f:
		switch = False
		for line in f:
			# If coupling label is found, activate switch
			if "Total nuclear spin-spin coupling J (Hz):" in line:
				switch = True
				continue
			# This label comes at the end of the coupling section, so deactivate switch
			elif "End of Minotr" in line:
				switch = False
				continue

			if switch:
				# All coupling lines contain "D", all index lines do not
				if "D" not in line:
					# Get indices for this section
					tokens = line.split()
					i_indices = np.asarray(tokens, dtype=int)
				else:
					# Assign couplings (array is diagonalised in log file, so this is fiddly)
					tokens = line.split()
					index_j = int(tokens[0]) - 1
					for i in range(len(tokens)-1):
						index_i = i_indices[i] - 1
						coupling = float(tokens[i+1].replace("D","E"))
						couplings[index_i][index_j] = coupling
						couplings[index_j][index_i] = coupling

	return shift_array, couplings
