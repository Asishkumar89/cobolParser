# -*- coding: utf-8 -*-

# @title
!mkdir -p /content/jars
!wget -O /content/jars/spark-cobol_2.12-2.11.0.jar https://repo1.maven.org/maven2/za/co/absa/cobrix/spark-cobol_2.12/2.11.0/spark-cobol_2.12-2.11.0.jar
!wget -O /content/jars/cobol-parser_2.12-2.11.0.jar https://repo1.maven.org/maven2/za/co/absa/cobrix/cobol-parser_2.12/2.11.0/cobol-parser_2.12-2.11.0.jar

!apt-get update
!apt-get install -y openjdk-8-jdk-headless
!pip install pyspark==3.4.0

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin:" + os.environ["PATH"]

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CobolColabJarExample") \
    .config("spark.jars", "/content/jars/spark-cobol_2.12-2.11.0.jar,/content/jars/cobol-parser_2.12-2.11.0.jar") \
    .getOrCreate()

df = spark.read.format("cobol") \
    .option("copybook", "file:///content/test1_copybook.cob") \
    .load("file:///content/example.bin")

df.printSchema()
df.show()

df = spark.read.format("cobol") \
    .option("copybook", "file:///content/test1_copybook.cob") \
    .load("file:///content/example.bin")

df.write.mode("overwrite").json("file:///content/output_json")
