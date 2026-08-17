from pyspark.sql import SparkSession


COPYBOOK_PATH = "file:///Users/asishkumar/mainframe_parser/spark_cobrix/cobrix/data/GENERIC_RECORD.cpy"
DATA_PATH = "file:///Users/asishkumar/mainframe_parser/spark_cobrix/cobrix/data/generic_record_500mb.dat"
OUTPUT_PATH = "file:///Users/asishkumar/mainframe_parser/spark_cobrix/cobrix/output/generic_record_parquet"


spark = (
    SparkSession.builder
    .appName("ReadGenericRecordWithCobrix")
    .config("spark.sql.shuffle.partitions", "8")
    .getOrCreate()
)

df = (
    spark.read
    .format("cobol")
    .option("copybook", COPYBOOK_PATH)
    .option("encoding", "EBCDIC")
    .option("ebcdic_code_page", "cp500")
    .option("record_format", "F")
    .option("schema_retention_policy", "collapse_root")
    .load(DATA_PATH)
)

df.printSchema()
df.show(5, truncate=False)

df.write.mode("overwrite").parquet(OUTPUT_PATH)

spark.stop()
