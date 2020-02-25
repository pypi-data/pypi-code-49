from pyspark.sql import DataFrame
from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext("local", "Simple App")
spark = SparkSession(sc)

class DataFrameWithZipWithIndex(DataFrame):
    def __init__(self, df):
        super(self.__class__, self).__init__(df._jdf, df.sql_ctx)

    def zipWithIndex(self):
        return (self.rdd
                .zipWithIndex()
                .map(lambda row: (row[1], ) + row[0])
                .toDF(["_idx"] + self.columns))

df = sc.parallelize([("a", 1)]).toDF(["foo", "bar"])

with_zipwithindex = DataFrameWithZipWithIndex(df)

isinstance(with_zipwithindex, DataFrame)
