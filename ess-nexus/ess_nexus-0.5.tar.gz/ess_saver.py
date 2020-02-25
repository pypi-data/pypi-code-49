#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#module that creates a saver for ess files
Created on Feb 25 2020
@author: Natalia Milas
"""

import h5py
import datetime


class ess_nexus:
    filename = None
    file = None
    nxentry = None

    def __init__(self, filename=None):
        if filename is not None:
            self.filename = filename
            self.file = h5py.File(filename, 'w')
            # add groups:
            # File entry
            self.nxentry = self.file.create_group('entry')
            self.nxentry.attrs['NX_class'] = 'NXentry'
            self.nxentry.attrs['filename'] = self.filename
            self.nxentry.attrs['hdf5_version'] = 'v1.10'
            self.nxentry.attrs['nexus_version'] = 'v2020.1'
            self.nxentry.attrs['h5py_version'] = '2.10.0'

            # File User
            self.nxentry.create_group('user')
            self.nxentry['user'].attrs['NX_class'] = 'NXuser'

            # File Instruments
            self.nxentry.create_group('instruments')
            self.nxentry['instruments'].attrs['NX_class'] = 'NXinstrument'

    def get_filename(self):
        return self.filename

    def get_file(self):
        return self.file

    def get_entry(self):
        return self.nxentry

    def create_file(self, filename):
        if (self.filename != filename) and (filename is not None):
            self.filename = filename
            self.file = h5py.File(filename, 'w')

            # add groups:
            # File entry
            self.nxentry = self.file.create_group('entry')
            self.nxentry.attrs['NX_class'] = 'NXentry'

            # File User
            self.nxentry.create_group('user')
            self.nxentry['user'].attrs['NX_class'] = 'NXuser'

            # File Instruments
            self.nxentry.create_group('instruments')
            self.nxentry['instruments'].attrs['NX_class'] = 'NXinstrument'

    def file_attributes(self, dic):
        for key in dic.keys():
            self.nxentry.attrs[key] = dic[key]

    def create_file_entry(self, run_cycle='None', entry_identifier='None', title='None', description='None',
                          start_time='None'):
        if self.nxentry is not None:
            self.nxentry.attrs['run_cycle'] = run_cycle
            self.nxentry.attrs['entry_identifier'] = entry_identifier
            self.nxentry.attrs['title'] = title
            self.nxentry.attrs['experiment_description'] = description
            if start_time is 'None':
                self.nxentry.attrs['start_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            else:
                self.nxentry.attrs['start_time'] = start_time

    def create_file_user(self, name='None', role='None', affiliation='None', facility_user_id='None'):
        if self.nxentry is not None:
            self.nxentry['user'].attrs['name'] = name
            self.nxentry['user'].attrs['role'] = role
            self.nxentry['user'].attrs['affiliation'] = affiliation
            self.nxentry['user'].attrs['facility_user_id'] = facility_user_id

    def add_instrument(self, group_name, nxtype, name='None', location='None', description='None', channel='None',
                       epics_channels='None', value='None'):
        instrument = self.nxentry.get(group_name)
        if self.nxentry.get(group_name) is None:
            instrument = self.nxentry['instruments'].create_group(group_name)
        instrument.attrs['NXClass'] = nxtype
        instrument.attrs['name'] = name
        instrument.attrs['location'] = location
        instrument.attrs['description'] = description
        instrument.attrs['channel'] = channel
        instrument.attrs['epics_channels'] = epics_channels
        instrument.attrs['value'] = value

    def add_instrument_attributes(self, instrument_name, dic):
        path = 'instruments/' + instrument_name
        if self.nxentry.get(path) is not None:
            for key in dic:
                self.nxentry[path].attrs[key] = dic[key]

    # functions that are instrument specific (NXradio_frequency,NXbeam_instrumentation,NXmagnet,NXlinac_element,NXlab_instrument)
    def add_radiofrequency(self, group_name, name='None', location='None', description='None', channel='None',
                           epics_channels='None', value='None'):
        instrument = self.nxentry.get(group_name)
        if self.nxentry.get(group_name) is None:
            instrument = self.nxentry['instruments'].create_group(group_name)
        instrument.attrs['NXClass'] = 'NXradio_frequency'
        instrument.attrs['name'] = name
        if name == 'None':
            instrument.attrs['name'] = group_name
        instrument.attrs['location'] = location
        instrument.attrs['description'] = description
        instrument.attrs['channel'] = channel
        instrument.attrs['epics_channels'] = epics_channels
        instrument.attrs['value'] = value

    def add_beam_instrumentation(self, group_name, name='None', location='None', description='None', channel='None',
                                 epics_channels='None', value='None'):
        instrument = self.nxentry.get(group_name)
        if self.nxentry.get(group_name) is None:
            instrument = self.nxentry['instruments'].create_group(group_name)
        instrument.attrs['NXClass'] = 'NXbeam_instrumentation'
        instrument.attrs['name'] = name
        if name == 'None':
            instrument.attrs['name'] = group_name
        instrument.attrs['location'] = location
        instrument.attrs['description'] = description
        instrument.attrs['channel'] = channel
        instrument.attrs['epics_channels'] = epics_channels
        instrument.attrs['value'] = value

    def add_magnet(self, group_name, name='None', location='None', description='None', channel='None',
                   epics_channels='None', value='None'):
        instrument = self.nxentry.get(group_name)
        if self.nxentry.get(group_name) is None:
            instrument = self.nxentry['instruments'].create_group(group_name)
        instrument.attrs['NXClass'] = 'NXmagnet'
        instrument.attrs['name'] = name
        if name == 'None':
            instrument.attrs['name'] = group_name
        instrument.attrs['location'] = location
        instrument.attrs['description'] = description
        instrument.attrs['channel'] = channel
        instrument.attrs['epics_channels'] = epics_channels
        instrument.attrs['value'] = value

    def add_linac_element(self, group_name, name='None', location='None', description='None', channel='None',
                          epics_channels='None', value='None'):
        instrument = self.nxentry.get(group_name)
        if self.nxentry.get(group_name) is None:
            instrument = self.nxentry['instruments'].create_group(group_name)
        instrument.attrs['NXClass'] = 'NXlinac_element'
        instrument.attrs['name'] = name
        if name == 'None':
            instrument.attrs['name'] = group_name
        instrument.attrs['location'] = location
        instrument.attrs['description'] = description
        instrument.attrs['channel'] = channel
        instrument.attrs['epics_channels'] = epics_channels
        instrument.attrs['value'] = value

    def add_lab_instrument(self, group_name, name='None', location='None', description='None', channel='None',
                           epics_channels='None', value='None'):
        instrument = self.nxentry.get(group_name)
        if self.nxentry.get(group_name) is None:
            instrument = self.nxentry['instruments'].create_group(group_name)
        instrument.attrs['NXClass'] = 'NXlab_instrument'
        instrument.attrs['name'] = name
        if name == 'None':
            instrument.attrs['name'] = group_name
        instrument.attrs['location'] = location
        instrument.attrs['description'] = description
        instrument.attrs['channel'] = channel
        instrument.attrs['epics_channels'] = epics_channels
        instrument.attrs['value'] = value

    def add_source(self, source_name, name='None', source_type='Ion Source', probe='proton', power='None',
                   emittance_x='None', emittance_y='None', energy='None', current=None, frequency=None,
                   pulse_width='None', mode='None', notes='None'):
        source = self.nxentry.get(source_name)
        if self.nxentry.get(source_name) is None:
            source = self.nxentry['instruments'].create_group(source_name)
        source.attrs['NXClass'] = 'NXsource'
        source.attrs['name'] = name
        if name == 'None':
            source.attrs['name'] = source_name
        source.attrs['type'] = source_type
        source.attrs['probe'] = probe
        source.attrs['power'] = power
        source.attrs['emittance_x'] = emittance_x
        source.attrs['emittance_y'] = emittance_y
        source.attrs['energy'] = energy
        source.attrs['current'] = current
        source.attrs['frequency'] = frequency
        source.attrs['pulse_width'] = pulse_width
        source.attrs['mode'] = mode
        source.attrs['notes'] = notes

    def add_source_attributes(self, source_name, dic):
        path = 'instruments/' + source_name
        if self.nxentry.get(path) is not None:
            for key in dic:
                self.nxentry[path].attrs[key] = dic[val]

    def create_parameters(self, group_name, dic):
        if self.nxentry.get(group_name) is None:
            parameters = self.nxentry.create_group(group_name)
            parameters.attrs['NXClass'] = 'NXparameters'
        else:
            parameters = self.nxentry.get(group_name)
        for key in dic:
            parameters.attrs[key] = dic[key]

    def create_note(self, group_name, dic):
        if self.nxentry.get(group_name) is None:
            note = self.nxentry.create_group(group_name)
            note.attrs['NXClass'] = 'NXnote'
        else:
            note = self.nxentry.get(group_name)
        for key in dic:
            note.attrs[key] = dic[key]

    def add_dataset(self, group_name, dataset_name, dataset, attibute_dic):
        nxdata = self.nxentry.get(group_name)
        if nxdata is None:
            nxdata = self.nxentry.create_group(group_name)
        data = nxdata.create_dataset(dataset_name, data=dataset)  # , compression='gzip',compression_opts=9)
        data.attrs['NX_class'] = 'NXdata'
        # include attributes
        for key in attibute_dic.keys():
            data.attrs[key] = attibute_dic[key]

    def add_timeseries_dataset(self, group_name, dataset_name, dataset, attibute_dic):
        nxdata = self.nxentry.get(group_name)
        if nxdata is None:
            nxdata = self.nxentry.create_group(group_name)
        print(nxdata)
        data = nxdata.create_dataset(dataset_name, data=dataset)  # , compression='gzip', compression_opts=9)
        data.attrs['NX_class'] = 'NXlog'
        # include attributes
        for key in attibute_dic.keys():
            data.attrs[key] = attibute_dic[key]

    def add_data_attributes(self, group_name, dic):
        if self.nxentry.get(group_name) is not None:
            for key in dic:
                self.nxentry[group_name].attrs[key] = dic[key]

    def close(self):
        if self.file is not None:
            self.nxentry.attrs['end_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.file.close()


