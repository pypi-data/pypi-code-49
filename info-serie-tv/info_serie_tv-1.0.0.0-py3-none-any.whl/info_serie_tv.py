import json, os, requests

class SerieTvItaly_bot():
	def __init__(self, api_account):
		self.api = api_account

	def terminal_api(self):
		self.serie_json = self.api.execute_command(1, 'terminal_api', 'r')

		if self.serie_json['ok'] == True:
			self.login = True
		else:
			self.error = self.serie_json['info']
			self.login = False

	def beauty_print(self):
		serie_complete_infos = self.serie_json['detailed_infos']
		id_names = list()
		for short_name in serie_complete_infos:
			print("Informazioni sulla serie {name}\n\n\tIl primo episodio fu trasmesso il {first_air_date}\n\tLa serie TV in quale stato è? {status}\n\tUltima proiezione {last_air_date}\n\tUltimo episodio trasmesso S{last_se_nr} E{last_ep_nr}\n\n\tPagina web della serie {homepage}\n\n\tGeneri della serie TV {genres}\n\n\tEmittenti serie TV {networks}\n\tProduttori serie {prodctors}\n\n\tDati revisionati il {update_time}\n\n\n".format(**self.serie_json['detailed_infos'][short_name]))


class Bot_API(SerieTvItaly_bot):
	def __init__(self, id, pw):
		self.id = id
		self.pw = pw

	def execute_command(self, version, name_function, type_action, params={}, headers={}):
		def_paras = {'a_id':self.id, 'a_pw':self.pw}
		if (len(params) != 0):
			for key in params:
				def_paras[key] = params[key]
		response = requests.get("https://serietvitalia.ml/api/" + type_action + "/" + str(version) + "/" + name_function, params=def_paras, headers=headers)
		json_response = response.json()
		return json_response

def main():
	api_account = Bot_API('terminal_api', 'terminal_api')
	bot_accout = SerieTvItaly_bot(api_account)
	bot_accout.terminal_api()
	
	if bot_accout.login:
		bot_accout.beauty_print()

	else:
		print("Server error: {}".format(bot_accout.error))


if __name__ == '__main__':
	main()