"""
Main application for generating COVID-19 visualizations.
"""
from data_fetcher import fetch_covid_data, filter_country_data, filter_continent_data
from data_processor import get_latest_data_by_country, calculate_continent_deaths, pivot_continent_data
from visualizer import create_deaths_by_continent_chart, create_cases_comparison_chart


def main():
    # Fetch data
    df = fetch_covid_data()
    
    if not df.empty:
        # Process country data for deaths visualization
        df_countries = filter_country_data(df)
        latest_data = get_latest_data_by_country(df_countries)
        continent_deaths = calculate_continent_deaths(latest_data)
        
        # Process continent data for cases visualization
        df_continents = filter_continent_data(df)
        df_pivot = pivot_continent_data(df_continents)
        
        # Generate visualizations
        deaths_chart = create_deaths_by_continent_chart(continent_deaths)
        cases_chart = create_cases_comparison_chart(df_pivot)
        
        print(f"Visualizations created: '{deaths_chart}', '{cases_chart}'")
    else:
        print("Could not load data to generate visualizations.")


if __name__ == "__main__":
    main()