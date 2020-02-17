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

from PyQt5.QtCore import QSettings
from attrdict import AttrDict

import os
import importlib.util
import json
import copy
import sys

from .arguments import Parser

class Modules:
    """Interface to modules"""

    def __init__(self):
        self._load_module_settings()
        if not self.load():
            self.select_modules_gui(ask_till_ready=True)

    def _load_module_settings(self):
        settings = QSettings()
        extra = settings.value('modules/folders', defaultValue='')
        self.default_module = AttrDict(dict(path=os.path.abspath( os.path.join(os.path.dirname(os.path.dirname(__file__)), 'modules') ),
                                            enabled = bool(settings.value('modules/enable_default', defaultValue=0, type=int)),
                                            nodelete = True))
        mtr = settings.value('modules/extra', defaultValue='[]', type=str)
        self.modules = [copy.deepcopy(self.default_module)]
        for m in json.loads(mtr):
            i = AttrDict(dict(path = m['path'],
                              enabled = bool(m.get('enabled', True)),
                              nodelete = bool(m.get('nodelete', True))))
            self.modules.append(i)

    def set_modules(self, modules):
        default_enabled = self.default_module.enabled
        modules = [AttrDict(i) for i in modules]
        extras = []
        for i in modules:
            if i.path == self.default_module.path:
                default_enabled = i.enabled
            else:
                extras.append(i)
        settings = QSettings()
        settings.setValue('modules/enable_default', int(default_enabled))
        settings.setValue('modules/extra', json.dumps(extras))
        self._load_module_settings()
        return self.load()

    def select_modules_gui(self, ask_till_ready=False):
        from PyQt5.QtWidgets import QDialog
        from ..gui.module_selector import ChecklistDialog
        while True:
            form = ChecklistDialog(self.modules)
            if form.exec_() == QDialog.Accepted:
                ask_till_ready = not self.set_modules(form.moduledict)
            if not ask_till_ready:
                break

    def _load(self, md):
        """Loading of all modules"""

        modprefix = 'iocbio.kinetics.custom_module.'
        imported = []
        for (dirpath, dirnames, filenames) in os.walk(md):
            filenames.sort()
            for filename in filenames:
                if filename.endswith('.py'):
                    fname = os.path.join(dirpath, filename)
                    dname = os.path.abspath(dirpath)
                    mname = 'iocbio.kinetics.custom_module' + dname
                    if filename != '__init__.py':
                        mname += '.' + filename[:-3]
                    mname = mname.replace(os.sep, '.')
                    spec = importlib.util.spec_from_file_location(mname, fname, submodule_search_locations=[os.path.abspath(dirpath)])
                    mod = importlib.util.module_from_spec(spec)
                    sys.modules[spec.name] = mod
                    imported.append(mod)

        for mod in imported:
            print('Loading', mod.__file__)
            mod.__loader__.exec_module(mod)

            apis = getattr(mod, 'IocbioKineticsModule', [])
            if 'analyzer' in apis: self._analyzers.append(mod)
            if 'args' in apis: self._args.append(mod)
            if 'database_info' in apis: self._db_info.append(mod)
            if 'database_schema' in apis: self._db_ini.append(mod)
            if 'database_processor' in apis: self._db_proc.append(mod)
            if 'reader' in apis: self._readers.append(mod)

    def load(self):
        """(Re-)Load modules"""

        self._args = []
        self._db_info = []
        self._db_ini = []
        self._db_proc = []
        self._readers = []
        self._analyzers = []

        moddirs = []
        for m in self.modules:
            if m['enabled']:
                moddirs.append(m['path'])

        print('\nModules:')
        try:
            for md in moddirs:
                self._load(md)
        except:
            import traceback
            from PyQt5.QtWidgets import QMessageBox
            txt = "Error occured while importing modules:\n\n" + \
                traceback.format_exc() + "\n\nPlease change modules selection or fix the module(s)"
            err = QMessageBox(QMessageBox.Critical,
                              "IOCBIO Kinetics: Failed to load module(s)",
                              txt)
            print(txt)
            err.exec_()
            return False

        print()
        print('Command line options:')
        for m in self._args:
            print(m.__file__)

        print()
        print('Database initialization:')
        for m in self._db_ini:
            print(m.__file__)

        print()
        print('Database record information:')
        for m in self._db_info:
            print(m.__file__)

        print()
        print('Database processors:')
        for m in self._db_proc:
            print(m.__file__)

        print()
        print('Data readers:')
        for m in self._readers:
            print(m.__file__)

        print()
        print('Analyzers:')
        for m in self._analyzers:
            print(m.__file__)

        print('\n')
        return True

    def analyzers(self, database, data):
        Analyzer = {}
        overall_plot = {}
        overall_stats = []
        for m in self._analyzers:
            A, p, s = m.analyzer(database, data)
            if A is not None and A:
                print('Analyzer ROI', m.__file__, ' / '.join(A.keys()))
                Analyzer.update(A)
            if p is not None and p:
                print('Analyzer overall plot', m.__file__, ' / '.join(p.keys()))
                overall_plot.update(p)
            if s is not None and s:
                print('Analyzer overall stats', m.__file__)
                overall_stats.extend(s)
        return Analyzer, overall_plot, overall_stats

    def _parser(self, protocols):
        p = Parser()
        for m in self._args:
            s = m.args(p)
            if s is not None:
                protocols = protocols + s + '\n'
        return p, protocols

    def args(self, parser, protocols):
        p, protocols = self._parser(protocols)
        p.fill_argparser(parser)
        return protocols

    def gui(self):
        protocols = 'Experiment protocols:\n'
        p, protocols = self._parser(protocols)
        g = p.fill_gui(protocols)
        return p, g

    def create_data(self, database, experiment_id=None, args=None):
        for m in self._readers:
            data = m.create_data(database=database, experiment_id=experiment_id, args=args)
            if data is not None:
                print('Data loaded with', m.__file__)
                if experiment_id is not None and data.experiment_id != experiment_id:
                    print('\n*** Error with the data or data loader ***')
                    print('There is inconsistency in requested and loaded experimental IDs')
                    print('Requested experiment_id:', experiment_id)
                    print('Data experiment_id:', data.experiment_id)
                    print()
                    raise RuntimeError('Experiment IDs do not match')
                return data
        return None

    def database_info(self, database):
        if len(self._db_info) > 0:
            sql = "COALESCE("
            sql += ",".join([ "(" + m.database_info(database) + ")" for m in self._db_info])
            sql += ", 'none')"
        else:
            sql = "'none'"
        return sql

    def database_process(self, database, data, args):
        if args is not None:
            for m in self._db_proc:
                m.database_process(database, data, args)

    def database_schema(self, database):
        for m in self._db_ini:
            m.database_schema(database)
