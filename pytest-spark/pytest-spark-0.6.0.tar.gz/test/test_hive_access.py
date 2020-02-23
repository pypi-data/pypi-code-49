import pyspark
import pytest


try:
    from pyspark.sql import SparkSession
except ImportError:
    SPARK1 = True
else:
    SPARK1 = False


@pytest.mark.skipif(SPARK1, reason="requires Spark 2.x")
def test_hive_access_is_enabled_by_default(spark_session):
    default_db = spark_session.catalog.listDatabases()[0]
    assert default_db.name == 'default'


@pytest.mark.skipif(SPARK1, reason="requires Spark 2.x")
def test_hive_access_create_table(spark_session):
    default_db = spark_session.catalog.listDatabases()[0]
    assert default_db.name == 'default'
