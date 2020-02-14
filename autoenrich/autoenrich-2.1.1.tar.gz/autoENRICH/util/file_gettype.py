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

def get_type(filename):

	extension = filename.split('.')[-1]
	if extension == 'sdf':
		if len(filename.split('.')) > 2:
			if filename.split('.')[-2] == 'nmredata':
				type = 'nmredata'
			else:
				type = 'sdf'
		else:
			type = 'sdf'

	elif extension == 'xyz':
		type = 'xyz'

	elif extension == 'log':
		type = 'g09'

	elif extension == 'mol2':
		type = 'mol2'

	else:
		print('type not recognised for file ', filename, ' please check file and specify type')
		type = ''

	return type
