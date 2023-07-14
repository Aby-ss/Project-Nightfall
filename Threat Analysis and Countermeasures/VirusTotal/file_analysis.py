import requests

url = "https://www.virustotal.com/api/v3/files"

files = { "file": ("Batsyy.zip", open("Batsyy.zip", "rb"), "application/zip") }
payload = { "password": "BatsyZippy" }
headers = {
    "accept": "application/json",
    "x-apikey": "41033a47cf93b08bb54269ba13a31b85f239399ac46f00d0e4b3559931de22d3"
}

response = requests.post(url, data=payload, files=files, headers=headers)

print(response.text)