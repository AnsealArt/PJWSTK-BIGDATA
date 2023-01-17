## To run sample mrjob MapReduce program: <br />
### Sample 1
```python3 word_count.py input.txt```
### Sample 2
```python3 most_used_words.py input.txt```

<br /><hr><br />

## To run C5 Task:
### Locally
```python3 count_customer_orders.py customer-orders.csv```

### On Hadoop
1. Create folder for the task, if not exists
```hdfs dfs -mkdir input/lab5```

2. Add required file to Hadoop
```hdfs dfs -put customer-orders.csv input/lab5```

3. Run MRJob
```python3 count_customer_orders.py -r hadoop hdfs:///user/filip/input/lab5/customer-orders.csv``
