"""
Configuration file for the COVID-19 visualization project.
"""
import os


# Data source configuration
DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

# Visualization configuration
CHART_COLORS = {
    'deaths_by_continent': '#1f77b4',
    'cases_comparison': ['#ff7f0e', '#2ca02c'],
    'vaccination_scatter': '#d62728',
    'case_progression': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
}

CHART_SIZES = {
    'deaths_by_continent': (12, 6),
    'cases_comparison': (14, 7),
    'vaccination_scatter': (12, 8),
    'case_progression': (14, 8)
}

# Dashboard configuration
DASHBOARD_TITLE = "COVID-19 Data Visualization Dashboard"
DASHBOARD_LAYOUT = "wide"

# File paths
OUTPUT_DIR = "output"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Chart filenames
DEATHS_CHART_FILENAME = os.path.join(OUTPUT_DIR, "deaths_per_million_by_continent.png")
CASES_CHART_FILENAME = os.path.join(OUTPUT_DIR, "new_cases_smoothed_europe_asia.png")
VACCINATION_CHART_FILENAME = os.path.join(OUTPUT_DIR, "vaccination_vs_deaths_scatter.png")
PROGRESSION_CHART_FILENAME = os.path.join(OUTPUT_DIR, "case_progression_by_continent.png")