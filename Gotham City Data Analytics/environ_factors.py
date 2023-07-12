import requests

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
            print("Air quality data for", location)
            print("Parameter:", measurement['parameter'])
            print("Value:", measurement['value'], measurement['unit'])
            print("Date:", measurement['date']['utc'])
        else:
            print("No air quality data found for", location)
    else:
        print("Error occurred while fetching data. Response content:")
        print(response.content)

# Example usage
get_air_quality_data("Dubai")
