import requests
import json
import pandas as pd

def fetch_nyc_weather():
    # NYC Coordinates
    lat, lon = 40.7128, -74.0060
    
    # Let's get January 2024 data (adjust dates to match your Parquet file)
    url = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date=2024-01-01&end_date=2024-01-31&hourly=temperature_2m,precipitation"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Save raw JSON for our 'Raw' layer
        with open('data/raw/weather_data.json', 'w') as f:
            json.dump(data, f)
        print("Weather data downloaded successfully!")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    fetch_nyc_weather()