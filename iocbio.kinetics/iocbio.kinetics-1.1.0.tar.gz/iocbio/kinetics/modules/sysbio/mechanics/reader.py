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

from iocbio.kinetics.io.data import Data, Carrier

### Required definition for exported module ###
IocbioKineticsModule = ['args', 'reader']

### Implementaiton


class SarcomereLengthFluorescenceData(object):

    def __init__(self, filename, experiment_type):
        self.mfile = filename
        self.ffile = filename[:-3] + '-analysis.h5'
        self.experiment_type = experiment_type

        if not os.path.isfile(self.ffile):
            raise IOError('Analysis file containing fluorescence data is not found. Looking for file:', self.ffile)

        self._init_sarcomere_length()
        self._init_fluorescence()
        self._init_events()
        self._init_fiber_deformation()

    def _init_sarcomere_length(self):
        main_h5 = h5py.File(self.mfile, 'r')
        analysis_h5 = h5py.File(self.ffile, 'r')
        attrs = main_h5['Configuration'].attrs
        confstr = ''
        akey = list(attrs)
        akey.sort()
        for a in akey: confstr = confstr+str(a)+str(attrs[a])

        m_time = str(attrs['m_time'].decode())
        if m_time[2] == '.' and m_time[5] == '.':
            day = m_time[0:2]
            month = m_time[3:5]
            year = m_time[6:10]
            a = ('.').join([year, month, day])
            m_time = a + m_time[len(a):]

        self.experiment_id = hashlib.sha256(confstr.encode('utf-8')).hexdigest() + '_' + m_time
        self.m_time = m_time # attrs['m_time'].decode()
        try:
            self.sarcomere_length = analysis_h5['Bonito_SISO/sarcomere length/sarcomere length']
            self.sarcomere_length_time = analysis_h5['Bonito_SISO/sarcomere length/time']
            print('SL from analysis file')
        except:
            self.sarcomere_length = main_h5['ProtocolMyocyteMechanics/mechanics/sarcomere length']
            self.sarcomere_length_time = main_h5['ProtocolMyocyteMechanics/mechanics/time']

        xsize = min(self.sarcomere_length.size, self.sarcomere_length_time.size)
        self.sarcomere_length = self.sarcomere_length[:xsize]
        self.sarcomere_length_time = self.sarcomere_length_time[:xsize]

        self.name = main_h5['Information'].attrs['name'].decode()
        self.attrs = dict(attrs)
        main_h5.close()
        analysis_h5.close()

    def _init_fiber_deformation(self):
        main_h5 = h5py.File(self.mfile, 'r')
        for fiber in ['fiber left', 'fiber right']:
            deformation = main_h5['ProtocolMyocyteMechanics/mechanics/'+fiber+' deformation']
            time = main_h5['ProtocolMyocyteMechanics/mechanics/time']
            xsize = min(deformation.size, time.size)
            deformation = deformation[:xsize]
            time = time[:xsize]
            fibername = fiber.split(' ')[-1]
            setattr(self, 'deformation_'+fibername, deformation)
            setattr(self, 'deformation_'+fibername+'_time', time)

        main_h5.close()

    def _init_fluorescence(self):
        analysis_h5 = h5py.File(self.ffile, 'r')

        for camera in ['Hamamatsu_C11440_Bottom', 'Hamamatsu_C11440_Side']:
            if camera+'/intensity' not in analysis_h5:
                continue
            dset_keys = analysis_h5[camera+'/intensity'].keys()
            cell_key, bg_key = None, None
            for k in dset_keys:
                if 'cell' == k.lower():
                    cell_key = k
                if 'bg' == k.lower():
                    bg_key = k
            if cell_key is None or bg_key is None:
                raise ValueError('Did not find fluorescence data for a cell or background from datasets:', dset_keys)

            t = analysis_h5[camera+'/intensity/%s_time' % cell_key].value
            fc = analysis_h5[camera+'/intensity/%s' % cell_key].value[0,:]
            fb = analysis_h5[camera+'/intensity/%s' % bg_key].value[0,:]

            tsize = min(t.size, fc.size, fb.size)
            t = t[:tsize]
            fc = fc[:tsize]
            fb = fb[:tsize]
            knots_steps = int(t.size/50)
            bg_spline = LSQUnivariateSpline(t, fb, t[knots_steps:-knots_steps+1][::knots_steps])

            setattr(self, 'fluorescence_'+camera, fc-bg_spline(t))
            setattr(self, 'fluorescence_'+camera+'_time', t)

        analysis_h5.close()

    def _init_events(self):
        et = self.experiment_type

        self.events = {}

        if (et == 'ufreqcasl' or et == 'lfreqcasl') and self.attrs['STIMULATOR_Enable'] == 1:
            cmd = []
            for el in self.attrs['STIMULATOR_FrequencyCommand'].decode().split(';'):
                l = el.strip().split(' ')
                if len(l) != 2:
                    raise ValueError('Something wrong with STIMULATOR_FrequencyCommand', self.attrs['STIMULATOR_FrequencyCommand'].split(';'))
                cmd.append([float(l[0]), l[1]])

            t_total = 0
            self.events[t_total] = cmd[0][1]
            for i in range(len(cmd)-1):
                t, fr = cmd[i]
                t_total += t
                if float(cmd[i+1][1]) < 0.0001:
                    name = cmd[i+1][1]
                else:
                    name = '%s -> %s' % (fr, cmd[i+1][1])
                self.events[t_total] = name

            if 0:
                t, fr = cmd[-1]
                t_total += t
                self.events[t_total] = fr


