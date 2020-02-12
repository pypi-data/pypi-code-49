import td_pyspark
from py4j.protocol import Py4JJavaError
from pyspark.sql import SparkSession
import unittest
from datetime import datetime

class TDPySparkTest(unittest.TestCase):
    SAMPLE_TABLE = "sample_datasets.www_access"

    @classmethod
    def setUpClass(self):
        builder = SparkSession.builder.appName("td-pyspark-test")
        self.td = td_pyspark.TDSparkContextBuilder(builder)\
            .build()

        self.test_db_name = 'td_pyspark_test_{}'.format(str(datetime.now().timestamp()).replace('.', '_'))
        self.td.create_database_if_not_exists(self.test_db_name)

    @classmethod
    def tearDownClass(self):
        self.td.drop_database_if_exists(self.test_db_name)
        self.td.spark.stop()

    def get_source_sample(self):
        return self.td.table(self.SAMPLE_TABLE).df().limit(3)

    def create_or_refresh(self, table_name):
        target_table = self.td.table(table_name)
        target_table.drop_if_exists()
        target_table.create_if_not_exists()
        return target_table

    def test_show(self):
        df = self.td.table("sample_datasets.www_access") \
            .within("+2d/2014-10-04")\
            .df()
        df.show()

    def test_context_db(self):
        self.td.use("sample_datasets")
        df = self.td.table("www_access") \
            .df().limit(3)
        self.assertEqual(df.count(), 3)

    def test_read(self):
        df = self.get_source_sample()
        self.assertEqual(df.count(), 3)
        self.assertEqual(len(df.schema), 9)

    def test_exists(self):
        self.assertTrue(self.td.db("sample_datasets").exists())
        self.assertTrue(self.td.db(self.test_db_name).exists())

    def test_insert(self):
        table_name = "{}.test_insert".format(self.test_db_name)
        target_table = self.create_or_refresh(table_name)
        df = self.get_source_sample()
        self.td.insert_into(df, table_name)

        count = target_table.df().count()
        self.assertEqual(count, 3)

    def test_error_mode(self):
        table_name = "{}.test_error_mode_mode".format(self.test_db_name)
        self.create_or_refresh(table_name)
        df = self.get_source_sample()
        # 'error' mode is default
        def write_with_error_mode():
            self.td.write(df, table_name)

        self.assertRaises(Exception, write_with_error_mode)

    def test_append_mode(self):
        table_name = "{}.test_append_mode".format(self.test_db_name)
        target_table = self.create_or_refresh(table_name)
        df = self.get_source_sample()
        self.td.write(df, table_name, "append")
        self.td.write(df, table_name, "append")

        count = target_table.df().count()
        self.assertEqual(count, 6)

    def test_overwrite_mode(self):
        table_name = "{}.test_overwrite_mode".format(self.test_db_name)
        target_table = self.create_or_refresh(table_name)
        df = self.get_source_sample()
        self.td.write(df, table_name, "overwrite")
        self.td.write(df, table_name, "overwrite")

        count = target_table.df().count()
        self.assertEqual(count, 3)

    def test_create(self):
        table_name = "{}.test_create".format(self.test_db_name)
        target_table = self.create_or_refresh(table_name)
        df = self.get_source_sample()
        self.td.create_or_replace(df, table_name)

        count = target_table.df().count()
        self.assertEqual(count, 3)

    def test_create_udp_l(self):
        table_name = "{}.test_create_udp_l".format(self.test_db_name)
        target_table = self.create_or_refresh(table_name)
        df = self.get_source_sample()
        self.td.create_udp_l(table_name, 'code')
        self.td.insert_into(df, table_name)

        count = target_table.df().count()
        self.assertEqual(count, 3)

    def test_create_udp_s(self):
        table_name = "{}.test_create_udp_s".format(self.test_db_name)
        target_table = self.create_or_refresh(table_name)
        df = self.get_source_sample()
        self.td.create_udp_s(table_name, 'path')
        self.td.insert_into(df, table_name)

        count = target_table.df().count()
        self.assertEqual(count, 3)

    def test_supported_site(self):
        endpoints = td_pyspark.TDSparkContextBuilder.ENDPOINTS
        self.assertTrue('us' in endpoints)
        self.assertTrue('jp' in endpoints)
        self.assertTrue('eu01' in endpoints)

    def test_set_api_endpoints(self):
        builder = td_pyspark.TDSparkContextBuilder(SparkSession.builder.appName("endpoint-config-test"))
        builder.api_endpoint("api-development.treasuredata.com")\
            .presto_endpoint("api-development-presto.treasuredata.com")\
            .plazma_endpoint("api-development-plazma.treasuredata.com")

    def test_presto(self):
        df = self.td.presto('select * from sample_datasets.www_access limit 3')
        self.assertTrue(len(df.schema), 9)
        self.assertTrue(df.count(), 3)

    def test_default_jar_path(self):
        jar_path = td_pyspark.TDSparkContextBuilder.default_jar_path()
        self.assertTrue(jar_path.endswith('td-spark-assembly.jar'))

    def test_new_apikey(self):
        new_td = self.td.with_apikey("new_key")
        def invalid_apikey():
            new_td.table(self.SAMPLE_TABLE).df().take(1)

        self.assertRaises(Py4JJavaError, invalid_apikey)

    def test_write_with_new_apikey(self):
        table_name = "{}.test_write_with_new_apikey".format(self.test_db_name)
        self.create_or_refresh(table_name)
        df = self.get_source_sample()
        self.td.write(df, table_name, "append")

        new_td = self.td.with_apikey("new_key")
        def invalid_apikey():
            new_td.write(df, table_name, "append")

        self.assertRaises(Py4JJavaError, invalid_apikey)

    def test_within_time_range(self):
        table = self.td.table(self.SAMPLE_TABLE)
        # This time range assumed to run td-spark on US site
        # The time column should be defined with created time, and it should
        # be different from other sites. This default datetime might be changed.
        begin_datetime = "2014-10-03 09:12:00"
        end_datetime = "2014-10-03 09:13:00"
        df1 = table.within_utc_time_range(begin_datetime, end_datetime).df()
        df2 = table.within_time_range(begin_datetime, end_datetime).df()

        self.assertEqual(df1.count(), df2.count())
        self.assertEqual(df1.head(), df2.head())

        df_tokyo = table.within_time_range(
            begin_datetime, end_datetime, "Asia/Tokyo"
        ).df()
        self.assertNotEqual(df1.count(), df_tokyo.count())
        self.assertNotEqual(df1.head(), df_tokyo.head())

        df_tokyo2 = table.within_time_range(
            "2014-10-03 18:12:00", "2014-10-03 18:13:00", "Asia/Tokyo"
        ).df()
        self.assertEqual(df1.count(), df_tokyo2.count())
        self.assertEqual(df1.head(), df_tokyo2.head())


if __name__ == "__main__":
    unittest.main()
