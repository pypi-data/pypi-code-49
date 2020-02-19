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
from iocbio.kinetics.handler.experiment_generic import ExperimentGeneric
from iocbio.kinetics.constants import database_table_experiment


### Required definition for exported module ###
IocbioKineticsModule = ['args', 'reader', 'database_schema', 'database_info']

### Implementation

class ExperimentConfocalCaTransient(ExperimentGeneric):

    database_table = "confocal_catransient"
    datatype_generic = "Calcium Fluorescence Transient"
    datatype_specific = "Sysbio LSM XT Calcium Fluorescence Transient"

    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(ExperimentConfocalCaTransient.database_table) +
                 "(experiment_id text not null, filename text, title text, voxel_x real, voxel_t real, trace text, " +
                 "sparks_stage text not null, " +
                 "PRIMARY KEY (experiment_id), " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE, " +
                 "FOREIGN KEY (sparks_stage) REFERENCES sparks_stage(stage_id) ON DELETE CASCADE " +
                 ")"
        )

    @staticmethod
    def get_data(database, experiment_id):
        from iocbio.kinetics.io.data import Data, Carrier
        import msgpack, base64
        import numpy as np

        hw = ExperimentGeneric.hardware(database, experiment_id)
        if hw != 'sysbio/lsm xt':
            return None

        for q in database.query('SELECT trace, filename FROM ' + database.table(ExperimentConfocalCaTransient.database_table) +
                                ' WHERE experiment_id=:expid', expid = experiment_id):
            t = msgpack.unpackb(base64.b64decode(q.trace))
            d = { key.decode(): val for key,val in t.items() }
            return Data( experiment_id,
                         config = { 'filename': q.filename, 'events': {} },
                         type = ExperimentConfocalCaTransient.datatype_specific,
                         type_generic = ExperimentConfocalCaTransient.datatype_generic,
                         name = q.filename,
                         xname = 'Time', xunit = 's',
                         data = { 'fluorescence': { 'x': np.array(d['t']),
                                                    'y': Carrier('Fluorescence', 'AU', np.array(d['fluorescence'])) } },
                         xlim = (d['t'][0], d['t'][-1]),
                         )
            
        return  None
        

    @staticmethod
    def get_sparks_stages(db, sparks_expid):
        regs = []
        for q in db.query('SELECT e.experiment_id, s.stage_id, e.filename, s."start", s."end" FROM sparks_stage s ' +
                          'JOIN sparks_experiment e ON e.experiment_id=s.experiment_id ' +
                          'WHERE s.experiment_id=:eid AND s.name=:name', eid=sparks_expid, name='pacing'):
            regs.append(q)
        return regs

    @staticmethod
    def has_record(database, experiment_id):
        try:
            res = database.has_record(ExperimentConfocalCaTransient, experiment_id=experiment_id)
        except:
            res = False
        return res

    @staticmethod
    def store_experiment(database, experiment_id, sparks_stage_id, filename, start, end):
        from iocbio.kinetics.handler.experiment_generic import ExperimentGeneric
        from tifffile.tifffile import TiffFile        
        import msgpack, base64
        import os, time
        import numpy as np

        print('Loading TIFF', filename)
        title = os.path.basename(filename)
        epo = os.path.getmtime(filename)
        tstring = time.strftime("%Y.%m.%d %H:%M", time.localtime(epo))
        with TiffFile(filename) as tif:
            if tif.is_lsm is True:
                data = tif.asarray()[:,0,0,0,:]
                dx = tif.lsm_metadata['VoxelSizeX'] # in meters #* 1e6 # in microns
                deltat = tif.lsm_metadata['TimeIntervall']*1e3 # in seconds * 1000 # in milli seconds
                dimX = tif.lsm_metadata['DimensionX']
                dimTime = tif.lsm_metadata['DimensionTime']
                print('Lines', start/deltat, end/deltat)
                i0 = int(start/deltat)
                i1 = int(end/deltat)
                dy = data.mean(axis=1).astype(np.float64)
                dt = deltat*np.arange(0, dy.shape[0])
                dy = dy[i0:i1]
                dt = dt[i0:i1] / 1e3 # back to seconds
            else:
                print("Don't know how to load this TIFF")
                return # don't know what to do

        trace = base64.b64encode(msgpack.packb({'t': list(dt), 'fluorescence': list(dy)})).decode()
        
        ExperimentGeneric.store(database, experiment_id, time=tstring,
                                type_generic=ExperimentConfocalCaTransient.datatype_generic,
                                type_specific=ExperimentConfocalCaTransient.datatype_specific,
                                hardware="sysbio/lsm xt")

        if database.has_record(ExperimentConfocalCaTransient.database_table, experiment_id=experiment_id):
            database.query("UPDATE " + database.table(ExperimentConfocalCaTransient.database_table) +
                           " SET filename=:fname, title=:title, voxel_x=:vx, voxel_t=:vt, trace=:trace, sparks_stage=:sparks_stage_id " +
                           " WHERE experiment_id=:experiment_id",
                           experiment_id=experiment_id, fname=filename, title=title, vx=dx, vt=deltat, trace=trace, sparks_stage_id=sparks_stage_id)
        else:
            database.query("INSERT INTO " + database.table(ExperimentConfocalCaTransient.database_table) +
                           "(experiment_id,filename,title,voxel_x,voxel_t,trace,sparks_stage) " +
                           "VALUES(:experiment_id,:fname,:title,:vx,:vt,:trace,:sparks_stage_id)",
                           experiment_id=experiment_id, fname=filename, title=title, vx=dx, vt=deltat, trace=trace, sparks_stage_id=sparks_stage_id)
                           

#########################################
########## Modules API ##################
def args(parser):
    parser.add(name='sparks_expid', help='IOCBIO Sparks experiment ID')
    
    return '''Confocal Calcium Transient:
---------------------------
Protocol is automatically detected through name of of the selected
region in the experiment by IOCBIO Sparks software. For calcium
transients to be analyzed, set the name to 'pacing'.
'''

def database_info(database):
    return "SELECT title from %s s where s.experiment_id=e.experiment_id" % database.table("confocal_catransient")

def database_schema(db):
    ExperimentConfocalCaTransient.database_schema(db)

def create_data(database, experiment_id=None, args=None):
    sparks_expid = getattr(args, 'sparks_expid', None)
    data = None
    
    if sparks_expid is not None:
        for s in ExperimentConfocalCaTransient.get_sparks_stages(database, sparks_expid):
            expid = s.experiment_id + ' - ' + s.stage_id
            filename = s.filename
            if not ExperimentConfocalCaTransient.has_record(database, expid):
                database.set_read_only(False)
                ExperimentConfocalCaTransient.store_experiment(database, experiment_id=expid, sparks_stage_id=s.stage_id,
                                                               filename=s.filename, start=s.start, end=s.end)
            data = create_data(database, experiment_id=expid)

    elif experiment_id is not None:
        data = ExperimentConfocalCaTransient.get_data(database, experiment_id) 
        
    return data
