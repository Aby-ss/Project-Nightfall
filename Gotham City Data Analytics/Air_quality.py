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


city = 'Dubai'
api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': 'E9SmCxTQQtyVD79D96wfpg==7Z30WK1D8Do2AOcN'})

if response.status_code == requests.codes.ok:
    json_data = response.json()

    overall_aqi = json_data['overall_aqi']
    CO_concentration = json_data['CO']['concentration']
    CO_aqi = json_data['CO']['aqi']
    PM10_concentration = json_data['PM10']['concentration']
    PM10_aqi = json_data['PM10']['aqi']
    SO2_concentration = json_data['SO2']['concentration']
    SO2_aqi = json_data['SO2']['aqi']
    PM25_concentration = json_data['PM2.5']['concentration']
    PM25_aqi = json_data['PM2.5']['aqi']
    O3_concentration = json_data['O3']['concentration']
    O3_aqi = json_data['O3']['aqi']
    NO2_concentration = json_data['NO2']['concentration']
    NO2_aqi = json_data['NO2']['aqi']

    air_quality = Panel(f"Overall Air Quality Index [aqi]: {overall_aqi}\n\n[b]C0 Conc.[/]: {CO_concentration}  [b]C0 AQI[/]: {CO_aqi}\n[b]PM10 Conc.[/]: {PM10_concentration}  [b]PM10 AQI[/]: {PM10_aqi}\n[b]SO2 Conc.[/]: {SO2_concentration}   [b]SO2 AQI[/]: {SO2_aqi}\n[b]PM25 Conc.[/]: {PM25_concentration}  [b]PM25 AQI[/]: {PM25_aqi}\n[b]O3 Conc.[/]: {O3_concentration}  [b]O3 AQI[/]: {O3_aqi}\n[b]NO2 Conc.[/]: {NO2_concentration}  [b]NO2 AQI[/]: {NO2_aqi}", title=f"Air Quality Index for [i]{city}[/]", title_align="left", border_style="bold white", box = box.SQUARE)
    print(air_quality)
else:
    print(Panel.fit(f"[b]Error: {response.status_code}: {response.text}", border_style="bold red", box = box.SQUARE))