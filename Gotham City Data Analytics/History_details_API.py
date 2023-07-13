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

text = 'roman empire'
api_url = 'https://api.api-ninjas.com/v1/historicalevents?text={}'.format(text)
response = requests.get(api_url, headers={'X-Api-Key': 'E9SmCxTQQtyVD79D96wfpg==7Z30WK1D8Do2AOcN'})
if response.status_code == requests.codes.ok:
    events = response.json()

    for event in events:
        year = event['year']
        month = event['month']
        day = event['day']
        event_desc = event['event']


        print(Panel(f"{event_desc}", title=f"{year} - {month} - {day}", title_align="left", border_style="bold white", box = box.SQUARE))
else:
    print("Error:", response.status_code, response.text)