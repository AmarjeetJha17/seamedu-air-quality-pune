# Seamedu Air Quality Pune 🌫️

**Data Analytics Excellence Award Project – Pune Air Quality & Public Health Crisis (Seamedu Awards 2026)**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)

## 🎯 Overview

**Seamedu Air Quality Pune** is a comprehensive **data analytics project** that analyzes Pune’s Air Quality Index (AQI) and major pollutants from **2017 to 2024**.  

It uncovers critical seasonal patterns, pollutant correlations, statistical significance of winter vs summer pollution, and builds a **linear regression model** to quantify the public health risk associated with PM2.5 levels.

The project includes:
- In-depth exploratory data analysis in a Colab notebook
- Statistical hypothesis testing
- Interactive **Streamlit dashboard** for real-time exploration
- Cleaned datasets and professional visualizations

**Live Dashboard**: [🔗 seamedu-air-quality-pune.streamlit.app](https://seamedu-air-quality-pune.streamlit.app/)

## 🔥 The Problem

Pune, one of India’s fastest-growing cities, faces a severe and worsening air pollution crisis. High levels of PM2.5, PM10, CO, and other pollutants are directly linked to respiratory diseases, cardiovascular issues, and reduced life expectancy — especially during winter months when pollution peaks.

Despite increasing awareness, actionable, data-driven insights and public dashboards have been limited. This project bridges that gap by turning raw AQI data into clear, evidence-based stories and tools for citizens, policymakers, and researchers.

## 💡 Key Insights

- **Winter AQI is statistically significantly higher** than summer (p < 0.001)
- Strongest pollutant correlations:
  - PM2.5 ↔ PM10: **0.92**
  - PM2.5 ↔ CO: **0.78**
- Linear regression model successfully quantifies **health risk from PM2.5 exposure**
- Clear seasonal patterns and pollutant relationships visualized through interactive charts and heatmaps

## ✨ Features

- Full Exploratory Data Analysis (EDA) in Jupyter Notebook
- Statistical tests (t-test for seasonal difference)
- Linear Regression model (PM2.5 → Health Risk)
- Interactive Streamlit Dashboard with:
  - AQI trends over time
  - Pollutant correlation heatmap
  - Seasonal comparisons
  - Model predictions
- Cleaned and ready-to-use datasets
- Professional visualizations (including correlation heatmap)

## 🛠 Tech Stack

- **Language**: Python
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Statistics & Modeling**: SciPy, Statsmodels
- **Dashboard**: Streamlit
- **Environment**: Google Colab + Local Python

## 📁 Project Structure

```bash
seamedu-air-quality-pune/
├── Air_Quality_Pune_Seamedu.ipynb        # Main analysis & modeling notebook
├── app.py                                # Streamlit interactive dashboard
├── cleaned_daily_aqi.csv                 # Processed daily AQI data
├── cleaned_hourly_pollutants.csv         # Processed hourly pollutant data
├── pollutants_corelation_heatmap.png     # Correlation visualization
├── requirements.txt                      # Python dependencies
├── .gitignore
└── README.md
