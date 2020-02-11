from timeseries_etl.timeseries_etl import TimeSeriesEtl
from timeseries_etl.network_service import NetworkServicePostGis
from pandas import DataFrame, Timedelta
import datetime


class TestEtlFunctions():
    db_type = 'vertica'
    host = '172.24.76.116'
    port = 5433
    user = 'dbadmin'
    password = 'Telvent2011'
    dbname = 'pems'
    schema = 'public'

    def test_get_measures(self):
        ts_etl = TimeSeriesEtl(self.db_type, self.host, self.port, self.user, self.password, self.dbname, self.schema)
        result = ts_etl.get_measure_ts('measure_point_5min', 23, ['speed', 'volume'], 5)
        assert result.shape[0] > 0 and isinstance(result, DataFrame)

    def test_create_lists_of_tsdatainfo(self):
        list_of_tsinfo = TimeSeriesEtl.create_list_of_tsdatainfo('measure_point_5min', [1, 2, 23], ['speed', 'volume'])
        assert len(list_of_tsinfo) == 3

    def test_build_dataset(self):
        ts_etl = TimeSeriesEtl(self.db_type, self.host, self.port, self.user, self.password, self.dbname, self.schema)
        list_of_pred_info = TimeSeriesEtl.create_list_of_tsdatainfo('measure_point_5min', [1, 2, 23],
                                                                    ['speed', 'volume'])
        target_info = TimeSeriesEtl.create_list_of_tsdatainfo('measure_point_5min', [25], ['speed'])
        dataset = ts_etl.build_dataset(list_of_pred_info, [-1, -5], target_info, [4], 5)
        min_date = dataset.index.min()
        # make sure that the first value of the first column is the same as the one that was shifted one period + 5 mins
        assert (dataset.loc[min_date]['speed_1'] == dataset.loc[min_date + Timedelta(minutes=5)]['speed_1_-5'])
        # same with a shift of 5 periods
        assert (dataset.loc[min_date]['speed_1'] == dataset.loc[min_date + Timedelta(minutes=25)]['speed_1_-25'])
        # finally with the target measure to predict. Make sure is shifted back from the horizon
        assert (dataset.loc[min_date]['speed_25_20'] == dataset.loc[min_date + Timedelta(minutes=20)]['speed_25'])

    def test_build_wrong_dataset(self):
        """
        Test the build dataset procedure when the items are not present in the DB
        """
        ts_etl = TimeSeriesEtl(self.db_type, self.host, self.port, self.user, self.password, self.dbname, self.schema)
        list_of_pred_info = TimeSeriesEtl.create_list_of_tsdatainfo('measure_point_5min', [999999, 888888, 3333333],
                                                                    ['speed', 'volume'])
        target_info = TimeSeriesEtl.create_list_of_tsdatainfo('measure_point_5min', [25], ['speed'])
        dataset = ts_etl.build_dataset(list_of_pred_info, [-1, -5], target_info, [4], 5)
        min_date = dataset.index.min()
        # make sure that the first value of the first column is the same as the one that was shifted one period + 5 mins
        assert (dataset.fillna(0).loc[min_date]['speed_999999'] ==
                dataset.fillna(0).loc[min_date + Timedelta(minutes=5)]['speed_999999_-5'])
        # same with a shift of 5 periods
        assert (dataset.fillna(0).loc[min_date]['speed_999999'] ==
                dataset.fillna(0).loc[min_date + Timedelta(minutes=25)]['speed_999999_-25'])
        # finally with the target measure to predict. Make sure is shifted back from the horizon
        assert (dataset.fillna(0).loc[min_date]['speed_25_20'] ==
                dataset.fillna(0).loc[min_date + Timedelta(minutes=20)]['speed_25'])

    def test_build_constrained_dataset(self):
        ts_etl = TimeSeriesEtl(self.db_type, self.host, self.port, self.user, self.password, self.dbname, self.schema)
        list_of_pred_info = TimeSeriesEtl.create_list_of_tsdatainfo('measure_point_5min', [1, 2, 23],
                                                                    ['speed', 'volume'])
        target_info = TimeSeriesEtl.create_list_of_tsdatainfo('measure_point_5min', [25], ['speed'])
        from_date = datetime.datetime.strptime('2019-03-01', '%Y-%m-%d')
        dataset = ts_etl.build_dataset(list_of_pred_info, [-1, -5], target_info, [4], 5, from_date)
        min_date = dataset.index.min()
        # make sure that the first value of the first column is the same as the one that was shifted one period + 5 mins
        assert (dataset.loc[min_date]['speed_1'] == dataset.loc[min_date + Timedelta(minutes=5)]['speed_1_-5'])
        # same with a shift of 5 periods
        assert (dataset.loc[min_date]['speed_1'] == dataset.loc[min_date + Timedelta(minutes=25)]['speed_1_-25'])
        # finally with the target measure to predict. Make sure is shifted back from the horizon
        assert (dataset.loc[min_date]['speed_25_20'] == dataset.loc[min_date + Timedelta(minutes=20)]['speed_25'])

    def test_waze_alerts(self):
        # Alerts are in a different DB
        db_type = 'vertica'
        host = '172.24.9.121'
        port = 5433
        user = 'dbadmin'
        password = 'default'
        dbname = 'pems'
        schema = 'public'
        ts_etl = TimeSeriesEtl(db_type, host, port, user, password, dbname, schema)
        # We extract the data with a date constraint
        from_date = datetime.datetime.strptime('2020-01-10', '%Y-%m-%d')
        waze_df = ts_etl.get_waze_alerts_ts('alerts_mad', 'ACCIDENT', 15, from_date)
        min_date = waze_df.index.min()
        # Check that the minimum date is met. We assume waze has events every day
        assert min_date.day == 10 and min_date.month == 1 and min_date.year == 2020

    def test_network_service_postgis(self):
        # Network is in a different DB. Let's use DGT INT
        host = '172.24.76.193'
        port = '5432'
        user = 'postgres'
        password = 'Telvent2011'
        dbname = 'ICM'
        schema = 'currentds'
        table = 'oip_link'
        geom_field = 'location'
        longitude = -3.692049
        latitude = 40.318132
        distance = 0.005
        net_service = NetworkServicePostGis(host, port, user, password, dbname, schema, table, geom_field)
        res_df = net_service.find_link_by_coords(longitude, latitude, distance)
        assert res_df.head(1)['id'][0] == 2775

