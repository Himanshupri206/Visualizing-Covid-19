"""
Module for generating visualizations of COVID-19 data.
"""
import matplotlib.pyplot as plt
from config import CHART_COLORS, CHART_SIZES, DEATHS_CHART_FILENAME, CASES_CHART_FILENAME


def create_deaths_by_continent_chart(continent_deaths, filename=DEATHS_CHART_FILENAME):
    """
    Create a bar chart showing average deaths per million by continent.
    
    Parameters:
    continent_deaths (pandas.Series): Series with continents as index and mean deaths per million as values
    filename (str): Name of the file to save the chart to
    
    Returns:
    str: Path to the saved chart
    """
    plt.figure(figsize=CHART_SIZES['deaths_by_continent'])
    continent_deaths.plot(kind='bar', color=CHART_COLORS['deaths_by_continent'])
    plt.title('Average Deaths per Million by Continent')
    plt.xlabel('Continent')
    plt.ylabel('Deaths per Million')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    
    return filename


def create_cases_comparison_chart(df_pivot, filename=CASES_CHART_FILENAME):
    """
    Create a line chart comparing smoothed new cases between Europe and Asia.
    
    Parameters:
    df_pivot (pandas.DataFrame): Pivoted DataFrame with dates as index and continents as columns
    filename (str): Name of the file to save the chart to
    
    Returns:
    str: Path to the saved chart
    """
    plt.figure(figsize=CHART_SIZES['cases_comparison'])
    df_pivot['Europe'].plot(label='Europe')
    df_pivot['Asia'].plot(label='Asia')
    plt.title('Smoothed New Cases in Europe and Asia')
    plt.xlabel('Date')
    plt.ylabel('Smoothed New Cases')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    
    return filename