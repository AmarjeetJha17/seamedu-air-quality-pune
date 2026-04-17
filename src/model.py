"""
Statistical modeling and forecasting logic.
Contains ARIMA fitting, forecasting, and helper functions.
"""

import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from config.settings import SARIMAX_ORDER, SARIMAX_SEASONAL_ORDER, FORECAST_STEPS


def prepare_timeseries(daily_df: pd.DataFrame) -> pd.Series:
    """
    Convert daily AQI dataframe to a date-indexed time series
    suitable for SARIMAX modeling.
    
    Args:
        daily_df: DataFrame with 'Date' and 'AQI' columns.
    
    Returns:
        pd.Series with daily frequency, forward-filled.
    """
    ts = daily_df.set_index('Date')['AQI'].asfreq('D')
    ts = ts.ffill()
    return ts


def fit_sarimax(series: pd.Series, order: tuple = SARIMAX_ORDER, seasonal_order: tuple = SARIMAX_SEASONAL_ORDER):
    """
    Fit a SARIMAX model on the given time series.
    
    Args:
        series: Date-indexed AQI series.
        order: SARIMAX (p, d, q) order. Defaults to config setting.
        seasonal_order: SARIMAX (P, D, Q, s) seasonal order. Defaults to config setting.
    
    Returns:
        Fitted SARIMAX model results.
    """
    model = SARIMAX(series, order=order, seasonal_order=seasonal_order, enforce_stationarity=False, enforce_invertibility=False)
    return model.fit(disp=False)


def forecast_aqi(model_fit, steps: int = FORECAST_STEPS) -> pd.DataFrame:
    """
    Generate AQI forecast with confidence intervals.
    
    Args:
        model_fit: Fitted SARIMAX model.
        steps: Number of days to forecast.
    
    Returns:
        DataFrame with columns: Date, Forecast, Lower_CI, Upper_CI
    """
    forecast = model_fit.get_forecast(steps=steps)
    forecast_index = pd.date_range(
        start=model_fit.fittedvalues.index[-1] + pd.Timedelta(days=1),
        periods=steps,
        freq='D'
    )
    conf_int = forecast.conf_int()

    return pd.DataFrame({
        'Date': forecast_index,
        'Forecast': np.maximum(0, forecast.predicted_mean.values),
        'Lower_CI': np.maximum(0, conf_int.iloc[:, 0].values),
        'Upper_CI': np.maximum(0, conf_int.iloc[:, 1].values),
    })
