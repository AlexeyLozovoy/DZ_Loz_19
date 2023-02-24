import requests
import json

api_pog = 'f85a073f0d0c3a12646d88a02a309000'
city = input("Ведите город: ")
pog = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_pog}'

resp = requests.get(pog)
data = json.loads(resp.text)

temp = data['main']['temp']
wind = data['wind']['speed']
print("Температура: ", round((temp-273.15), 1))
print("Скорость ветра: ", wind)
