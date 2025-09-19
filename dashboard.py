"""
Interactive COVID-19 dashboard using Streamlit.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data_fetcher import fetch_covid_data, filter_country_data
from data_processor import get_latest_data_by_country, calculate_continent_deaths
from visualizer import create_deaths_by_continent_chart, create_cases_comparison_chart


# Set page configuration
st.set_page_config(
    page_title="COVID-19 Data Visualization Dashboard",
    page_icon="📊",
    layout="wide"
)


@st.cache_data
def load_data():
    """Load and cache the COVID-19 data."""
    df = fetch_covid_data()
    return df


def main():
    # Title and description
    st.title("📊 COVID-19 Data Visualization Dashboard")
    st.markdown("""
    This dashboard provides interactive visualizations of global COVID-19 data.
    The data is sourced from [Our World in Data](https://ourworldindata.org/coronavirus-source-data).
    """)
    
    # Load data
    with st.spinner("Loading data..."):
        df = load_data()
    
    if df.empty:
        st.error("Failed to load data. Please try again later.")
        return
    
    # Sidebar for filters
    st.sidebar.header("Filters")
    
    # Date range selector
    min_date = df['date'].min().date()
    max_date = df['date'].max().date()
    
    start_date = st.sidebar.date_input("Start date", min_date, min_value=min_date, max_value=max_date)
    end_date = st.sidebar.date_input("End date", max_date, min_value=min_date, max_value=max_date)
    
    # Filter data by date range
    df_filtered = df[(df['date'].dt.date >= start_date) & (df['date'].dt.date <= end_date)]
    
    # Filter for country data only
    df_countries = filter_country_data(df_filtered)
    
    # Continent selector
    continents = ['All'] + sorted(df_countries['continent'].dropna().unique().tolist())
    selected_continent = st.sidebar.selectbox("Select continent", continents)
    
    if selected_continent != 'All':
        df_countries = df_countries[df_countries['continent'] == selected_continent]
    
    # Main content
    tab1, tab2, tab3 = st.tabs(["Overview", "Visualizations", "Data Explorer"])
    
    with tab1:
        st.header("Data Overview")
        
        # Key metrics
        latest_data = get_latest_data_by_country(df_countries)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Countries", latest_data['location'].nunique())
        
        with col2:
            total_cases = latest_data['total_cases'].sum()
            st.metric("Total Cases", f"{total_cases:,.0f}")
        
        with col3:
            total_deaths = latest_data['total_deaths'].sum()
            st.metric("Total Deaths", f"{total_deaths:,.0f}")
        
        with col4:
            avg_fatality_rate = (total_deaths / total_cases) * 100 if total_cases > 0 else 0
            st.metric("Avg Fatality Rate", f"{avg_fatality_rate:.2f}%")
        
        # Deaths by continent chart
        st.subheader("Average Deaths per Million by Continent")
        continent_deaths = calculate_continent_deaths(latest_data)
        
        if not continent_deaths.empty:
            fig = px.bar(
                x=continent_deaths.index,
                y=continent_deaths.values,
                labels={'x': 'Continent', 'y': 'Average Deaths per Million'},
                color=continent_deaths.values,
                color_continuous_scale='blues'
            )
            fig.update_layout(
                xaxis_tickangle=-45,
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.header("Interactive Visualizations")
        
        # Time series chart
        st.subheader("COVID-19 Cases Over Time")
        
        # Aggregate data by date
        daily_data = df_countries.groupby('date').agg({
            'new_cases_smoothed': 'sum',
            'new_deaths_smoothed': 'sum'
        }).reset_index()
        
        # Create time series chart
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=daily_data['date'],
            y=daily_data['new_cases_smoothed'],
            mode='lines',
            name='New Cases (Smoothed)',
            line=dict(color='blue')
        ))
        fig.add_trace(go.Scatter(
            x=daily_data['date'],
            y=daily_data['new_deaths_smoothed'],
            mode='lines',
            name='New Deaths (Smoothed)',
            line=dict(color='red')
        ))
        fig.update_layout(
            title="Global COVID-19 Cases and Deaths Over Time",
            xaxis_title="Date",
            yaxis_title="Count",
            height=600
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Scatter plot: GDP vs Cases
        st.subheader("Total Cases vs GDP per Capita")
        scatter_data = latest_data.dropna(subset=['gdp_per_capita', 'total_cases_per_million'])
        
        if not scatter_data.empty:
            fig = px.scatter(
                scatter_data,
                x='gdp_per_capita',
                y='total_cases_per_million',
                color='continent',
                hover_name='location',
                size='population',
                log_x=True,
                size_max=60
            )
            fig.update_layout(
                title="Total Cases per Million vs GDP per Capita",
                xaxis_title="GDP per Capita (log scale)",
                yaxis_title="Total Cases per Million",
                height=600
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.header("Data Explorer")
        st.markdown("Explore the raw data used in this dashboard.")
        
        # Display data table
        st.dataframe(df_countries, use_container_width=True)
        
        # Download button
        csv = df_countries.to_csv(index=False)
        st.download_button(
            label="Download filtered data as CSV",
            data=csv,
            file_name="covid_data_filtered.csv",
            mime="text/csv"
        )


if __name__ == "__main__":
    main()