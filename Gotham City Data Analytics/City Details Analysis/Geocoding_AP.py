import requests

city = 'london'
api_url = 'https://api.api-ninjas.com/v1/geocoding?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})

if response.status_code == requests.codes.ok:
    data = response.json()
    if data:
        location = data[0]
        name = location["name"]
        latitude = location["latitude"]
        longitude = location["longitude"]
        country = location["country"]

        print("Name:", name)
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print("Country:", country)
    else:
        print("No data available for the specified city.")
else:
    print("Error:", response.status_code, response.text)