import sys
import pyspark
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

    conf = SparkConf().setAppName("Word Count - Python").setMaster('local[*]')
    session = pyspark.sql.SparkSession.builder.config(conf=conf).getOrCreate()

    rdd = session.sparkContext.textFile("example.txt")
    rdd = rdd.cache()

    print(rdd.flatMap(lambda text: text.split()).countByValue())