from iocbio.kinetics.calc.bump import AnalyzerBumpDatabase
from iocbio.kinetics.calc.generic import XYData

### Module flag
IocbioKineticsModule = ['analyzer', 'database_schema']


class AnalyzerTutorialPrimary(AnalyzerBumpDatabase):

    database_table = "tutorial_primary"

    @staticmethod
    def database_schema(db):
        AnalyzerBumpDatabase.database_schema(db, AnalyzerTutorialPrimary.database_table, peak=False)
    
    def __init__(self, database, data):
        # initialization of base class
        AnalyzerBumpDatabase.__init__(self, database,
                                      # name of the database table used to store data
                                      AnalyzerTutorialPrimary.database_table,
                                      # data and corresponding x- and y- arguments
                                      data, data.x('sarcomere_length'), data.y('sarcomere_length').data,
                                      # we look at shortening, not increase. For bump, it means that peak is False
                                      peak=False,
                                      # units of the value
                                      valunit=data.y('sarcomere_length').unit)
        self.axisnames = XYData(data.xname, data.y('sarcomere_length').name)
        self.axisunits = XYData(data.xunit, data.y('sarcomere_length').unit)
        # when searching for time to peak, we need reference value for it
        self.update_reference_time(data)
        # fit data
        self.fit()

    def update_reference_time(self, data):
        x0, x1 = data.xlim()
        events = data.config['events']
        # default reference
        self.t_reference = 0
        for et, ev in events.items():
            if et > x0 and et < x1:
                # the first reference within the region of interest
                self.t_reference = et
                break

    def fit(self):
        AnalyzerBumpDatabase.fit(self, n=3, points_per_node=4, max_nodes=25)
        
    def update_data(self, data):
        # called when user is moving regions of interest
        self.update_reference_time(data)
        # update data in base class
        AnalyzerBumpDatabase.update_data(self, data.x('sarcomere_length'), data.y('sarcomere_length').data)
        # fit the data
        self.fit()

    def update_event(self, event_name):
        self.data.event_name = event_name
        self.data.event_value = AnalyzerTutorialPrimary.eventvalue(event_name)

    @staticmethod
    def eventvalue(event_name):
        try:
            # events are in form "beat Number"
            evalue = float(event_name.split()[1])
        except:
            evalue = None
        return evalue
        
    @staticmethod
    def slice(data, x0, x1):
        # create a slice of data
        sdata = data.slice(x0, x1)
        # determine event corresponding to the data if any
        events = data.config['events']
        # default, if we don't find any
        sdata.event_name = ""
        sdata.event_value = None
        for et, ev in events.items():
            if et > x0 and et < x1:
                # the first reference within the region of interest
                sdata.event_name = ev
                sdata.event_value = AnalyzerTutorialPrimary.eventvalue(ev)
                break
        return sdata

    @staticmethod
    def auto_slicer(data):
        events = data.config['events']
        # no events in data, nothing to make slices with
        ekeys = list(events.keys())
        ekeys.sort()
        if len(ekeys) == 0: return []

        sliced_data = []
        width = 0.9
        offset = 0.05
        for et in ekeys:
            sdata = AnalyzerTutorialPrimary.slice(data, et-offset, et-offset+width)
            sliced_data.append(sdata)
        return sliced_data


# Module API
def analyzer(database, data):
    Analyzer = {}
    if data.type_generic == "Sarcomere shortening":
        # as a key, we define type of ROI used later in secondary analyzers as well
        Analyzer['default'] = AnalyzerTutorialPrimary
    # only primary analyzer is returned this time
    return Analyzer, None, None

# definition of database_schema function
def database_schema(db):
    AnalyzerTutorialPrimary.database_schema(db)
