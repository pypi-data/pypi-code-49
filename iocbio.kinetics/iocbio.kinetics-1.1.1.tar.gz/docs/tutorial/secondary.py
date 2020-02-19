from iocbio.kinetics.calc.linreg import AnalyzerLinRegress
from iocbio.kinetics.constants import database_table_experiment, database_table_roi
from iocbio.kinetics.calc.generic import XYData, Stats

from .primary import AnalyzerTutorialPrimary

import numpy as np
from PyQt5.QtCore import pyqtSignal, QObject

### Module flag
IocbioKineticsModule = ['analyzer']

# General signaling class
class AnalyzerTutorialSignals(QObject):
    sigUpdate = pyqtSignal()

class AnalyzerTutorialSecondary(AnalyzerLinRegress):

    database_table = 'tutorial_duration_linregress'
    
    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerTutorialSecondary.database_table) +
                 "(experiment_id text not null PRIMARY KEY, " +
                 "slope double precision not null, intercept double precision, " +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(database_table_experiment) + "(experiment_id) ON DELETE CASCADE)")

    def __init__(self, database, data):
        AnalyzerTutorialSecondary.database_schema(database)        
        # initialization of base class: start with empty data
        AnalyzerLinRegress.__init__(self, [], [])
        # create signals attribute
        self.signals = AnalyzerTutorialSignals()
        # store connection to the database
        self.database = database
        # store experiment_id
        self.experiment_id = data.experiment_id
        # define axes
        self.axisnames = XYData("Beat No", "Duration")
        self.axisunits = XYData("#", "s")
        # fetch data from the database
        self.get_data()
        # fit data
        self.fit()

    def get_data(self):
        c = self.database
        beat = []
        duration = []
        for row in c.query(
"""select b.data_id, b.value + a.value as duration, r.event_name, r.event_value AS beat_nr
from %s b
join %s a on b.data_id=a.data_id
join %s r on b.data_id=r.data_id
where a.type='after 50' and b.type='before 50' and r.experiment_id=:experiment_id""" % (c.table(AnalyzerTutorialPrimary.database_table),
                                                                                       c.table(AnalyzerTutorialPrimary.database_table),
                                                                                       c.table(database_table_roi)),
                experiment_id = self.experiment_id):
            n = row.beat_nr
            d = row.duration
            if n is not None:
                beat.append(n)
                duration.append(d)
        self.experiment = XYData(np.array(beat), np.array(duration))

    def fit(self):
        AnalyzerLinRegress.fit(self)
        if self.intercept is None or self.slope is None:
            return # data are not ready
        c = self.database
        # do we need to update or insert?
        if self.database.has_record(AnalyzerTutorialSecondary.database_table, experiment_id=self.experiment_id):
            c.query("UPDATE " + c.table(AnalyzerTutorialSecondary.database_table) +
                    " SET slope=:slope, intercept=:intercept WHERE experiment_id=:experiment_id",
                    slope=self.slope, intercept=self.intercept, experiment_id=self.experiment_id)
        else:
            c.query("INSERT INTO " + c.table(AnalyzerTutorialSecondary.database_table) +
                    "(experiment_id, slope, intercept) VALUES(:experiment_id,:slope,:intercept)",
                    experiment_id=self.experiment_id, slope=self.slope, intercept=self.intercept)
        self.stats['linreg slope'] = Stats("Slope", "seconds/beat", self.slope)
        self.stats['linreg intercept'] = Stats("Intercept", "seconds", self.intercept)
        self.signals.sigUpdate.emit()

    def update(self):
        self.get_data()
        self.fit()


# Module API
def analyzer(database, data):
    if data.type_generic == "Sarcomere shortening":
        p = AnalyzerTutorialSecondary(database, data)
        # as a key, we define type of ROI used later in secondary analyzers as well
        return None, { 'default': p }, [p]
    return None, None, None
