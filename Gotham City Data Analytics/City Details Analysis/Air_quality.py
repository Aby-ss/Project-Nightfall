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

    print("overall_aqi:", overall_aqi)
    print("CO_concentration:", CO_concentration)
    print("CO_aqi:", CO_aqi)
    print("PM10_concentration:", PM10_concentration)
    print("PM10_aqi:", PM10_aqi)
    print("SO2_concentration:", SO2_concentration)
    print("SO2_aqi:", SO2_aqi)
    print("PM25_concentration:", PM25_concentration)
    print("PM25_aqi:", PM25_aqi)
    print("O3_concentration:", O3_concentration)
    print("O3_aqi:", O3_aqi)
    print("NO2_concentration:", NO2_concentration)
    print("NO2_aqi:", NO2_aqi)
else:
    print("Error:", response.status_code, response.text)