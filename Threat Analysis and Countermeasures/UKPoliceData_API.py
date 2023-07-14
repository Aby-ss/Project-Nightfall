import requests

from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install
install(show_locals=True)

url = "https://ukpolicedata.p.rapidapi.com/%7Bforce-id%7D/%7Bneighbourhood-id%7D/events"

headers = {
	"X-RapidAPI-Key": "3c07ea8d1bmsh488a9163b679e0ep1233d4jsnfe1622183af4",
	"X-RapidAPI-Host": "ukpolicedata.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())