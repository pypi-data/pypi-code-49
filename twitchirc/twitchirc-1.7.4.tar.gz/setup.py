#  Library to make crating bots for Twitch chat easier.
#  Copyright (c) 2019 Maciej Marciniak
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import setup

setup(
    name='twitchirc',
    python_requires='>=3.7',
    version='1.7.4',
    packages=['twitchirc'],
    url='https://www.github.com/mm2pl/twitchirc',
    license='GPLv3',
    author='mm2pl',
    author_email='u.y@o2.pl',
    description='Unofficial library for Twitch irc.'
)
