"""
Test all components of the COVID-19 visualization project.
"""
import os
from data_fetcher import fetch_covid_data
from data_processor import get_latest_data_by_country, calculate_continent_deaths
from visualizer import create_deaths_by_continent_chart

def test_data_fetching():
    """Test data fetching functionality."""
    print("Testing data fetching...")
    df = fetch_covid_data()
    if not df.empty:
        print(f"✓ Data fetching successful. Shape: {df.shape}")
        return True
    else:
        print("✗ Data fetching failed.")
        return False

def test_data_processing():
    """Test data processing functionality."""
    print("Testing data processing...")
    df = fetch_covid_data()
    if not df.empty:
        latest_data = get_latest_data_by_country(df)
        continent_deaths = calculate_continent_deaths(latest_data)
        if not continent_deaths.empty:
            print("✓ Data processing successful.")
            return True
        else:
            print("✗ Data processing failed.")
            return False
    else:
        print("✗ Data processing failed - no data to process.")
        return False

def test_visualization():
    """Test visualization functionality."""
    print("Testing visualization...")
    df = fetch_covid_data()
    if not df.empty:
        latest_data = get_latest_data_by_country(df)
        continent_deaths = calculate_continent_deaths(latest_data)
        if not continent_deaths.empty:
            filename = create_deaths_by_continent_chart(continent_deaths, 'output/test_chart.png')
            if os.path.exists(filename):
                print(f"✓ Visualization successful. File created: {filename}")
                return True
            else:
                print("✗ Visualization failed - file not created.")
                return False
        else:
            print("✗ Visualization failed - no data to visualize.")
            return False
    else:
        print("✗ Visualization failed - no data to visualize.")
        return False

def main():
    """Run all tests."""
    print("Testing all components of the COVID-19 visualization project...\n")
    
    tests = [
        test_data_fetching,
        test_data_processing,
        test_visualization
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()  # Add a blank line between tests
    
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The modular components are working correctly.")
    else:
        print("❌ Some tests failed. Please check the implementation.")

if __name__ == "__main__":
    main()