import requests
from rich import print
from rich.panel import Panel

from rich.traceback import install
install(show_locals=True    )

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
        print('Failed to fetch BLS data.')
        return None

def format_bls_data(series_data):
    rows = []
    for data_point in series_data:
        year = data_point['year']
        period = data_point['period']
        value = data_point['value']
        footnotes = data_point['footnotes'][0]['text']
        rows.append(f'{year}-{period}: {value} ({footnotes})')
    
    panel = Panel.fit(rows, title='BLS Data')
    return panel

# Replace with your BLS API key
api_key = 'YOUR_API_KEY'

# Example usage
series_id = 'CUUR0000SA0'  # Consumer Price Index for All Urban Consumers, All Items
start_year = 2018
end_year = 2022

bls_data = get_bls_data(series_id, start_year, end_year, api_key)
if bls_data:
    formatted_data = format_bls_data(bls_data)
    print(formatted_data)
