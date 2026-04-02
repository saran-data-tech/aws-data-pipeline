from pyspark.sql import SparkSession

from pyspark.sql.functions import col, when
from pyspark.sql.types import *


spark= SparkSession.builder \
    .appName("MyApp2") \
    .master("local[*]") \
    .getOrCreate()

df=(spark.read
.format("csv") \
.option("header",True)
.option("path","/Users/saranraj/Documents/data.csv")
.load()
)

data = (("saran raj",28),("claude",35))
df=spark.createDataFrame(data,["name","age"])
df=df.withColumn(
"status",
    when (col("age")>=30,"nailed")
        .otherwise("nul")
)

df.show()