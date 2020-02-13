import pandas as pd
import unittest
from datetime import datetime

from features_factory.input_features import DateTimeInputFeature
from features_factory.two_component_features import DurationFeature


class TestDurationFeature(unittest.TestCase):

    def test_generate(self):
        start = DateTimeInputFeature('start')
        end = DateTimeInputFeature('end')
        duration_h = DurationFeature('duration_h', start_time_feat=start, end_time_feat=end, units='hours')
        duration_m = DurationFeature('duration_m', start_time_feat=start, end_time_feat=end, units='minutes')
        duration_s = DurationFeature('duration_s', start_time_feat=start, end_time_feat=end, units='seconds')

        df = pd.DataFrame({start.name(): [datetime(2018, 1, 18, 8, 30)] * 2,
                           end.name(): [datetime(2018, 1, 18, 15), datetime(2018, 1, 19, 15)]})

        df = duration_h.insert_into(duration_m.insert_into(duration_s.insert_into(df)))

        self.assertEqual(6.5, df.at[0, duration_h.name()])
        self.assertEqual(390, df.at[0, duration_m.name()])
        self.assertEqual(23400, df.at[0, duration_s.name()])

        self.assertEqual(30.5, df.at[1, duration_h.name()])
        self.assertEqual(1830, df.at[1, duration_m.name()])
        self.assertEqual(109800, df.at[1, duration_s.name()])
