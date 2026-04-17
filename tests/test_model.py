"""
Basic tests for the SARIMAX model module.
Run with: python -m pytest tests/ -v
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data_loader import load_daily_aqi
from src.model import prepare_timeseries, fit_sarimax, forecast_aqi


def test_prepare_timeseries():
    """Test that the time series is properly prepared."""
    df = load_daily_aqi()
    ts = prepare_timeseries(df)
    assert not ts.empty, "Time series is empty"
    assert ts.index.freq == 'D', "Expected daily frequency"
    assert ts.isna().sum() == 0, "Time series has NaN values after ffill"


def test_sarimax_fit():
    """Test that SARIMAX model fits without errors."""
    df = load_daily_aqi()
    ts = prepare_timeseries(df)
    model_fit = fit_sarimax(ts)
    assert model_fit is not None, "Model fit returned None"


def test_forecast_output_shape():
    """Test that forecast output has expected columns and length."""
    df = load_daily_aqi()
    ts = prepare_timeseries(df)
    model_fit = fit_sarimax(ts)
    forecast_df = forecast_aqi(model_fit, steps=30)  # short forecast for speed
    assert len(forecast_df) == 30
    assert 'Date' in forecast_df.columns
    assert 'Forecast' in forecast_df.columns
    assert 'Lower_CI' in forecast_df.columns
    assert 'Upper_CI' in forecast_df.columns
