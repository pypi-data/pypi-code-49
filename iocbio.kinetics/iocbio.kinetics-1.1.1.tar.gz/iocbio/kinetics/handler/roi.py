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
from PyQt5.QtCore import pyqtSignal, QObject
from iocbio.kinetics.constants import database_table_roi, database_table_experiment


class ROIHandler(QObject):
    """Handler for regions of interests

    Access for records defining region of interest in the
    experiment. This class is responsible for keeping generic
    information regarding region of interests, such as their location
    and event names or values. For that, a dedicated table is created
    by the class. This class is used internally and access to the table
    data by the modules is expected to be done via SQL.

    Database table name is defined by
    :class:`..constants.database_table_roi` and has the following
    columns:

    - experiment_id: text, reference to experiments table record
    - data_id: text, primary key
    - type: text
    - x0: double, start of the region of interest
    - x1: double, end of the region of interest
    - event_name: text, name of the event, if any
    - event_value: double, value of the event, if any

    Parameters
    ----------
    database : iocbio.kinetics.io.db.DatabaseInterface
      Database access
    data : iocbio.kinetics.io.data.Data
      Data descriptor
    Analyzer : dict
      Primary data analyzer as a dictionary. The primary data analyzer(s) should be given by class name,
      not object.

    Attributes
    ----------
    database : iocbio.kinetics.io.db.DatabaseInterface
      Database access
    data : iocbio.kinetics.io.data.Data
      Data descriptor
    experiment_id : str
      Experiment ID
    self.rois : dict
      Regions of interest
    current_roi : str
      Selected ROI
    Analyzer : dict
      Primary analyzer(s)
    """

    sigRois = pyqtSignal(dict, list)
    sigActiveRoi = pyqtSignal(str)
    sigActiveRoiAnalyser = pyqtSignal(object)
    sigActiveRoiType = pyqtSignal(str)
    sigUpdate = pyqtSignal() # emitted when some stats has changed by analyzers

    database_table = database_table_roi

    @staticmethod
    def database_schema(db):
        """Create ROI database table if it is missing"""
        
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(ROIHandler.database_table) +
                 "(experiment_id text not null, data_id text PRIMARY KEY, type text not null, " +
                 "x0 double precision, x1 double precision, event_name text, event_value double precision, " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE" +
                 ")")

    def __init__(self, database, data, Analyzer):
        QObject.__init__(self)

        self.database = database
        self.data = data
        self.experiment_id = data.experiment_id
        self.rois = {}
        self.current_roi = None
        self.Analyzer = Analyzer

        if self.Analyzer is not None and self.Analyzer:
            
            if self.database is not None:
                c = self.database
                for row in c.query("SELECT data_id, type, x0, x1, event_name, event_value FROM " +
                                   self.database.table(ROIHandler.database_table) +
                                   " WHERE experiment_id=:experiment_id", experiment_id=self.experiment_id):
                    rdata = self.data.slice(row.x0,row.x1,data_id=row.data_id,
                                            event_name=row.event_name,event_value=row.event_value)
                    analyzer = self.Analyzer[row.type](self.database, rdata)
                    self.rois[row.data_id] = { 'type': row.type,
                                               'data': rdata,
                                               'analyzer': analyzer }
                    analyzer.signals.sigUpdate.connect(self.sigUpdate)

            if not bool(self.rois):
                for t in Analyzer:
                    sliced_data = Analyzer[t].auto_slicer(data)
                    for k in sliced_data:
                        self.add(rdata = k, roi_type = t)

    def trigger_updates(self):
        srt = self.sorted_roi_list
        self.sigRois.emit(self.rois, srt)
        if bool(self.rois and len(srt) > 0):
            self.set_active(srt[0])
        self.sigUpdate.emit()

    def add(self, roi_type, rng=None, rdata=None):
        if rng is None and rdata is None: return

        if rng is not None:
            x0, x1 = rng
            rdata = self.Analyzer[roi_type].slice(self.data, x0, x1)
        else:
            x0, x1 = rdata.xlim()

        # record in the database first
        if self.database is not None:
            c = self.database
            c.query("INSERT INTO " + self.database.table(ROIHandler.database_table) +
                    "(experiment_id, data_id, type, x0, x1, event_name, event_value) " +
                    "VALUES (:experiment_id, :data_id, :type, :x0, :x1, :event_name, :event_value)",
                    experiment_id=self.experiment_id, data_id=rdata.data_id, type=roi_type, x0=x0, x1=x1,
                    event_name=rdata.event_name, event_value=rdata.event_value)

        analyzer = self.Analyzer[roi_type](self.database, rdata)
        self.rois[rdata.data_id] = { 'type': roi_type,
                                     'data': rdata,
                                     'analyzer': analyzer }
        analyzer.signals.sigUpdate.connect(self.sigUpdate)

        self.sigRois.emit(self.rois, self.sorted_roi_list)
        self.set_active(rdata.data_id)

    def remove(self, data_id):
        if data_id not in self.rois: return
        self.rois[data_id]['analyzer'].remove()
        del self.rois[data_id]
        if self.database is not None:
            c = self.database
            c.query("DELETE FROM " + self.database.table(ROIHandler.database_table)  +
                    " WHERE experiment_id=:experiment_id AND data_id=:data_id",
                    experiment_id=self.experiment_id, data_id=data_id)
        self.sigRois.emit(self.rois, self.sorted_roi_list)
        self.set_active(None)

    def update_range(self, roi_id, coords):
        if roi_id not in self.rois: return
        roi = self.rois[roi_id]
        x0, x1 = coords

        data = self.data.slice(x0, x1,
                               data_id=roi['data'].data_id,
                               event_name=roi['data'].event_name,
                               event_value=roi['data'].event_value)
        self.rois[roi_id]['data'] = data
        self.rois[roi_id]['analyzer'].update_data(data)

        c = self.database
        c.query("UPDATE " + self.database.table(ROIHandler.database_table) +
                " SET x0=:x0, x1=:x1 WHERE experiment_id=:experiment_id AND data_id=:data_id",
                x0=x0, x1=x1, experiment_id=self.experiment_id, data_id=data.data_id)

    def update_event(self, roi_id, event_name):
        if roi_id not in self.rois: return
        self.rois[roi_id]['analyzer'].update_event(event_name)
        self.rois[roi_id]['data'] = self.rois[roi_id]['analyzer'].data

        c = self.database
        data = self.rois[roi_id]['analyzer'].data
        c.query("UPDATE " + self.database.table(ROIHandler.database_table) +
                " SET event_name=:event_name, event_value=:event_value WHERE experiment_id=:experiment_id AND data_id=:data_id",
                event_name=data.event_name, event_value=data.event_value,
                experiment_id=self.experiment_id, data_id=data.data_id)
        self.sigUpdate.emit()

    def set_active(self, roi_id):
        if self.current_roi == roi_id or (roi_id not in self.rois and roi_id is not None):
            return

        self.current_roi = roi_id
        self.sigActiveRoi.emit(roi_id)

        if roi_id is not None:
            self.sigActiveRoiAnalyser.emit(self.rois[self.current_roi]['analyzer'])
            self.sigActiveRoiType.emit(self.rois[self.current_roi]['type'])
        else:
            self.sigActiveRoiAnalyser.emit(None)
            self.sigActiveRoiType.emit(None)

    def get_roi_data(self, roi_id):
        return self.rois[roi_id]['data']

    @property
    def sorted_roi_list(self):
        if self.database is None:
            return []
        else:
            c = self.database
            l = c.query("SELECT data_id FROM " +
                         self.database.table(ROIHandler.database_table) +
                         " WHERE experiment_id=:experiment_id ORDER BY type,x0,x1 ASC",
                         experiment_id=self.experiment_id )
            return [el.data_id for el in l]
