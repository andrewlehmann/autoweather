import schedule
import time


def job():
	import sendmessage
	import location
	import getweather
	ip = location.get_ip()
	lat, lon = location.get_location(ip)
	weather = getweather.get_weather(lat, lon)

	msg = createmessage.create_message(weather)
	t_phone, m_phone = createmessage.phone_numbers()
	createmessage.send_message(t_phone, m_phone, msg)


def main:
	schedule.every()day.at("08:00").do(job, 'job running')

	while True:
		schedule.run_pending()
		time.sleep(60)

if __name__ == "__main__":
	main()