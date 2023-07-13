import requests

text = 'roman empire'
api_url = 'https://api.api-ninjas.com/v1/historicalevents?text={}'.format(text)
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
if response.status_code == requests.codes.ok:
    events = response.json()

    for event in events:
        year = event['year']
        month = event['month']
        day = event['day']
        event_desc = event['event']

        print(f"Date: {year}-{month}-{day}")
        print(f"Event: {event_desc}")
        print()
else:
    print("Error:", response.status_code, response.text)