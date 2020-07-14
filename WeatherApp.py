import requests
import json
'''
response = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=ece01c417e112ffcec3c1924f295a020")

# Headers is a dictionary
print(response.headers)
# Get the content-type from the dictionary.
print(response.headers["content-type"])

data = response.json()
print(type(data))
print(data)
data_main = data['main']

print('This is the temperature %s' % (data_main['temp']) + '\nThe presure is %s ' %(data_main['pressure']))
'''


location = requests.get('http://api.ipstack.com/check?access_key=94f8d96d2a77f4ac1d5e740e906a872d')
response_locaton = location.json()
latitude_location = response_locaton['latitude']
longitude_location = response_locaton['longitude']
country_code = response_locaton['country_code']
city_location = response_locaton['city']
print(f'Your current location is {city_location},{country_code}')
response1 = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={latitude_location}&lon={longitude_location}&units=metric&appid=ece01c417e112ffcec3c1924f295a020")
data1 = response1.json()
weather = data1['main']
temp = weather['temp']
pressure = weather['pressure']
humidity = weather['humidity']
print(f'The temperature is {temp} \nThe pressure is {pressure} \nThe humidity is {humidity}')

enter_city_location = input('Enter a city location \n')
response2 = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={enter_city_location}&units=metric&appid=ece01c417e112ffcec3c1924f295a020')
data2 = response2.json()
weather2 = data2['main']
temp2 = weather2['temp']
pressure2 = weather['pressure']
humidity2 = weather['humidity']
print(f'The weather conditions for {enter_city_location} are : ')
print(f'The temperature is {temp2} \nThe pressure is {pressure2} \nThe humidity is {humidity2}')



