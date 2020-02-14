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
import copy

from autoENRICH.ml.models.model import genericmodel
from sklearn.model_selection import KFold
import sys

try:
	import tensorflow as tf
	from keras.models import Sequential
	from keras.layers import Dense, Activation, Flatten
	from keras.optimizers import RMSprop
	from keras.callbacks import EarlyStopping
except:
	print('Tensorflow not available')


class NNmodel(genericmodel):
	def __init__(self, id='NNmodel', x=[], y=[], params={}, model_args={}):
		genericmodel.__init__(self, id, x, y, params, model_args)

	def train(self):
		self.net = Sequential()

		self.net.add(Dense(int(self.params['hidden_neurons']), input_shape=self.train_x[0].shape, kernel_initializer='random_uniform'))
		self.net.add(Activation('relu'))

		if self.params['hidden_layers'] > 1:
			for layer in range(int(self.params['hidden_layers'])-1):
				self.net.add(Dense(int(self.params['hidden_neurons']), input_shape=self.train_x[0].shape, kernel_initializer='random_uniform'))
				self.net.add(Activation('relu'))
		self.net.add(Flatten())

		self.net.add(Dense(1, input_dim=int(self.params['hidden_neurons']), kernel_initializer='random_uniform'))
		optzer = RMSprop(lr=10**self.params['learning_rate'], rho=0.9)
		self.net.compile(optimizer=optzer, loss='mse')

		es = EarlyStopping(monitor='loss', mode='min', verbose=1)

		self.net.fit(self.train_x, self.train_y, epochs=int(self.params['nn_epochs']), batch_size=int(self.params['batch_size']), verbose=1, callbacks=[es])
		self.trained = True

	def predict(self, test_x):

		print(self.train_x.shape, test_x.shape)
		pred_y = self.net.predict(test_x, batch_size=None)

		return pred_y

	def cv_predict(self, fold):
		kf = KFold(n_splits=fold)
		kf.get_n_splits(self.train_x)
		pred_y = []

		for train_index, test_index in kf.split(self.train_x):

			tmp_train_x = np.asarray(self.train_x[train_index])
			tmp_train_y = self.train_y[train_index]
			tmp_test_x = np.asarray(self.train_x[test_index])
			tmp_test_y = self.train_y[test_index]

			tmp_model = copy.deepcopy(self)
			tmp_model.train_x = tmp_train_x
			tmp_model.train_y = tmp_train_y

			tmp_model.train()

			pred_y.extend(tmp_model.predict(tmp_test_x))

		pred_y = np.asarray(pred_y)

		return pred_y















###
