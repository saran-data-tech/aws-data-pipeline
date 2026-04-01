from pyspark.sql import SparkSession

from pyspark.sql.functions import col, when

spark = SparkSession.builder \
    .appName("MyApp") \
    .master("local[*]") \
    .getOrCreate()


df =( spark.read
.format("csv") \
.option("header", True) \
.option("path", "/Users/saranraj/Documents/data.csv") \
.load()
      )
data = [("saran",22),("varun",24)]
df = spark.createDataFrame(data,["name","age"])
df = df.withColumn(
    "status",
    when(col("age") >= 18, "eligible")
    .otherwise("not eligible")
)
df.show()





