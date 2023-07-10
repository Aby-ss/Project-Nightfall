import json
import http.client
from rich.pretty import pprint

from rich.traceback import install
install(show_locals=True)

import requests

url = "https://api.tomorrow.io/v4/weather/forecast?location=new%20york&apikey=oTQpnpQiblAW9o2yVziW3FmFl5U9dUlR"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)