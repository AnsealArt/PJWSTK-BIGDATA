/usr/local/hadoop/bin/hdfs dfs -mkdir input/lab4-3 ; \
/usr/local/hadoop/bin/hdfs dfs -put inputdata.txt input/lab4-3/ ; \
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar \
-file mapper.py -mapper "python3 mapper.py" \
-file reducer.py -reducer "python3 reducer.py" \
-input input/lab4-3/inputdata.txt \
-output output/lab4-3/count_input_words ; \
/usr/local/hadoop/bin/hdfs dfs -cat output/lab4-3/count_input_words/*
