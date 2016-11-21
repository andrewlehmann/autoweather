import schedule
import time
import sendmessage
import location
import getweather
import mongo


def job():

    lat, lon = location.get_location()
    weather = getweather.get_weather(lat, lon)  # retrieve weather info
    print 'got weather'

    mongo.insert(weather)           # put info in database
    print 'data inserted'

    msg = sendmessage.create_message(weather)
    sendmessage.send_message(msg)
    print 'message sent'
    return


def main():
    # schedule.every().day.at("08:00").do(job)
    job()
    # while True:
    #    schedule.run_pending()
    #    time.sleep(60)


if __name__ == "__main__":
    main()
