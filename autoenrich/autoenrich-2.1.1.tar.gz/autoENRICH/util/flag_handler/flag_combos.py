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

def check_combination(modelflag, featureflag):


	if modelflag == 'KRR':
		if featureflag not in ['CMAT', 'aSLATM', 'ACSF']:
			return False

	elif modelflag == 'FCHL':
		if featureflag != 'FCHL':
			return False


	elif modelflag == 'NN':
		return True


	elif modelflag == 'TFM':
		if featureflag != 'BCAI':
			return False

	else:
		return False


	return True
