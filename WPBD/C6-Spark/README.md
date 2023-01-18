# Running Python scripts on Apache Spark

### To run any script
```spark-submit script.py```

### To run MRJob script on Spark
> ```python3 script.py -r spark datafile.extension ```

Example: 
> ```python3 count_customer_orders_sorted.py -r spark customer-orders.csv```