from datetime import datetime
import csv
import time
from time import sleep
import math
import keyboard
import numpy as np
import asciichartpy
import requests

from rich import print
from rich import box
from rich.tree import Tree
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.layout import Layout 
from rich.table import Table

from rich.live import Live
from rich.prompt import Prompt
from rich.progress import track
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn

from rich.traceback import install
install(show_locals=True)


url = "https://api.tomorrow.io/v4/weather/forecast?location=Dubai&timesteps=1d&units=metric&apikey=oTQpnpQiblAW9o2yVziW3FmFl5U9dUlR"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

data = response.json()

# Retrieve the first timeframe from the "daily" timeline
first_timeframe = data["timelines"]["daily"][0]

# Extract weather values for the first timeframe
cloud_base_avg = first_timeframe["values"]["cloudBaseAvg"]
cloud_base_max = first_timeframe["values"]["cloudBaseMax"]
cloud_base_min = first_timeframe["values"]["cloudBaseMin"]
cloud_ceiling_avg = first_timeframe["values"]["cloudCeilingAvg"]
cloud_ceiling_max = first_timeframe["values"]["cloudCeilingMax"]
cloud_ceiling_min = first_timeframe["values"]["cloudCeilingMin"]
cloud_cover_avg = first_timeframe["values"]["cloudCoverAvg"]
cloud_cover_max = first_timeframe["values"]["cloudCoverMax"]
cloud_cover_min = first_timeframe["values"]["cloudCoverMin"]
dew_point_avg = first_timeframe["values"]["dewPointAvg"]
dew_point_max = first_timeframe["values"]["dewPointMax"]
dew_point_min = first_timeframe["values"]["dewPointMin"]
evapotranspiration_avg = first_timeframe["values"]["evapotranspirationAvg"]
evapotranspiration_max = first_timeframe["values"]["evapotranspirationMax"]
evapotranspiration_min = first_timeframe["values"]["evapotranspirationMin"]
freezing_rain_intensity_avg = first_timeframe["values"]["freezingRainIntensityAvg"]
freezing_rain_intensity_max = first_timeframe["values"]["freezingRainIntensityMax"]
freezing_rain_intensity_min = first_timeframe["values"]["freezingRainIntensityMin"]
humidity_avg = first_timeframe["values"]["humidityAvg"]
humidity_max = first_timeframe["values"]["humidityMax"]
humidity_min = first_timeframe["values"]["humidityMin"]
ice_accumulation_avg = first_timeframe["values"]["iceAccumulationAvg"]
ice_accumulation_lwe_avg = first_timeframe["values"]["iceAccumulationLweAvg"]
ice_accumulation_lwe_max = first_timeframe["values"]["iceAccumulationLweMax"]
ice_accumulation_lwe_min = first_timeframe["values"]["iceAccumulationLweMin"]
moonrise_time = first_timeframe["values"]["moonriseTime"]
moonset_time = first_timeframe["values"]["moonsetTime"]
precipitation_probability_avg = first_timeframe["values"]["precipitationProbabilityAvg"]
precipitation_probability_max = first_timeframe["values"]["precipitationProbabilityMax"]
precipitation_probability_min = first_timeframe["values"]["precipitationProbabilityMin"]
pressure_surface_level_avg = first_timeframe["values"]["pressureSurfaceLevelAvg"]
pressure_surface_level_max = first_timeframe["values"]["pressureSurfaceLevelMax"]
pressure_surface_level_min = first_timeframe["values"]["pressureSurfaceLevelMin"]
rain_accumulation_avg = first_timeframe["values"]["rainAccumulationAvg"]
rain_accumulation_lwe_avg = first_timeframe["values"]["rainAccumulationLweAvg"]
rain_accumulation_lwe_max = first_timeframe["values"]["rainAccumulationLweMax"]
rain_accumulation_lwe_min = first_timeframe["values"]["rainAccumulationLweMin"]
rain_intensity_avg = first_timeframe["values"]["rainIntensityAvg"]
rain_intensity_max = first_timeframe["values"]["rainIntensityMax"]
rain_intensity_min = first_timeframe["values"]["rainIntensityMin"]
sleet_accumulation_avg = first_timeframe["values"]["sleetAccumulationAvg"]
sleet_accumulation_lwe_avg = first_timeframe["values"]["sleetAccumulationLweAvg"]
sleet_accumulation_lwe_max = first_timeframe["values"]["sleetAccumulationLweMax"]
sleet_accumulation_lwe_min = first_timeframe["values"]["sleetAccumulationLweMin"]
snow_accumulation_avg = first_timeframe["values"]["snowAccumulationAvg"]
snow_accumulation_lwe_avg = first_timeframe["values"]["snowAccumulationLweAvg"]
snow_accumulation_lwe_max = first_timeframe["values"]["snowAccumulationLweMax"]
snow_accumulation_lwe_min = first_timeframe["values"]["snowAccumulationLweMin"]
sunrise_time = first_timeframe["values"]["sunriseTime"]
sunset_time = first_timeframe["values"]["sunsetTime"]
temperature_apparent_avg = first_timeframe["values"]["temperatureApparentAvg"]
temperature_apparent_max = first_timeframe["values"]["temperatureApparentMax"]
temperature_apparent_min = first_timeframe["values"]["temperatureApparentMin"]
temperature_avg = first_timeframe["values"]["temperatureAvg"]
temperature_max = first_timeframe["values"]["temperatureMax"]
temperature_min = first_timeframe["values"]["temperatureMin"]
#uv_health_concern_avg = first_timeframe["values"]["uvHealthConcernAvg"]
uv_health_concern_max = first_timeframe["values"]["uvHealthConcernMax"]
uv_health_concern_min = first_timeframe["values"]["uvHealthConcernMin"]
uv_index_avg = first_timeframe["values"]["uvIndexAvg"]
uv_index_max = first_timeframe["values"]["uvIndexMax"]
uv_index_min = first_timeframe["values"]["uvIndexMin"]
visibility_avg = first_timeframe["values"]["visibilityAvg"]
visibility_max = first_timeframe["values"]["visibilityMax"]
visibility_min = first_timeframe["values"]["visibilityMin"]
weather_code_max = first_timeframe["values"]["weatherCodeMax"]
weather_code_min = first_timeframe["values"]["weatherCodeMin"]
wind_direction_avg = first_timeframe["values"]["windDirectionAvg"]
wind_gust_avg = first_timeframe["values"]["windGustAvg"]
wind_gust_max = first_timeframe["values"]["windGustMax"]
wind_gust_min = first_timeframe["values"]["windGustMin"]
wind_speed_avg = first_timeframe["values"]["windSpeedAvg"]
wind_speed_max = first_timeframe["values"]["windSpeedMax"]
wind_speed_min = first_timeframe["values"]["windSpeedMin"]

predicted_weather = Panel.fit(f" Cloud Base Avg: {cloud_base_avg}\n Cloud Ceiling Avg: {cloud_ceiling_avg}\n Cloud Cover Avg: {cloud_cover_avg}\n Dew Point Avg: {dew_point_avg}\n Evapotranspiration Avg: {evapotranspiration_avg}\n Humidity Avg: {humidity_avg}\n Precipitation Probability Avg: {precipitation_probability_avg}\n Rain Accumulation Avg: {rain_accumulation_avg}\n Rain Intensity Avg: {rain_intensity_avg}\n Snow Accumation: {snow_accumulation_avg}\n Sleet Accumulation Avg: {sleet_accumulation_avg}\n UV Index Avg: {uv_index_avg}\n Visibility Avg: {visibility_avg}\n Wind Gust Avg: {wind_gust_avg}\n Wind Speed Avg: {wind_speed_avg}", title="Predicted Weather", title_align="left", border_style="bold green", box = box.SQUARE)
print(predicted_weather) # Printable in other file imports