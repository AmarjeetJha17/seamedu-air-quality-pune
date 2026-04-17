"""Sidebar component for the Streamlit dashboard."""

import streamlit as st


def render():
    """Render the sidebar with project info."""
    with st.sidebar:
        st.header("About this Project")
        st.write(
            "Historical AQI analysis for Pune with statistical tests, "
            "interactive visualizations, and SARIMAX forecasting."
        )
        st.write("**Live Demo** for Seamedu Awards 2026 – Data Analytics Excellence")
        st.caption("Data up to Dec 2024 | Forecast till 2026")
        st.divider()
        st.write("👨‍💻 Built by Amarjit Jha")
        st.write(
            "GitHub: [seamedu-air-quality-pune]"
            "(https://github.com/AmarjeetJha17/seamedu-air-quality-pune)"
        )
