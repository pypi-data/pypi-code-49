from time import sleep as  sl
from time import time  as  ti
from datetime import datetime

# Sleep
def sleep(secounds):
	return sl(secounds)

# Time
def time():
	return ti()

# Date
class date:
	def now(args):
		return datetime.now().strftime(args)

	def all():
		return date.now('%d/%m/%Y %H:%M:%S') 

	def day():
		return date.now('%d')

	def month():
		return date.now('%m')

	def year():
		return date.now('%Y')

	def hour():
		return date.now('%H')

	def minute():
		return date.now('%M')

	def secound():
		return date.now('%S')
