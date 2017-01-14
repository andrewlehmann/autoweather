import schedule
import time

import message
import location
import getweather
import mongo


def job():

    lat, lon = location.get_location()  # retrieve latitude, longitude
    weather = getweather.get_weather(lat, lon)   # get weather via gps
    mongo.insert(weather)           # put info in database

    avg_high, avg_low = mongo.avg_high_and_low(weather) # Retrieve averages
    weather['Average_High'] = avg_high
    weather['Average_Low'] = avg_low

    msg = message.create_message(weather)  # creates text message
    message.send_message(msg)  # send text message
    print "Message sent"

def automate():
    schedule.every().day.at("08:00").do(job)  # run every day at 8AM
    while True:  # run infinitely
        schedule.run_pending()
        time.sleep(60)  # check every 60 seconds to see if it's 8AM

def main():
    automate()
    # job()
    
if __name__ == "__main__":
    main()
