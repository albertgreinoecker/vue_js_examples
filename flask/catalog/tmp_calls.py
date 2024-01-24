import requests

res = requests.put('http://localhost:8080/user/3', json={'info' : {'id' : 4, 'name' : 'Franz', 'rfid' : 50, 'motorwert' : 'neu'}}).json()
print(res)