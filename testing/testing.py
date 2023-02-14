import requests
import json

url = 'http://127.0.0.1:5000/api/login'
data = {'email': 'myusername', 'password': 'mypassword'}
headers = {'Content-type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(response.text)
