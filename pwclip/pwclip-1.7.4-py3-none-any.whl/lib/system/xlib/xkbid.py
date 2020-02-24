"""xkbid - x keyboard id"""
# -*- encoding: utf-8 -*-

from subprocess import Popen, PIPE, DEVNULL

def xkbid():
	o, e = Popen('xinput', stdout=PIPE, stderr=PIPE, shell=True).communicate()
	if o:
		o = o.decode()
	if e:
		e = e.decode()
		print(e)
	ln = [l.split()[-4] for l in o.split('\n') if 'keyboard' in l.lower()][-1]
	return int(ln.split('=')[1])
