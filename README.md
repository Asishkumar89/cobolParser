# Cobrix COBOL parsing quick start

This repository contains Cobrix, a Spark-based library for reading COBOL/EBCDIC files using a COBOL copybook.

## What you need

- Python with PySpark
- Spark 3.4.x
- Scala 2.12
- Java 8 (recommended for Spark 3.4)

## Local PySpark example

Start PySpark with Cobrix:

```sh
export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
pyspark --packages za.co.absa.cobrix:spark-cobol_2.12:2.11.0
```

Then run:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CobolExample").getOrCreate()

df = spark.read.format("cobol") \
    .option("copybook", "file:///Users/asishkumar/mainframe_parser/spark_cobrix/cobrix/data/test1_copybook.cob") \
    .load("file:///Users/asishkumar/mainframe_parser/spark_cobrix/cobrix/data/test1_data")

df.printSchema()
df.show()
```

## Write output as JSON

```python
df.write.mode("overwrite").json("file:///Users/asishkumar/mainframe_parser/spark_cobrix/cobrix/output/test1_json")
```

## Colab setup

Use this in Google Colab:

```python
!apt-get update
!apt-get install -y openjdk-8-jdk-headless
!pip install pyspark==3.4.0

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin:" + os.environ["PATH"]

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CobolColabExample") \
    .config("spark.jars.packages", "za.co.absa.cobrix:spark-cobol_2.12:2.11.0") \
    .getOrCreate()
```

Then upload your copybook and data folder and run:

```python
df = spark.read.format("cobol") \
    .option("copybook", "file:///content/test1_copybook.cob") \
    .load("file:///content/test1_data")

df.show()
```

## Notes

- Use Java 8 with Spark 3.4 to avoid startup issues.
- If `format("cobol")` does not work, try the full source name:

```python
df = spark.read.format("za.co.absa.cobrix.spark.cobol.source") \
    .option("copybook", "file:///content/test1_copybook.cob") \
    .load("file:///content/test1_data")
```

- For nested COBOL structures, JSON or Parquet is usually better than CSV.
# cobolParser
