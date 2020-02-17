#!/usr/bin/env python

"""
Testing recurrence plot implementations according to the fixed radius neighbourhood.
"""

import numpy as np
import unittest

from pyrqa.neighbourhood import FixedRadius, \
    RadiusCorridor
from pyrqa.selector import SingleSelector
from pyrqa.time_series import TimeSeries
from pyrqa.variants.test_corpus import TestCorpusClassic, TestCorpusCross
from pyrqa.variants.rp.radius.baseline import Baseline
from pyrqa.variants.rp.radius.execution_engine import ExecutionEngine

from pyrqa.variants.rp.radius.column_materialisation_byte import \
    ColumnMaterialisationByte
from pyrqa.variants.rp.radius.row_materialisation_byte import \
    RowMaterialisationByte

VARIANTS = (ColumnMaterialisationByte,
            RowMaterialisationByte)

__author__ = "Tobias Rawald"
__copyright__ = "Copyright 2015, 2018, 2019, 2020 The PyRQA project"
__credits__ = ["Tobias Rawald",
               "Mike Sips"]
__license__ = "Apache-2.0"
__maintainer__ = "Tobias Rawald"
__email__ = "pyrqa@gmx.net"
__status__ = "Development"


class TestRPFixedRadiusClassic(TestCorpusClassic):
    """
    Tests for RP, Fixed Radius, Classic.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up test.

        :cvar time_series: Random time series consisting either of a random number of up to 1024 floating point values.
        :cvar neighbourhood: Neighbourhood condition.
        """

        cls.time_series_length = pow(2, 10)
        cls.time_series = TimeSeries(np.random.rand(cls.time_series_length))

        cls.neighbourhood = FixedRadius(np.random.uniform(.1, 1.))

    def perform_recurrence_analysis_computations(self,
                                                 settings,
                                                 opencl=None,
                                                 verbose=False,
                                                 edge_length=None,
                                                 selector=SingleSelector(),
                                                 variants_kwargs=None,
                                                 all_variants=False):
        if opencl:
            opencl.reset()

        if not edge_length:
            edge_length = settings.max_number_of_vectors

        baseline = Baseline(settings,
                            verbose=verbose)

        result_baseline = baseline.run()

        if all_variants:
            execution_engine = ExecutionEngine(settings,
                                               opencl=opencl,
                                               verbose=False,
                                               edge_length=edge_length,
                                               selector=selector,
                                               variants=VARIANTS,
                                               variants_kwargs=variants_kwargs)

            result = execution_engine.run()

            self.compare_recurrence_plot_results(result_baseline,
                                                 result)
        else:
            for variant in VARIANTS:
                execution_engine = ExecutionEngine(settings,
                                                   opencl=opencl,
                                                   verbose=False,
                                                   edge_length=edge_length,
                                                   selector=selector,
                                                   variants=(variant,),
                                                   variants_kwargs=variants_kwargs)

                result = execution_engine.run()

                self.compare_recurrence_plot_results(result_baseline,
                                                     result,
                                                     variant=variant)


class TestRPRadiusCorridorClassic(TestRPFixedRadiusClassic):
    """
    Tests for RP, Radius Corridor.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up test.

        :cvar time_series: Random time series consisting either of a random number of up to 1024 floating point values.
        :cvar neighbourhood: Neighbourhood condition.
        """

        cls.time_series_length = pow(2, 10)
        cls.time_series = TimeSeries(np.random.rand(cls.time_series_length))

        inner_radius = np.random.uniform(.1, 1.)
        outer_radius = np.random.uniform(inner_radius, 1.)

        cls.neighbourhood = RadiusCorridor(inner_radius=inner_radius,
                                           outer_radius=outer_radius)


if __name__ == "__main__":
    unittest.main()


class TestRPFixedRadiusCross(TestCorpusCross):
    """
    Tests for RP, Fixed Radius, Cross.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up test.

        :cvar time_series_x: Random time series consisting either of a random number of up to 1024 floating point values.
        :cvar time_series_y: Random time series consisting either of a random number of up to 1024 floating point values.
        :cvar neighbourhood: Neighbourhood condition.
        """

        cls.data_x = np.random.rand(np.random.randint(pow(2, 9),
                                                      pow(2, 10)))
        cls.time_delay_x = np.random.randint(low=1,
                                             high=10)
        cls.time_series_x = TimeSeries(data=cls.data_x,
                                       time_delay=cls.time_delay_x)

        cls.data_y = np.random.rand(np.random.randint(pow(2, 9),
                                                      pow(2, 10)))
        cls.time_delay_y = np.random.randint(low=1,
                                             high=10)
        cls.time_series_y = TimeSeries(data=cls.data_y,
                                       time_delay=cls.time_delay_y)

        cls.time_series = (cls.time_series_x,
                           cls.time_series_y)

        cls.neighbourhood = FixedRadius(np.random.uniform(.1, 1.))

    def perform_recurrence_analysis_computations(self,
                                                 settings,
                                                 opencl=None,
                                                 verbose=False,
                                                 edge_length=None,
                                                 selector=SingleSelector(),
                                                 variants_kwargs=None,
                                                 all_variants=False):
        if opencl:
            opencl.reset()

        if not edge_length:
            edge_length = settings.max_number_of_vectors

        baseline = Baseline(settings,
                            verbose=verbose)

        result_baseline = baseline.run()

        if all_variants:
            execution_engine = ExecutionEngine(settings,
                                               opencl=opencl,
                                               verbose=False,
                                               edge_length=edge_length,
                                               selector=selector,
                                               variants=VARIANTS,
                                               variants_kwargs=variants_kwargs)

            result = execution_engine.run()

            self.compare_recurrence_plot_results(result_baseline,
                                                 result)
        else:
            for variant in VARIANTS:
                execution_engine = ExecutionEngine(settings,
                                                   opencl=opencl,
                                                   verbose=False,
                                                   edge_length=edge_length,
                                                   selector=selector,
                                                   variants=(variant,),
                                                   variants_kwargs=variants_kwargs)

                result = execution_engine.run()

                self.compare_recurrence_plot_results(result_baseline,
                                                     result,
                                                     variant=variant)


class TestRPRadiusCorridorCross(TestRPFixedRadiusCross):
    """
    Tests for RP, Radius Corridor, Cross.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up test.

        :cvar time_series_x: Random time series consisting either of a random number of up to 1024 floating point values.
        :cvar time_series_y: Random time series consisting either of a random number of up to 1024 floating point values.
        :cvar neighbourhood: Neighbourhood condition.
        """

        cls.data_x = np.random.rand(np.random.randint(pow(2, 9),
                                                      pow(2, 10)))
        cls.time_series_x = TimeSeries(data=cls.data_x)

        cls.data_y = np.random.rand(np.random.randint(pow(2, 9),
                                                      pow(2, 10)))
        cls.time_series_y = TimeSeries(data=cls.data_y)

        cls.time_series = (cls.time_series_x,
                           cls.time_series_y)

        inner_radius = np.random.uniform(.1, 1.)
        outer_radius = np.random.uniform(inner_radius, 1.)

        cls.neighbourhood = RadiusCorridor(inner_radius=inner_radius,
                                           outer_radius=outer_radius)