import keyring
from twilio.rest import TwilioRestClient


def twilio_creds(): #twillo credentials
	sid = keyring.get_password("Twillosid", "sid")
	auth = keyring.get_password("Twilloauth", "auth")
	return sid, auth

def phone_numbers():
	twilio_phone = keyring.get_password("Twiliophone", "phone")
	my_phone = keyring.get_password("myphone", "phone")
	return twilio_phone, my_phone

def create_message(w_list):
	message = 'Current temp: %s \nLow: %s \nHigh: %s \nDescription: %s \n'\
	 % (w_list[0], w_list[1], w_list[2], w_list[3])
	return message


def send_message(t_phone, my_phone, msg):
	sid, auth = twilio_creds()
	t = TwilioRestClient(sid, auth)
	t.messages.create(body=msg, from_=t_phone, to=my_phone)
	return

	



