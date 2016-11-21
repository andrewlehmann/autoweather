import requests
import json
import urllib2


def get_ip():
    ip = requests.get('http://api.ipify.org').text
    return ip


def get_location():
    url = 'http://ipinfo.io/' + get_ip() + '/json'
    response = urllib2.urlopen(url)
    data = json.load(response)
    loc = data['loc']
    lat = loc.split(',')[0]
    lon = loc.split(',')[1]
    return lat, lon
