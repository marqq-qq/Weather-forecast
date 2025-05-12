import requests

API_KEY = "your_api_key"
city = "your_city"
#the country code can be found at https://countrycode.org/ (you need to use the ISO code)
country_code = "your_country_code"
#the language ISO code can be found at https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
language = "your_language"

url_city_coordinates = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country_code}&appid={API_KEY}"
city_data = requests.get(url_city_coordinates).json()
latitude = city_data[0]['lat']
longitude = city_data[0]['lon']

#you can also use the imperial unit of measurement (to do this, replace metric with imperial in the "units" parameter)
url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric&lang={language}"
weather_data = requests.get(url_weather).json()

main_weather = weather_data['weather'][0]['main']
temperature = format(float(weather_data['main']['temp']), ".1f")
feels_like_temp = format(float(weather_data['main']['feels_like']), ".1f")
pressure = weather_data['main']['pressure']
wind_speed = weather_data['wind']['speed']

print(f"There is/are {main_weather} in {city} now, the temperature is {temperature} degrees Celsius, it feels like {feels_like_temp}\n"
      f"pressure is {pressure} mmHg, wind speed is {wind_speed} m/s")
