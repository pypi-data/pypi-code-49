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

def construct_param_dict(modelflag, featureflag, targetflag):

	params = {}
	param_ranges = {}
	param_logs = {}

	if modelflag == 'KRR':
		param_ranges['sigma'] = [-5, 5]
		param_logs['sigma'] = 'log'

		param_ranges['lamda'] = [-10, 1]
		param_logs['lamda'] = 'log'

	elif modelflag == 'FCHL':
		param_ranges['sigma'] = [-5, 5]
		param_logs['sigma'] = 'log'

		param_ranges['lamda'] = [-10, 1]
		param_logs['lamda'] = 'log'

		param_ranges['two_body_scaling'] = [1, 4]
		param_logs['two_body_scaling'] = 'lin'

		param_ranges['three_body_scaling'] = [1, 4]
		param_logs['three_body_scaling'] = 'lin'

		param_ranges['two_body_width'] = [0, 3]
		param_logs['two_body_width'] = 'lin'

		param_ranges['three_body_width'] = [1, 4]
		param_logs['three_body_width'] = 'lin'

		param_ranges['three_body_power'] = [1, 4]
		param_logs['three_body_power'] = 'lin'

		param_ranges['two_body_power'] = [2, 5]
		param_logs['two_body_power'] = 'lin'

		param_ranges['cut_start'] = [0, 3]
		param_logs['cut_start'] = 'lin'

		param_ranges['alchemy_period_width'] = [1, 4]
		param_logs['alchemy_period_width'] = 'lin'

		param_ranges['alchemy_group_width'] = [1, 4]
		param_logs['alchemy_group_width'] = 'lin'

	elif modelflag == 'NN':
		param_ranges['hidden_neurons'] = [1, 100]
		param_logs['hidden_neurons'] = 'lin'

		param_ranges['hidden_layers'] = [1, 10]
		param_logs['hidden_layers'] = 'lin'

		param_ranges['learning_rate'] = [-5, 2]
		param_logs['learning_rate'] = 'log'

		param_ranges['nn_epochs'] = [1, 100]
		param_logs['nn_epochs'] = 'lin'

		param_ranges['batch_size'] = [1, 100]
		param_logs ['batch_size'] = 'lin'

		pass

	elif modelflag == 'TFM':
		param_ranges['d_model'] = [400, 800]
		param_logs['d_model'] = 'lin'

		param_ranges['n_layer'] = [10, 18]
		param_logs['n_layer'] = 'lin'

		param_ranges['d_inner'] = [3700, 3900]
		param_logs['d_inner'] = 'lin'

		param_ranges['feature_dim'] = [199.9, 200.1]
		param_logs['feature_dim'] = 'lin'

		param_ranges['final_dim'] = [279.9, 280.1]
		param_logs['final_dim'] = 'lin'

		param_ranges['dropout'] = [0.02, 0.04]
		param_logs['dropout'] = 'lin'

		param_ranges['dropatt'] = [0.0, 0.01]
		param_logs['dropatt'] = 'lin'

		param_ranges['final_dropout'] = [0.03, 0.04]
		param_logs['final_dropout'] = 'lin'

		param_ranges['n_head'] = [9, 11]
		param_logs['n_head'] = 'lin'

		param_ranges['eta_min'] = [-6, -7]
		param_logs['eta_min'] = 'log'

		param_ranges['learning_rate'] = [0.0009, 0.0011]
		param_logs['learning_rate'] = 'lin'


	if featureflag == 'CMAT':
		param_ranges['cutoff'] = [1, 10]
		param_logs['cutoff'] = 'lin'

		param_ranges['central_decay'] = [0, 10]
		param_logs['central_decay'] = 'lin'

		param_ranges['interaction_cutoff'] = [0, 10]
		param_logs['interaction_cutoff'] = 'lin'

		param_ranges['interaction_decay'] = [0, 10]
		param_logs['interaction_decay'] = 'lin'


	elif featureflag == 'aSLATM':
		param_ranges['cutoff'] = [1, 10]
		param_logs['cutoff'] = 'lin'

	elif featureflag == 'FCHL':
		param_ranges['cutoff'] = [1, 10]
		param_logs['cutoff'] = 'lin'

	elif featureflag == 'ACSF':
		param_ranges['cutoff'] = [1, 10]
		param_logs['cutoff'] = 'lin'

		param_ranges['nRs2'] = [1, 10]
		param_logs['nRs2'] = 'lin'

		param_ranges['nRs3'] = [1, 10]
		param_logs['nRs3'] = 'lin'

		param_ranges['nTs'] = [1, 10]
		param_logs['nTs'] = 'lin'

		param_ranges['eta2'] = [0, 10]
		param_logs['eta2'] = 'lin'

		param_ranges['eta3'] = [0, 10]
		param_logs['eta3'] = 'lin'

		param_ranges['zeta'] = [0, 10]
		param_logs['zeta'] = 'lin'

		param_ranges['acut'] = [1, 10]
		param_logs['acut'] = 'lin'

		param_ranges['bin_min'] = [0, 10]
		param_logs['bin_min'] = 'lin'

	elif featureflag == 'BCAI':
		param_ranges['cutoff'] = [0, 10]
		param_logs['cutoff'] = 'lin'


	return param_ranges, param_logs






























###
