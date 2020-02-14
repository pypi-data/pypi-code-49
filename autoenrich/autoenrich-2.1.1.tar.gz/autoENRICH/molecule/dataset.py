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


from .nmrmol import nmrmol
from autoENRICH.util.file_gettype import get_type
import numpy as np
np.set_printoptions(threshold=99999999999)

class dataset(object):

	def __init__(self):

		self.mols = []
		self.x = []
		self.y = []
		self.r = []
		self.mol_order = []

		self.params = {}


	def get_mols(self, files, type='', label_part=0):
		self.mols = []
		for file in files:
			id = file.split('/')[-1].split('.')[0].split('_')[label_part]
			mol = nmrmol(molid=id)

			if type == '':
				ftype = get_type(file)
			else:
				ftype = type

			mol.read_nmr(file, ftype)
			self.mols.append(mol)
			#print(id)
			#print(mol.coupling_len)


	def get_features_frommols(self, args, params={}):

		featureflag = args['featureflag']
		targetflag = args['targetflag']
		try:
			max = args['max_size']
		except:
			max = 200

		if 'cutoff' in params:
			if params['cutoff'] < 0.1:
				params['cutoff'] = 0.1
		else:
			params['cutoff'] = 5.0


		x = []
		y = []
		r = []

		self.params = params

		if featureflag in ['aSLATM', 'CMAT', 'FCHL', 'ACSF']:
			from autoENRICH.ml.features import QML_features
		elif featureflag in ['BCAI']:
			from autoENRICH.ml.features import TFM_features
		elif featureflag in ['dummy']:
			from autoENRICH.ml.features import GNR_features

		if featureflag == 'dummy':
			for mol in self.mols:
				_x, _y, _r = GNR_features.get_dummy_features([mol], targetflag)
				x.extend(_x)
				y.extend(_y)
				r.extend(_r)


		elif featureflag == 'aSLATM':
			mbtypes = QML_features.get_aSLATM_mbtypes(self.mols)
			for mol in self.mols:
				_x, _y, _r = QML_features.get_aSLATM_features([mol], targetflag, params['cutoff'], max=max, mbtypes=mbtypes)
				x.extend(_x)
				y.extend(_y)
				r.extend(_r)


		elif featureflag == 'CMAT':

			# Set (not found) parameters to defaults
			if not 'central_decay' in params:
				params['central_decay'] = -1
			if not 'interaction_cutoff' in params:
				params['interaction_cutoff'] = 1000000.0
			if not 'interaction_decay' in params:
				params['interaction_decay'] = -1

			for mol in self.mols:
				if len(mol.types) >max:
					args['max_size'] = len(mol.types)
					print('WARNING, SETTING MAXIMUM MOLECULE SIZE TO, ', max)
			for mol in self.mols:
				_x, _y, _r = QML_features.get_CMAT_features([mol], targetflag, params['cutoff'], args['max_size'], central_decay=params['central_decay'],
														interaction_cutoff=params['interaction_cutoff'], interaction_decay=params['interaction_decay'])
				x.extend(_x)
				y.extend(_y)
				r.extend(_r)


		elif featureflag == 'FCHL':
			for mol in self.mols:
				if len(mol.types) >max:
					max = len(mol.types)
					print('WARNING, SETTING MAXIMUM MOLECULE SIZE TO, ', max)

				'''
				for mol in self.mols:
				_x, _y, _r = QML_features.get_FCHL_features([mol], targetflag, params['cutoff'], max)
				x.extend(_x)
				y.extend(_y)
				r.extend(_r)
				'''
			x, y, r = QML_features.get_FCHL_features(self.mols, targetflag, params['cutoff'], max)


		elif featureflag == 'ACSF':
			elements = set()
			for tmp_mol in self.mols:
				elements = elements.union(tmp_mol.types)
			elements = sorted(list(elements))

			# Set (not found) parameters to defaults


			for mol in self.mols:
				_x, _y, _r = QML_features.get_ACSF_features([mol], targetflag, params['cutoff'], elements=elements, nRs2=params['nRs2'],
												nRs3=params['nRs3'], nTs=params['nTs'], eta2=params['eta2'], eta3=params['eta3'], zeta=params['zeta'],
												acut=params['acut'], bin_min=params['bin_min'])
				x.extend(_x)
				y.extend(_y)
				r.extend(_r)

		elif featureflag == 'BCAI':
			x, y, r, mol_order = TFM_features.get_BCAI_features(self.mols, targetflag)

		else:
			print('Feature flag not recognised, no feature flag: ', featureflag)

		if featureflag == 'BCAI':
			self.x = x
			self.y = y
			self.r = r
			self.mol_order = mol_order
		else:
			self.x = np.asarray(x)
			self.y = np.asarray(y)
			self.r = r

		if featureflag not in ['dummy', 'BCAI']:
			print('Reps generated, shape: ', self.x.shape)

	def get_features_fromfiles(self, files, featureflag='CMAT', targetflag='CCS', cutoff=5.0, max=400, mbtypes=[], elements=[]):
		self.params = {}

		x = []
		y = []
		r = []

		if featureflag == 'aSLATM':
			mbtypes = QML_features.get_aSLATM_mbtypes([])
			for file in files:
				id = file.split('.')[0].split('_')[-1]
				mol = nmrmol(id)
				mol.read_nmr(file, 'nmredata')
				_x, _y, _r = QML_features.get_aSLATM_features(mol, targetflag, cutoff, mbtypes)
				x.extend(_x)
				y.extend(_y)
				r.extend(_r)


		elif featureflag == 'CMAT':
			for file in files:
				id = file.split('.')[0].split('_')[-1]
				mol = nmrmol(id)
				mol.read_nmr(file, 'nmredata')
				_x, _y, _r = QML_features.get_CMAT_features(mol, targetflag, cutoff, max)
				x.extend(_x)
				y.extend(_y)
				r.extend(_r)


		elif featureflag == 'FCHL':
			for file in files:
				id = file.split('.')[0].split('_')[-1]
				mol = nmrmol(id)
				mol.read_nmr(file, 'nmredata')
				_x, _y, _r = QML_features.get_FCHL_features(mol, targetflag, cutoff, max)
				x.extend(_x)
				y.extend(_y)
				r.extend(_r)


		elif featureflag == 'ACSF':
			for file in files:
				id = file.split('.')[0].split('_')[-1]
				mol = nmrmol(id)
				mol.read_nmr(file, 'nmredata')
				_x, _y, _r = QML_features.get_ACSF_features(mol, targetflag, cutoff, elements)
				x.extend(_x)
				y.extend(_y)
				r.extend(_r)

		elif featureflag == 'BCAI':
			for file in files:
				id = file.split('.')[0].split('_')[-1]
				mol = nmrmol(id)
				mol.read_nmr(file, 'nmredata')
				_x, _y, _r = TFM_features.get_BCAI_features(mol, targetflag, cutoff)
				x.extend(_x)
				y.extend(_y)
				r.extend(_r)

		self.x = np.asarray(x)
		self.y = np.asarray(y)
		self.r = r


	def assign_from_ml(self, pred_y, var, zero=True):
		assert len(self.r) > 0, print('Something went wrong, nothing to assign')

		for mol in self.mols:
			if zero:
				mol.coupling = np.zeros((len(mol.types), len(mol.types)), dtype=np.float64)
				mol.shift = np.zeros((len(mol.types)), dtype=np.float64)

			for r, ref in enumerate(self.r):

				if mol.molid != ref[0]:
					continue

				if len(ref) == 2:
					for t in range(len(mol.types)):
						if ref[1] == t:
							mol.shift[t] = pred_y[r]
							mol.shift_var[t] = var[r]

				elif len(ref) == 3:
					for t1 in range(len(mol.types)):
						for t2 in range(len(mol.types)):
							if ref[1] == t1 and ref[2] == t2:
								mol.coupling[t1][t2] = pred_y[r]
								mol.coupling_var[t1][t2] = var[r]











##
