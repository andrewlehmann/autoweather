import schedule
import time

import sendmessage
import location
import getweather
import mongo


def job():
    
    lat, lon = location.get_location() # retrieve latitude, longitude
    weather = getweather.get_weather(lat, lon)  # retrieve weather info for gps coords
    mongo.insert(weather)           # put info in database
    msg = sendmessage.create_message(weather) #creates text message
    sendmessage.send_message(msg)  # send text message
    print "Message sent"


def main():
    schedule.every().day.at("08:00").do(job) #run job() every day at 8AM
    
    while True: #run infinitely
        schedule.run_pending()
        time.sleep(60) #check every 60 seconds to see if it's 8AM


if __name__ == "__main__":
    main()
