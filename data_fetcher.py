"""
Module for fetching COVID-19 data from Our World in Data.
"""
import pandas as pd


def fetch_covid_data(url="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"):
    """
    Fetch COVID-19 data from Our World in Data.
    
    Parameters:
    url (str): URL to the CSV file containing COVID-19 data
    
    Returns:
    pandas.DataFrame: DataFrame containing the fetched data
    """
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()


def filter_country_data(df):
    """
    Filter the DataFrame to include only country-level data.
    
    Parameters:
    df (pandas.DataFrame): DataFrame containing COVID-19 data
    
    Returns:
    pandas.DataFrame: Filtered DataFrame containing only country-level data
    """
    if not df.empty:
        # Convert 'date' column to datetime
        df['date'] = pd.to_datetime(df['date'])
        
        # Filter out aggregate data (rows for continents, etc.)
        df_countries = df[df['continent'].notna()].copy()
        return df_countries
    return df


def filter_continent_data(df):
    """
    Filter the DataFrame to include only continent-level data.
    
    Parameters:
    df (pandas.DataFrame): DataFrame containing COVID-19 data
    
    Returns:
    pandas.DataFrame: Filtered DataFrame containing only continent-level data
    """
    if not df.empty:
        # Convert 'date' column to datetime
        df['date'] = pd.to_datetime(df['date'])
        
        # Filter for continent data
        df_continents = df[df['continent'].isna() & df['location'].isin(['Europe', 'Asia'])]
        return df_continents
    return df