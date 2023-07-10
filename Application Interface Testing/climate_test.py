import requests

url = "https://api.tomorrow.io/v4/weather/forecast?location=new%20york&timesteps=1d&units=metric&apikey=oTQpnpQiblAW9o2yVziW3FmFl5U9dUlR"

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
uv_health_concern_avg = first_timeframe["values"]["uvHealthConcernAvg"]
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

# Print each variable on a separate line
print("Cloud Base Avg:", cloud_base_avg)
print("Cloud Base Max:", cloud_base_max)
print("Cloud Base Min:", cloud_base_min)
print("Cloud Ceiling Avg:", cloud_ceiling_avg)
print("Cloud Ceiling Max:", cloud_ceiling_max)
print("Cloud Ceiling Min:", cloud_ceiling_min)
print("Cloud Cover Avg:", cloud_cover_avg)
print("Cloud Cover Max:", cloud_cover_max)
print("Cloud Cover Min:", cloud_cover_min)
print("Dew Point Avg:", dew_point_avg)
print("Dew Point Max:", dew_point_max)
print("Dew Point Min:", dew_point_min)
print("Evapotranspiration Avg:", evapotranspiration_avg)
print("Evapotranspiration Max:", evapotranspiration_max)
print("Evapotranspiration Min:", evapotranspiration_min)
print("Freezing Rain Intensity Avg:", freezing_rain_intensity_avg)
print("Freezing Rain Intensity Max:", freezing_rain_intensity_max)
print("Freezing Rain Intensity Min:", freezing_rain_intensity_min)
print("Humidity Avg:", humidity_avg)
print("Humidity Max:", humidity_max)
print("Humidity Min:", humidity_min)
print("Ice Accumulation Avg:", ice_accumulation_avg)
print("Ice Accumulation LWE Avg:", ice_accumulation_lwe_avg)
print("Ice Accumulation LWE Max:", ice_accumulation_lwe_max)
print("Ice Accumulation LWE Min:", ice_accumulation_lwe_min)
print("Moonrise Time:", moonrise_time)
print("Moonset Time:", moonset_time)
print("Precipitation Probability Avg:", precipitation_probability_avg)
print("Precipitation Probability Max:", precipitation_probability_max)
print("Precipitation Probability Min:", precipitation_probability_min)
print("Pressure Surface Level Avg:", pressure_surface_level_avg)
print("Pressure Surface Level Max:", pressure_surface_level_max)
print("Pressure Surface Level Min:", pressure_surface_level_min)
print("Rain Accumulation Avg:", rain_accumulation_avg)
print("Rain Accumulation LWE Avg:", rain_accumulation_lwe_avg)
print("Rain Accumulation LWE Max:", rain_accumulation_lwe_max)
print("Rain Accumulation LWE Min:", rain_accumulation_lwe_min)
print("Rain Intensity Avg:", rain_intensity_avg)
print("Rain Intensity Max:", rain_intensity_max)
print("Rain Intensity Min:", rain_intensity_min)
print("Sleet Accumulation Avg:", sleet_accumulation_avg)
print("Sleet Accumulation LWE Avg:", sleet_accumulation_lwe_avg)
print("Sleet Accumulation LWE Max:", sleet_accumulation_lwe_max)
print("Sleet Accumulation LWE Min:", sleet_accumulation_lwe_min)
print("Snow Accumulation Avg:", snow_accumulation_avg)
print("Snow Accumulation LWE Avg:", snow_accumulation_lwe_avg)
print("Snow Accumulation LWE Max:", snow_accumulation_lwe_max)
print("Snow Accumulation LWE Min:", snow_accumulation_lwe_min)
print("Sunrise Time:", sunrise_time)
print("Sunset Time:", sunset_time)
print("Temperature Apparent Avg:", temperature_apparent_avg)
print("Temperature Apparent Max:", temperature_apparent_max)
print("Temperature Apparent Min:", temperature_apparent_min)
print("Temperature Avg:", temperature_avg)
print("Temperature Max:", temperature_max)
print("Temperature Min:", temperature_min)
print("UV Health Concern Avg:", uv_health_concern_avg)
print("UV Health Concern Max:", uv_health_concern_max)
print("UV Health Concern Min:", uv_health_concern_min)
print("UV Index Avg:", uv_index_avg)
print("UV Index Max:", uv_index_max)
print("UV Index Min:", uv_index_min)
print("Visibility Avg:", visibility_avg)
print("Visibility Max:", visibility_max)
print("Visibility Min:", visibility_min)
print("Weather Code Max:", weather_code_max)
print("Weather Code Min:", weather_code_min)
print("Wind Direction Avg:", wind_direction_avg)
print("Wind Gust Avg:", wind_gust_avg)
print("Wind Gust Max:", wind_gust_max)
print("Wind Gust Min:", wind_gust_min)
print("Wind Speed Avg:", wind_speed_avg)
print("Wind Speed Max:", wind_speed_max)
print("Wind Speed Min:", wind_speed_min)