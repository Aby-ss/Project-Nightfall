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

# Replace 'YOUR_API_KEY' with your actual API key from NewsAPI
api_key = 'd88f50af7b21490889c52621330e9a2c'

# Specify the endpoint and parameters
url = 'https://newsapi.org/v2/everything'
params = {
    'q': 'Dubai',  # Replace 'city' with the desired city or region
    'apiKey': api_key
}

# Send the request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Iterate over the articles
    for article in data['articles']:
        title = article['title']
        description = article['description']
        source = article['source']['name']
        
        print(Panel(f"{description}", title=f"{title}", subtitle=f"{source}", title_align="left", subtitle_align="left", border_style="bold white", box = box.SQUARE))
else:
    print(f"Error: {response.status_code}")
