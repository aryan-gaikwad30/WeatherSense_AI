"""
AQI Conversion Engine

Uses linear interpolation to estimate AQI
from PM2.5 concentration.

Reference:
Indian CPCB AQI breakpoints (educational use).
"""


BREAKPOINTS = [

    # PM2.5 Low, High, AQI Low, AQI High

    (0.0, 30.0, 0, 50),

    (30.1, 60.0, 51, 100),

    (60.1, 90.0, 101, 200),

    (90.1, 120.0, 201, 300),

    (120.1, 250.0, 301, 400),

    (250.1, 500.0, 401, 500)

]


def estimate_aqi(pm25):

    """
    Estimate AQI using linear interpolation.
    """

    for bp_low, bp_high, aqi_low, aqi_high in BREAKPOINTS:

        if bp_low <= pm25 <= bp_high:

            aqi = (
                ((aqi_high - aqi_low) /
                (bp_high - bp_low))
                *
                (pm25 - bp_low)
            ) + aqi_low

            return round(aqi)

    return 500


def aqi_category(aqi):

    """
    AQI Category based on CPCB ranges.
    """

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Satisfactory"

    elif aqi <= 200:
        return "Moderately Polluted"

    elif aqi <= 300:
        return "Poor"

    elif aqi <= 400:
        return "Very Poor"

    return "Severe"


def aqi_color(aqi):

    """
    Returns dashboard color.
    """

    if aqi <= 50:
        return "green"

    elif aqi <= 100:
        return "yellow"

    elif aqi <= 200:
        return "orange"

    elif aqi <= 300:
        return "red"

    elif aqi <= 400:
        return "purple"

    return "maroon"