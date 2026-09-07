from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# 1. Create a Spark session
spark = SparkSession.builder \
    .appName("CreateDataFrame") \
    .getOrCreate()

# 2. Define the data and schema
data = [("siva", 34), ("karthik", 28)]
schema = ["name", "age"]

# 3. Create DataFrame
df = spark.createDataFrame(data, schema=schema)

# 4. Show the DataFrame
df.show()

# 5. (Optional) Print schema
df.printSchema()


