import unittest

from test import * 
from dripy.survey import SurveyData
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Test_test_case_name(unittest.TestCase):

    def setUp(self):
        return

    def test_import_csv_survey(self):
        survey_data = SurveyData(TEST_CSV_SURVEY_DATA)
        self.assertEqual(survey_data.md[0],1084)

    def test_import_excel_survey(self):
        survey_data = SurveyData(TEST_EXCEL_SURVEY_DATA)
        self.assertEqual(survey_data.md[0],1084)

    def test_plot_3d(self):
        survey_data = SurveyData(TEST_CSV_SURVEY_DATA)
        figure = survey_data.plot_3d()
        plt.show()

    def test_plot_3d_on_existing_figure(self):
        survey_data = SurveyData(TEST_CSV_SURVEY_DATA)
        figure = survey_data.plot_3d()

        survey_data_modified = SurveyData(TEST_CSV_SURVEY_DATA_MODIFIED)
        survey_data_modified.plot_3d(figure=figure)

        plt.show()

    def tearDown(self):
        return