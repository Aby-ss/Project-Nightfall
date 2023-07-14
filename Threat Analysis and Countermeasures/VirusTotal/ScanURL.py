import requests

url = "https://www.virustotal.com/api/v3/urls"

headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded"
}

response = requests.post(url, headers=headers)

print(response.text)