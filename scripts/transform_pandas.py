import pandas as pd
import json

print("Starting Pandas Transformation...")

# 1. Load the Data Sources
# Source 1: Parquet
taxi_df = pd.read_parquet("data/raw/yellow_tripdata_2024-01.parquet")

# Source 2: CSV
zones_df = pd.read_csv("data/raw/taxi_zone_lookup.csv")

# Source 3: JSON (Weather)
with open('data/raw/weather_data.json', 'r') as f:
    weather_data = json.load(f)

# 2. Flatten Weather Data
# Convert the 'hourly' dictionary into a DataFrame
weather_df = pd.DataFrame(weather_data['hourly'])
weather_df['time'] = pd.to_datetime(weather_df['time'])

# 3. Prepare Taxi Data
# Convert pickup time to datetime and create a join key (the hour)
taxi_df['tpep_pickup_datetime'] = pd.to_datetime(taxi_df['tpep_pickup_datetime'])
taxi_df['pickup_hour'] = taxi_df['tpep_pickup_datetime'].dt.floor('h')

# 4. The Joins
print("Joining datasets...")
# Join with Zones
df_merged = taxi_df.merge(zones_df, left_on='PULocationID', right_on='LocationID', how='left')

# Join with Weather
final_df = df_merged.merge(weather_df, left_on='pickup_hour', right_on='time', how='left')

# 5. Save the result
output_path = "data/transformed/final_taxi_data.parquet"
final_df.to_parquet(output_path)

print(f"SUCCESS! Transformation complete. Data saved to {output_path}")
