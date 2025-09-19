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
        print("Starting data fetch...")
        df = pd.read_csv(url)
        print(f"Data fetch complete. Shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    df = fetch_covid_data()
    if not df.empty:
        print("Data fetch successful!")
        print(df.head())
    else:
        print("Data fetch failed.")