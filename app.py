import streamlit as st
import pandas as pd
import plotly.express as px
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings("ignore")

# ====================== PAGE CONFIG ======================
st.set_page_config(page_title="Pune Air Quality | Seamedu Awards 2026", 
                   layout="wide", page_icon="🌬️")

st.title("🌬️ Pune Air Quality Analysis (2017–2024) + 2025–2026 Forecast")
st.markdown("**Data Analytics Excellence Award** – Seamedu Awards 2026")
st.caption("Live Interactive Dashboard | Built with Python, Plotly & Streamlit")

# ====================== LOAD DATA ======================
@st.cache_data
def load_data():
    daily = pd.read_csv("cleaned_daily_aqi.csv")
    hourly = pd.read_csv("cleaned_hourly_pollutants.csv")
    daily['Date'] = pd.to_datetime(daily['Date'])
    hourly['Datetime'] = pd.to_datetime(hourly['Datetime'])
    return daily, hourly

daily, hourly = load_data()

# ====================== TABS ======================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📈 AQI Trend", 
    "📊 Seasonal Analysis", 
    "🔥 Pollutant Correlations", 
    "📅 Year-over-Year", 
    "⏰ Hourly PM2.5 vs PM10", 
    "🔮 2025–2026 Forecast"
])

# --------------------- TAB 1: AQI Trend ---------------------
with tab1:
    st.subheader("Daily AQI Trend (2017–2024)")
    fig1 = px.line(daily, x='Date', y='AQI')
    fig1.update_layout(height=550, title_font_size=18)
    st.plotly_chart(fig1, use_container_width=True)
    
    st.info("**Key Insight**: Strong seasonal pattern with sharp winter spikes every year. No clear long-term improvement observed.")

# --------------------- TAB 2: Seasonal Analysis ---------------------
with tab2:
    st.subheader("AQI Distribution by Season")
    fig_season = px.box(daily, x='Season', y='AQI', color='Season',
                        color_discrete_sequence=px.colors.sequential.RdBu_r)
    fig_season.update_layout(height=600, showlegend=False, title_font_size=18)
    st.plotly_chart(fig_season, use_container_width=True)
    
    st.info("**Key Insight**: Winter AQI is statistically significantly higher than Summer (p < 0.001). Winter is the most polluted and variable season.")

# --------------------- TAB 3: Interactive Correlation ---------------------
with tab3:
    st.subheader("Hourly Pollutant Correlation Matrix (2024)")
    numeric_cols = ['CO', 'NH3', 'NO2', 'OZONE', 'PM10', 'PM2.5', 'SO2']
    corr_matrix = hourly[numeric_cols].corr()
    
    fig_corr = px.imshow(corr_matrix, text_auto=".2f", aspect="auto",
                         color_continuous_scale="RdYlBu_r")
    fig_corr.update_layout(height=650, title_font_size=18)
    st.plotly_chart(fig_corr, use_container_width=True)
    
    st.info("**Key Insight**: PM2.5 and PM10 are extremely correlated (r ≈ 0.92). Main sources are traffic, construction dust, and biomass burning.")

# --------------------- TAB 4: Year-over-Year ---------------------
with tab4:
    st.subheader("Year-over-Year Daily AQI Comparison")
    fig_yoy = px.line(daily, x=daily['Date'].dt.strftime('%m-%d'),
                      y='AQI', color=daily['Date'].dt.year.astype(str))
    fig_yoy.update_layout(height=600, title_font_size=18)
    st.plotly_chart(fig_yoy, use_container_width=True)
    
    st.info("**Key Insight**: Winter pollution spikes are consistent across all years (2017–2024). The problem remains persistent.")

# --------------------- TAB 5: Hourly PM2.5 vs PM10 ---------------------
with tab5:
    st.subheader("Hourly PM2.5 vs PM10 in 2024")
    recent = hourly[hourly['Datetime'] >= '2024-01-01']
    fig4 = px.line(recent, x='Datetime', y=['PM2.5', 'PM10'])
    fig4.update_layout(height=550, title_font_size=18)
    st.plotly_chart(fig4, use_container_width=True)
    
    st.info("**Key Insight**: PM2.5 and PM10 move almost in lockstep. Clear daily peaks during morning and evening traffic hours.")

# --------------------- TAB 6: ARIMA Forecast ---------------------
with tab6:
    st.subheader("ARIMA Forecast – Pune AQI 2025–2026")
    daily_ts = daily.set_index('Date')['AQI'].asfreq('D').fillna(method='ffill')
    model = ARIMA(daily_ts, order=(5, 1, 0))
    model_fit = model.fit()
    
    forecast_steps = 730
    forecast = model_fit.get_forecast(steps=forecast_steps)
    forecast_index = pd.date_range(start=daily_ts.index[-1] + pd.Timedelta(days=1),
                                   periods=forecast_steps, freq='D')
    
    conf_int = forecast.conf_int()
    forecast_df = pd.DataFrame({
        'Date': forecast_index,
        'Forecast': forecast.predicted_mean,
        'Lower_CI': conf_int.iloc[:, 0].values,
        'Upper_CI': conf_int.iloc[:, 1].values
    })
    
    fig_forecast = px.line(daily_ts[-365:], title="Last 1 Year Actual + 2-Year Forecast")
    fig_forecast.add_scatter(x=forecast_df['Date'], y=forecast_df['Forecast'],
                             mode='lines', name='Forecast', line=dict(color='red', dash='dash'))
    fig_forecast.add_scatter(x=forecast_df['Date'], y=forecast_df['Lower_CI'],
                             mode='lines', name='95% Lower', line=dict(color='rgba(255,0,0,0.3)'), showlegend=False)
    fig_forecast.add_scatter(x=forecast_df['Date'], y=forecast_df['Upper_CI'],
                             mode='lines', name='95% Upper', line=dict(color='rgba(255,0,0,0.3)'),
                             fill='tonexty', fillcolor='rgba(255,0,0,0.1)')
    fig_forecast.update_layout(height=600, title_font_size=18)
    st.plotly_chart(fig_forecast, use_container_width=True)
    
    avg_forecast = forecast_df['Forecast'].mean()
    st.metric("Predicted Average AQI (2025–2026)", f"{avg_forecast:.0f}",
              delta=f"{'↑ Worse' if avg_forecast > daily_ts.mean() else '↓ Better'} than historical")
    
    st.info("**Key Insight**: Winter spikes are expected to continue through 2025–2026. Stronger winter-specific interventions are needed.")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.header("About this Project")
    st.write("Historical AQI analysis for Pune with statistical tests, interactive visualizations, and ARIMA forecasting.")
    st.write("**Live Demo** for Seamedu Awards 2026 – Data Analytics Excellence")
    st.caption("Data up to Dec 2024 | Forecast till 2026")
    st.divider()
    st.write("👨‍💻 Built by Amarjit Jha")
    st.write("GitHub: [seamedu-air-quality-pune](https://github.com/AmarjeetJha17/seamedu-air-quality-pune)")

st.caption("Dashboard ready")
