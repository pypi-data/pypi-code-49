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

def HPS(dataset, args):

	if args['searchflag'] == 'grid':
		from .hyperparameter_tuning import HPS_grid
		dset, score = HPS_grid.grid_search(dataset, args)

	elif args['searchflag'] == 'gaussian':
		from .hyperparameter_tuning import HPS_gaussian
		dset, score = HPS_gaussian.gaussian_search(dataset, args)

	elif args['searchflag'] == 'random':
		from .hyperparameter_tuning import HPS_random
		dset, score = HPS_random.random_search(dataset, args)

	print('Model optimised, score = ', score)

	return dset, score
