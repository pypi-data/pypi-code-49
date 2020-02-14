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

import bayes_opt as bayes
from bayes_opt import BayesianOptimization
from bayes_opt import UtilityFunction
from bayes_opt.observer import JSONLogger
from bayes_opt.event import Events
from bayes_opt.util import load_logs

import pickle
import numpy as np

import copy

from autoENRICH.ml.hyperparameter_tuning import HPS_generic as generic

# Load iterations from previous run
def load_logs(args):
	# Input:
	# args: global argument dictionary

	# Returns: list of paremeters and scores to read into gaussian process
	to_load = []
	try:
		with open(args['logfile'], 'r') as f:
			switch = False
			for line in f:
				if 'START' in line:
					switch = True
				elif switch:
					items = line.split()
					if items[0] == 'i':
						headers = items[1:]
						headers = [x.strip(' ') for x in headers]

					else:
						params = {}
						for i in range(2, len(headers)):
							if headers[i-1] == 'Mins':
								continue
							params[headers[i-1]] = float(items[i])
						score = float(items[1])

						to_load.append([params, score])
	except Exception as e:
		print(e)
		return []

	return to_load


def gaussian_search(dataset, args):

	# determine whether log dictionary was provided
	if len(args['param_logs']) == 0:
		check_logs = False
	else:
		check_logs = True

	pbounds = {}
	for param in args['param_ranges'].keys():
		if args['param_logs'][param] == 'no':
			continue
		#pbounds[param] = (args['param_ranges'][param][0], args['param_ranges'][param][1])
		pbounds[param] = (0, 1)

	optimizer = BayesianOptimization(
		f=None,
		pbounds=pbounds,
		verbose=0, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
		random_state=None
	)
	utility = UtilityFunction(kind="ucb", kappa=args['kappa'], xi=args['xi'])

	if args['load']:
		print('Loading previous data. . .')
		to_load = load_logs(args)
		for log in to_load:
			optimizer.register(params=log[0], target=(99999.99-log[1])/99999.99)
		print('Loaded ', len(to_load), ' datapoints')

	generic.setup_logfile(args)

	if args['load']:
		for params, score in to_load:
			with open(args['logfile'], 'a') as f:
				iter = -1
				string = '{i:<10d}\t{score:<10.5f}'.format(i=iter, score=score)
				for param in args['param_list']:
					if args['param_logs'][param] == 'no':
						continue
					string = string + '\t{param:<20.4g}'.format(param=params[param])
				print(string, file=f)

	BEST_SCORE = 999.999
	BEST_PARAMS = {}
	searched = []
	force_random = False
	for e in range(int(args['epochs'])):

		if force_random or (args['random'] > 0 and e%args['random'] == 0):
			print('RANDOM')
			next_point_to_probe = {}
			for param in args['param_ranges'].keys():
				if args['param_logs'][param] == 'no':
					continue

				next_point_to_probe[param] = np.random.uniform(0, 1)
				#next_point_to_probe[param] = np.random.uniform(args['param_ranges'][param][0], args['param_ranges'][param][1])
			force_random = False
		else:
			next_point_to_probe = optimizer.suggest(utility)


		for param in args['param_ranges'].keys():
			if args['param_logs'][param] == 'no':
				continue
			next_point_to_probe[param] = (next_point_to_probe[param]*(args['param_ranges'][param][1]-args['param_ranges'][param][0])) + args['param_ranges'][param][0]

		if check_logs:
			for param in args['param_ranges'].keys():
				if args['param_logs'][param] == 'no':
					continue
				if 'log' in args['param_logs'][param]:
					next_point_to_probe[param] = 10**next_point_to_probe[param]

		score, BEST_SCORE, BEST_PARAMS = generic.HPS_iteration(e, dataset, args, next_point_to_probe=copy.copy(next_point_to_probe),
															BEST_SCORE=BEST_SCORE, BEST_PARAMS=BEST_PARAMS)

		searched.append(next_point_to_probe)
		try:
			optimizer.register(params=next_point_to_probe, target=(99999.99-score)/99999.99)
		except KeyError as e:
			print(e)
			print('Non-unique point generated, (increasing kappa value and) skipping (kappa = ',args['kappa'],')')
			args['kappa'] += 1.0
			utility = UtilityFunction(kind="ei", kappa=args['kappa'], xi=args['xi'])
			print('(forcing random point)')
			force_random = True


	outname = generic.save_models(dataset, BEST_PARAMS, args)
	print('Optimised model(s) saved in ', outname)

	return dataset, BEST_SCORE

























###
