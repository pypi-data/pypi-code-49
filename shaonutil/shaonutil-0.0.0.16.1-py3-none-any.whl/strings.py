"""String"""
import string
import random
import pprint

def nicely_print(dictionary,print=True):
	"""Prints the nicely formatted dictionary - shaonutil.strings.nicely_print(object)"""
	if print: pprint.pprint(dictionary)

	# Sets 'pretty_dict_str' to 
	return pprint.pformat(dictionary)

def change_dic_key(dic,old_key,new_key):
	dic[new_key] = dic.pop(old_key)
	return dic


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    for c in range(10):
        letters = letters + str(c)

    return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == '__main__':
	pass