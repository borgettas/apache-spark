from pyspark.sql import SparkSession
from pyspark.sql import functions as f


spark = SparkSession.builder.appName('SparkStreaming').getOrCreate()
lines = spark.readStream\
    .format('socket')\
    .option('host', 'localhost')\
    .option('port', 9010)\
    .load()

words = lines.select(f.explode(f.split(lines.value, ' ')).alias('word'))
word_counts = words.groupBy('word').count()

query = word_counts.writeStream\
    .outputMode('complete')\
    .format('console')\
    .start()

query.awaitTermination()