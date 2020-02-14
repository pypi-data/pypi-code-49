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

import autoENRICH.file_read.orca_read as orcaread
import autoENRICH.file_creation.orca_submission as orcasub
from autoENRICH.file_creation import HPC_submission as HPCsub

def setup_resubmission(molecule, prefs, path=''):

	for conformer in molecule.conformers:
		optstatus = orcaread.get_opt_status(conformer.opt_log)

		if optstatus != 'successful':
			conformer.opt_in = orcasub.make_optin(prefs, conformer, path + 'optimisation/')
			conformer.opt_log = conformer.optin.split('.')[0] + '.log'
			conformer.opt_status = 'pre-submission'
			opt_files.append(conformer.opt_in)

		nmrstatus = orcaread.get_nmr_status(conformer.nmr_log)
		if conformer.nmr_status != 'successful' and conformer.opt_status == 'successful':
			conformer.nmr_in = orcasub.make_nmrin(prefs, conformer, path + 'nmr/')
			conformer.nmr_log = conformer.nmr_in.split('.') + '.log'
			conformer.nmr_status = 'pre-submission'
			nmr_files.append(conformer.nmr_in)

	for tag, in_files in zip(['OPT', 'NMR'], [opt_files, nmr_files]):

		system = prefs['comp']['system']
		if tag == 'OPT':
			memory = prefs['opt']['memory']
			processors = prefs['opt']['processors']
			walltime = prefs['opt']['walltime']
		if tag == 'NMR':
			memory = prefs['nmr']['memory']
			processors = prefs['nmr']['processors']
			walltime = prefs['nmr']['walltime']

		files = len(in_files)
		chunks = HPCsub.get_chunks(files)
		for ck in range(chunks):
			start = (ck * max) + 1
			end = ((ck + 1) * max)
			if end > files:
				end = files

			jobname = 'aE_' + molecule.molid + '_' + str(ck) + tag +  '_RESUB'
			header = HPCsub.make_HPC_header(jobname=jobname, system=system, nodes=1, ppn=processors, walltime=walltime, mem=memory)

			strings = HPCsub.make_orca_batch_submission(prefs, in_files, start, end, ck)

			if prefs['comp']['system'] == 'BC3':
				filename = path + 'RESUB_' + tag + '_' + molecule.molid + '_' + str(ck) + '.qsub'
			elif prefs['comp']['system'] == 'BC4':
				filename = path + 'RESUB_' + tag + '_' + molecule.molid + '_' + str(ck) + '.slurm'
			elif prefs['comp']['system'] == 'localbox':
				filename = path + 'RESUB_' + tag + '_' + molecule.molid + '_' + str(ck) + '.sh'
			with open(filename, 'w') as f:
				for string in header:
					print(string, file=f)
				for string in strings:
					print(string, file=f)

		print('Created ', len(chunks), ' ',  tag, 'resubmission files. . .')


















###
