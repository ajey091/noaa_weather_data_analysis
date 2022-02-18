from noaa_sdk import NOAA

n = NOAA()
n.points_forecast(40.7314, -73.8656, type='forecastGridData')
