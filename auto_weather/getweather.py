import json
import requests
import urllib2


def get_weather(lat, lon):
	url = 'http://forecast.weather.gov/MapClick.php?lat=' + \
		lat + '&lon=' + long + '&FcstType=json'
	response = urllib2.urlopen(url)
	data = json.load(response)
	current_temp = data[3]['temp'][0]
	low = data[2]['temperature'][0]
	high = data[2]['temperature'][1]
	desc = data[2]['text'][0]
	return current_temp, low, high, desc