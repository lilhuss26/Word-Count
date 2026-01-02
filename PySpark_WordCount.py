from pyspark.sql.functions import split, explode, count, col, desc
from pyspark.sql.types import StringType
from pyspark.sql import SparkSession
import re

myspark = SparkSession.builder.appName("word_counter").getOrCreate()

with open("Football Analytics With Python & R Learning Data Science Through the Lens of Sports.txt", "r") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = re.sub(r"[\s\n]+", " ",data[i].strip())

df = myspark.createDataFrame(data, StringType()).toDF("sentences")
df = df.select(explode(split("sentences"," ")).alias("words"))

word_counts = df.groupBy("words").count()
word_counts = word_counts.orderBy(desc("count"))
word_counts.show(10)
