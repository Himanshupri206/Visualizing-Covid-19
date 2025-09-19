"""
Create a sample visualization using our modular approach.
"""
import pandas as pd
import matplotlib.pyplot as plt
from data_fetcher import fetch_covid_data, filter_country_data
from data_processor import get_latest_data_by_country, calculate_continent_deaths
from visualizer import create_deaths_by_continent_chart

def main():
    print("Creating sample visualization using modular approach...")
    
    # Fetch data
    print("1. Fetching data...")
    df = fetch_covid_data()
    
    if not df.empty:
        print(f"   Data fetched successfully. Shape: {df.shape}")
        
        # Process data
        print("2. Processing data...")
        df_countries = filter_country_data(df)
        latest_data = get_latest_data_by_country(df_countries)
        continent_deaths = calculate_continent_deaths(latest_data)
        
        print("3. Creating visualization...")
        # Generate visualization
        filename = create_deaths_by_continent_chart(continent_deaths)
        print(f"   Visualization created: {filename}")
        print("Sample visualization created successfully!")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    main()