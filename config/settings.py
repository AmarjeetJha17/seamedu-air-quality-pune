"""
Central configuration for the Seamedu Air Quality Pune project.
All paths, model parameters, and column definitions live here.
"""

from pathlib import Path

# ======================== PATHS ========================
PROJECT_ROOT = Path(__file__).parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
OUTPUTS_FIGURES = PROJECT_ROOT / "outputs" / "figures"
OUTPUTS_REPORTS = PROJECT_ROOT / "outputs" / "reports"

# ======================== DATA FILES ========================
DAILY_AQI_FILE = DATA_PROCESSED / "cleaned_daily_aqi.csv"
HOURLY_POLLUTANTS_FILE = DATA_PROCESSED / "cleaned_hourly_pollutants.csv"

# ======================== MODEL PARAMETERS ========================
SARIMAX_ORDER = (5, 1, 0)
SARIMAX_SEASONAL_ORDER = (1, 0, 0, 7)
FORECAST_STEPS = 730  # ~2 years

# ======================== COLUMN DEFINITIONS ========================
POLLUTANT_COLS = ['CO', 'NH3', 'NO2', 'OZONE', 'PM10', 'PM2.5', 'SO2']
DATE_COL = 'Date'
DATETIME_COL = 'Datetime'
AQI_COL = 'AQI'
SEASON_COL = 'Season'
