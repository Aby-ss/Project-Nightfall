import requests

url = "https://api.tomorrow.io/v4/weather/forecast?location=new%20york&timesteps=1d&units=metric&apikey=oTQpnpQiblAW9o2yVziW3FmFl5U9dUlR"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

data = response.json()

# Retrieve the first timeframe from the "daily" timeline
first_timeframe = data["timelines"]["daily"][0]

# Print the weather values for the first timeframe
print(first_timeframe["values"])