"""
General utility functions for the project.
"""


def aqi_category(aqi_value: float) -> str:
    """
    Map an AQI numeric value to its WHO/Indian standard category.
    
    Args:
        aqi_value: Numeric AQI value.
    
    Returns:
        Category string (e.g. 'Good', 'Moderate', 'Unhealthy', etc.)
    """
    if aqi_value <= 50:
        return "Good"
    elif aqi_value <= 100:
        return "Satisfactory"
    elif aqi_value <= 200:
        return "Moderate"
    elif aqi_value <= 300:
        return "Poor"
    elif aqi_value <= 400:
        return "Very Poor"
    else:
        return "Severe"


def aqi_color(category: str) -> str:
    """Return a hex color for an AQI category (useful for visualizations)."""
    colors = {
        "Good": "#009966",
        "Satisfactory": "#58a84b",
        "Moderate": "#ffde33",
        "Poor": "#ff9933",
        "Very Poor": "#cc0033",
        "Severe": "#660099",
    }
    return colors.get(category, "#999999")
