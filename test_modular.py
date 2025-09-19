"""
Test script to verify the modular code works correctly.
"""
from data_fetcher import fetch_covid_data
from data_processor import get_latest_data_by_country, calculate_continent_deaths
from visualizer import create_deaths_by_continent_chart
import os

def main():
    print("Testing modular COVID-19 visualization code...")
    
    # Fetch data
    print("Fetching data...")
    df = fetch_covid_data()
    
    if not df.empty:
        print(f"Data fetched successfully. Shape: {df.shape}")
        
        # Process data
        print("Processing data...")
        # Get the latest data for each country
        latest_data = get_latest_data_by_country(df)
        # Calculate the mean of total_deaths_per_million for each continent
        continent_deaths = calculate_continent_deaths(latest_data)
        
        print("Creating visualization...")
        # Generate visualization
        filename = create_deaths_by_continent_chart(continent_deaths, 'output/test_deaths_by_continent.png')
        print(f"Visualization created: {filename}")
        
        # Check if file exists
        if os.path.exists(filename):
            print("Test passed! Visualization created successfully.")
        else:
            print("Test failed! Visualization file not found.")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    main()