from keyring import get_password
from twilio.rest import Client


def twilio_creds():  # twillo credentials
    sid = get_password("Twillosid", "sid")
    auth = get_password("Twilloauth", "auth")
    return sid, auth


def phone_numbers():
    twilio_phone = get_password("Twiliophone", "phone")
    my_phone = get_password("myphone", "phone")
    return twilio_phone, my_phone


def create_message(w_list):  # create actual message to be sent
    message = '''Current temp: {w[Current_Temp]}
        Low: {w[Low]}
        High: {w[High]}
        Description: {w[Description]}
        Average High: {w[Average_High]}
        Average Low: {w[Average_Low]}'''
    return message.format(w=w_list)


def send_message(msg):
    t_phone, my_phone = phone_numbers()
    sid, auth = twilio_creds()
    t = Client(sid, auth)
    t.messages.create(body=msg, from_=t_phone, to=my_phone)
