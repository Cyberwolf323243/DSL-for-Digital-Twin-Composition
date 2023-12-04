import requests
import json

url = "http://localhost:8080/api/2/things"
jsonObj = {
        'title': 'Car Battery',
	'description': 'DT of a Car Battery',
        'features': {
            'electricity': {
                'properties': {
                    'max_capacity': 1000,
                    'charge': 500,
                    'consumption': 0,
                }
            },
        },
        }

response = requests.post(url, json = jsonObj, auth = ('ditto', 'ditto'))

with open("thingId.txt", "w") as file:
    file.write(json.loads(response.text)["thingId"])

print("Instanciated twin instance and saved thingId")
