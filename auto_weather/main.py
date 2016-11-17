import schedule
import time
import sendmessage
import location
import getweather


def job():
	ip = location.get_ip()
	lat, lon = location.get_location(ip)
	weather = getweather.get_weather(lat, lon)

	msg = sendmessage.create_message(weather)
	t_phone, m_phone = sendmessage.phone_numbers()
	sendmessage.send_message(t_phone, m_phone, msg)
	print 'message sent'
	return


def main():
	schedule.every().day.at("08:00").do(job, 'job running')

	while True:
		schedule.run_pending()
		time.sleep(60)
	

if __name__ == "__main__":
	main()
