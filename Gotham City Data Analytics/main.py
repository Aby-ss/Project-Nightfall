from datetime import datetime
import csv
import time
from time import sleep
import math
import keyboard
import numpy as np
import asciichartpy

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

layout = Layout()

layout.split_column(
    Layout(name = "Header", size=3),
    Layout(name = "Body"),
    Layout(name = "Footer", size=3)
)

layout["Body"].split_row(
    Layout(name="Right"), # Use Right side for Weather Analytics and News
    Layout(name="Left")
)

layout["Right"].split_column(
    Layout(name="Weather", size=17),
    Layout(name="News")
)

layout["Left"].split_column(
    Layout(name="Others"),
    Layout(name="History Details")
)

layout["Others"].split_row(
    Layout(name="Air Quality"),
    Layout(name="Overall Country")
)

layout["Weather"].split_row(
    Layout(name="Weather Forecast"),
    Layout(name="Environmental Factors")
)

class Header:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "🗃", "[b]Main Systems[/]-[i]Project: Nightfall[/]", datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="bold white")
    
class Footer:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_row("[i]It's not who i am underneath, but what i do that defines me. - The Dark Knight[/]")
        return Panel(grid, style="white on black")
    
def climate_analysis():
    import climate_analytics as Climate_analysis
    return Climate_analysis.predicted_weather

def enviromental_factors():
    import environ_factors as EV_factors
    return EV_factors.get_air_quality_data("London")

def air_Quality():
    import Air_quality as AQ
    
    
layout["Header"].update(Header())
layout["Footer"].update(Footer())
layout["Weather Forecast"].update(climate_analysis())
layout["Environmental Factors"].update(enviromental_factors())

print(layout)