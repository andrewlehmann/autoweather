import keyring
from twilio.rest import TwilioRestClient


def twilio_creds(): #twillo credentials
	sid = keyring.get_password("Twillosid", "sid")
	auth = keyring.get_password("Twilloauth", "auth")
	twilio_phone = keyring.get_password("Twiliophone", "phone")
	my_phone = keyring.get_password("myphone", "phone")

	return sid, auth#, twilio_phone, my_phone

def create_message(t_phone, my_phone, ):
	t = TwilioRestClient(twilio_creds())
	#message = t.messages.create(body = )


def send_message():
	



