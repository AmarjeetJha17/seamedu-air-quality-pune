"""Tab 3: Pollutant Correlation Matrix visualization."""

import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from config.settings import POLLUTANT_COLS


def render(hourly):
    """Render the Pollutant Correlations tab."""
    st.subheader("Hourly Pollutant Correlation Matrix (2024)")
    corr_matrix = hourly[POLLUTANT_COLS].corr()

    fig = px.imshow(
        corr_matrix, text_auto=".2f", aspect="auto",
        color_continuous_scale="RdYlBu_r"
    )
    fig.update_layout(height=650, title_font_size=18)
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "**Key Insight**: PM2.5 and PM10 are extremely correlated (r ≈ 0.92). "
        "Main sources are traffic, construction dust, and biomass burning."
    )
