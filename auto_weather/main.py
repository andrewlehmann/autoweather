import schedule
import time


def job():
	import sendmessage
	import location
	import getweather
	import mongo
	
	ip = location.get_ip()
	lat, lon = location.get_location(ip)
	weather = getweather.get_weather(lat, lon)

	db = mongo.get_database()
	insert(db, weather)			#put info in database

	msg = sendmessage.create_message(weather)
	t_phone, m_phone = sendmessage.phone_numbers()
	sendmessage.send_message(t_phone, m_phone, msg)
	today = time.strftime("%x")
	print 'message sent on %s' % today
	return


def main():
	schedule.every().day.at("08:00").do(job)

	while True:
		schedule.run_pending()
		time.sleep(60)
	

if __name__ == "__main__":
	main()