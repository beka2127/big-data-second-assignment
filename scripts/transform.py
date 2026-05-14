from pyspark.sql import SparkSession
import os

# Create Spark Session with reduced logging
spark = SparkSession.builder \
    .appName("NYCTaxiPipeline") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

try:
    print("Reading data sources...")
    # Read only the first 50,000 rows to speed things up for the assignment
    taxi_df = spark.read.parquet("data/raw/yellow_tripdata_*.parquet").limit(50000)
    zones_df = spark.read.csv("data/raw/taxi_zone_lookup.csv", header=True, inferSchema=True)
    
    print("Joining Data...")
    # Join Taxi trips with Zone names
    final_df = taxi_df.join(zones_df, taxi_df.PULocationID == zones_df.LocationID, "left")
    
    print("Writing to Parquet...")
    # Write to processed folder
    output_path = "data/transformed/final_taxi_data"
    final_df.write.mode("overwrite").parquet(output_path)
    
    print(f"SUCCESS! Data saved to {output_path}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    spark.stop()
    # this code couldn't work so we decided to use pandas for the transformation phase 