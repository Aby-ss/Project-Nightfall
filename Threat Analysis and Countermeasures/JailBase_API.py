import requests

url = "https://jailbase-jailbase.p.rapidapi.com/recent/"

querystring = {"source_id":"<REQUIRED>"}

headers = {
	"X-RapidAPI-Key": "3c07ea8d1bmsh488a9163b679e0ep1233d4jsnfe1622183af4",
	"X-RapidAPI-Host": "jailbase-jailbase.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())