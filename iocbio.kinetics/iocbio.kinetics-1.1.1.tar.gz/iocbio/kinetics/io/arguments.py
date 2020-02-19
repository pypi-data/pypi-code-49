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
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit

from attrdict import AttrDict

from ..gui.custom_widgets import SmallLabel

# Classes related to specifying program arguments

class Option:
    """Realization of program option"""

    def __init__(self, name=None, help=None):
        self.name = name
        self.help = help

    def fill_argparser(self, parser):
        parser.add_argument('--' + self.name.replace('_', '-'),
                            type=str, default = None,
                            help=self.help)

    def fill_gui(self, layout):
        self._gui = QLineEdit()
        layout.addRow(self.name.replace('_', ' ').title(), self._gui)
        layout.addRow(SmallLabel(self.help.replace('\n', '<br>\n')))

    def gui_value(self):
        return self._gui.text()

        
class Parser:
    """Keeps definition of program options"""
    
    def __init__(self):
        self.options = []

    def add(self, name, help=None):
        self.options.append( Option(name=name, help=help) )

    def fill_argparser(self, parser):
        for o in self.options:
            o.fill_argparser(parser)

    def fill_gui(self, protocols):
        self.options.insert(0, Option(name='protocol', help=protocols))
        form = QFormLayout()
        for o in self.options:
            o.fill_gui(form)
        wid = QWidget()
        wid.setLayout(form)
        return wid
        
    def get_options_gui(self):
        response = dict()
        for o in self.options:
            v = o.gui_value()
            if v:
                response[o.name] = v
            else:
                response[o.name] = None
        return AttrDict(response)
