import json
import requests
import urllib2
from time import strftime


def get_weather(lat, lon):
	url = 'http://forecast.weather.gov/MapClick.php?lat=' + \
		str(lat) + '&lon=' + str(lon) + '&FcstType=json'
	response = urllib2.urlopen(url)
	data = json.load(response)		#load json weather info
	current_temp = data['currentobservation']['Temp']
	low = data['data']['temperature'][0]
	high = data['data']['temperature'][1]
	desc = data['data']['text'][0]

	w_list = {	#weather dict
		"Current_Temp": current_temp, 
		"Low": low, 
		"High": high, 
		"Description": desc,
		"Date": strftime("%x")
		}

	return w_list