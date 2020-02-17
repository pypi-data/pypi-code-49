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
# Adds cardiomyocyte ID as specified on command line to the experiment

### Module flag
IocbioKineticsModule = ['args', 'database_processor']

def args(parser):
    parser.add(name='mousecm',
               help='Link mouse cardiomyocyte isolation ID to the imported experiment. Use id from prep_cardiomyocyte_mouse table.')
    return None

def database_process(database, data, args):
    if args.mousecm is not None and data is not None:
        if database.read_only:
            print('Cannot set mouse cardiomyocyte ID - database in readonly mode. Add --rw to program options')
        else:
            database_table = database.table("experiment_to_mouse_cardiomyocytes")
            database.query("INSERT INTO " + database_table +
                           " (preparation, experiment) " +
                           "VALUES(:preparation,:experiment)",
                           preparation = args.mousecm,
                           experiment = data.experiment_id)