class DeriveMechSlices(object):

    def __init__(self, events):
        etime = sorted(list(events.keys()))
        data = []
        frq_rng = []
        for i in range(len(etime)-1):
            t0 = etime[i]
            t1 = etime[i+1]
            if '->' in events[etime[i]]:
                fr1, fr2 = map(float, events[etime[i]].split('->'))
                wpulse = 1/fr2
                npulses = int(np.floor(fr2*(t1 - t0)))

                for j in range(npulses):
                    data.append([t0+(j+0.5)*wpulse, t0+(j+1.5)*wpulse, j, fr2])
                frq_rng.append([t0, t1, fr2])

            else:
                fr1 = float(events[etime[i]])
                frq_rng.append([t0, t1, fr1])

        self.data = np.array(data)
        self.frq_rng = np.array(frq_rng)
        self.t0 = self.data[:,0]
        self.t1 = self.data[:,1]

    def get_reference_time(self, t):
        if t < self.t0.min() or t > self.t1.max():
            return 0
        else:
            for t0, t1, n, fr in self.data:
                if t0 <= t < t1:
                    for ft0, ft1, fr2 in self.frq_rng:
                        if ft0 <= t < ft1 and fr2 == fr:
                            return t0
        return 0

    def get_pulse_no(self, t):
        if t < self.t0.min() or t > self.t1.max():
            return 0
        else:
            for t0, t1, n, fr in self.data:
                if t0 <= t < t1:
                    for ft0, ft1, fr2 in self.frq_rng:
                        if ft0 <= t < ft1 and fr2 == fr:
                            return n
        return 0

    def get_pulse_width(self, t):
        for t0, t1, n in self.frq_rng:
            if t0 <= t < t1:
                if n > 0:
                    if t+1/n > t1:
                        return t1-t
                    return 1/n
                else:
                    return 1.0
        return 1.0


class DataMech(Data):

    def new_range(self, x):
        return [x, x+self._ranger.get_pulse_width(x)]

    def _sinit__(self):
        '''Secrect init for enabling usage of functions below'''
        self._ranger = DeriveMechSlices(self.config['events'])

    def get_pulse_no(self, t):
        return self._ranger.get_pulse_no(t)

    def get_reference_time(self, t):
        return self._ranger.get_reference_time(t)

    def get_auto_slice_ranges(self):
        data = []
        #for i in range( min(self._ranger.data.shape[0]-1, 2) ):# for testing
        for i in range(self._ranger.data.shape[0]-1):
            t0, t1, _, _ = self._ranger.data[i]
            if t1 > self._ranger.data[i+1][0]:
                continue
            else:
                data.append([t0,t1])
        return np.array(data)
        # return self._ranger.data[:,:2]



#########################################
########## Modules API ##################

def args(parser):
    return '''Mechanics:
----------
ufreqcasl - Unloaded cardiomyocyte Ca and SL stimulation frequency response
lfreqcasl - Loaded cardiomyocyte Ca and SL stimulation frequency response
'''


