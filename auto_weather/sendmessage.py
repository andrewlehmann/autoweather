import keyring


sid = keyring.get_password("Twillosid", "sid")
auth = keyring.get_password("Twilloauth", "auth")