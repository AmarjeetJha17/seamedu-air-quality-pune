"""Tab 5: Hourly PM2.5 vs PM10 Analysis visualization."""

import streamlit as st
import plotly.express as px


def render(hourly):
    """Render the Hourly PM2.5 vs PM10 tab."""
    st.subheader("Hourly PM2.5 vs PM10 in 2024")
    recent = hourly[hourly['Datetime'] >= '2024-01-01']
    fig = px.line(recent, x='Datetime', y=['PM2.5', 'PM10'])
    fig.update_layout(height=550, title_font_size=18)
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "**Key Insight**: PM2.5 and PM10 move almost in lockstep. "
        "Clear daily peaks during morning and evening traffic hours."
    )
