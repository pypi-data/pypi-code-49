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
import os
import hashlib

from collections import OrderedDict

import iocbio.kinetics.global_vars as g
from iocbio.kinetics.io.data import Data, Carrier

### Required definition for exported module ###
IocbioKineticsModule = ['args', 'reader']

### Implementaiton

def readabs(filename, expno):
    data = []
    with open(filename, 'r') as f:
        for r in f:
            try:
                d = [float(k) for k in r.split()]
                data.append([d[expno*2], d[expno*2+1]])
            except:
                continue
    return data

def args(parser):
    parser.add(name='spectro_column', 
               help='Column in experimental data when its supported. For example, in spectro_cytox protocol')
    return '''Spectrophotometer
-----------------
spectro
spectro_cytox
spectro_trace
'''

def create_data(database, experiment_id=None, args=None):
    import csv, json
    from .experiment_spectro import ExperimentSpectro
    from iocbio.kinetics.handler.experiment_generic import ExperimentGeneric

    filename=getattr(args, "file_name", None)
    fulltxt=None
    protocol = getattr(args, "protocol", None)
    column = getattr(args, "spectro_column", None)

    if experiment_id is not None:
        fulltxt = ExperimentSpectro.get_fulltxt(database, experiment_id)
        if fulltxt is None: return None
        j = json.loads(fulltxt)
        meta = j['meta']
        datatxt = j['data']
        filename = j['filename']
    else:
        if protocol not in ['spectro', 'spectro_cytox', 'spectro_trace'] or filename is None:
            return None

        meta = []
        datatxt = {}

        # create meta file
        if protocol in ['spectro_cytox', 'spectro_trace']:
            if column is None: column='1'
            if protocol == 'spectro_cytox': p = 'Spectro CytOx'
            elif protocol == 'spectro_trace': p = 'Spectro Trace'
            else: raise RuntimeError('Spectro protocol reader internal error: %s' % protocol)
            meta.append([p, '', ''])
            meta.append(['', os.path.basename(filename), column])
        # load meta file
        else:
            with open(filename, 'r') as f:
                for r in csv.reader(f):
                    meta.append(r)

        proto = meta[0][0]
        dirname = os.path.dirname(filename)

        # load files
        for dpoint in meta[1:]:
            datatxt[dpoint[1]] = open(os.path.join(dirname, dpoint[1]), 'r').read()

        fulltxt = json.dumps({'meta': meta, 'data': datatxt, 'filename': filename})

    expid = hashlib.sha256(fulltxt.encode('utf-8')).hexdigest()

    time = []
    absorb = []
    events = {}
    events_timepoint = {}
    protocol = meta[0][0].strip()
    # parse and fill data
    t0 = 0.0
    exp_date=''
    exp_time=''
    for dpoint in meta[1:]:
        t = []
        d = []
        expno = int(dpoint[2])-1
        for l in datatxt[dpoint[1]].splitlines():
            r = l.strip().split()
            try:
                rd = [float(k) for k in r]
                t.append(rd[expno*2] / 60.0 + t0)
                d.append(rd[expno*2+1])
            except:
                try:
                    if r[expno*3]=='Date' and r[expno*3+1]=='Collected':
                        dlist = r[expno*3+2].split('/')
                        exp_date = '.'.join([dlist[2], ("%02d"%int(dlist[0])), ("%02d"%int(dlist[1])) ])
                    elif r[expno*3]=='Time' and r[expno*3+1]=='Collected':
                        exp_time = r[expno*3+2]
                except:
                    continue
        ename = dpoint[0]
        events[ename] = {'name': ename, 'time': [t[0], t[-1]]}
        events_timepoint[ t[0] ] = ename
        time.extend(t)
        absorb.extend(d)
        t0 = t[-1] + 1.0 # add one minute between experiments

    data = Data(expid,
                config={'events': events_timepoint, 'events_slice': events, 'this file': filename, 'experiment title': os.path.basename(filename)},
                type="Thermo Evo 600 " + protocol,
                type_generic = "Spectro " + protocol,
                time = exp_date + " " + exp_time,
                name = filename,
                xname = "Time", xunit = "min",
                xlim = (time[0], time[-1]),
                data = OrderedDict( [
                    ('abs', { "x": np.array(time),
                              "y": Carrier("absorbance", "Abs", absorb) })
                    ] ),
    )

    data.fulltext = fulltxt

    if database is not None and not ExperimentGeneric.has_record(database, data.experiment_id):
        database.read_only = False
        ExperimentSpectro.store(database, data)

    return data


if __name__=='__main__':
    # python3 spectro_reader.py /home/sysbio-data/data/spectrophotometer/2018/180803-AGATw/ATPase-activity.csv
    import sys
    filename = sys.argv[1]
    data = create_data(None, filename)
    print(data.config,'\n',
          data.type,'\n',
          data.type_generic,'\n',
          data.time,'\n',
          data.name,'\n',
          data.x,'\n',
          data.y)
    exit()
