import requests

city = input('Enter cite name : ')

link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=3a53f1820f8f1f7060d0d4c5daa94cce&units=metric"

data = requests.get(url = link).json()


lon = data['coord']['lon']
lat = data['coord']['lat']

forecast = f" https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly&appid=3a53f1820f8f1f7060d0d4c5daa94cce&units=metric"


desc = data['weather'][0]['description']
temp = data['main']['temp']
humi = data['main']['humidity']

width = 35

# print('*'*width)
# print(f"*{city.title():^33}*")
# print('*' * width)
# print(f"* Description   {desc:>16} *")
# print(f"* Temperature   {temp:>16} *")
# print(f"* Humidity      {humi:>16} *")
# print('*' * width)



data = requests.get(url = forecast).json()
print(data)