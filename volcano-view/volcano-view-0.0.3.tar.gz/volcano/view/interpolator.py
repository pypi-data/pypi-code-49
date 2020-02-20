from datetime import timedelta

class Interpolator:
    def __init__(self):
        self.prolongate_last_value = True
        self.time_deadband_secs = 1.0

    def try_get_value_on(self, values, dtm):
        prev_elt = None
        next_elt = None

        for elt in values:
            t = elt[1]
            if self.is_close_enough(t, dtm):
                return elt[0]

            if t < dtm:
                prev_elt = elt
            else:
                next_elt = elt
                break
        
        if prev_elt is None and next_elt is None:
            return None
        
        if prev_elt is None and next_elt is not None:   # our timestamp is before first element
            return None

        if prev_elt is not None and next_elt is None:   # our timestamp is after last element
            if self.prolongate_last_value:
                return prev_elt[0]
            else:
                return None

        assert prev_elt and next_elt

        dif_a_ms = dtm - prev_elt[1]
        dif_b_ms = next_elt[1] - dtm

        #if ( difA_ms <= this._MaxValueValidity_Ms || difB_ms <= this._MaxValueValidity_Ms )
        percent = dif_a_ms.total_seconds() / (dif_a_ms.total_seconds() + dif_b_ms.total_seconds())
        return prev_elt[0] + percent * (next_elt[0] - prev_elt[0]);

    # values: [(value, time, anything_else), ...]
    def interpolate_sorted_values(self, values, readouts, first_readout_start):
        
        rs = []
        
        ivl_start_tm = first_readout_start
        ivl_start_value = self.try_get_value_on (values, first_readout_start)

        for ivl_end_tm in readouts:
            ivl_end_val = self.try_get_value_on (values, ivl_end_tm)

            if ivl_start_value is not None and ivl_end_val is not None:
                if ivl_end_val >= ivl_start_value:
                    rs.append ( ivl_end_val - ivl_start_value )
                else:
                    rs.append ( None )

                ivl_start_value = ivl_end_val

            elif ivl_start_value is None and ivl_end_val is None:
                rs.append ( None )
            elif ivl_start_value is None:
                # то есть у нас есть показание счетчика на сегодня, но мы не знаем предыдущих показаний
                # очевидно, что в этом случае потребление за любой предшествующий интервал нам неизвестно.
                rs.append ( None )
                ivl_start_value = ivl_end_val
            else:
                assert ivl_end_val is None
                rs.append ( None )
                ivl_start_value = None

        return rs

    # Checks whether dates 'a' and 'b' differ not more than Deadband
    def is_close_enough(self, d1, d2):
        delta = d2 - d1 if d1 <= d2 else d1 - d2
        return delta.total_seconds () <= self.time_deadband_secs
