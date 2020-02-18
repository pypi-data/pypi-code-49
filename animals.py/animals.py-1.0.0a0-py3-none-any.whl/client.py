import requests
import random

class RequestError(Execption):
	"""Base Exception"""
	pass

class Animals:
	"""
	Base Class for the module. This module uses https://some-random-api.ml/. 
	This module can be used to get random animals image/fact. 
	This is a simple module, which uses requests library.
	
	Attributes
	---------------
	
	image
		Returns the url of the animal image
		
		Parameters
		------------------
		animal: :class: `str`
			The animal which you are going to get the url.
			If not animal given it will give a random image.
			
	fact
		Return the fact of the animal image
		
		Parameters
		------------------
		animal: :class: `str`
			The animal which you are going to get the fact.
			If not animal given it will give a random fact
	"""
	
	def image(animal=None):
		options = ("cat", "dog", "koala", "fox", "birb", "red_panda", "panda", "racoon", "kangaroo")
		if animal is not in options and animal != None:
			raise RequestError(animal + "is not a valid options\nValid Options are cat, dog, koala, fox, birb, red_panda, panda, racoon, kangaroo")
			
		if animal == None:
			choice = random.choice(options)
			r = requests.get(f"https://some-random-api.ml/img/{choice}")
			r = r.json()
			url = r["link"]
			return url
			
		else:
			r = requests.get(f"https://some-random-api.ml/img/{animal}")
			r = r.json()
			url = r["link"]
			return url