"""
Data loading and validation utilities.
Centralizes all data I/O so both notebooks and dashboard use the same logic.
"""

import pandas as pd
import sys
from pathlib import Path

# Add project root to path so config is importable
sys.path.insert(0, str(Path(__file__).parent.parent))
from config.settings import DAILY_AQI_FILE, HOURLY_POLLUTANTS_FILE, DATE_COL, DATETIME_COL


def load_daily_aqi() -> pd.DataFrame:
    """
    Load and return the cleaned daily AQI dataset.
    
    Returns:
        pd.DataFrame with 'Date' column parsed as datetime.
    """
    df = pd.read_csv(DAILY_AQI_FILE)
    df[DATE_COL] = pd.to_datetime(df[DATE_COL])
    return df


def load_hourly_pollutants() -> pd.DataFrame:
    """
    Load and return the cleaned hourly pollutant dataset.
    
    Returns:
        pd.DataFrame with 'Datetime' column parsed as datetime.
    """
    df = pd.read_csv(HOURLY_POLLUTANTS_FILE)
    df[DATETIME_COL] = pd.to_datetime(df[DATETIME_COL])
    return df


def validate_daily_aqi(df: pd.DataFrame) -> dict:
    """Run basic data quality checks on the daily AQI dataframe."""
    return {
        "rows": len(df),
        "null_dates": int(df[DATE_COL].isna().sum()),
        "null_aqi": int(df['AQI'].isna().sum()),
        "date_range": f"{df[DATE_COL].min().date()} to {df[DATE_COL].max().date()}",
    }


def validate_hourly_pollutants(df: pd.DataFrame) -> dict:
    """Run basic data quality checks on the hourly pollutant dataframe."""
    return {
        "rows": len(df),
        "null_datetimes": int(df[DATETIME_COL].isna().sum()),
        "columns": list(df.columns),
        "datetime_range": f"{df[DATETIME_COL].min()} to {df[DATETIME_COL].max()}",
    }
