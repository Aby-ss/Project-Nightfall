import requests

url = "https://www.virustotal.com/api/v3/urls"

payload = { "url": "https://github.com/Aby-ss" }
headers = {
    "accept": "application/json",
    "x-apikey": "41033a47cf93b08bb54269ba13a31b85f239399ac46f00d0e4b3559931de22d3",
    "content-type": "application/x-www-form-urlencoded"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)