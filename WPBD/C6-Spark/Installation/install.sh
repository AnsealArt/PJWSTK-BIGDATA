sudo apt install openjdk-11-jre-headless  && \
wget https://downloads.apache.org/spark/spark-3.3.1/spark-3.3.1-bin-without-hadoop.tgz && \
tar -xvzf spark-3.3.1-bin-without-hadoop.tgz spark-3.3.1-bin-without-hadoop && \
sudo mv spark-3.3.1-bin-without-hadoop /usr/local/spark && \
cp /usr/local/spark/conf/spark-env.sh.template /usr/local/spark/conf/spark-env.sh

#### Now need to modify spark-env.sh with SPARK_DIST_CLASSPATH variable
# sudo nano /usr/local/spark/conf/spark-env.sh

#### Write to file
# export SPARK_DIST_CLASSPATH=$(/usr/local/hadoop/bin/hadoop classpath)

#### Then add Spark to PATH
# export PATH=$PATH:/usr/local/spark/bin

#### Then relog bashrc settings
# source ~./bashrc

#### Finally we can run lines count script
# hdfs dfs -mkdir spark_data && hdfs dfs -put /usr/local/spark/README.md ./spark_data
# pyspark
# rdd = sc.textFile("spark_data/README.md")
# rdd.count()