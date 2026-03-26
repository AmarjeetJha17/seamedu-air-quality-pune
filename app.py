import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Pune AQI Dashboard", layout="wide")
st.title("🏆 Pune Air Quality & Public Health Crisis")
st.markdown("**Seamedu Awards 2026 – Data Analytics Excellence Award**")

# Load cleaned data
daily = pd.read_csv("cleaned_daily_aqi.csv")

# Sidebar filter
st.sidebar.header("Filters")
year_filter = st.sidebar.multiselect("Select Year", 
                                    options=sorted(daily['Year'].unique()), 
                                    default=sorted(daily['Year'].unique()))

daily_filtered = daily[daily['Year'].isin(year_filter)]

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📈 AQI Trend", "🌡️ Seasonal Analysis", "🔥 Pollutant Correlations", "📊 Health Risk Regression"])

with tab1:
    st.subheader("Daily AQI Trend (2017–2024)")
    fig1 = px.line(daily_filtered, x='Date', y='AQI', title='Pune Daily AQI Trend')
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.subheader("AQI Distribution by Season")
    fig2 = px.box(daily_filtered, x='Season', y='AQI', color='Season', title='Seasonal Distribution')
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.subheader("Pollutant Correlation Heatmap (2024 Hourly)")
    st.image("pollutants_corelation_heatmap.png", use_column_width=True)
    st.caption("Strongest correlation: PM2.5 ↔ PM10 (r ≈ 0.92)")

with tab4:
    st.subheader("Linear Regression: AQI Trend with OLS Fit")
    # Fix: Use Time_Index (different column) for regression
    daily_filtered = daily_filtered.sort_values('Date').copy()
    daily_filtered['Time_Index'] = range(len(daily_filtered))
    
    fig_reg = px.scatter(daily_filtered, x='Time_Index', y='AQI', 
                         trendline="ols", 
                         title="Overall AQI Trend with Linear Regression (OLS)")
    st.plotly_chart(fig_reg, use_container_width=True)
    
    st.caption("Shows long-term AQI trend with best-fit line. Winter months consistently higher.")

st.success("Dashboard ready")
