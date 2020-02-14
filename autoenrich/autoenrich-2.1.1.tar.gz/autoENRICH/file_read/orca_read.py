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

# Get status of ORCA optimisation
def get_opt_status(file):
	# Input:
	#	file: filename

	# Returns: status

	status = 'unknown'
	try:
		with open(file, 'r') as f:
			for line in f:
				if 'SUCCESS' in line:
					status = 'successful'
				if 'ERROR' in line:
					status = 'failed'
	except Exception as e:
		status = 'not submitted'

	return status

# Get status of ORCA NMR calculation
def get_nmr_status(file):
		# Input:
		#	file: filename

		# Returns: status
	status = 'unknown'
	with open(file, 'r') as f:
		for line in f:
			if 'SUCCESS' in line:
				status = 'successful'
			if 'ERROR' in line:
				status = 'failed'
	return status

# Read Optimisation energy from ORCA optimisation file
def read_opt(file):
	# Input:
	#	file: filename
	# Returns: energy

	# Go through file looking for this line
	# SCF Energy:    -1072.8219232141
	energy = 0.0
	with open(file ,'r') as f:
		for line in f:
			if 'SCF Energy:' in line:
				items=line.split()
				energy = float(items[-1])

	return energy

# Need to write this
def read_nmr(file):



	return shift, coupling
