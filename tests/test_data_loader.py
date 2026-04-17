"""
Basic tests for the data loading module.
Run with: python -m pytest tests/ -v
"""

import sys
from pathlib import Path

# Ensure project root is importable
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data_loader import load_daily_aqi, load_hourly_pollutants, validate_daily_aqi


def test_daily_aqi_loads():
    """Test that the daily AQI dataset loads without errors."""
    df = load_daily_aqi()
    assert not df.empty, "Daily AQI dataframe is empty"
    assert 'Date' in df.columns, "Missing 'Date' column"
    assert 'AQI' in df.columns, "Missing 'AQI' column"


def test_hourly_pollutants_loads():
    """Test that the hourly pollutant dataset loads without errors."""
    df = load_hourly_pollutants()
    assert not df.empty, "Hourly pollutants dataframe is empty"
    assert 'Datetime' in df.columns, "Missing 'Datetime' column"


def test_no_null_dates():
    """Test that there are no null dates in the daily dataset."""
    df = load_daily_aqi()
    assert df['Date'].isna().sum() == 0, "Found null values in Date column"


def test_aqi_values_positive():
    """Test that AQI values are non-negative."""
    df = load_daily_aqi()
    assert (df['AQI'] >= 0).all(), "Found negative AQI values"


def test_daily_validation():
    """Test the data validation function returns expected keys."""
    df = load_daily_aqi()
    report = validate_daily_aqi(df)
    assert "rows" in report
    assert "null_dates" in report
    assert "date_range" in report
    assert report["null_dates"] == 0
