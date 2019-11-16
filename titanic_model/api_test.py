import requests
import json

local_url = "http://localhost:7071/api/model_deployment"
data = [
    {
    'pclass': '1',
    'age': 29,
    'embarked': 'C',
    'sex': 'female'
    },
    {
    'pclass': '1',
    'age': 29,
    'embarked': 'C',
    'sex': 'male'
    },
    {
    'pclass': '2',
    'age': 29,
    'embarked': 'C',
    'sex': 'female'
    },
    {
    'pclass': '2',
    'age': 29,
    'embarked': 'C',
    'sex': 'male'
    }
]

r = requests.post(local_url, json=json.dumps(data))
print(r)
print(r.text)