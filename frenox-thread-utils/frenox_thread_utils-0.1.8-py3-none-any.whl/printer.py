## a must for py2
from __future__ import print_function

import datetime
from colorama import init
from termcolor import colored
from threading import RLock

PRINT_LOCK = RLock()

## initialize colorama
init()
_id = 1

FORMAT = "%m-%d-%Y %H:%M:%S.%f"

class Printer:
	def __init__(self, id=None):
		global _id
		if id is None:
			self.id = str(_id)
			_id += 1
		else:
			self.id = id

	def str(self):
		return "{} {} {} {}".format(datetime.datetime.now().strftime(FORMAT)[:-3], "| task", self.id, "|")

	def print(self, *args):
		with PRINT_LOCK:
			print(datetime.datetime.now().strftime(FORMAT)[:-3], "| task", self.id, "|", *args, flush=True)

	def info(self, *args):
		with PRINT_LOCK:
			print(datetime.datetime.now().strftime(FORMAT)[:-3], "|", colored("[INFO]", 'green'), " | task", self.id, "|", *args, flush=True)

	def error(self, *args):
		with PRINT_LOCK:
			print(datetime.datetime.now().strftime(FORMAT)[:-3], "|", colored("[ERROR]", 'red'), "| task", self.id, "|", *args, flush=True)

	def warning(self, *args):
		with PRINT_LOCK:
			print(datetime.datetime.now().strftime(FORMAT)[:-3], "|", colored("[WARN]", 'yellow'), " | task", self.id, "|", *args, flush=True)
