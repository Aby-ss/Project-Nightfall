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

city = 'london'
api_url = 'https://api.api-ninjas.com/v1/geocoding?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': 'E9SmCxTQQtyVD79D96wfpg==7Z30WK1D8Do2AOcN'})

if response.status_code == requests.codes.ok:
    data = response.json()
    if data:
        location = data[0]
        name = location["name"]
        latitude = location["latitude"]
        longitude = location["longitude"]
        country = location["country"]

        print("Name:", name)
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print("Country:", country)
    else:
        print("No data available for the specified city.")
else:
    print("Error:", response.status_code, response.text)