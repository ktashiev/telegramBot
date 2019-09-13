import time

import pyowm

owm = pyowm.OWM('dad12bb47b731ab11ef9b3959a731c75', language='ru')

observation = owm.weather_at_place('Bishkek')
w = observation.get_weather()
weather_result = {}
weather_result['temp_now'] = w.get_temperature('celsius')['temp']
weather_result['temp_max'] = w.get_temperature('celsius')['temp_max']
weather_result['temp_min'] = w.get_temperature('celsius')['temp_min']
weather_result['humidity'] = w.get_humidity()
weather_result['speed'] = w.get_wind()['speed']
weather_result['status'] = w.get_detailed_status()
weather_result['time'] = time.ctime()
