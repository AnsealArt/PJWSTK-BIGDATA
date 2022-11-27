/usr/local/hadoop/bin/hdfs dfs -mkdir input/lab4 || \
/usr/local/hadoop/bin/hdfs dfs -put /home/filip/scripts/lab4/short_story.txt || \
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar \
-files /home/filip/scripts/lab4/mapper.py -mapper "python3 mapper.py" \
-files /home/filip/scripts/lab4/reducer.py -reducer "python3 reducer.py" \
-input short_story.txt \
-output count_words || \
/usr/local/hadoop/bin/hdfs dfs -cat count_words_output.txt/* | sort -g -k 2,2 --reverse | head -n 10
