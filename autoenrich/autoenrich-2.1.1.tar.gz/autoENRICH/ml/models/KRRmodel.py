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
import qml
from sklearn.model_selection import KFold
import copy
import sys

class KRRmodel(genericmodel):

	def __init__(self, id='KRRmodel', x=[], y=[], params={}, model_args={}):
		genericmodel.__init__(self, id, x, y, params, model_args)
		self.alpha = []


	def train(self, train_x=[], train_y=[]):
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
			k.append(qml.kernels.laplacian_kernel(Xr[d], Xr[d], self.params['sigma']) + self.params['lamda'] * np.identity(Xr[d].shape[0]))

		# loop through kernels
		K = k[0]
		if len(k) > 1:
			for i in range(1, len(k)):
				# multiply kernels so result is k1 * k2 * k3 ...
				K = K * k[i]

		# get the KRR prefactors, i.e. this is the training of the network
		self.alpha = qml.math.cho_solve(K, train_y)

		# report training state
		self.trained = True


	def predict(self, test_x, train_x=[]):

		if len(train_x) == 0:
			train_x = self.train_x

		ks = []
		assert test_x.shape[1] == train_x.shape[1]

		dimensions = train_x.shape[1]

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
			ks.append(qml.kernels.laplacian_kernel(Xe[d], Xr[d], self.params['sigma']))

		# loop through kernels
		Ks = ks[0]
		if len(ks) > 1:
			for i in range(1, len(ks)):
				# multiply kernels so result is k1 * k2 * k3 ...
				Ks = Ks * ks[i]

		# predict values of y
		y_pred = np.dot(Ks, self.alpha)

		return y_pred
