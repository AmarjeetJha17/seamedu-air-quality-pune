"""Tab 1: Daily AQI Trend visualization."""

import streamlit as st
import plotly.express as px


def render(daily):
    """Render the Daily AQI Trend tab."""
    st.subheader("Daily AQI Trend (2017–2024)")
    fig = px.line(daily, x='Date', y='AQI')
    fig.update_layout(height=550, title_font_size=18)
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "**Key Insight**: Strong seasonal pattern with sharp winter spikes "
        "every year. No clear long-term improvement observed."
    )
