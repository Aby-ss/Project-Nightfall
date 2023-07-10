import requests
from datetime import datetime

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


API_KEY = "oTQpnpQiblAW9o2yVziW3FmFl5U9dUlR"
LOCATION = "25.2048,55.2708"

def get_weather_data():
    url = f"https://api.tomorrow.io/v4/timelines?location={LOCATION}&fields=temperature_2m,weatherCode&units=metric&timesteps=1d&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


def format_weather_data(data):
    weather_data = []
    timelines = data.get("data", {}).get("timelines", [])
    if timelines:
        timeline = timelines[0]
        intervals = timeline.get("intervals", [])
        if intervals:
            interval = intervals[0]
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

    if weather_data:
        start_time, weather_code, temperature = weather_data[0]
        icon = get_weather_icon(weather_code)
        print(f"Date: {start_time.date()}")
        print(f"Weather: {icon}")
        print(f"Temperature: {temperature}°C")
    else:
        print(
            Panel.fit(
                "No weather data available for the requested location.",
                border_style="bold red",
                box=box.SQUARE,
            )
        )


if __name__ == "__main__":
    main()