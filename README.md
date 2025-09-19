# COVID-19 Data Visualization Project

## Overview
This project provides visualizations of global COVID-19 data to help understand the pandemic's impact across different regions. The visualizations are generated from data provided by Our World in Data, which aggregates information from various sources including national health ministries and the World Health Organization.

## Features
- Bar chart showing average deaths per million by continent
- Line chart comparing smoothed new cases between Europe and Asia
- Interactive dashboard (coming soon)

## Data Source
The data is sourced from [Our World in Data](https://ourworldindata.org/coronavirus-source-data), specifically from their GitHub repository: https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv

## Installation
1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To generate the visualizations, simply run:
```bash
python covid_visualization.py
```

This will create two PNG files:
- `deaths_per_million_by_continent.png`
- `new_cases_smoothed_europe_asia.png`

## Requirements
- Python 3.7+
- Pandas
- Matplotlib

See [requirements.txt](requirements.txt) for specific versions.

## Project Structure
- [`covid_visualization.py`](file:///c%3A/Users/adnan/Desktop/Projects/Visualizing%20Covid-19/covid_visualization.py): Main script for generating visualizations
- [`requirements.txt`](file:///c%3A/Users/adnan/Desktop/Projects/Visualizing%20Covid-19/requirements.txt): Python package dependencies
- `*.png`: Generated visualization files

## Methodology
1. Data is fetched directly from Our World in Data's GitHub repository
2. Data preprocessing:
   - Convert date column to datetime format
   - Filter out aggregate data to focus on country-level information
3. Visualization generation:
   - Calculate average deaths per million by continent
   - Compare smoothed new cases between Europe and Asia

## Contributing
Feel free to fork this repository and submit pull requests with improvements or additional visualizations.

## License
This project is open source and available under the MIT License.