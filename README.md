# Seamedu Air Quality Pune 🌫️

**Data Analytics Excellence Award Project – Pune Air Quality & Public Health Crisis (Seamedu Awards 2026)**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)

## 🎯 Overview

**Seamedu Air Quality Pune** is a comprehensive **data analytics and visualization project** analyzing Pune's Air Quality Index (AQI) and major pollutants from **2017 to 2024**.

The project uncovers critical seasonal patterns, pollutant correlations, statistical differences between winter and summer pollution, and builds predictive models (using SARIMAX forecasting) to quantify public health risks associated with PM2.5 levels.

It features:
- In-depth Exploratory Data Analysis (EDA) in a Colab notebook
- Statistical hypothesis testing
- SARIMAX time-series forecasting
- Interactive **Streamlit dashboard** for real-time exploration
- Cleaned datasets and professional visualizations

**Live Dashboard**: [🔗 seamedu-air-quality-pune.streamlit.app](https://seamedu-air-quality-pune.streamlit.app/)

## 🔥 The Problem

Pune, one of India's fastest-growing cities, is facing a severe and worsening air pollution crisis. High levels of PM2.5, PM10, CO, and other pollutants are directly linked to respiratory diseases, cardiovascular issues, and reduced life expectancy — especially during winter months when pollution peaks dramatically.

This project turns raw AQI data into actionable, data-driven insights for citizens, policymakers, researchers, and environmental agencies.

## 💡 Key Insights

- **Winter AQI is statistically significantly higher** than summer (p < 0.001)
- Strongest pollutant correlations:
  - PM2.5 ↔ PM10: **0.92**
  - PM2.5 ↔ CO: **0.78**
- SARIMAX model provides future AQI forecasting
- Clear seasonal patterns and year-to-year trends visualized

## ✨ Features

- Complete Exploratory Data Analysis (EDA) with statistical tests
- SARIMAX forecasting
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
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Statistics & Modeling**: SciPy, Statsmodels, SARIMAX
- **Dashboard**: Streamlit
- **Environment**: Google Colab + Local Python

## 📁 Project Structure

```
seamedu-air-quality-pune/
│
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Git ignore rules
│
├── config/
│   └── settings.py                     # Centralized paths, model params, column defs
│
├── data/
│   ├── raw/                            # Original untouched datasets
│   └── processed/                      # Cleaned, analysis-ready data
│       ├── cleaned_daily_aqi.csv       # Daily AQI values (2017–2024)
│       └── cleaned_hourly_pollutants.csv  # Hourly pollutant levels
│
├── notebooks/
│   └── Air_Quality_Pune_Seamedu.ipynb  # Full EDA, modeling & SARIMAX forecasting
│
├── src/                                # Reusable Python modules
│   ├── __init__.py
│   ├── data_loader.py                  # Data loading & validation functions
│   ├── model.py                        # SARIMAX fitting & forecasting logic
│   └── utils.py                        # AQI category mapping & helpers
│
├── dashboard/                          # Streamlit interactive dashboard
│   ├── app.py                          # Dashboard entry point (slim)
│   ├── __init__.py
│   ├── components/                     # One file per dashboard tab
│   │   ├── __init__.py
│   │   ├── aqi_trend.py                # Tab 1: Daily AQI trend
│   │   ├── seasonal.py                 # Tab 2: Seasonal analysis
│   │   ├── correlations.py             # Tab 3: Pollutant correlation matrix
│   │   ├── year_over_year.py           # Tab 4: Year-over-year comparison
│   │   ├── hourly_analysis.py          # Tab 5: Hourly PM2.5 vs PM10
│   │   └── forecast.py                 # Tab 6: SARIMAX forecast
│   └── styles/                         # Custom CSS (optional)
│
├── outputs/
│   ├── figures/                        # Generated visualizations
│   │   ├── sarimax_forecast.png
│   │   ├── daily_aqi_analysis.png
│   │   ├── monthly_aqi_analysis.png
│   │   ├── seasonal_analysis.png
│   │   ├── year_to_year_comparison.png
│   │   └── pollutants_correlation_heatmap.png
│   └── reports/                        # Exported stats / summaries
│
└── tests/                              # Data & model validation tests
    ├── test_data_loader.py
    └── test_model.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/AmarjeetJha17/seamedu-air-quality-pune.git
cd seamedu-air-quality-pune

# Install dependencies
pip install -r requirements.txt
```

### Run the Dashboard

```bash
streamlit run dashboard/app.py
```

### Run Tests

```bash
python -m pytest tests/ -v
```

### Explore the Full Analysis

Open `notebooks/Air_Quality_Pune_Seamedu.ipynb` in Google Colab (recommended) or Jupyter Notebook and run all cells.

## 📊 Dataset

| File | Description |
|---|---|
| `data/processed/cleaned_daily_aqi.csv` | Daily AQI values (2017–2024) |
| `data/processed/cleaned_hourly_pollutants.csv` | Hourly pollutant levels (PM2.5, PM10, CO, etc.) |

Both datasets are already cleaned and ready for analysis.

## 📈 Visualizations

- Pollutant correlation heatmap
- Daily, Monthly & Seasonal AQI analysis
- Year-to-year comparison
- SARIMAX forecasting model output

All visualizations are included in `outputs/figures/`.

## 🔮 Future Enhancements

- Real-time AQI API integration
- Advanced forecasting models (LSTM, Prophet)
- Air quality alert system
- Public health impact dashboard with hospital data
- Mobile-friendly Progressive Web App (PWA)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repository and submit a pull request.

## 📄 License

This project is open-source and available under the MIT License.

## 🙏 Acknowledgements

Built with ❤️ in Pune for Seamedu Awards 2026 – Data Analytics Excellence Award.
Special thanks to open data sources and the Seamedu community.
