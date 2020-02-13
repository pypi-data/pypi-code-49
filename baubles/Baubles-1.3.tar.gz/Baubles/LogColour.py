#!/usr/bin/env python3

import os,re,sys,logging
from dateutil import tz
from datetime import date, datetime, timedelta

from Baubles.Colours import Colours

class ColouredFormatter(logging.Formatter):

	def __init__(self, msg, use_colour = True):
		self.colours = Colours(colour=use_colour)
		self.levels = {
			'DEBUG':	self.colours.Blue,
			'INFO':	 self.colours.Green,
			'WARNING':  self.colours.Orange,
			'ERROR':	self.colours.Purple,
			'CRITICAL': self.colours.Red,
		}
		self.gmt = tz.gettz('UTC')
		self.ltz = tz.gettz() # empty arg == local time zone
		#logging.Formatter.__init__(self, msg)

	def format(self, record):
		d = datetime(1970,1,1)
		td = timedelta(seconds=record.created)
		dt = d + td
		nt = dt.replace(tzinfo=self.gmt).astimezone(self.ltz)
		level = self.levels[record.levelname] + record.levelname[0:4]
		return ''.join([
			self.colours.Orange,
			'[',
			self.colours.Teal,
			nt.strftime('%Y-%m-%d %H:%M:%S'),
			' ',
			level,
			self.colours.Teal,
			' ',
			record.name,
			self.colours.Orange,
			'] ',
			self.colours.Off,
			str(record.msg),
		])

class ColouredLogger(logging.Logger):
	def __init__(self, name):
		logging.Logger.__init__(self, name, logging.DEBUG)
		colour_formatter = ColouredFormatter(name)
		console = logging.StreamHandler()
		console.setFormatter(colour_formatter)
		self.addHandler(console)
		return


def main():
	logging.setLoggerClass(ColouredLogger)
	log = logging.getLogger(os.path.basename(sys.argv[0]).replace('.py',''))
	
	log.debug('this is debug')
	log.info('this is info')
	log.warning('this is warning')
	log.error('this is error')
	log.critical('this is critical')
	
	return

if __name__ == '__main__': main()
