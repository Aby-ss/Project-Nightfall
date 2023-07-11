import requests
from rich import print

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

# Replace with your BLS API key
api_key = '5688c521d1d54d98a2392ed6601bf137'

# Example usage
series_id = 'CUUR0000SA0'  # Consumer Price Index for All Urban Consumers, All Items
start_year = 2018
end_year = 2022

bls_data = get_bls_data(series_id, start_year, end_year, api_key)
if bls_data:
    for data_point in bls_data:
        year = data_point['year']
        period = data_point['periodName']
        value = data_point['value']
        print(f'{year} {period}: {value}')
