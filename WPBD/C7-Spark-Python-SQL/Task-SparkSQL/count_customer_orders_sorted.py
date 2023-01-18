import sys
import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, Row

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

def mapper(line):
    fields = line.split(',')

    return Row(
        customer_id = int(fields[0]),
        product_id  = int(fields[1]),
        amount      = float(fields[2])
    )


rdd = spark.sparkContext.textFile("customer-orders.csv")
rdd_table = rdd.map(mapper)
customer_orders = spark.createDataFrame(rdd_table).cache()

customer_orders.createOrReplaceTempView("TMP_VIEW_CUSTOMER_ORDERS")

df_customer_orders_grouped = spark.sql("""
        SELECT customer_id AS `Customer ID` 
             , ROUND(SUM(amount), 2) AS `Bill`
        FROM TMP_VIEW_CUSTOMER_ORDERS
    GROUP BY customer_id
    ORDER BY SUM(amount) DESC
    """)

df_customer_orders_grouped.show()
    

    