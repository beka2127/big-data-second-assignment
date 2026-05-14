import duckdb
import os

print("Connecting to DuckDB...")

# 1. Create (or connect to) a local database file
# This will create a file named 'nyc_analytics.db' in your project root
con = duckdb.connect('nyc_analytics.db')

# 2. Load the transformed Parquet file into a DuckDB table
# DuckDB's 'read_parquet' is incredibly fast
print("Loading Parquet data into DuckDB...")
con.execute("""
    CREATE OR REPLACE TABLE taxi_weather_analytics AS 
    SELECT * FROM read_parquet('data/transformed/final_taxi_data.parquet')
""")

# 3. Quick verification check
print("Verifying data...")
row_count = con.execute("SELECT COUNT(*) FROM taxi_weather_analytics").fetchone()[0]
print(f"Success! Loaded {row_count} rows into the 'taxi_weather_analytics' table.")

# 4. Bonus: Create a View for the Dashboard
# This makes it easier for BI tools like Power BI or Tableau to read specific insights
con.execute("""
    CREATE OR REPLACE VIEW daily_summary AS 
    SELECT 
        pickup_hour::DATE as date,
        COUNT(*) as total_trips,
        AVG(temperature_2m) as avg_temp,
        AVG(precipitation) as avg_precip,
        AVG(fare_amount) as avg_fare
    FROM taxi_weather_analytics
    GROUP BY 1
""")
con.close()
print("Database is ready! You can now connect your BI tool to 'nyc_analytics.db'.")