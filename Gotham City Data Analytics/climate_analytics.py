import requests
from datetime import datetime
from rich import print

API_KEY = "oTQpnpQiblAW9o2yVziW3FmFl5U9dUlR"
LOCATION = "Dubai"

def get_weather_data():
    url = f"https://api.tomorrow.io/v4/timelines?location={LOCATION}&fields=temperature_2m,weatherCode&units=metric&timesteps=1d&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def format_weather_data(data):
    weather_data = []
    timelines = data.get("data", {}).get("timelines", [])
    for timeline in timelines:
        interval = timeline.get("intervals", [])[0]
        start_time = datetime.fromisoformat(interval.get("startTime"))
        weather_code = interval.get("values", {}).get("weatherCode")
        temperature = interval.get("values", {}).get("temperature_2m")
        weather_data.append((start_time, weather_code, temperature))
    return weather_data

def get_weather_icon(weather_code):
    if weather_code == 1000:  # Clear
        return "☀️"
    elif weather_code == 1001:  # Partly cloudy
        return "⛅"
    elif weather_code == 1100:  # Mostly cloudy
        return "☁️"
    elif weather_code == 1101:  # Overcast
        return "☁️"
    elif weather_code == 2000:  # Foggy
        return "🌫️"
    elif weather_code == 2100:  # Light fog
        return "🌁"
    elif weather_code == 3000:  # Light drizzle
        return "🌦️"
    elif weather_code == 3001:  # Drizzle
        return "🌧️"
    elif weather_code == 3002:  # Heavy drizzle
        return "🌧️"
    elif weather_code == 4000:  # Light rain
        return "🌦️"
    elif weather_code == 4001:  # Moderate rain
        return "🌧️"
    elif weather_code == 4002:  # Heavy rain
        return "⛈️"
    elif weather_code == 5000:  # Light snow
        return "🌨️"
    elif weather_code == 5001:  # Moderate snow
        return "🌨️"
    elif weather_code == 5002:  # Heavy snow
        return "❄️"
    elif weather_code == 6000:  # Light showers
        return "🌦️"
    elif weather_code == 6001:  # Showers
        return "🌧️"
    elif weather_code == 6002:  # Heavy showers
        return "⛈️"
    elif weather_code == 7000:  # Light snow showers
        return "🌨️"
    elif weather_code == 7001:  # Snow showers
        return "🌨️"
    elif weather_code == 7002:  # Heavy snow showers
        return "❄️"
    else:
        return "❓"

def main():
    data = get_weather_data()
    weather_data = format_weather_data(data)

    for start_time, weather_code, temperature in weather_data:
        icon = get_weather_icon(weather_code)
        print(f"{start_time.date()}: {icon}  {temperature}°C")

main()