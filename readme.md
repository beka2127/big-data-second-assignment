# NYC Taxi & Weather Analytics: Advanced ETL Pipeline

## Project Overview
This project implements a resilient and scalable data pipeline that integrates NYC taxi trip data, neighborhood mapping, and real-time weather analytics. By combining large-scale Parquet files with live API data, we provide insights into how environmental conditions impact urban transportation patterns.

## Pipeline Architecture
Our architecture follows the "Medallion" structure (Raw -> Processed -> Analytical):

1.  **Extraction:** 
    *   **Source 1:** NYC TLC Yellow Taxi Trip Records (Parquet).
    *   **Source 2:** Taxi Zone Lookup Table (CSV).
    *   **Source 3:** Open-Meteo Historical Weather API (JSON).
2.  **Transformation (PySpark & Pandas):** 
    *   Data cleaning (handling nulls and filtering outliers).
    *   Schema enforcement and type conversion.
    *   Multi-source joins to align taxi pickups with hourly weather data.
3.  **Loading (DuckDB):** 
    *   High-performance storage in a local DuckDB analytical database.
    *   Creation of optimized SQL views for Business Intelligence reporting.
4.  **Orchestration (Prefect):** 
    *   Automated workflow management ensuring scripts run in the correct sequence with retry logic.
5.  **Visualization (Power BI):** 
    *   Interactive dashboard showing correlations between weather, demand, and revenue.

## Team Contributions 
- **Bereket Shegye (Lead):** 
- **berhan tesfay:** 
- **zewdu werede:** 
- **kalkidan anberbir:** 
- **zelalem zeleke:** 
- **lamrot girma:**
- **hana solomon:** 
- **hailemaryam assefa:**

## Key Insights Gained
- **Weather Sensitivity:** Taxi demand shows a significant correlation with precipitation; trip volume increases during moderate rain as users pivot from walking to ride-hailing.
- **Revenue Hotspots:** The integration of the Zone Lookup CSV revealed that while Manhattan has the highest volume, the average fare and tip percentage are significantly higher for trips originating near major transit hubs during inclement weather.
- **Operational Efficiency:** By utilizing DuckDB for the analytical layer, query performance for the dashboard was improved by over 80% compared to querying raw Parquet files directly.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the full pipeline: `python main_pipeline.py`
3. Open `nyc_analytics.db` in Power BI to view the dashboard.