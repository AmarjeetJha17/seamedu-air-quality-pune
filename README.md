# Seamedu Air Quality Pune 🌫️

**Data Analytics Excellence Award Project – Pune Air Quality & Public Health Crisis (Seamedu Awards 2026)**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)

## 🎯 Overview

**Seamedu Air Quality Pune** is a comprehensive **data analytics and visualization project** analyzing Pune’s Air Quality Index (AQI) and major pollutants from **2017 to 2024**.

The project uncovers critical seasonal patterns, pollutant correlations, statistical differences between winter and summer pollution, and builds predictive models (including Linear Regression and ARIMA forecasting) to quantify public health risks associated with PM2.5 levels.

It features:
- In-depth Exploratory Data Analysis (EDA) in a Colab notebook
- Statistical hypothesis testing
- ARIMA time-series forecasting
- Interactive **Streamlit dashboard** for real-time exploration
- Cleaned datasets and professional visualizations

**Live Dashboard**: [🔗 seamedu-air-quality-pune.streamlit.app](https://seamedu-air-quality-pune.streamlit.app/)

## 🔥 The Problem

Pune, one of India’s fastest-growing cities, is facing a severe and worsening air pollution crisis. High levels of PM2.5, PM10, CO, and other pollutants are directly linked to respiratory diseases, cardiovascular issues, and reduced life expectancy — especially during winter months when pollution peaks dramatically.

This project turns raw AQI data into actionable, data-driven insights for citizens, policymakers, researchers, and environmental agencies.

## 💡 Key Insights

- **Winter AQI is statistically significantly higher** than summer (p < 0.001)
- Strongest pollutant correlations:
  - PM2.5 ↔ PM10: **0.92**
  - PM2.5 ↔ CO: **0.78**
- Linear Regression model successfully quantifies **health risk from PM2.5 exposure**
- ARIMA model provides future AQI forecasting
- Clear seasonal patterns and year-to-year trends visualized

## ✨ Features

- Complete Exploratory Data Analysis (EDA) with statistical tests
- Linear Regression + ARIMA forecasting
- Interactive Streamlit Dashboard featuring:
  - AQI trends over time
  - Pollutant correlation heatmap
  - Seasonal & monthly comparisons
  - Model predictions and forecasts
- Professional visualizations (heatmaps, time-series plots, box plots, etc.)
- Fully cleaned and ready-to-use datasets

## 🛠 Tech Stack

- **Language**: Python
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Statistics & Modeling**: SciPy, Statsmodels, ARIMA
- **Dashboard**: Streamlit
- **Environment**: Google Colab + Local Python

## 📁 Project Structure

```bash
seamedu-air-quality-pune/
├── Air_Quality_Pune_Seamedu.ipynb          # Main analysis, modeling & ARIMA forecasting
├── app.py                                  # Streamlit interactive dashboard
├── cleaned_daily_aqi.csv                   # Processed daily AQI data (2017–2024)
├── cleaned_hourly_pollutants.csv           # Processed hourly pollutant data
├── pollutants_corelation_heatmap.png       # Pollutant correlation heatmap
├── ARIMA_forecast.png                      # ARIMA forecasting visualization
├── Daily AQI analysis.png
├── Monthly AQI analysis.png
├── seasonal analysis.png
├── year_to_year_comparison.png
├── requirements.txt
├── .gitignore
└── README.md
```
# Explore the Full Analysis
Open Air_Quality_Pune_Seamedu.ipynb in Google Colab (recommended) or Jupyter Notebook and run all cells.
📊 Dataset
cleaned_daily_aqi.csv → Daily AQI values (2017–2024)
cleaned_hourly_pollutants.csv → Hourly pollutant levels (PM2.5, PM10, CO, etc.)
Both datasets are already cleaned and ready for analysis.

# 📈 Visualizations
Pollutant correlation heatmap
Daily, Monthly & Seasonal AQI analysis
Year-to-year comparison
ARIMA forecasting model output
(All visualizations are included as .png files in the repository.)

# 🔮 Future Enhancements
Real-time AQI API integration
Advanced forecasting models (LSTM, Prophet)
Air quality alert system
Public health impact dashboard with hospital data
Mobile-friendly Progressive Web App (PWA)

# 🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to fork the repository and submit a pull request.
📄 License
This project is open-source and available under the MIT License.

# 🙏 Acknowledgements
Built with ❤️ in Pune for Seamedu Awards 2026 – Data Analytics Excellence Award.
Special thanks to open data sources and the Seamedu community.
