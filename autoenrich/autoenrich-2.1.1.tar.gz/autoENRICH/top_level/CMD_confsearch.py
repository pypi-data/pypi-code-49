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

from autoENRICH.file_creation.structure_formats import xyz
from autoENRICH.file_creation import confsearch
from autoENRICH.file_creation import HPC_submission as HPCsub
import pybel as pyb

def conformational_search(molecule, prefs, pickle_file, path=''):
	# Read relevant preferences
	iterations = prefs['conf_search']['iterations']
	maxconfs = prefs['conf_search']['maxconfs']
	RMSthresh = prefs['conf_search']['RMSthresh']
	Ethresh = prefs['conf_search']['Ethresh']

	system = prefs['comp']['system']
	python_env = prefs['comp']['python_env']
	aE_dir = prefs['comp']['aE_directory']
	memory = prefs['conf_search']['memory']
	processors = prefs['conf_search']['processors']
	walltime = prefs['conf_search']['walltime']

	# Try reading pybel mol object from xyz named according to molname
	try:
		file = path + molecule.molid + '.xyz'
		mol = next(pyb.readfile('xyz', file))
	# If not, make a molecule xyz file and then read the pybel mol object
	except:
		file = path + molecule.molid + '_INIT.xyz'
		xyz.nmrmol_to_xyz(molecule, file, num=-404)
		mol = next(pyb.readfile('xyz', file))

	smiles = mol.write("smi").split()[0]

	scriptname = 'conf_search/do_confsearch.py'
	confsearch.make_confsearch_script(scriptname, pickle_file, molecule, smiles,
									iterations=iterations, RMSthresh=RMSthresh,
									maxconfs=maxconfs, Ethresh=Ethresh, path=path)

	jobname = 'aE_' + molecule.molid + '_confsearch'
	strings = HPCsub.make_HPC_header(jobname=jobname, system=system, nodes=1, ppn=processors, walltime=walltime, mem=memory)
	strings.append('source activate {env:<10s}'.format(env=python_env))
	strings.append('python {0:<10s}'.format(scriptname))

	if prefs['comp']['system'] == 'BC3':
		filename = path + 'confsearch_' + molecule.molid + '_' + '.qsub'
	elif prefs['comp']['system'] == 'BC4':
		filename = path + 'confsearch_' + molecule.molid + '_' + '.slurm'
	elif prefs['comp']['system'] == 'localbox':
		filename = path + 'confsearch_'+ molecule.molid + '_' + '.sh'

	with open(filename, 'w') as f:
		for string in strings:
			print(string, file=f)

	print('Conformational search script + submission file produced')












###
