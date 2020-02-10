#  Copyright (C) 2020  Kunal Mehta <legoktm@member.fsf.org>
#
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
#

from setuptools import setup

setup(
    name='Flask-ULS',
    version='0.2.0',
    packages=['flask_uls'],
    url='https://git.legoktm.com/legoktm/flask-uls',
    license='GPL-3.0-or-later',
    python_requires='>=3.5',
    install_requires=['Flask'],
    include_package_data=True,
    author='Kunal Mehta',
    author_email='legoktm@member.fsf.org',
    long_description=open('README.rst').read(),
    description='Easy to use integration of the Universal Language Selector '
                'in Flask applications',
)
