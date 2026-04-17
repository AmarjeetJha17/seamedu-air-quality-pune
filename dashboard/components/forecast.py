"""Tab 6: SARIMAX Forecast visualization."""

import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from src.model import prepare_timeseries, fit_sarimax, forecast_aqi


def render(daily):
    """Render the SARIMAX Forecast tab."""
    st.subheader("SARIMAX Forecast – Pune AQI 2025–2026")

    # Prepare data and fit model
    daily_ts = prepare_timeseries(daily)
    model_fit = fit_sarimax(daily_ts)
    forecast_df = forecast_aqi(model_fit)

    # Plot: last 1 year actual + 2-year forecast
    fig = px.line(daily_ts[-365:], title="Last 1 Year Actual + 2-Year Forecast")
    fig.add_scatter(
        x=forecast_df['Date'], y=forecast_df['Forecast'],
        mode='lines', name='Forecast',
        line=dict(color='red', dash='dash')
    )
    fig.add_scatter(
        x=forecast_df['Date'], y=forecast_df['Lower_CI'],
        mode='lines', name='95% Lower',
        line=dict(color='rgba(255,0,0,0.3)'), showlegend=False
    )
    fig.add_scatter(
        x=forecast_df['Date'], y=forecast_df['Upper_CI'],
        mode='lines', name='95% Upper',
        line=dict(color='rgba(255,0,0,0.3)'),
        fill='tonexty', fillcolor='rgba(255,0,0,0.1)'
    )
    fig.update_layout(height=600, title_font_size=18)
    st.plotly_chart(fig, use_container_width=True)

    # Summary metric
    avg_forecast = forecast_df['Forecast'].mean()
    delta_text = '↑ Worse' if avg_forecast > daily_ts.mean() else '↓ Better'
    st.metric(
        "Predicted Average AQI (2025–2026)",
        f"{avg_forecast:.0f}",
        delta=f"{delta_text} than historical"
    )

    st.info(
        "**Key Insight**: Winter spikes are expected to continue through 2025–2026. "
        "Stronger winter-specific interventions are needed."
    )
