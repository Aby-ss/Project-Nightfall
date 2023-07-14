import requests

from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install
install(show_locals=True)

url = "https://jgentes-crime-data-v1.p.rapidapi.com/crime"

querystring = {"startdate":"9/19/2015","enddate":"9/25/2015","long":"-122.5076392","lat":"37.757815"}

headers = {
	"X-RapidAPI-Key": "3c07ea8d1bmsh488a9163b679e0ep1233d4jsnfe1622183af4",
	"X-RapidAPI-Host": "jgentes-Crime-Data-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())