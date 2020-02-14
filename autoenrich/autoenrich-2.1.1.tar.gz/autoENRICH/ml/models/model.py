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


import qml

import numpy as np
import copy
from qml.math import cho_solve
from qml.kernels import laplacian_kernel
from sklearn.model_selection import KFold

import tracemalloc
# top level model class

class genericmodel(object):

	def __init__(self, id='genericmodel', train_x=[], train_y=[], params={},
									model_args={}):

		self.train_x = train_x
		self.train_y = train_y

		self.params = params
		self.args = model_args

		self.trained = False


	def train(self):
		print('Stub function, why are you running this ??')

	def predict(self):
		print('Stub function, why are you running this ??')


	def cv_predict(self, fold):
		kf = KFold(n_splits=fold)
		kf.get_n_splits(self.train_x)
		pred_y = []

		for train_index, test_index in kf.split(self.train_x):

			self.train(train_x=self.train_x[train_index], train_y=self.train_y[train_index])

			pred_y.extend(self.predict(self.train_x[test_index], train_x=self.train_x[train_index]))

		pred_y = np.asarray(pred_y)

		return pred_y


























##
