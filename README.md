# PJWSTK-BIGDATA
WPBD and WBD

## Useful information
### Hadoop start
```/usr/local/hadoop/sbin/start-all.sh```

### Add folder to HDFS
```hdfs dfs -mkdir folder/subfolder```

### Add file to HDFS
```hdfs dfs -put localfolder/localfile.extension hdfsfolder/hdfssubfolder```

### Read file from HDFS
```hdfs dfs -cat folder/file.extension/*```

### Set Hadoop to be able to use Hadoop and HDFS commands instead of whole lines
```export HADOOP_HOME=/usr/local/hadoop```
```export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin```