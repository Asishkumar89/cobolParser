Terminal command used to run the job


export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)

spark-submit \
  --packages za.co.absa.cobrix:spark-cobol_2.12:2.11.0 \
  read_generic_record_cobrix.py
