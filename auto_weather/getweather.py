import json
import urllib2

from time import strftime


def get_weather(lat, lon):
    url = 'http://forecast.weather.gov/MapClick.php?lat=' + \
        str(lat) + '&lon=' + str(lon) + '&FcstType=json'
    response = urllib2.urlopen(url)
    data = json.load(response)
    weather = parse(data)  # better to make variable here or
    return weather         # return parse(data)?


def parse(data):
    current_temp = data['currentobservation']['Temp']
    low = data['data']['temperature'][0]
    high = data['data']['temperature'][1]
    desc = data['data']['text'][0]
    # put all data into a dictionary for easy db storage
    w_list = {
        "Current_Temp": current_temp,
        "Low": low,
        "High": high,
        "Description": desc,
        "Date": strftime("%x")
    }
    return w_list
