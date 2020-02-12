import json


def validate_dictionary_value(data_dict):
	for key, value in data_dict.items():
		try:
			if value.strip():
				pass
			else:
				data[key] = None
		except:
			if value == None:
				data_dict[key] = None

	return data_dict

def message_value(message, info, value):
	counter_message = {}
	counter_message ['counter_message'] = message
	counter_message['counter_value'] = value
	
	if info != {}:
		if info is not None and type(info) == type({}):
			counter_info =  info
			try:
				counter_info_str = json.dumps(counter_info)
				counter_info = json.loads(counter_info_str)
				counter_info = validate_dictionary_value(counter_info)
				counter_message['info'] = counter_info

			except Exception as e:
				print("GDLOGGING : please provide info as dict")
				print(str(e))
				counter_message['info'] = {"gdlogging_error": str(e)}
				pass
	
	return counter_message
