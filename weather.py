import time

import pyowm

owm = pyowm.OWM('dad12bb47b731ab11ef9b3959a731c75', language='ru')

observation = owm.weather_at_place('Bishkek')
w = observation.get_weather()
weather_result = {}
weather_result['temp_now'] = str(int(w.get_temperature('celsius')['temp'])) + '°C'
weather_result['temp_max'] = str(int(w.get_temperature('celsius')['temp_max'])) + '°C'
weather_result['temp_min'] = str(int(w.get_temperature('celsius')['temp_min'])) + '°C'
weather_result['humidity'] = str(w.get_humidity()) + '%'
weather_result['speed'] = str(w.get_wind()['speed']) + 'км/ч'
weather_result['status'] = str(w.get_detailed_status())
weather_result['time'] = str(time.ctime()).replace('2019', '')
