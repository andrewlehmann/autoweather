import keyring


def twillo_creds(): #twillo credentials
	sid = keyring.get_password("Twillosid", "sid")
	auth = keyring.get_password("Twilloauth", "auth")
	return sid, auth


