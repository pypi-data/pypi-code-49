
class BaseReader:
    def reload_wx(self):
        raise NotImplementedError()
    
        # rval: ( {id, parent_id, title}, ... )
    def read_hr_wx(self, filter = None):
        raise NotImplementedError()

        # rval: ( {id, title, eu, cumulative: bool}, ... )
    def read_qt_wx(self, cumulative: bool):
        raise NotImplementedError()
            
    '''
        rval:{
            start: 'iso-formatted date of beginning of first record'
            readouts: ['', ...] -- list of iso timestamps of ENDs of records
            series:[
                {hr_id, qt_id, values:[1,2,3]}, ...
            ]
        }
    '''
    def read_data_wx (self, hr_ids, qt_id, all_ivl, sub_ivl, finished):
        raise NotImplementedError()
