import requests

url = "https://realty-mole-property-api.p.rapidapi.com/properties"

querystring = {"address":"5500 Grand Lake Dr, San Antonio, TX, 78244"}

headers = {
	"X-RapidAPI-Key": "3c07ea8d1bmsh488a9163b679e0ep1233d4jsnfe1622183af4",
	"X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())