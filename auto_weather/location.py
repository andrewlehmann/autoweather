import requests
import json
import urllib.request, urllib.error, urllib.parse


# retrieve IP address of initiating machine
def get_ip():
    response = urllib.request.urlopen('http://api.ipify.org')
    ip = response.read().decode('utf-8')
    return ip

# use IP address to return latitude and longitude
def get_location():
    url = 'http://ipinfo.io/' + get_ip() + '/json'
    response = urllib.request.urlopen(url)
    readable_response = response.read().decode('utf-8')
    data = json.loads(readable_response)
    loc = data['loc']
    lat = loc.split(',')[0]
    lon = loc.split(',')[1]
    return lat, lon
