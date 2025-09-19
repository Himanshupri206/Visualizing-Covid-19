import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from Our World in Data
try:
    df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
except Exception as e:
    print(f"Error loading data: {e}")
    df = pd.DataFrame()

if not df.empty:
    # --- Preprocessing ---
    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Filter out aggregate data (rows for continents, etc.)
    df_countries = df[df['continent'].notna()].copy()

    # --- Bar chart: deaths_per_million across continents ---
    # Get the latest data for each country
    latest_data = df_countries.loc[df_countries.groupby('location')['date'].idxmax()]
    # Calculate the mean of total_deaths_per_million for each continent
    continent_deaths = latest_data.groupby('continent')['total_deaths_per_million'].mean().sort_values(ascending=False)

    plt.figure(figsize=(12, 6))
    continent_deaths.plot(kind='bar')
    plt.title('Average Deaths per Million by Continent')
    plt.xlabel('Continent')
    plt.ylabel('Deaths per Million')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('deaths_per_million_by_continent.png')
    plt.close()

    # --- Line chart: new_cases_smoothed for Europe and Asia ---
    # Use the continental data provided in the dataset
    df_continents = df[df['continent'].isna() & df['location'].isin(['Europe', 'Asia'])]
    
    # Pivot the data to plot easily
    df_pivot = df_continents.pivot(index='date', columns='location', values='new_cases_smoothed')

    plt.figure(figsize=(14, 7))
    df_pivot['Europe'].plot(label='Europe')
    df_pivot['Asia'].plot(label='Asia')
    plt.title('Smoothed New Cases in Europe and Asia')
    plt.xlabel('Date')
    plt.ylabel('Smoothed New Cases')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('new_cases_smoothed_europe_asia.png')
    plt.close()

    print("Visualizations created: 'deaths_per_million_by_continent.png', 'new_cases_smoothed_europe_asia.png'")
else:
    print("Could not load data to generate visualizations.")