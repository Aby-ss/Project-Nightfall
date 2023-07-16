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

def get_air_quality_data(location):
    base_url = "https://api.openaq.org/v1/measurements"
    parameters = {
        "city": location,
        "limit": 1,
        "order_by": "datetime",
        "sort": "desc"
    }
    
    response = requests.get(base_url, params=parameters)
    data = response.json()
    
    if response.status_code == 200:
        results = data['results']
        
        if results:
            measurement = results[0]
            Location_of_search = location
            Parameter = measurement['parameter']
            Value = measurement['value'], measurement['unit']
            Date = measurement['date']['utc']
        
        else:
            print("No air quality data found for", location)
    else:
        print("Error occurred while fetching data. Response content:")
        print(response.content)

# Example usage
get_air_quality_data("Dubai")
