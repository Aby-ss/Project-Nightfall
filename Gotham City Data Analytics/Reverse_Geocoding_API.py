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

lat = 51.509865
lon = -0.118092
api_url = 'https://api.api-ninjas.com/v1/reversegeocoding?lat={}&lon={}'.format(lat, lon)

response = requests.get(api_url, headers={'X-Api-Key': 'E9SmCxTQQtyVD79D96wfpg==7Z30WK1D8Do2AOcN'})
if response.status_code == requests.codes.ok:
    data = response.json()
    for location in data:
        country = location["country"]
        name = location["name"]

        print("Name:", name)
        print("Country:", country)
        
        print(Panel.fit(f"[b]Country[/]: {country}    [b]Name[/]: {name}", border_style="bold white", box = box.SQUARE))
else:
    print(Panel.fit(f"[b]Error: {response.status_code}: {response.text}", border_style="bold red", box = box.SQUARE))