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

from . import HPS_generic as generic
import numpy as np
import itertools
import pickle
import sys


def random_search(dataset, args):

	# determine whether log dictionary was provided
	if len(args['param_logs']) == 0:
		check_logs = False
	else:
		check_logs = True


	generic.setup_logfile(args)

	BEST_SCORE = 999.999
	BEST_PARAMS = {}
	next_point_to_probe = {}

	for _ in range(int(args['epochs'])):
		for param in args['param_ranges'].keys():
			if args['param_logs'][param] == 'no':
				continue
			next_point_to_probe[param] = np.random.uniform(args['param_ranges'][param][0], args['param_ranges'][param][1])

		if check_logs:
			for param in args['param_ranges'].keys():
				if args['param_logs'][param] == 'no':
					continue
				if args['param_logs'][param] == 'log':
					next_point_to_probe[param] = 10**next_point_to_probe[param]


		score, BEST_SCORE, BEST_PARAMS = generic.HPS_iteration(_, dataset, args, next_point_to_probe=next_point_to_probe,
															BEST_SCORE=BEST_SCORE, BEST_PARAMS=BEST_PARAMS)

	outname = generic.save_models(dataset, BEST_PARAMS, args)
	print('Optimised model saved in ', outname)

	return dataset, BEST_SCORE
