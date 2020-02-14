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

def Get_optimal_HP(rep, parameter='HCS', dataset='set3'):
	optimal = {
					'set2_all' :	{'cmat' : {	'HCS' : {'sigma':100, 'lambda':1e-14, 'cutoff':2.0},
												'CCS' : {'sigma':1e+10, 'lambda':1e-8, 'cutoff':3.0},
												'J1CH' : {'sigma':54555.9, 'lambda':0.0001, 'cutoff':3.0}},

									'slatm'	: { 'HCS' : {'sigma':10, 'lambda':1e-8, 'cutoff':5.0},
												'CCS' : {'sigma':10, 'lambda':1e-8, 'cutoff':5.0},
												'J1CH' : {'sigma':10, 'lambda':1e-8, 'cutoff':5.0}},

									'fchl'	: {	'HCS' : {'sigma':10, 'lambda':1e-8, 'cutoff':5.0},
												'CCS' : {'sigma':10, 'lambda':1e-8, 'cutoff':5.0}}},

					'set2_hcno' :	{'cmat' : {	'HCS' : {'sigma':1e+10, 'lambda':1e-8, 'cutoff':3.0},
												'CCS' : {'sigma':1e+10, 'lambda':1e-8, 'cutoff':3.0},
												'J1CH' : {'sigma':2e+09, 'lambda':1e-08, 'cutoff':3.0}},

									'slatm'	: { 'HCS' : {'sigma':177828, 'lambda':1e-8, 'cutoff':7.0},
												'CCS' : {'sigma':177828, 'lambda':1e-8, 'cutoff':7.0},
												'J1CH' : {'sigma':1624, 'lambda':1e-12, 'cutoff':4.0}},

									'fchl'	: {	'HCS' : {'sigma':10, 'lambda':1e-8, 'cutoff':5.0},
												'CCS' : {'sigma':10, 'lambda':1e-8, 'cutoff':5.0}}},

					'set3' :		{'cmat' : {	'HCS' : {'sigma':2.511e+7, 'lambda':1e-6, 'cutoff':3.0}, #0.53
												'CCS' : {'sigma':1e+10, 'lambda':1e-8, 'cutoff':3.0},
												'J1CH' : {'sigma':119356, 'lambda':1.1e-05, 'cutoff':1.82}}, #2.63

									'slatm'	: { 'HCS' : {'sigma':30683.8, 'lambda':3.9e-05, 'cutoff':7.52}, # 0.45
												'CCS' : {'sigma':13.4951, 'lambda':1.8e-16, 'cutoff':6.88}, # 4.04
												'J1CH' : {'sigma':8.503e+06, 'lambda':2.5e-08, 'cutoff':6.49}}, #1.53

									'fchl'	: {	'HCS' : {'sigma':0.431, 'lambda':0.0068, 'cutoff':4.67}, # 0.37
												'CCS' : {'sigma':0.352, 'lambda':0.0023, 'cutoff':7.82}, # 3.87
												'J1CH' : {'sigma':1.414, 'lambda':9.3e-06, 'cutoff':9.93}}},

					'set4' :		{'cmat' : {	'HCS' : {'sigma':2.511e+7, 'lambda':1e-6, 'cutoff':3.0}, #0.53
												'CCS' : {'sigma':1e+10, 'lambda':1e-8, 'cutoff':3.0},
												'J1CH' : {'sigma':1.66, 'lambda':1.5e-10, 'cutoff':1.66}}, #1.63

									'slatm'	: { 'HCS' : {'sigma':30683.8, 'lambda':3.9e-05, 'cutoff':7.52}, # 0.45
												'CCS' : {'sigma':13.4951, 'lambda':1.8e-16, 'cutoff':6.88}, # 4.04
												'J1CH' : {'sigma':26.6671, 'lambda':7.3e-12, 'cutoff':9.28}}, #0.94

									'fchl'	: {	'HCS' : {'sigma':5.92947, 'lambda':1.4e-06, 'cutoff':6.26}, # 0.26
												'CCS' : {'sigma':0.210613, 'lambda':0.0045, 'cutoff':5.06}, # 3.04
												'1JCH' : {'sigma':2.23, 'lambda':7.7e-07, 'cutoff':5.12}, # 0.94
												'1JNH' : {'sigma':2.23, 'lambda':7.7e-07, 'cutoff':5.12},
												'2JCH' : {'sigma':2.23, 'lambda':7.7e-07, 'cutoff':5.12},
												'2JNH' : {'sigma':2.23, 'lambda':7.7e-07, 'cutoff':5.12},
												'2JHH' : {'sigma':2.23, 'lambda':7.7e-07, 'cutoff':5.12},
												'3JCH' : {'sigma':2.23, 'lambda':7.7e-07, 'cutoff':5.12},
												'3JNH' : {'sigma':2.23, 'lambda':7.7e-07, 'cutoff':5.12},
												'3JHH' : {'sigma':2.23, 'lambda':7.7e-07, 'cutoff':5.12}}}}




	sigma = optimal[dataset][rep][parameter]['sigma']
	lamda = optimal[dataset][rep][parameter]['lambda']
	cutoff = optimal[dataset][rep][parameter]['cutoff']

	return sigma, lamda, cutoff
