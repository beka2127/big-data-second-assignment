from prefect import task, flow
import subprocess

@task(retries=3, retry_delay_seconds=10)
def run_extraction():
    print("Starting Extraction...")
    # This runs your existing script
    subprocess.run(["python", "scripts/extract_weather.py"], check=True)

@task
def run_transformation():
    print("Starting Transformation...")
    subprocess.run(["python", "scripts/transform_pandas.py"], check=True)

@task
def run_loading():
    print("Starting Loading to DuckDB...")
    subprocess.run(["python", "scripts/load_to_duckdb.py"], check=True)

@flow(name="NYC Taxi ETL Pipeline")
def nyc_taxi_pipeline():
    # Define the order of execution
    extract = run_extraction()
    transform = run_transformation(wait_for=[extract])
    load = run_loading(wait_for=[transform])

if __name__ == "__main__":
    nyc_taxi_pipeline()