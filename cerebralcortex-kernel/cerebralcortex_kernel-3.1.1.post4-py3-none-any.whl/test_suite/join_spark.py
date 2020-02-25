from cerebralcortex.core.util.spark_helper import get_or_create_sc
from functools import reduce
import math
from pyspark.sql import functions as F
from pyspark.sql.types import *
import json
# from pyspark.sql.functions import pandas_udf,PandasUDFType
from pyspark.sql.types import StructType
from pyspark.sql.functions import pandas_udf, PandasUDFType
from pyspark.sql.window import Window

#df3=reduce(lambda x, y: x.join(y, ['timestamp'], how='left'), dfs)

sqlContext = get_or_create_sc("sqlContext")

schema = StructType([
        StructField("question_text", StringType()),
        StructField("finish_time", IntegerType()),
        StructField("response_option", ArrayType(StringType())),
        StructField("prompt_time", IntegerType()),
        StructField("question_type", StringType()),
        StructField("response", ArrayType(StringType())),
        StructField("question_id", IntegerType())
    ])


schema2 = sqlContext.read.json("/home/ali/IdeaProjects/MD2K_DATA/q1.json",multiLine=True).schema
def str_to_json(data):

    dd= json.loads(data)
    print(type(dd))
    return dd
str_to_json_udf = F.udf(str_to_json)

ema = sqlContext.read.text("/home/ali/IdeaProjects/MD2K_DATA/q1.json", wholetext=True)
ema.show()

df=ema.withColumn("value", F.from_json(ema.value,schema2))
df.printSchema()
df.select("qa.question_text").show(truncate=False)
dfa=sqlContext.read.parquet("/home/ali/IdeaProjects/MD2K_DATA/cc3/moral_sample_data/accel/")
dfg=sqlContext.read.parquet("/home/ali/IdeaProjects/MD2K_DATA/cc3/moral_sample_data/gyro/")

from cerebralcortex.markers.brushing.util import get_orientation_data
accel2 = get_orientation_data(ds=dfa, sensor_type="accel", wrist="left")

# df1.orderBy("timestamp").show()
# df2.orderBy("timestamp")
#dfa=dfa.select("timestamp","version","x","y","z")
dfa.show(1,truncate=False)
dfg.show(1,truncate=False)



schemaa = dfa.schema
schemag = dfg.schema

@pandas_udf(schemaa, PandasUDFType.GROUPED_MAP)
def _a(pdf):
    pdf.set_index("timestamp", inplace=True)
    pdf = pdf.resample("60ms").bfill(limit=1).interpolate()
    pdf.ffill(inplace=True)
    pdf.reset_index(drop=False, inplace=True)
    pdf.sort_index(axis=1, inplace=True)
    pdf.dropna()
    return pdf

@pandas_udf(schemag, PandasUDFType.GROUPED_MAP)
def _g(pdf):
    pdf.set_index("timestamp", inplace=True)
    pdf = pdf.resample("60ms").bfill(limit=1).interpolate()
    pdf.ffill(inplace=True)
    pdf.reset_index(drop=False, inplace=True)
    pdf.sort_index(axis=1, inplace=True)
    pdf.dropna()
    return pdf

dfa2 = dfa.groupBy("user").apply(_a)
dfg2 = dfg.groupBy("user").apply(_g)
dfs = [dfa2,dfg2]
df3=reduce(lambda x, y: x.join(y, ['timestamp'], how='left'), dfs)
df4 = dfa2.join(dfg2, on=['user', 'timestamp', 'version'],
                                      how='full').orderBy('timestamp')
df4.show(10,truncate=False)

# complentary filter
w = Window.partitionBy()

window = Window.partitionBy(df4['user']).orderBy(df4['timestamp'])
# Create column
df5=df4.select('*', F.rank().over(window).alias('index'))

def get_x(thetaX_accel):
    return 0

dt = 1.0/16  #1/16.0;
M_PI =  math.pi;
hpf = 0.90;
lpf = 0.10;

filter_udf = F.udf(get_x, DoubleType())
dff = df5.withColumn("thetaX_accel", ((F.atan2(-F.col("accelerometer_z"),F.col("accelerometer_y"))*180/M_PI))*lpf)\
    .withColumn("thetax", (F.lag("thetaX_accel").over(window)+F.col("gyroscope_x")*dt)*hpf+F.col("thetaX_accel"))

dff.show(10)


print('Done')

