import schedule
import time

import message
import location
import getweather
import mongo


def job():
    lat, lon = location.get_location()
    weather = getweather.get_weather(lat, lon)
    mongo.insert(weather)
    # get averages for last week
    weather['Average_High'], weather['Average_Low'] = mongo.avg_high_and_low()
    # create and send message w/ twilio
    msg = message.create_message(weather)
    message.send_message(msg)
    print("Message sent")


def automate():
    schedule.every().day.at("08:00").do(job)  # run every day at 8AM
    while True:  # run infinitely
        schedule.run_pending()
        time.sleep(60)  # check every 60 seconds to see if it's 8AM


def main():
    automate()
    #job()

if __name__ == "__main__":
    main()
