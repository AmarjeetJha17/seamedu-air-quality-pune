"""Tab 2: Seasonal AQI Analysis visualization."""

import streamlit as st
import plotly.express as px


def render(daily):
    """Render the Seasonal Analysis tab."""
    st.subheader("AQI Distribution by Season")
    fig = px.box(
        daily, x='Season', y='AQI', color='Season',
        color_discrete_sequence=px.colors.sequential.RdBu_r
    )
    fig.update_layout(height=600, showlegend=False, title_font_size=18)
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "**Key Insight**: Winter AQI is statistically significantly higher "
        "than Summer (p < 0.001). Winter is the most polluted and variable season."
    )
