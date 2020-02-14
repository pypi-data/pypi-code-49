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

import json
import sys


def read_prefs(file):
	try:
		with open(file, 'r') as json_file:
			prefs = json.load(json_file)
	except Exception as E:
		print('Error reading preferences file ', file)
		print(E)
		print('Exiting. . .')
		sys.exit(0)


	return prefs

def write_default_prefs(file):

	prefs = {}
	prefs['conf_search'] = {}
	prefs['conf_search']['iterations'] = 200
	prefs['conf_search']['maxconfs'] = 100
	prefs['conf_search']['RMSthresh'] = 0.1
	prefs['conf_search']['Ethresh'] = 100000

	prefs['mol'] = {}
	prefs['mol']['charge'] = 0
	prefs['mol']['multiplicity'] = 1

	prefs['comp'] = {}
	prefs['comp']['parallel'] = True
	prefs['comp']['system'] = 'BC3'
	prefs['comp']['python_env'] = 'env_IMP'
	prefs['comp']['aE_directory'] = "../../aE/"

	prefs['optimisation'] = {}
	prefs['optimisation']['memory'] = 12
	prefs['optimisation']['processors'] = 4
	prefs['optimisation']['opt'] = 'tight'
	prefs['optimisation']['freq'] = False
	prefs['optimisation']['functional'] = 'mPW1PW'
	prefs['optimisation']['basisset'] = '6-311g(d,p)'
	prefs['optimisation']['solvent'] = 'none'
	prefs['optimisation']['grid'] = 'ultrafine'
	prefs['optimisation']['custom_cmd_line'] = False
	prefs['optimisation']['nodes'] = 1
	prefs['optimisation']['walltime'] = '100:00:00'

	prefs['NMR'] = {}
	prefs['NMR']['memory'] = 12
	prefs['NMR']['processors'] = 4
	prefs['NMR']['functional'] = 'wB97X-D3'
	prefs['NMR']['basisset'] = '6-311g(d,p)'
	prefs['NMR']['aux_basis_set'] = 'def2/JK'
	prefs['NMR']['solvent'] = 'none'
	prefs['NMR']['custom_cmd_line'] = False
	prefs['NMR']['nodes'] = 1
	prefs['NMR']['walltime'] = '100:00:00'
	prefs['NMR']['shift_nuclei'] = ['H', 'C', 'N', 'O', 'F']
	prefs['NMR']['spin_nuclei'] = ['H', 'C']
	prefs['NMR']['spin_thresh'] = 20.0

	json.dump(prefs, open(file, 'w'), indent=4)