def create_data(database, experiment_id=None, args=None):
    from iocbio.kinetics.handler.experiment_generic import ExperimentGeneric
    from .experiment_mechanics import ExperimentMechanics

    filename = getattr(args, "file_name", None)
    mode = getattr(args, "protocol", None)

    if experiment_id is not None:
        filename, mode = ExperimentMechanics.get_fname_mode(database, experiment_id)

    if filename is None or not filename.endswith('.h5'):
        return None
    
    if mode not in ['ufreqcasl', 'lfreqcasl']:
        return None
    
    if mode == 'ufreqcasl':
        t = 'Unloaded cardiomyocyte Ca and SL stimulation frequency response'
        r = SarcomereLengthFluorescenceData(filename, mode)
        dd = OrderedDict([('sarcomere length', { 'x': r.sarcomere_length_time, 'y': Carrier('Sarcomere length', 'um', r.sarcomere_length) }) ])
        if hasattr(r,'fluorescence_Hamamatsu_C11440_Side_time'):
            dd['fluorescence side'] = { 'x': r.fluorescence_Hamamatsu_C11440_Side_time,
                                        'y': Carrier('Background corrected fluorescence', 'AU', r.fluorescence_Hamamatsu_C11440_Side) }

        if hasattr(r, 'fluorescence_Hamamatsu_C11440_Bottom_time'):
            dd['fluorescence bottom'] = { 'x': r.fluorescence_Hamamatsu_C11440_Bottom_time,
                                          'y': Carrier('Background corrected fluorescence', 'AU', r.fluorescence_Hamamatsu_C11440_Bottom) }
        if  hasattr(r,'fluorescence_Hamamatsu_C11440_Side_time') and  hasattr(r, 'fluorescence_Hamamatsu_C11440_Bottom_time'):
            xlimlist =(min(r.sarcomere_length_time[0], r.fluorescence_Hamamatsu_C11440_Side_time[0], r.fluorescence_Hamamatsu_C11440_Bottom_time[0]),
                       max(r.sarcomere_length_time[-1], r.fluorescence_Hamamatsu_C11440_Side_time[-1], r.fluorescence_Hamamatsu_C11440_Bottom_time[-1]))
        elif hasattr(r,'fluorescence_Hamamatsu_C11440_Side_time') and not hasattr(r, 'fluorescence_Hamamatsu_C11440_Bottom_time'):
            xlimlist =(min(r.sarcomere_length_time[0], r.fluorescence_Hamamatsu_C11440_Side_time[0]),
                       max(r.sarcomere_length_time[-1], r.fluorescence_Hamamatsu_C11440_Side_time[-1]))



        data = DataMech(r.experiment_id,
                        config = {'filename': filename,
                                  'mode': mode, 'events': r.events},
                        type = 'SBMicroscope Mechanics ' + t,
                        type_generic = 'Mechanics ' + t,
                        time = r.m_time,
                        name = r.name,
                        xname = 'Time', xunit = 's',
                        xlim = xlimlist,
                        data = dd,
        )


    elif mode == 'lfreqcasl':
        t = 'Loaded cardiomyocyte Ca and SL stimulation frequency response'
        r = SarcomereLengthFluorescenceData(filename, mode)

        data = DataMech(r.experiment_id,
                        config = {'filename': filename,
                                  'mode': mode, 'events': r.events},
                        type = 'SBMicroscope Mechanics ' + t,
                        type_generic = 'Mechanics ' + t,
                        time = r.m_time,
                        name = r.name,
                        xname = 'Time', xunit = 's',
                        xlim = (min(r.sarcomere_length_time[0], r.fluorescence_Hamamatsu_C11440_Side_time[0], r.fluorescence_Hamamatsu_C11440_Bottom_time[0], r.deformation_left[0],r.deformation_right[0]),
                                max(r.sarcomere_length_time[-1], r.fluorescence_Hamamatsu_C11440_Side_time[-1], r.fluorescence_Hamamatsu_C11440_Bottom_time[-1], r.deformation_left_time[-1],r.deformation_right_time[-1])),
                        data = OrderedDict ( [
                            ('sarcomere length', { 'x': r.sarcomere_length_time, 'y': Carrier('Sarcomere length', 'um', r.sarcomere_length) }),
                            ('fluorescence side', { 'x': r.fluorescence_Hamamatsu_C11440_Side_time,
                                                    'y': Carrier('Background corrected fluorescence', 'AU', r.fluorescence_Hamamatsu_C11440_Side) }),
                            ('fluorescence bottom', { 'x': r.fluorescence_Hamamatsu_C11440_Bottom_time,
                                                      'y': Carrier('Background corrected fluorescence', 'AU', r.fluorescence_Hamamatsu_C11440_Bottom) }),

                            ('sarcomere length ', { 'x': r.sarcomere_length_time, 'y': Carrier('Sarcomere length', 'um', r.sarcomere_length) }),
                            ('deformation left fiber',{'x': r.deformation_left_time, 'y': Carrier('Left fiber deformation', 'um', r.deformation_left)}),
                            ('deformation right fiber',{'x': r.deformation_right_time, 'y': Carrier('Left right deformation', 'um', r.deformation_right)})] ),
        )
    else:
        raise NotImplementedError('Mode unknown %s' % mode)


    data._sinit__()

    if not ExperimentGeneric.has_record(database, data.experiment_id):
        database.set_read_only(False)
        ExperimentMechanics.store(database, data)

    g.data = data

    return data


if __name__=='__main__':
    # python3 mechanics_reader.py /home/mari/Katsed/stokes/171117-AGATk-Ca-mech/C7-Ca-mech-max-2017.11.17_13.24.31_collected.h5
    import sys
    filename = sys.argv[1]
    data = create_data(None, 'ufreqcasl', filename)
    #print(data)
    #exit()

    r = SarcomereLengthFluorescenceData(filename)
    print(r.events)

    import pylab as plt

    fig = plt.figure()
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)

    ax1.plot(r.sarcomere_length_time, r.sarcomere_length)

    ax2.plot(r.fluorescence_Hamamatsu_C11440_Side_time, r.fluorescence_Hamamatsu_C11440_Side)

    ax3.plot(r.fluorescence_Hamamatsu_C11440_Bottom_time, r.fluorescence_Hamamatsu_C11440_Bottom)

    for t in sorted(list(r.events.keys())):
        print(t)
        s = r.events[t]

        for ax in [ax1, ax2, ax3]:
            ax.axvline(t, color='k')
            ax.text(t, 0, s, color='k')

    plt.show()
