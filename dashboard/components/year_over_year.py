"""Tab 4: Year-over-Year AQI Comparison visualization."""

import streamlit as st
import plotly.express as px


def render(daily):
    """Render the Year-over-Year comparison tab."""
    st.subheader("Year-over-Year Daily AQI Comparison")
    fig = px.line(
        daily,
        x=daily['Date'].dt.strftime('%m-%d'),
        y='AQI',
        color=daily['Date'].dt.year.astype(str)
    )
    fig.update_layout(height=600, title_font_size=18)
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "**Key Insight**: Winter pollution spikes are consistent across all years "
        "(2017–2024). The problem remains persistent."
    )
