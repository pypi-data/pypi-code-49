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

# make batch / submission scripts for HPC jobs

# Get number of max file chunks to produce job submission scripts for
def get_chunks(files, end=-1, start=-1, max=50):
	# Input:
	# files: number of calculation files
	# end: end file number (-1 reverts to last file)
	# start: start file number (-1 reverts to first file)
	# max: max number of files per submission batch

	# Returns: number of submission scripts required

	# "-1" used as flags to mean use all files
	if start < 0 and end < 0:
		start = 1

		if files > max:
			# Get chunks as remainder
			chunks = files / max
			# Check if any remaining
			if files % max > 0:
				# If so, add additional chunk
				chunks = int(chunks) + 1
		else:
			# Always need at least one chunk
			chunks = 1
			end = files
	# If start andor end are specified
	else:
		# Allow for only one of start/end to be specified
		if start == -1:
			start = 1
		if end == -1:
			end = files
		# If more than 1 chunk needed
		if end - start >= max:
			# Get chunks as remainder
			chunks = files / max
			# Check if any remaining
			if files % max > 0:
				# If so, add additional chunk
				chunks = int(chunks) + 1
		else:
			chunks = 1

	# Ensure chunks is an integer (with division it gets cast as float)
	chunks = int(chunks)

	return chunks

# Make generic part of file for use on HPC
def make_HPC_header(jobname='auto-ENRICH', system='PBS', nodes=1, ppn=1, walltime="100:00:00", mem=3):
	# Input:
	# jobname: name for job on HPC system
	# system: type of system
	# nodes: number of nodes to run on
	# ppn: number of processors per node to run on
	# walltime: time to run for
	# mem: memory to request (in GB)

	# Returns: strings containing lines for file

	strings = []

	# NEED BC4 AND GPU VERSION

	if system == 'PBS':
		strings.append('# submission script for PBS')
		strings.append("#PBS -l nodes={0:<1d}:ppn={1:<1d}".format(nodes, ppn))
		strings.append("#PBS -l walltime={0:<9s}".format(walltime))
		strings.append("#PBS -l mem={0:<1d}GB".format(mem))
		strings.append("#PBD -N {0:<10s}".format(jobname))
		strings.append("cd $PBS_O_WORKDIR")
	elif system == 'slurm':
		# sbatch version
		strings.append('# submission script for slurm')
	elif system == 'localbox':
		strings.append('# submission script for local linux box')

	return strings

def make_HPC_orca_batch_submission(prefs, molname, in_array, start, end, jobname='auto-ENRICH', nodes=1, ppn=1, mem=3, walltime="100:00:00"):
	# Input:
	#	prefs: preferences dictionary
	# 	molname: name of molecule
	#	in_array: file containing names of conformer input files
	#	start: conformer id to start at
	#	end: conformer id to end at
	#	jobname: name for job on cluster
	#	nodes: number of nodes to request
	#	ppn: number of processors per node to run on
	#	mem: memory to request (in GB)
	#	walltime: time to run for

	# Returns: strings containing lines for file

	strings = []
	strings.append('#!/bin/bash')
	if prefs['comp']['system'] == 'PBS':
		strings.append("#PBS -l nodes={0:<1d}:ppn={1:<1d}".format(nodes, ppn))
		strings.append("#PBS -l walltime={0:<9s}".format(walltime))
		strings.append("#PBS -l mem={0:<1d}GB".format(mem))
		if prefs['comp']['parallel']:
			strings.append("#PBS -N {0:>1s}".format(jobname))
			strings.append("#PBS -t {0:>1d}-{1:<1d}".format(start, end))
			strings.append("cd $PBS_O_WORKDIR")
			strings.append("NMRNAME=$(gawk -v y=${{PBS_ARRAYID}} 'NR == y' {0:<5s})".format(in_array))
			strings.append("OUTNAME=$( echo $NMRNAME | sed 's/\.in/\.log/')")
			strings.append("orca ${NMRNAME} > ${OUTNAME}")
		else:
			strings.append("cd $PBS_O_WORKDIR")
			strings.append("for i in $(seq {0:>1d} 1 {1:<1d});".format(start, end))
			strings.append("do")
			strings.append("  NMRNAME=$(gawk -v y=${i} 'NR == y' {0:<5s})".format(in_array))
			strings.append("  base=${NMRNAME::${#NMRNAME}-4}")
			strings.append("  FILE=${base}.log")
			strings.append("OUTNAME=$( echo $NMRNAME | sed 's/.in/.log/')")
			strings.append("  if test -f '$FILE'; then")
			strings.append("    continue")
			strings.append("  else")
			strings.append("    orca ${NMRNAME} > ${OUTNAME}")
			strings.append("  fi")
			strings.append("done")

	elif prefs['comp']['system'] =='BC4':
		print('not done yet . . .')
	elif prefs['comp']['system'] == 'localbox':
		strings.append("NUMBERS=$(seq {0:>1d} {1:<1d})".format(start, end))
		strings.append("for NUM in ${NUMBERS}; do")
		strings.append("  NMRNAME=$(head -n${{NUM}}" + " {0:<5s} | tail -1)".format(in_array))
		strings.append("  OUTNAME=$( echo $NMRNAME | sed 's/.in/.log/')")
		strings.append("  orca ${NMRNAME} > ${OUTNAME}")
		strings.append("done")

	return strings
