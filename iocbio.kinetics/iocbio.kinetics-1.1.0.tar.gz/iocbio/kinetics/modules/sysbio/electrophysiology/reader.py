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
#!/usr/bin/env python3

import numpy as np
import h5py
import os
import hashlib
from scipy.interpolate import LSQUnivariateSpline
from collections import OrderedDict
import iocbio.kinetics.global_vars as g

### Required definition for exported module ###
IocbioKineticsModule = ['args', 'reader']

### Implementaiton

class ElectroFluorescenceData(object):

    @staticmethod
    def ltcc_events():
        n = 14
        v = [str(i) for i in 5*np.arange(n) - 40]
        t = 9*np.arange(n) + 8
        return zip(t,v)

    @staticmethod
    def ltcc_events_legacy():
        n = 14
        v = [str(i) for i in 5*np.arange(n) - 40]
        t = 3*np.arange(n) + 2
        return zip(t,v)

    @staticmethod
    def srrecovery_by_ltcc_events():
        n = 18
        v = ['pulse_'+str(i) for i in np.arange(n)]
        t = np.arange(n)
        return zip(t,v)

    def __init__(self, filename, experiment_type):
        self.efile = filename
        self.ffile = filename[:-3] + '-analysis.h5'

        self.experiment_type = experiment_type

        if not os.path.isfile(self.ffile):
            raise IOError('Analysis file containing fluorescence data is not found. Looking for file:', self.ffile)

        self._init_currents()
        self._init_fluorescence()
        self._init_events()

    def _init_currents(self):
        eh5 = h5py.File(self.efile, 'r')
        attrs = eh5['Configuration'].attrs
        confstr = ''
        akey = list(attrs)
        akey.sort()
        for a in akey: confstr = confstr+str(a)+str(attrs[a])

        m_time = str(attrs['m_time'].decode())
        self.exp_date = None
        if m_time[2] == '.' and m_time[5] == '.':
            day = m_time[0:2]
            month = m_time[3:5]
            year = m_time[6:10]
            a = ('.').join([year, month, day])
            m_time = a + m_time[len(a):]
            self.exp_date = int(year+month+day)

        self.experiment_id = hashlib.sha256(confstr.encode('utf-8')).hexdigest() + '_' + m_time
        self.m_time = m_time # attrs['m_time'].decode()
        self.dt = attrs['PROTOCOL_ELECTROPHYSIOLOGY_Dt']
        self.t = eh5['ProtocolElectrophysiology/electrophysiology/relative time'].value
        self.v = eh5['ProtocolElectrophysiology/electrophysiology/command signal'].value
        self.c = eh5['ProtocolElectrophysiology/electrophysiology/recorded signal 1'].value
        xsize = min(self.t.size, self.v.size, self.c.size)
        self.t = self.t[:xsize]
        self.v = self.v[:xsize]
        self.c = self.c[:xsize]

        self.name = eh5['Information'].attrs['name'].decode()
        if 'cell_id' not in eh5['Information'].attrs:
            raise KeyError('"cell_id" not found! Add "cell_id" to the Information group and try again')
        self.cell_id = int(eh5['Information'].attrs['cell_id'])
        eh5.close()

    def _init_fluorescence(self):
        fh5 = h5py.File(self.ffile, 'r')
        if 'andor' in fh5:
            camera = 'andor'
            eh5 = h5py.File(self.efile, 'r')
            try:
                t = eh5['ImageStream/Andor/time'].value
            except:
                t = eh5['ImageStream/Andor/programmed time'].value
                print('Using programmed time')
            eh5.close()
        if 'Andor' in fh5:
            camera = 'Andor'
            t = fh5[camera+'/intensity/cell_time'].value

        fc = fh5[camera+'/intensity/cell'].value[0,:]
        fb = fh5[camera+'/intensity/background'].value[0,:]
        fh5.close()

        tsize = min(t.size, fc.size, fb.size)
        t = t[:tsize]
        fc = fc[:tsize]
        fb = fb[:tsize]

        knots_steps = int(t.size/50)
        #print(t[0], t[knots_steps:-knots_steps+1][::knots_steps], t[-1])
        bg_spline = LSQUnivariateSpline(t, fb, t[knots_steps:-knots_steps+1][::knots_steps])
        #self.fluorescence = np.interp(self.t, t, fc-bg_spline(t))
        self.fluorescence_y = fc-bg_spline(t)
        self.fluorescence_t = t

    def _init_events(self):
        et = self.experiment_type
        self.events = {}

        if et == 'ltcc':
            if self.exp_date is not None and self.exp_date < 20151117:
                print('ltcc_events_legacy')
                for t, v in self.ltcc_events_legacy():
                    self.events[t] = str(v)
            else:
                for t, v in self.ltcc_events():
                    self.events[t] = str(v)

        elif et == 'kill':
            self.events = {}

        elif et == 'srcontent_by_ncx':
            t = max(0, np.round(self.fluorescence_t[np.argmax(self.fluorescence_y)] - 2.))
            self.events[t] = 'Caffeine'

        elif et == 'srrecovery_by_ltcc':
            for t, v in self.srrecovery_by_ltcc_events():
                self.events[t] = str(v)

        else:
            raise NotImplementedError('Mode electrophysiology experiment type %s' % et)


