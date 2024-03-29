import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName('tepst') \
    .getOrCreate()

df = spark.read \
    .option("header", "true") \
    .csv('fhv_tripdata_2021-07.csv.gz')

df.show()
