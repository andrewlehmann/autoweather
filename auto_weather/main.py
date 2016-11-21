import schedule
import time


def job():
	import sendmessage
	import location
	import getweather
	
	ip = location.get_ip()
	lat, lon = location.get_location(ip)
	weather = getweather.get_weather(lat, lon)

	msg = sendmessage.create_message(weather)
	t_phone, m_phone = sendmessage.phone_numbers()
	sendmessage.send_message(t_phone, m_phone, msg)
	now = time.strftime("%c")
	print 'message sent at %s' % now
	return


def main():
	schedule.every().day.at("18:57").do(job())

	while True:
		schedule.run_pending()
		time.sleep(60)
	

if __name__ == "__main__":
	main()
