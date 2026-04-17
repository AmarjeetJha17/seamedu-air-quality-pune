"""
Seamedu Air Quality Pune — Streamlit Dashboard
================================================
Slim entry point. All tab logic lives in dashboard/components/.
Run with: streamlit run dashboard/app.py
"""

import sys
from pathlib import Path
import warnings

# Ensure project root is on the path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from src.data_loader import load_daily_aqi, load_hourly_pollutants
from dashboard.components import (
    aqi_trend,
    seasonal,
    correlations,
    year_over_year,
    hourly_analysis,
    forecast,
    sidebar,
)

warnings.filterwarnings("ignore")

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Pune Air Quality | Seamedu Awards 2026",
    layout="wide",
    page_icon="🌬️",
)

st.title("🌬️ Pune Air Quality Analysis (2017–2024) + 2025–2026 Forecast")
st.markdown("**Data Analytics Excellence Award** – Seamedu Awards 2026")
st.caption("Live Interactive Dashboard | Built with Python, Plotly & Streamlit")

# ====================== LOAD DATA ======================
@st.cache_data
def load_data():
    daily = load_daily_aqi()
    hourly = load_hourly_pollutants()
    return daily, hourly

daily, hourly = load_data()

# ====================== TABS ======================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📈 AQI Trend",
    "📊 Seasonal Analysis",
    "🔥 Pollutant Correlations",
    "📅 Year-over-Year",
    "⏰ Hourly PM2.5 vs PM10",
    "🔮 2025–2026 Forecast",
])

with tab1:
    aqi_trend.render(daily)

with tab2:
    seasonal.render(daily)

with tab3:
    correlations.render(hourly)

with tab4:
    year_over_year.render(daily)

with tab5:
    hourly_analysis.render(hourly)

with tab6:
    forecast.render(daily)

# ====================== SIDEBAR ======================
sidebar.render()

st.caption("Dashboard ready")
