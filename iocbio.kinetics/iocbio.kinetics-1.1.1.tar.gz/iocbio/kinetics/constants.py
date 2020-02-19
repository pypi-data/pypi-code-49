# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2019-2020
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  This file is part of project: IOCBIO Kinetics
#
# Constants used in several places in the code

"""Constants that are used throughout the code

Use the following constants when referring to the database tables:

- database_table_experiment: Name of the database table keeping a
  record regarding the experiment. See
  :class:`.handler.experiment_generic.ExperimentGeneric` for details.

- database_table_roi: Name of the database table keeping a record
  regarding each ROI. See
  :class:`.handler.roi.ROIHandler` for details.

To use in the modules, import with

from iocbio.kinetics.constants import database_table_roi, database_table_experiment

"""


database_table_experiment = "experiment"
database_table_roi = "roi"
