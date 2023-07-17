import requests
import json

from rich import box
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.traceback import install
install(show_locals = True)

name = "United Kingdom"
api_url = f'https://api.api-ninjas.com/v1/country?name={name}'
response = requests.get(api_url, headers={'X-Api-Key': 'E9SmCxTQQtyVD79D96wfpg==7Z30WK1D8Do2AOcN'})
if response.status_code == requests.codes.ok:
    name = response.json()[0]["name"]
    population = response.json()[0]["population"]
    tourists = response.json()[0]["tourists"]
    region = response.json()[0]["region"]
    currency = response.json()[0]["currency"]["name"]
    gdp = response.json()[0]["gdp"]
    gdp_growth = response.json()[0]["gdp_growth"]
    capital = response.json()[0]["capital"]
    
    country_panel = Panel.fit(f"[b green] Name: {name}\n Capital: {capital}\n Region: {region}[/]\n[b] GDP || GPD grwoth: {gdp} | {gdp_growth}\n Currency: {currency}\n Tourists: {tourists}", title = f"[b]{name}", title_align="left", border_style = "b white", box = box.SQUARE)
    print(country_panel)
else:
    print(Panel(f"Error: {response.status_code} {response.text}", border_style="bold red", box = box.SQUARE))