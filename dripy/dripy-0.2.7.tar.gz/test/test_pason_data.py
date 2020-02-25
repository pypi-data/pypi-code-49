import unittest
from numpy import argmax
from test import *
from dripy.dripy import PasonData

class Test_PasonData(unittest.TestCase):

    def setUp(self):
        self.pason_data = PasonData(TEST_PASON_DATA)        
    
    def test_pason_torque(self):
        """Tests that the torque attribute returns expected values.  This test is important becauase the pason data set has two torque columns and the PasonData class needs to pick the one that comes first in the PasonData.STANDARD_VARIABLES['torque'] list.        
        
        """
        torque = self.pason_data.torque[299:310]
        self.assertListEqual([round(t,2) for t in torque], [round(t,2) for t in TEST_EXPECTED_PASON_TORQUE])

    def test_pason_time(self):
        """Tests that the time attribute returns expected values.
        
        """
        time = self.pason_data.time[0:10]
        self.assertListEqual(time, TEST_EXPECTED_PASON_TIME)
    
    def test_pason_rpm_attr(self):
        """Tests that the rpm attribute returns expected values.
        
        """
        rpm = self.pason_data.rpm[2000:2010]
        self.assertListEqual(rpm, TEST_EXPECTED_PASON_RPM)
    
    def test_pason_rpm_data(self):
        """Tests that the 'rpm' entry in the `data` dictionary returns expected values.
        
        """
        rpm = self.pason_data.data['rpm'].values[2000:2010]
        self.assertListEqual(list(rpm), TEST_EXPECTED_PASON_RPM)
    
    def test_pason_rpm_data_csv_name(self):
        """Tests that the 'rotary_rpm' entry in the `data` returns expected values.
        
        """
        rpm = self.pason_data.data['rotary_rpm'].values[2000:2010]
        self.assertListEqual(list(rpm), TEST_EXPECTED_PASON_RPM)
        
    def test_get_gpm_setpoints(self):
        """Tests the `PasonData.get_setpoints` method.
        
        """
        set_points = self.pason_data.get_setpoints('gpm', show_plot=False)    
        self.assertListEqual(set_points, TEST_EXPECTED_GPM_SETPOINTS)
        
    def test_get_rpm_setpoints(self):
        """Tests the `PasonData.get_setpoints` method.
        
        """
        set_points = self.pason_data.get_setpoints('rpm', show_plot=False)        
        self.assertListEqual(set_points, TEST_EXPECTED_RPM_SETPOINTS)

    def test_get_setpoints_bad_input(self):
        """Tests the `PasonData.get_setpoints` method.
        
        """
        error_msg = None        
        try:
            _set_points = self.pason_data.get_setpoints('xxx', show_plot=False)       
        except ValueError as err:            
            error_msg = err.args[0]        
        self.assertEqual(error_msg,'signal_type must be a key in self.data')       

    def test_get_time_index(self):
        """Tests getting the index of a particular time value in `pason_data.data['time']`.
        
        """
        t_min = 100
        i_min = argmax(self.pason_data.data.index>=t_min)
        expected_i_min = 100

        self.assertEqual(i_min, expected_i_min)

    def tearDown(self):
        return
    
if __name__ == '__main__':
    unittest.main()
