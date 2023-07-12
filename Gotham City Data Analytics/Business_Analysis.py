from datetime import datetime
import csv
import time
import json
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

# Define your Yelp Fusion API credentials
api_key = 'p_uIld410DVuEtZnaciXDeOL9itRU-yn2C3Z2bCGRZ2ptAJ6Yc8IcySXJLuY3_j8HVQ0APDrxg6c4w7TtTj7Xb7LgT7FFEPskULbTYYR7J3yhzKd2aQuF2TDDqOuZHYx'

# API endpoint for business search
url = 'https://api.yelp.com/v3/businesses/search'

# Set parameters for the search
headers = {
    'Authorization': 'Bearer {}'.format(api_key),
}

params = {
    'term': 'restaurant',
    'location': 'San Francisco',
    'limit': 5
}

# Send GET request to Yelp API
response = requests.get(url, headers=headers, params=params)
data = response.json()

# Extract business information from the response
businesses = data['businesses']
for business in businesses:
    name = business['name']
    rating = business['rating']
    address = ', '.join(business['location']['display_address'])
    
    print(Panel(f"{name}\nBusiness Type: Restaurant\nRating: {rating}\nAddress: {address}", title=f"{name}", title_align="left", border_style="bold white", box = box.SQUARE))