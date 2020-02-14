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

def get_unique_part(files):

	parts = []

	for file in files:
		parts.append(file.split('/')[-1].split('.')[0].split('_'))

	label_part = 0

	for p1, part1 in enumerate(parts):
		for p2, part2 in enumerate(parts):
			if p1 == p2:
				continue
			for i in range(len(part1)):
				if part1[i] != part2[i]:
					label_part = i


	return label_part
