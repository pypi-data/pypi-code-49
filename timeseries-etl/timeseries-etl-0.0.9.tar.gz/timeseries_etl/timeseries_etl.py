# This is a module designed to extract TimeSeries as pandas Dataframes from a Database.
# It also allows to build datasets for statistics or machine learning purposes
# The main goal of the module is to extract all the data without any filtering or manipulation except from the one
# needed to build the pandas Dataframe in an efficient way such as filtering by date to reduce the size


import vertica_python
import psycopg2
import pandas as pd
from typing import List, NamedTuple
from datetime import datetime
from joblib import Parallel, delayed
from tqdm import tqdm
import argparse
import logging


# A case class that is going to represent the information needed to go to the database and retrieve a multivariate
# timeseries"
class TSDataDef(NamedTuple):
    table: str
    item_id: int
    # We decided to use several measures to retrieve all the measures for a given item with just one query
    measures: List[str]


class VerticaDao():
    def __init__(self, host: str, port: int, user: str, password: str, dbname: str):
        """
        A DAO class to access data from Vertica. The main function is execute query which will return a pandas Dataframe
        :param host:
        :param port:
        :param user:
        :param password:
        :param dbname:
        """
        self.conn_info = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'database': dbname,
            # 10 minutes timeout on queries
            'read_timeout': 200000,
            # default throw error on invalid UTF-8 results
            'unicode_error': 'strict',
            # SSL is disabled by default
            'ssl': False,
            'connection_timeout': 20
            # connection timeout is not enabled by default
        }
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.INFO)
        logger_handler = logging.StreamHandler()
        self.log.addHandler(logger_handler)
        logger_handler.setFormatter(
            logging.Formatter('%(asctime)s [%(levelname)s] : [%(module)s:%(lineno)d]-%(name)s : %(message)s'))

    def execute_query(self, query: str) -> pd.DataFrame:
        """
        :param query:
        :return: Returns a pandas Dataframe with the result of the query as a table
        """
        with vertica_python.connect(**self.conn_info) as connection:
            cur = connection.cursor('dict')
            self.log.info("Executing query: " + query)
            cur.execute(query)
            res_df = pd.DataFrame(cur.iterate())
        return res_df

    def get_table_schema(self, schema: str, table: str) -> pd.DataFrame:
        query = "SELECT table_schema, table_name, column_name, data_type, is_nullable " \
                "FROM columns WHERE table_schema = '{0}' " \
                "AND table_name = '{1}'".format(schema, table)
        df = self.execute_query(query)
        return df


class PostgresSqlDao():
    def __init__(self, host: str, port: str, user: str, password: str, dbname: str):
        """
        A DAO class to access data from PostgreSql. The main function is to execute a query which will return a pandas Dataframe
        :param host:
        :param port:
        :param user:
        :param password:
        :param dbname:
        """
        self.conn_info = {
            'host': host,
            'port': str(port),  # convert to string as psycopg2 expects a string
            'user': user,
            'password': password,
            'database': dbname,
        }
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.INFO)
        logger_handler = logging.StreamHandler()
        self.log.addHandler(logger_handler)
        logger_handler.setFormatter(
            logging.Formatter('%(asctime)s [%(levelname)s] : [%(module)s:%(lineno)d]-%(name)s : %(message)s'))

    def execute_query(self, query: str) -> pd.DataFrame:
        """
        :param query:
        :return: Returns a pandas Dataframe with the result of the query as a table
        """
        with psycopg2.connect(**self.conn_info) as connection:
            res_df = pd.read_sql_query(query, connection)
        return res_df

    def get_table_schema(self, schema: str, table: str) -> List:
        raise NotImplementedError("Not Implemented. Dao's should be refactored")


