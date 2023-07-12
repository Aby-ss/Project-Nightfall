import requests

# Replace 'YOUR_API_KEY' with your actual API key from NewsAPI
api_key = 'YOUR_API_KEY'

# Specify the endpoint and parameters
url = 'https://newsapi.org/v2/everything'
params = {
    'q': 'city',  # Replace 'city' with the desired city or region
    'apiKey': api_key
}

# Send the request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Iterate over the articles
    for article in data['articles']:
        title = article['title']
        description = article['description']
        source = article['source']['name']
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Source: {source}")
        print("---")
else:
    print(f"Error: {response.status_code}")
