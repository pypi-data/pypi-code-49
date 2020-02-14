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
from autoENRICH.ml.models.model import genericmodel
from sklearn.model_selection import KFold
import qml
import copy

class FCHLmodel(genericmodel):

	def __init__(self, id='FCHLmodel', x=[], y=[], params={}, model_args={}):
		genericmodel.__init__(self, id, x, y, params, model_args)

		if not 'cutoff' in self.params:
			self.params['cutoff'] = 5.0

		if not 'two_body_scaling' in self.params:
			self.params['two_body_scaling'] = np.sqrt(8)
		if not 'three_body_scaling' in self.params:
			self.params['three_body_scaling'] = 1.6
		if not 'two_body_width' in self.params:
			self.params['two_body_width'] = 0.2
		if not 'three_body_width' in self.params:
			self.params['three_body_width'] = np.pi
		if not 'two_body_power' in self.params:
			self.params['two_body_power'] = 4.0
		if not 'three_body_power' in self.params:
			self.params['three_body_power'] = 2.0
		if not 'cut_start' in self.params:
			self.params['cut_start'] = 1.0
		if not 'alchemy_period_width' in self.params:
			self.params['alchemy_period_width'] = 1.6
		if not 'alchemy_group_width' in self.params:
			self.params['alchemy_group_width'] =1.6


	def train(self,  train_x=[], train_y=[]):
		k = []

		if len(train_x) == 0:
			train_x = self.train_x
		if len(train_y) == 0:
			train_y = self.train_y

		try:
			dimensions = train_x.shape[1]
		except:
			print('training reps not in numpy array (KRRmodel.py, train, l26)')
			train_x = np.asarray(train_x)
			train_y = np.asarray(train_y)

		# reshape x array:
		Xr = []
		for _ in range(dimensions):
			Xr.append([])
		for x in train_x:
			for i in range(dimensions):
				Xr[i].append(x[i])
		Xr = np.asarray(Xr)

		# loop through representation sets in training set
		for d in range(dimensions):
			# append kernel for each representation set
			k.append(qml.fchl.get_atomic_symmetric_kernels(Xr[d], verbose=False,
					two_body_scaling=self.params['two_body_scaling'], three_body_scaling=self.params['three_body_scaling'],
					two_body_width=self.params['two_body_width'], three_body_width=self.params['three_body_width'],
					two_body_power=self.params['two_body_power'], three_body_power=self.params['three_body_power'],
					cut_start=self.params['cut_start'], cut_distance=self.params['cutoff'],
					fourier_order=1, alchemy="periodic-table",
					alchemy_period_width=self.params['alchemy_period_width'], alchemy_group_width=self.params['alchemy_group_width'],
					kernel="gaussian", kernel_args={'sigma':[self.params['sigma']]})[0] + self.params['lamda'] * np.identity(Xr[d].shape[0]))

		# loop through kernels
		K = k[0]
		if len(k) > 1:
			for i in range(1, len(k)):
				# multiply kernels so result is k1 * k2 * k3 ...
				K = K * k[i]

		# get the KRR prefactors, i.e. this is the training of the model
		self.alpha = qml.math.cho_solve(K, train_y)

		# report training state
		self.trained = True


	def predict(self, test_x, train_x=[]):
		ks = []

		if len(train_x) == 0:
			train_x = self.train_x

		assert np.asarray(test_x).shape[1] == np.asarray(train_x).shape[1]

		dimensions = np.asarray(train_x).shape[1]

		# reshape x arrays:
		Xe = []
		Xr = []
		for _ in range(dimensions):
			Xe.append([])
			Xr.append([])
		for x in test_x:
			for i in range(dimensions):
				Xe[i].append(x[i])
		for x in train_x:
			for i in range(dimensions):
				Xr[i].append(x[i])
		Xe = np.asarray(Xe)
		Xr = np.asarray(Xr)

		# loop through representation sets in training set
		for d in range(dimensions):
			# append kernel for each representation set
			ks.append(qml.fchl.get_atomic_kernels(Xe[d], Xr[d], verbose=False,
					two_body_scaling=self.params['two_body_scaling'], three_body_scaling=self.params['three_body_scaling'],
					two_body_width=self.params['two_body_width'], three_body_width=self.params['three_body_width'],
					two_body_power=self.params['two_body_power'], three_body_power=self.params['three_body_power'],
					cut_start=self.params['cut_start'], cut_distance=self.params['cutoff'],
					fourier_order=1, alchemy="periodic-table",
					alchemy_period_width=self.params['alchemy_period_width'], alchemy_group_width=self.params['alchemy_group_width'],
					kernel="gaussian", kernel_args={'sigma':[self.params['sigma']]})[0])


		# loop through kernels
		Ks = ks[0]
		if len(ks) > 1:
			for i in range(1, len(ks)):
				# multiply kernels so result is k1 * k2 * k3 ...
				Ks = Ks * ks[i]
		Ks = np.asarray(Ks)

		# predict values of y
		y_pred = np.dot(Ks, self.alpha)

		return y_pred




















##
