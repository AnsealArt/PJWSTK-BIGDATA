## Steps
1. Run Haddop Services:
```/usr/local/hadoop/sbin/start-all.sh```

2. Run script:
```./run.sh```

If doesn't run, need to add permissions:
```chmod 755 ./run.sh```

<br />

## Script Description
```;``` executes next command regardless of success or fail of the previous command (helps with multi-running)
1. ```/usr/local/hadoop/bin/hdfs dfs -mkdir input/lab4``` - create Hadoop directory
2. ```/usr/local/hadoop/bin/hdfs dfs -put /home/filip/scripts/lab4/short_story.txt``` - put data file into Hadoop
3. ```/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar -files /home/filip/scripts/lab4/mapper.py -mapper "python3 mapper.py" -files /home/filip/scripts/lab4/reducer.py -reducer "python3 reducer.py" -input short_story.txt -output count_words``` - run Java streaming module with own mapper and reducer
4. ```/usr/local/hadoop/bin/hdfs dfs -cat count_words_output.txt/* | sort -g -k 2,2 --reverse | head -n 10``` - read output and sort it to see most 10 frequent words

<br />

## Sample expected output
<pre>
the     112
I       66
and     61
of      50
in      41
a       41
to      40
my      35
with    22
was     21
</pre>