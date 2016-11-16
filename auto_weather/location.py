import requests
import json
import urllib2

def get_ip():
	ip = requests.get('https://api.ipify.org').text
	return ip

def get_location(ip):
	url = 'http://ipinfo.io/' + ip + '/json'
	response = urllib2.urlopen(url)
	data = json.load(response)
	loc = [data['loc'][0], data['loc'][1]]
	return loc