#########################################
########## Modules API ##################
def args(parser):
    parser.add(name='electro_condition',
               help='Electrophysiology experiment condition. For example: ttx, iso')
    return '''Electrophysiology:
------------------
ltcc - Voltage step prodocol to estimate LTCC current
kill - Fluorescence maximum from killing cardiomyocyte
srcontent_by_ncx - Caffeine induced calcium relase
srrecovery_by_ltcc - SR recovery after caffeine experiment
'''

def create_data(database, experiment_id=None, args=None):
    from iocbio.kinetics.io.data import Data, Carrier
    from iocbio.kinetics.handler.experiment_generic import ExperimentGeneric
    from .experiment_electrophysiology import ExperimentElectrophysiology

    filename=getattr(args, "file_name", None)
    mode = getattr(args, "protocol", None)
    condition = getattr(args, "electro_condition", None)

    if experiment_id is not None:
        filename, mode, condition = ExperimentElectrophysiology.get_fname_mode(database, experiment_id)

    if filename is None or not filename.endswith('.h5'):
        return None
    
    if mode == 'ltcc':
        t = 'LTCC'
    elif mode == 'kill':
        t = 'Fluorescence maximum'
    elif mode == 'srcontent_by_ncx':
        t = 'SR content by NCX'
    elif mode == 'srrecovery_by_ltcc':
        t = 'SR recovery by LTCC'
    else:
        return None    
    
    r = ElectroFluorescenceData(filename, mode)

    # if mode == 'kill':
    #     d = {'fluorescence': { 'x': r.fluorescence_t,
    #                            'y': Carrier('Background corrected fluorescence', 'AU', r.fluorescence_y) }}
    # else:
    d = OrderedDict( [ ('current', { 'x': r.t, 'y': Carrier('Current measured', 'pA', r.c) }),
                       #('voltage', Carrier('Voltage applied', 'mV', r.v)),
                       ('fluorescence', { 'x': r.fluorescence_t,
                                          'y': Carrier('Background corrected fluorescence', 'AU', r.fluorescence_y) }) ] )

    data = Data(r.experiment_id,
                config = {'dt': r.dt, 'filename': filename,
                          'mode': mode, 'events': r.events,
                          'cell_id': r.cell_id, 'condition': condition},
                type = 'SBMicroscope Electrophysiology ' + t,
                type_generic = 'Electrophysiology ' + t,
                time = r.m_time,
                name = r.name,
                xname = 'Time', xunit = 's',
                xlim = (min(r.t[0], r.fluorescence_t[0]), max(r.t[-1], r.fluorescence_t[-1])),
                data = d,
                add_range = 0.01)

    if not ExperimentGeneric.has_record(database, data.experiment_id):
        print('Record not found', data.experiment_id)
        database.set_read_only(False)
        ExperimentElectrophysiology.store(database, data)

    g.data = data
    return data


if __name__=='__main__':
    # python3 electrophysiology_reader.py /home/martinl/data/experiments/electro/mouse-ltype/171128-AGATw-electro/c1_iv_10uMttx_1_collected.h5
    import sys
    filename = sys.argv[1]
    data = create_data(None, filename)
    print(data)
