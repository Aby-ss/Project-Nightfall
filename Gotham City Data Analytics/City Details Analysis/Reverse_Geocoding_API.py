import requests

lat = 51.509865
lon = -0.118092
api_url = 'https://api.api-ninjas.com/v1/reversegeocoding?lat={}&lon={}'.format(lat, lon)

response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
if response.status_code == requests.codes.ok:
    data = response.json()
    for location in data:
        country = location["country"]
        name = location["name"]

        print("Name:", name)
        print("Country:", country)
else:
    print("Error:", response.status_code, response.text)