import requests
import json

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
    
    print(f"Name: {name}")
    print(f"Rating: {rating}")
    print(f"Address: {address}")
    print('---')