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
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QListWidget, QVBoxLayout, QLabel, QListWidgetItem
from PyQt5.QtGui import QMenu


class RoiListView(QWidget):
    sigActiveRoi = pyqtSignal(str)
    sigRoiRemove = pyqtSignal(str)

    def __init__(self):
        QWidget.__init__(self)

        self.roi_list = None
        self.active_roi = None

        self.list_widget = QListWidget()
        self.list_widget.uniformItemSizes()
        label = QLabel('ROI list:')
        self.list_widget.setMaximumWidth(label.sizeHint().width())
        self.list_widget.setContextMenuPolicy(Qt.CustomContextMenu)

        # {Event bindings
        self.list_widget.currentRowChanged.connect(self.update_selected)
        self.list_widget.customContextMenuRequested.connect(self.open_context_menu)
        # }

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.list_widget)
        self.setLayout(layout)

    def open_context_menu(self, position):
        menu = QMenu()
        menu.addAction('Remove', self.remove_item)
        menu.addAction('Remove all', self.remove_all_items)
        menu.exec_(self.list_widget.viewport().mapToGlobal(position))

    def remove_item(self):
        row = self.list_widget.currentRow()
        if row < 0 or row >= len(self.roi_list):
            return

        self.active_roi = None
        self.sigRoiRemove.emit(self.roi_list[row])

    def remove_all_items(self):
        print('Not implemented')
        return
        for row in range(self.list_widget.count())[::-1]:
            self.sigRoiRemove.emit(self.roi_list[row])
        self.active_roi = None

    def set_list(self, sorted_roi_list):
        self.list_widget.clear()
        self.roi_list = sorted_roi_list
        for i, roi_id in enumerate(self.roi_list):
            item = QListWidgetItem('%i' % (i+1,))
            item.roi_id = roi_id
            self.list_widget.addItem(item)

    def update_selected(self, i):
        if i < 0: return

        rid = self.roi_list[i]
        if self.active_roi == rid and self.active_roi is None:
            return
        self.sigActiveRoi.emit(rid)

    def set_active(self, roi_id):
        if roi_id in self.roi_list:
            self.active_roi = roi_id
            self.list_widget.setCurrentRow(self.roi_list.index(roi_id))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete and len(self.roi_list) > 0:
            self.remove_item()