class TimeSeriesEtl:
    from timeseries_etl.network_service import NetworkService
    """
    A class that will take care of extracting and enriching time series data coming from a Database
    """

    def __init__(self, db_type: str, host: str, port: int, user: str, password: str, dbname: str, schema: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
        self.schema = schema
        if db_type == 'vertica':
            self.dao = VerticaDao(host, port, user, password, dbname)
        self.log = logging.getLogger(self.__class__.__name__)

    def get_waze_alerts_ts(self, table: str, type: str, period: int, from_date: datetime = None) -> pd.DataFrame:
        """
        Get a timeseries of waze alerts. To find the alerts we have to provide the table that contains the info in the DB,
        the type of alert we are interested in, the period of time we want to use to assign a period timestamp to the events
        and optionally, an starting date. It's going to return a timeseries where the events are going to be assigned
        a timestamp equal to the beginning of their period. e.g. a 10:47 event will be assigned the 10:45 timestamp
        :param table:
        :param type:
        :param period:
        :param from_date:
        :return:
        """
        date_constraint = ""
        table_schema = self.dao.get_table_schema(self.schema, table)
        if 'creationMillis' in table_schema['column_name'].values:
            date_column = 'creationMillis'
            if from_date:
                date_constraint = "and creationMillis > '{0}' ".format(round(from_date.timestamp() * 1000))
        elif 'ts' in table_schema['column_name'].values:
            date_column = 'ts'
            if from_date:
                date_constraint = "and ts > '{0}' ".format(from_date)
        else:
            raise ValueError("No valid date column for this table")
        query = "select * from {0}.{1} where type = '{2}' {3} order by {4}".format(
            self.schema, table, type, date_constraint, date_column)
        df = self.dao.execute_query(query)
        if date_column == 'creationMillis':
            date_data = pd.to_datetime(df[date_column], unit='ms').dt.floor(str(period) + 'min')
        elif date_column == 'ts':
            date_data = df['ts'].dt.floor(str(period) + 'min')
        else:
            raise ValueError("No valid date column for this table")
        df['start_date'] = date_data
        return df.set_index('start_date')

    # This function will have to probably change depending on the type of waze ts: alerts, irregularities or jams
    @staticmethod
    def add_net_info_to_waze_ts(waze_ts: pd.DataFrame, net_service: NetworkService, max_dist: float = 0.00003):
        """
        This function will take an existing waze timeseries and add the information about the network coming from the
        network service.
        :param waze_ts:
        :param net_service:
        :param max_dist:
        :return:
        """

        # We define the function that is going to be applied to the whole df
        def add_network_data(row: pd.Series):
            nearest_links = net_service.find_link_by_coords(row['longitude'], row['latitude'], max_dist)
            if not nearest_links.empty:
                return row.add_prefix('waze_').append(nearest_links.iloc[0].add_prefix('link_'))
            else:
                return row.add_prefix('waze_')

        enriched_waze = waze_ts.apply(add_network_data, axis=1)
        return enriched_waze

    def get_measure_ts(self, table: str, item_id: int, measures: List[str], period: int,
                       from_date: datetime = None) -> pd.DataFrame:
        """
        Get a simple Pandas Dataframe representing a multivariate timeseries given by the following parameters
        :param table: The table in the DB
        :param item_id: The itemID which is normally the index of the DB table
        :param measures: A list of measures to retrieve which should match the columns in the DB
        :param period: The period of time to aggregate to
        :param from_date: (Optional) Parameter to limit the starting date
        :return: a Pandas Dataframe representing a multivariate timeseries
        """
        # example of result for item_id = 3 ['volume as volume_3', 'load as load_3']
        measures_columns = [m + ' as {0}_{1}'.format(m, item_id) for m in measures]
        date_constraint = ""
        if from_date:
            date_constraint = "and start_date > '{0}' ".format(from_date.strftime('%Y-%m-%d'))
        query = "select start_date, {0} from {1}.{2} where item_id = {3} {4} order by start_date".format(
            ', '.join(measures_columns), self.schema, table, item_id, date_constraint)
        df = self.dao.execute_query(query)
        if df.empty:
            # If the dataframe is empty then we can create an empty dataframe with only the name of the columns
            # In this way we will avoid key errors in subsequent operations if the query did not retrieve results
            df = pd.DataFrame(columns=['{0}_{1}'.format(m, item_id) for m in measures])
        if not df.empty:
            df = df.set_index('start_date')
            # eliminate duplicates
            df = df.loc[~df.index.duplicated(keep='first')]
        return df

    @staticmethod
    def create_list_of_tsdatainfo(table: str, item_ids: List[int], measure_names: List[str]) -> List[TSDataDef]:
        """
        A method that can be used to create a list of timeseries data definitions containing the item ids, the measures
        and the tables. This is just an auxiliary method
        :param table:
        :param item_ids:
        :param measure_names:
        :return:
        """
        list_res = []
        for it_id in item_ids:
            list_res.append(TSDataDef(table, it_id, measure_names))
        return list_res

    def __create_shifted_columns(self, df: pd.DataFrame, shifts: List[int], period: int) -> pd.DataFrame:
        """
        For each of the shift number in shifts, shift each of the columns of the df Dataframe. The period is just used
        to give the proper name to the shifted column
        :param df:
        :param shifts:
        :param period: This parameter is only used to put a name in the columns. It could be calculated directly from
        the Dataframe by measuring the deltas between timestamps
        :return:
        """
        for column in df.columns:
            for shift in shifts:
                new_column_name = '{0}_{1}'.format(column, shift * period)  # e.g volume_3_-5
                df[new_column_name] = df[column].shift(periods=-shift)
        return df

    def build_df_for_item(self, tsdatadef: TSDataDef, shifts: List[int], period: int,
                          from_date: datetime) -> pd.DataFrame:
        """
        A method that is used to build a dataframe representing a time series of values extracted from
        the database together with n = len(shifts) columns representing the timeseries but shifted.
        This function is used by the build_dataset function but it can be used inside a __main__ loop to parallelise
        the process
        :param self:
        :param tsdatadef:
        :param shifts:
        :param period:
        :param from_date:
        :return:
        """
        self.log.info(
            "Building dataframe for predictor {0}: shifts {1}, period {2}, from_date {3}".format(tsdatadef.item_id,
                                                                                                 shifts, period,
                                                                                                 from_date))
        df_predictor = self.get_measure_ts(tsdatadef.table, tsdatadef.item_id, tsdatadef.measures, period, from_date)
        if shifts:
            df_predictor = self.__create_shifted_columns(df_predictor, shifts, period)
        return df_predictor

    def build_dataset(self, predictors_info: List[TSDataDef], shifts: List[int], targets_info: List[TSDataDef],
                      targets_horizon: List[int], period: int, from_date: datetime = None) -> pd.DataFrame:
        """
        It builds a dataset that can be used later with machine learning algorithms or used for data visualisation
        It receives a list of information about the predictors in the form of TSDataDef classes. This predictors can
        be shifted n periods through the shifts argument which can have more than one shifts. The targets_info is going
        to have the information about the items to be predicted. The targets_horizon are the horizons in the future in
        number of periods.
        :param predictors_info:
        :param shifts:
        :param targets_info:
        :param targets_horizon:
        :param period:
        :param from_date: (Optional) It is possible to limit the starting date to use
        :return:
        """
        list_of_dfs = []
        # We don't really need separate loops for predictors_info and targets_info but we leave it like this if
        # needed in future implementations
        for predictor in predictors_info:
            list_of_dfs.append(self.build_df_for_item(predictor, shifts, period, from_date))
        for target in targets_info:
            list_of_dfs.append(self.build_df_for_item(target, targets_horizon, period, from_date))
        return pd.concat(list_of_dfs, axis=1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--db_type", type=str, default="vertica", help="the type of database to use",
                        choices=["vertica", "postgres"])
    parser.add_argument("host", type=str)
    parser.add_argument("port", type=int, default=5433)
    parser.add_argument("user", type=str)
    parser.add_argument("password", type=str)
    parser.add_argument("ptable", type=str, help="the table from where to extract the data for the predictor items")
    parser.add_argument("measure", type=str, help="the measure that should be used to build the timeseries e.g. speed")
    parser.add_argument("output", type=str,
                        help="the output file name to be used for the output file for both pickle and csv extensions. "
                             "e.g. /home/admin/dataset_dgt")
    parser.add_argument("-tt", "--ttable", type=str,
                        help="the table from where to extract the data for the target items")
    parser.add_argument("-t", "--target", type=int, help="the target item id that we want to predict")
    parser.add_argument("-ph", "--p_horizon", help="a list with n horizons for the predictors represented as a number "
                                                   "of periods", type=int, nargs="*", default=[])
    parser.add_argument("-th", "--t_horizon", help="a list with n horizons for the target represented as a number "
                                                   "of periods", type=int, nargs="*", default=[1, 2, 4])
    parser.add_argument("-db", "--database", type=str, default="pems",
                        help="the database to use. This is different from the type e.g. pems, icm...")
    parser.add_argument("-s", "--schema", type=str, default="public",
                        help="the schema from where to extract the info e.g. public, currentds...")
    parser.add_argument("-pk", "--pickle", action="store_true", help="whether to pickle or not the output dataframe")
    parser.add_argument("--date", type=str,
                        help="from which date should the process start extracting data from. The format is YYYY-MM-DD")
    parser.add_argument("--cpu", type=int, help="how many CPU's to use", default=4)
    parser.add_argument("--period", type=int, help="the period to use for the timeseries e.g. 5mins, 15 mins",
                        default=5)
    parser.add_argument("--var_thresh", type=int, help="the variance threshold. Every item with a value behind this "
                                                       "threshold won't be extracted",
                        default=5)
    args = parser.parse_args()
    vertica_dao = VerticaDao(args.host, args.port, args.user, args.password, args.database)
    # Increase the timeout as some queries are quite heavy
    vertica_dao.conn_info['connection_timeout'] = 2000
    vertica_dao.conn_info['read_timeout'] = 200000000
    date_cond = ""
    if args.date:
        date_cond = " where start_date > '{0}'".format(datetime.strptime(args.date, "%Y-%m-%d"))
    all_items = vertica_dao.execute_query(
        "select distinct item_id from {0}.{1}{2}".format(args.schema, args.ptable, date_cond))['item_id'].values
    query = "SELECT VARIANCE({2}) as var, item_id FROM {0}.{1} group by item_id having VARIANCE({2}) < {3}".format(
        args.schema, args.ptable, args.measure, args.var_thresh)
    items_low_variance = vertica_dao.execute_query(query)['item_id'].values
    final_items = list(set(all_items).difference(set(items_low_variance)))
    predictors_info = TimeSeriesEtl.create_list_of_tsdatainfo(args.ptable, final_items, [args.measure])
    targets_info = TimeSeriesEtl.create_list_of_tsdatainfo(args.ttable, [args.target], [args.measure])
    from_date = datetime.strptime(args.date, '%Y-%m-%d')
    # We don't really need separate loops for predictors_info and targets_info but we leave it like this if
    # needed in future implementations
    ts_etl = TimeSeriesEtl(args.db_type, args.host, args.port, args.user, args.password, args.database, args.schema)
    num_cores = args.cpu
    inputs_pred = tqdm(predictors_info)
    inputs_targ = tqdm(targets_info)
    list_of_dfs_pred = Parallel(n_jobs=num_cores)(
        delayed(ts_etl.build_df_for_item)(predictor, args.p_horizon, args.period, from_date) for predictor in
        inputs_pred)
    if args.target:
        list_of_dfs_targ = Parallel(n_jobs=num_cores)(
            delayed(ts_etl.build_df_for_item)(predictor, args.t_horizon, args.period, from_date) for predictor in
            inputs_targ)
        list_of_dfs_pred.extend(list_of_dfs_targ)
    final_df = pd.concat(list_of_dfs_pred, axis=1)
    final_df.to_csv('{0}.csv'.format(args.output), sep=";")
    if args.pickle:
        final_df.to_pickle('{0}.pkl'.format(args.output))
