import json
import urllib.request, urllib.error, urllib.parse

from time import strftime


# retrieve and load json data from weather.gov
def get_weather(lat, lon):
    print("getting weather json data")  # status checks
    url = 'http://forecast.weather.gov/MapClick.php?lat=' + \
        str(lat) + '&lon=' + str(lon) + '&FcstType=json'
    response = urllib.request.urlopen(url)
    readable = response.read().decode('utf-8')
    data = json.loads(readable)
    return parse(data)


# parse json data into json format and return dict of data
def parse(data):
    print("parsing data")
    current_temp = data['currentobservation']['Temp']
    high_num, low_num = high_low_check(data)
    low = data['data']['temperature'][low_num]
    high = data['data']['temperature'][high_num]
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


# check whether the leading entry in temp is the high or the low
def high_low_check(data):
    if data['time']['tempLabel'][0] == "High":
        return 0, 1 # high num, low num
    else:
        return 1, 0 # low num, high num
