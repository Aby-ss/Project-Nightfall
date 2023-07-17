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


def get_bls_data(series_id, start_year, end_year, api_key):
    url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/{series_id}'
    headers = {'Content-Type': 'application/json'}
    data = {
        "seriesid": [series_id],
        "startyear": str(start_year),
        "endyear": str(end_year),
        "registrationkey": api_key
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        result = response.json()
        series_data = result['Results']['series'][0]['data']
        return series_data
    else:
        print(f'Failed to fetch BLS data for series ID: {series_id}')
        return None

series_names = [
    "Consumer Price Index for All Urban Consumers",
    "All Employees, Total Nonfarm",
    "Unemployment Rate",
    "Producer Price Index by Industry",
    "Real Earnings"
]

series_ids = ['CUUR0000SA0', 'CES0000000001', 'LNS14000000', 'PCUOMFG-OMFGAP', 'CUSR0000SA0']

# Replace with your BLS API key
api_key = '5688c521d1d54d98a2392ed6601bf137'

for series_id, series_name in zip(series_ids, series_names):
    print(f"Series ID: {series_id}")
    print(f"Series Name: {series_name}")

    bls_data = get_bls_data(series_id, 2022, 2022, api_key)
    if bls_data:
        values = [f"{data_point['periodName']}: {data_point['value']}" for data_point in bls_data]
        panel = Panel.fit("\n".join(values), title=f'{series_id}-{series_name}', title_align="left", border_style="bold white", box = box.SQUARE)
        print(panel)
        print()