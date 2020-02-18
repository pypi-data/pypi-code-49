import pandas as pd
import numpy as np
import unittest

from automl.client.core.common.constants import TimeSeries, TimeSeriesInternal
from automl.client.core.common.exceptions import DataException, ClientException
from automl.client.core.common.time_series_data_frame import TimeSeriesDataFrame
from automl.client.core.common.forecasting_verify import Messages
from automl.client.core.common.forecasting_exception import NotTimeSeriesDataFrameException
from azureml.automl.runtime.featurizer.transformer.timeseries.short_grain_dropper import ShortGrainDropper
from pandas.util.testing import assert_frame_equal
from automl.client.core.common import utilities
from Cython.Compiler.Tests import TestGrammar


class TestGrainDropper(unittest.TestCase):
    """Test if Grain dropper works as expected."""
    GRAIN = 'gr'
    DATE = 'date'
    TGT = 'y'
    DATA_LEN = 40
    HORIZON = 10

    def setUp(self):
        """Set the default variables."""
        self.settings = {
            TimeSeries.TARGET_ROLLING_WINDOW_SIZE: 5,
            TimeSeries.TARGET_LAGS: [1],
            TimeSeriesInternal.CROSS_VALIDATIONS: 2,
            TimeSeries.MAX_HORIZON: self.HORIZON
        }
        self.dfs_train_good = []
        self.dfs_train_bad = []
        self.dfs_test = []
        self.good_grains = []
        for cnt in range(5):
            grain = "gr_{}".format(cnt)
            df = pd.DataFrame({
                self.DATE: pd.date_range('2019-01-01', freq='QS', periods=self.DATA_LEN),
                self.GRAIN: grain,
                'val': 42,
                self.TGT: np.arange(self.DATA_LEN).astype(float)
            })
            df_train = df[:self.DATA_LEN - self.HORIZON]
            df_test = df[self.DATA_LEN - self.HORIZON:].drop(self.TGT, axis=1)
            self.dfs_test.append(df_test)
            if cnt > 2:
                # break the grain to be small.
                df_train = df_train[:10]
                self.dfs_train_bad.append(df_train)
            else:
                self.good_grains.append(grain)
                self.dfs_train_good.append(df_train)
        unittest.TestCase.setUp(self)

    def _get_tsdf(self, data: list):
        """Return the TimeSeriesDataFrame."""
        if self.TGT in data[0].columns:
            return TimeSeriesDataFrame(
                pd.concat(data),
                time_colname=self.DATE,
                grain_colnames=self.GRAIN,
                ts_value_colname=self.TGT
            )
        else:
            return TimeSeriesDataFrame(
                pd.concat(data),
                time_colname=self.DATE,
                grain_colnames=self.GRAIN
            )

    def test_short_series(self):
        """Test if short time series are dropped."""
        dropper = ShortGrainDropper(**self.settings)
        X_train = self._get_tsdf(self.dfs_train_good + self.dfs_train_bad)
        X_test = self._get_tsdf(self.dfs_test)
        dropper.fit(X_train)
        transformed = dropper.transform(X_test)
        grains = list(transformed.index.get_level_values(1).unique())
        self.assertEqual(dropper.grains_to_keep, self.good_grains, "Wrong grains_to_keep parameter.")
        self.assertTrue(self.good_grains == grains)
        self.assertEqual(transformed.shape[0], 30, "Wrong number of rows.")
        # Test fit_transform
        dropper = ShortGrainDropper(**self.settings)
        transformed = dropper.fit_transform(X_train)
        grains = list(transformed.index.get_level_values(1).unique())
        self.assertTrue(self.good_grains == grains)
        self.assertEqual(transformed.shape[0], 90, "Wrong number of rows.")

    def test_non_existant_grains(self):
        """Test if non existing grains are removed from the test set."""
        dropper = ShortGrainDropper(**self.settings)
        dropper.fit(self._get_tsdf(self.dfs_train_good))
        transformed = dropper.transform(self._get_tsdf(self.dfs_test))
        grains = list(transformed.index.get_level_values(1).unique())
        self.assertTrue(self.good_grains == grains)
        self.assertEqual(transformed.shape[0], 30, "Wrong number of rows.")

    def test_all_grains_were_removed_fit(self):
        """Test exception is raised when all grains were removed from training."""
        dropper = ShortGrainDropper(**self.settings)
        X_train = self._get_tsdf(self.dfs_train_bad)
        with self.assertRaises(DataException):
            dropper.fit(X_train)

    def test_all_grains_were_removed_transform(self):
        """Test exceprion when all non existant grains were removed from prediction set."""
        dropper = ShortGrainDropper(**self.settings)
        dropper.fit(self._get_tsdf(self.dfs_train_good))
        with self.assertRaises(DataException):
            dropper.transform(self._get_tsdf(self.dfs_test[3:]))

    def test_non_fitted_transform_raises(self):
        """Test that predict on non fitted transform raises exception."""
        dropper = ShortGrainDropper(**self.settings)
        with self.assertRaises(ClientException):
            dropper.transform(self._get_tsdf(self.dfs_test))

    def test_non_fitted_grains_taises(self):
        """Test that grains_to_keep on non fitted transform raises exception."""
        dropper = ShortGrainDropper(**self.settings)
        with self.assertRaises(ClientException):
            dropper.grains_to_keep

    def test_raises_on_wrong_type(self):
        """Test if non data frame causes the exception."""
        dropper = ShortGrainDropper(**self.settings)
        X_train = self._get_tsdf(self.dfs_train_good)
        X_test = self._get_tsdf(self.dfs_test)
        with self.assertRaisesRegex(NotTimeSeriesDataFrameException, Messages.XFORM_INPUT_IS_NOT_TIMESERIESDATAFRAME):
            dropper.fit(X_train.values)
        with self.assertRaisesRegex(NotTimeSeriesDataFrameException, Messages.XFORM_INPUT_IS_NOT_TIMESERIESDATAFRAME):
            dropper.fit_transform(X_train.values)
        dropper.fit(X_train)
        with self.assertRaisesRegex(NotTimeSeriesDataFrameException, Messages.XFORM_INPUT_IS_NOT_TIMESERIESDATAFRAME):
            dropper.transform(X_test.values)

    def test_no_short_grain(self):
        """Test has_short_grains_in_train property."""
        dropper = ShortGrainDropper(**self.settings)
        X_train = self._get_tsdf(self.dfs_train_good)
        dropper.fit(X_train)
        self.assertFalse(dropper.has_short_grains_in_train, 'All grains should be long.')
        dropper = ShortGrainDropper(**self.settings)
        X_train = self._get_tsdf(self.dfs_train_good + self.dfs_train_bad)
        dropper.fit(X_train)
        self.assertTrue(dropper.has_short_grains_in_train, 'Some grains should be short.')
        # If the transform was not fitrted, the exception should be raised.
        dropper = ShortGrainDropper(**self.settings)
        with self.assertRaises(ClientException):
            dropper.has_short_grains_in_train

    def test_short_grain_with_original_order_col(self):
        """Test if original index column is not preventing correct grain dropping."""
        train = pd.concat(self.dfs_train_good + self.dfs_train_bad).reset_index(drop=True)
        train_ix = train.copy()
        train_ix[TimeSeriesInternal.DUMMY_ORDER_COLUMN] = train_ix.index

        test = pd.concat(self.dfs_test).reset_index(drop=True)
        test_ix = test.copy()
        test_ix[TimeSeriesInternal.DUMMY_ORDER_COLUMN] = test_ix.index

        def fit_and_transform(X_train, X_test):
            """fit_transform X_train and transform X_test."""
            X_train = self._get_tsdf([X_train])
            X_test = self._get_tsdf([X_test])
            dropper = ShortGrainDropper(**self.settings)
            trn = dropper.fit_transform(X_train)
            tst = dropper.transform(X_test)
            return trn, tst

        tr_train, tr_test = fit_and_transform(train, test)
        tr_train_ix, tr_test_ix = fit_and_transform(train_ix, test_ix)
        tr_train_ix.drop(TimeSeriesInternal.DUMMY_ORDER_COLUMN, axis=1, inplace=True)
        # If there is no missing indices, the short grain dropper should work as usual.
        assert_frame_equal(tr_train, tr_train_ix)
        tr_test_ix.drop(TimeSeriesInternal.DUMMY_ORDER_COLUMN, axis=1, inplace=True)
        assert_frame_equal(tr_test, tr_test_ix)

    def test_drop_by_index_column(self):
        """Test dropping by the index column."""
        dfs_train = []
        dfs_test = []
        train_exp = None
        test_exp = None
        min_points = utilities.get_min_points(
            self.settings[TimeSeries.TARGET_ROLLING_WINDOW_SIZE],
            self.settings[TimeSeries.TARGET_LAGS],
            self.settings[TimeSeries.MAX_HORIZON],
            self.settings[TimeSeriesInternal.CROSS_VALIDATIONS])
        length = min_points + self.settings[TimeSeries.MAX_HORIZON]
        for grain in ['good', 'bad']:
            df = pd.DataFrame({
                TestGrainDropper.DATE: pd.date_range('2001-01-01', freq='D', periods=length),
                TestGrainDropper.GRAIN: grain,
                'val': 42,
                TestGrainDropper.TGT: np.arange(42, 42 + length),
                TimeSeriesInternal.DUMMY_ORDER_COLUMN: np.arange(length)
            })
            df_train = df[:-self.settings[TimeSeries.MAX_HORIZON]].copy()
            df_test = df[-self.settings[TimeSeries.MAX_HORIZON]:].copy()
            dfs_test.append(df_test)
            if grain == 'bad':
                df_train[TimeSeriesInternal.DUMMY_ORDER_COLUMN][min_points - 1:] = np.NaN
            else:
                train_exp = self._get_tsdf([df_train])
                test_exp = self._get_tsdf([df_test])
            dfs_train.append(df_train)
        assert(train_exp is not None)
        assert(test_exp is not None)
        X_train = self._get_tsdf(dfs_train)
        X_test = self._get_tsdf(dfs_test)
        dropper = ShortGrainDropper(**self.settings)
        trn = dropper.fit_transform(X_train)
        assert_frame_equal(trn, train_exp, check_dtype=False)
        tst = dropper.transform(X_test)
        assert_frame_equal(tst, test_exp, check_dtype=False)


if __name__ == "__main__":
    unittest.main()
