"""
Module for processing COVID-19 data.
"""
import pandas as pd


def get_latest_data_by_country(df_countries):
    """
    Get the latest data for each country.
    
    Parameters:
    df_countries (pandas.DataFrame): DataFrame containing country-level data
    
    Returns:
    pandas.DataFrame: DataFrame with the latest data for each country
    """
    if not df_countries.empty:
        latest_data = df_countries.loc[df_countries.groupby('location')['date'].idxmax()]
        return latest_data
    return df_countries


def calculate_continent_deaths(latest_data):
    """
    Calculate the mean of total_deaths_per_million for each continent.
    
    Parameters:
    latest_data (pandas.DataFrame): DataFrame with the latest data for each country
    
    Returns:
    pandas.Series: Series with continents as index and mean deaths per million as values
    """
    if not latest_data.empty:
        continent_deaths = latest_data.groupby('continent')['total_deaths_per_million'].mean().sort_values(ascending=False)
        return continent_deaths
    return pd.Series()


def pivot_continent_data(df_continents):
    """
    Pivot the continent data for easier plotting.
    
    Parameters:
    df_continents (pandas.DataFrame): DataFrame containing continent-level data
    
    Returns:
    pandas.DataFrame: Pivoted DataFrame with dates as index and continents as columns
    """
    if not df_continents.empty:
        df_pivot = df_continents.pivot(index='date', columns='location', values='new_cases_smoothed')
        return df_pivot
    return pd.DataFrame()