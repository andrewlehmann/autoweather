import schedule
import time

import sendmessage
import location
import getweather
import mongo


def job():

    lat, lon = location.get_location()
    weather = getweather.get_weather(lat, lon)  # retrieve weather info
    mongo.insert(weather)           # put info in database
    msg = sendmessage.create_message(weather)
    sendmessage.send_message(msg)  # send text message
    print "Message sent"


def main():
    schedule.every().day.at("08:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()
