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

# Replace with your BLS API key
api_key = '5688c521d1d54d98a2392ed6601bf137'


# Example series IDs
series_ids = ['CUUR0000SA0', 'CES0000000001', 'LNS14000000', 'PCUOMFG-OMFGAP', 'CUSR0000SA0']
# CUUR0000SA0 - Consumer Price Index for All Urban Consumers, All Items: It measures the average change over time in the prices paid by urban consumers for a market basket of consumer goods and services.
# CES0000000001 - All Employees, Total Nonfarm: It represents the total number of nonfarm employees, including both private and government sectors.
# LNS14000000 - Unemployment Rate: It represents the percentage of the total labor force that is unemployed and actively seeking employment.
# PCUOMFG-OMFGAP - Producer Price Index by Industry: Manufacturing: It measures the average change over time in the selling prices received by domestic producers for their output of goods in the manufacturing sector.
# CUSR0000SA0 - Real Earnings: It measures the change in average weekly earnings adjusted for inflation, providing insights into changes in purchasing power for workers.


# Example year
year = 2022

for series_id in series_ids:
    bls_data = get_bls_data(series_id, year, year, api_key)
    if bls_data:
        print(f'Series ID: {series_id}')
        for data_point in bls_data:
            period = data_point['periodName']
            value = data_point['value']
            print(Panel(f'{period}: {value}'))
        print()
