import datetime

class ReportPeriod:
    def __init__(self, all_ivl, sub_ivl, only_finished: bool):
        assert all_ivl
        assert sub_ivl
        assert isinstance(only_finished, bool), only_finished

        setpt = datetime.datetime.now()
        last_readout_e = all_ivl.try_align (setpt, 'back' if only_finished else 'forward')
        if not last_readout_e:
            last_readout_e = all_ivl.normalized().try_align (setpt, 'back' if only_finished else 'forward')
            assert last_readout_e, all_ivl

        self.first_readout_start_ = all_ivl.subtract_from ( last_readout_e )
        self.readout_ends_ = []
        
        cr_start = self.first_readout_start_
        while cr_start < last_readout_e:
            cr_end = sub_ivl.add_to ( cr_start )
            
            self.readout_ends_.append ( cr_end )

            cr_start = cr_end

    def begin(self):    
        return self.first_readout_start_
    
    def end(self):      
        return self.readout_ends_[len(self.readout_ends_)-1]
    
    def readouts(self): 
        return self.readout_ends_

    def __str__(self):
        return '{} .. {}'.format(self.begin(), self.end())
