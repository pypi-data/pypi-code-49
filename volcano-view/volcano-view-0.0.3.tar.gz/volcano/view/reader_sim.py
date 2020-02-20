import random
import os.path
import json

# locals
from .web_exc import WebException
from .my_tools import to_map, read_json_wx
from .period import ReportPeriod
from .reader_base import BaseReader


_CFG_FILE_NAME = 'sim.json'

SAMPLE_SIM = {
    "qt":[
        {"id": "eap",  "title": "Энергия акт.",    "eu": "кВт*ч",  "cumulative": True},
        {"id": "erp",  "title": "Энергия реакт.",  "eu": "кВар*ч", "cumulative": True}
    ],
    "hr": [
        {"title": "Сайт 1", "id": "site1"},
        {"title": "Сайт 2", "id": "site2"}
    ]
}

class SimulationReader(BaseReader):
    def __init__(self, log):
        self.log = log
        self.hr_ = None
        self.qt_ = None     # ( {id, title, eu, cumulative: bool}, ... )
        
        random.seed ()
        

    def reload_wx(self):
        if not os.path.isfile(_CFG_FILE_NAME):
            log.warning('Creating sample file {}'.format(_CFG_FILE_NAME))
            # исключения не перехватываются - если файла нет и не получается создать, симуляция не будет работать
            with open(_CFG_FILE_NAME, 'w', encoding='utf-8') as f:
                f.write(json.dumps(SAMPLE_SIM, indent=4, ensure_ascii=False))

        data = read_json_wx(_CFG_FILE_NAME)

        self.hr_ = data.get('hr', None)
        if self.hr_ is None:
            raise Exception('"hr" node not found in {}'.format(_CFG_FILE_NAME))
        
        #self.qt_ = tuple( filter(lambda x: x['cumulative'] == True, sim['qt']) )
        self.qt_ = data.get('qt', None)
        if self.qt_ is None:
            raise Exception('"qt" node not found in {}'.format(_CFG_FILE_NAME))
    

        # rval: ( {id, parent_id, title}, ... )
    def read_hr_wx(self, filter = None):
        return self.hr_

        # rval: ( {id, title, eu, cumulative: bool}, ... )
    def read_qt_wx(self, cumulative: bool):
        return self.qt_
            
    def read_data_wx (self, hr_ids, qt_id, all_ivl, sub_ivl, finished):
        # ensure we have hr&qt loaded
        hr_list = self.read_hr_wx ()
        qt_list = self.read_qt_wx (True)

        hr_map = to_map (hr_list, 'id')
        qt_map = to_map (qt_list, 'id')

        hrs = []
        for hr_id in hr_ids:
            hr = hr_map.get ( hr_id, None )
            if hr is None: 
                raise WebException ( 'Hr "{}" does not exist'.format(hr_id) )
            hrs.append ( hr )

        qt = qt_map.get ( qt_id, None )
        if qt is None: 
            raise WebException ( 'Qt "{}" does not exist'.format(qt_id) )

        crp = ReportPeriod (all_ivl, sub_ivl, finished)
        
        series = []
        for hr in hrs:
            serie = {
                 'hr_id': hr['id']
                ,'qt_id': qt['id']
                ,'values': tuple ( map (lambda x: random.randint(0, 1000), crp.readouts()) )
            }
            series.append ( serie )
    
        return {
             'cumulative': True
            ,'start': crp.begin().isoformat()
            ,'readouts': tuple ( map (lambda x: x.isoformat(), crp.readouts()) )
            ,'series': series
        }
