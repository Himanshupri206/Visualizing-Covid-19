"""
Enhanced COVID-19 visualization script with additional chart types.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def fetch_data():
    """Fetch COVID-19 data from Our World in Data."""
    try:
        df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()


def preprocess_data(df):
    """Preprocess the data."""
    if not df.empty:
        # Convert 'date' column to datetime
        df['date'] = pd.to_datetime(df['date'])
        
        # Filter out aggregate data (rows for continents, etc.)
        df_countries = df[df['continent'].notna()].copy()
        return df_countries
    return df


def create_deaths_by_continent_chart(df_countries):
    """Create a bar chart showing average deaths per million by continent."""
    # Get the latest data for each country
    latest_data = df_countries.loc[df_countries.groupby('location')['date'].idxmax()]
    # Calculate the mean of total_deaths_per_million for each continent
    continent_deaths = latest_data.groupby('continent')['total_deaths_per_million'].mean().sort_values(ascending=False)

    plt.figure(figsize=(12, 6))
    bars = plt.bar(continent_deaths.index, continent_deaths.values, color='skyblue')
    plt.title('Average Deaths per Million by Continent', fontsize=16)
    plt.xlabel('Continent', fontsize=12)
    plt.ylabel('Deaths per Million', fontsize=12)
    plt.xticks(rotation=45)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.1f}',
                 ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('deaths_per_million_by_continent_enhanced.png')
    plt.close()
    
    return 'deaths_per_million_by_continent_enhanced.png'


def create_cases_comparison_chart(df):
    """Create a line chart comparing smoothed new cases between Europe and Asia."""
    # Use the continental data provided in the dataset
    df_continents = df[df['continent'].isna() & df['location'].isin(['Europe', 'Asia'])]
    
    # Pivot the data to plot easily
    df_pivot = df_continents.pivot(index='date', columns='location', values='new_cases_smoothed')

    plt.figure(figsize=(14, 7))
    plt.plot(df_pivot.index, df_pivot['Europe'], label='Europe', linewidth=2)
    plt.plot(df_pivot.index, df_pivot['Asia'], label='Asia', linewidth=2)
    plt.title('Smoothed New Cases in Europe and Asia', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Smoothed New Cases', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('new_cases_smoothed_europe_asia_enhanced.png')
    plt.close()
    
    return 'new_cases_smoothed_europe_asia_enhanced.png'


def create_vaccination_scatter_plot(df_countries):
    """Create a scatter plot comparing vaccination rates vs. death rates."""
    # Get the latest data for each country
    latest_data = df_countries.loc[df_countries.groupby('location')['date'].idxmax()]
    
    # Filter out countries with missing data
    scatter_data = latest_data.dropna(subset=['people_fully_vaccinated_per_hundred', 'total_deaths_per_million'])
    
    plt.figure(figsize=(12, 8))
    
    if not scatter_data.empty:
        plt.scatter(scatter_data['people_fully_vaccinated_per_hundred'], 
                    scatter_data['total_deaths_per_million'], 
                    alpha=0.6, 
                    s=60)
        
        # Add trend line only if we have data
        if len(scatter_data) > 1:
            z = np.polyfit(scatter_data['people_fully_vaccinated_per_hundred'], 
                           scatter_data['total_deaths_per_million'], 1)
            p = np.poly1d(z)
            plt.plot(scatter_data['people_fully_vaccinated_per_hundred'], 
                     p(scatter_data['people_fully_vaccinated_per_hundred']), 
                     "r--", alpha=0.8)
    
    plt.title('Vaccination Rates vs. Death Rates by Country', fontsize=16)
    plt.xlabel('People Fully Vaccinated per Hundred', fontsize=12)
    plt.ylabel('Total Deaths per Million', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('vaccination_vs_deaths_scatter.png')
    plt.close()
    
    return 'vaccination_vs_deaths_scatter.png'


def create_case_progression_area_chart(df_countries):
    """Create a stacked area chart for case progression by continent."""
    # Group by continent and date, then sum new cases
    continent_cases = df_countries.groupby(['continent', 'date'])['new_cases_smoothed'].sum().reset_index()
    
    if continent_cases.empty:
        # Create empty chart if no data
        plt.figure(figsize=(14, 8))
        plt.title('COVID-19 Case Progression by Continent', fontsize=16)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Smoothed New Cases', fontsize=12)
        plt.text(0.5, 0.5, 'No data available', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.tight_layout()
        plt.savefig('case_progression_by_continent.png')
        plt.close()
        return 'case_progression_by_continent.png'
    
    # Pivot the data
    pivot_data = continent_cases.pivot(index='date', columns='continent', values='new_cases_smoothed').fillna(0)
    
    # Resample to monthly frequency for better visualization
    pivot_monthly = pivot_data.resample('M').sum()
    
    plt.figure(figsize=(14, 8))
    plt.stackplot(pivot_monthly.index, 
                  pivot_monthly.T.values, 
                  labels=pivot_monthly.columns,
                  alpha=0.8)
    
    plt.title('COVID-19 Case Progression by Continent', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Smoothed New Cases', fontsize=12)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('case_progression_by_continent.png')
    plt.close()
    
    return 'case_progression_by_continent.png'


def main():
    # Fetch and preprocess data
    print("Fetching data...")
    df = fetch_data()
    
    if not df.empty:
        print("Preprocessing data...")
        df_countries = preprocess_data(df)
        
        # Generate visualizations
        print("Creating deaths by continent chart...")
        deaths_chart = create_deaths_by_continent_chart(df_countries)
        
        print("Creating cases comparison chart...")
        cases_chart = create_cases_comparison_chart(df)
        
        print("Creating vaccination scatter plot...")
        vaccination_chart = create_vaccination_scatter_plot(df_countries)
        
        print("Creating case progression area chart...")
        progression_chart = create_case_progression_area_chart(df_countries)
        
        print(f"Visualizations created:")
        print(f"  - {deaths_chart}")
        print(f"  - {cases_chart}")
        print(f"  - {vaccination_chart}")
        print(f"  - {progression_chart}")
    else:
        print("Could not load data to generate visualizations.")


if __name__ == "__main__":
    main()