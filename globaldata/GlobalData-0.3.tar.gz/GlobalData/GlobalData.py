#GlobalData.py
#p1.py
import time
import pickle as pk
import glob
from threading import Thread
import os.path as PATH
import os
import dill as d

'''
from Globals import *
gd = GlobalData()
def pp(data):
	print("data",data)
	return setBackgroundColor(data)
gd.Run("rotr",(100,200,233),pp)
'''

''' > > > > >
# gd.SaveFuncX("foo",(lambda:print("yo!!!")))
# x = lambda: print("XXXXXXX")
# gd.SaveFuncX("foo",x)
# gd.SaveFuncX("foo",lambda:os._exit(1))
# gd.SaveFuncX("foo",x)
# >>> gd.SaveFuncX("foo",(lambda:print(tt.ctime())))
 > > > > > Search funcExample1  '''

printX = False

def PubExit(gd):
	if gd is None:
		gd = GlobalData()

	gd.pub("exitAll",[True, time.time()])


def SubExit(gd, id = None):
	if gd is None:
		gd = GlobalData()
	gd.sub("exitAll",Exit,block = False)
	if id is not None:
		gd.sub("exit"+id,Exit,block = False)

# def SubExit(gd, id = None):
# 	if gd is None:
# 		gd = GlobalData()
# 	waitSubExitAll(gd)
# 	if id is not None:
# 		waitSubExitID(gd,id)
#
# def waitSubExitID(gd, id):
# 	t = Thread(target = waitSubExitIDT, args = [[gd, id],])
# 	t.start()
#
# def waitSubExitAll(gd):
# 	t = Thread(target = waitSubExitAllT, args = [[gd, ],])
# 	t.start()
#
# def waitSubExitIDT(data):
# 	gd, id = data
# 	gd.sub("exit"+id,Exit,block = True)
#
# def waitSubExitAllT(data):
# 	gd = data[0]
# 	gd.sub("exitAll",Exit,block = True)
# 	# gd.sub("exitAll",Exit,block = True)


###### from GlobalData import *
###### r = lambda c : c is 100 and True or (lambda a: print(a) is None and r(a))(c+1)

def exxit():
	print("SAYONARA!")
	os._exit(1)

def Exit(d=None):
	print("!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!")
	if d is None:
		exxit()
	else:
		print(d)
	data, channel = d
	if data[0]:
		# print("AAAAA")
		# printT(channel)
		# print("BBBB")
		exxit()
	else:
		print("Not Exiting...")

def waitExit(x = 3):
	t = Thread(target = waitExitT, args = [[x],])
	t.start()
def waitExitT(data):
	x = data[0]
	for i in range(x):
		print(("EXITING IN ",x-i))
		time.sleep(1)

	print("BYE!!!!!!!!")
	os._exit(1)
	print("BYE!!!!!!!!2")




def funcExample1():
	c = "foo"
	print("test channel = ",c)
	# fff = [(lambda: print("FFFFFFFF"))]
	gd = GlobalData()
	fff = gd.bindFunc(c)
	q = fff[0]
	while(True):
		time.sleep(0.01)
		print(fff, fff[0](), q())

def funcExample2():
	c = "foo"
	print("test channel = ",c)
	# fff = [(lambda: print("FFFFFFFF"))]
	gd = GlobalData()
	fff = gd.bindFunc(c)
	q = fff[0]
	while(True):
		time.sleep(0.01)
		print(fff, fff[0](), q())


def funcExample0():
	fff = [(lambda: print("FFFFFFFF"))]
	gd = GlobalData()
	gd.bind("fff",fff)
	while(True):
		d.loads(fff[0])()


def non():
	print("-----non-----")
	return None

class Wrapper:
	def __init__(self, data):
		self.data = [data]

	def __call__(self):
		return self.data[0]()

class GlobalData:
	#def __init__(self,dir = "/media/magic/EV1/GlobalData/", max = 100000000, wait=0.01):
	def __init__(self,dir = "X/GlobalData/", max = 10000000, wait=0.01, lowerCase = False, printPub = False, debug = False):
		# print("AAAAAAAAAAAAAAAAAAAAa")
		self.Threads = []
		self.Debug = [debug]
		self.dir = dir
		self.extChannel = ".gdc"
		self.extData    = ".gdd"
		self.__Channels = list()
		self.max = max
		self.wait = wait
		self.lowerCase = lowerCase
		self.printPub = printPub
		dbexist = PATH.exists(dir)
		if not dbexist:
			os.makedirs(dir)
		uT = Thread(target = self.__updateChannels, args = [self])
		uT.start()
		self.Threads.append(uT)

	def GetChannels(self):
		chn = list()
		for k in self.__Channels:
			a = k.split(".")[0]
			if a not in chn:
				chn.append(a)
		chn.sort()
		return chn

	def __updateChannels(self, data):
		#channels = sorted(glob.glob(dirPath+'*'),key=os.path.getmtime)
		ttt = str(time.time())
		#print("updating channels","OOOOOOOOOOOOOOOOOOO")
		while(True):
			# print("x Checking Channels...", ttt)
			channels = glob.glob(self.dir+'*')
			if len(channels) == 0:
				self.printF("0 Channels")
				self.__Channels = list()
			for c in channels:
				cn = c.split(self.dir)
				if len(cn)>0 and cn[-1] not in self.__Channels:
						self.__Channels.append(cn[-1])
						self.printF("added channel",cn[-1])
			time.sleep(0.1)

	def channelUpdate(self, channel, untilTrue = True):
		if self.lowerCase:
			channel = channel.lower()
		self.addChannel(channel)

		data = self.load(self.dir+channel+self.extChannel, untilTrue = untilTrue)
		if data is None:
			data = -1
		if (data > self.max):
			data = 0
		data += 1
		self.savePath(data,self.dir+channel+self.extChannel,untilTrue = untilTrue)

	def awaitChannelUpdate(self, channel):
		if self.lowerCase:
			channel = channel.lower()
		wait=self.wait
		d = self.load(self.dir+channel+self.extChannel)
		#print("ddddddddddddddddd",d)
		if d is None:
			d = self.load(self.dir+channel+self.extChannel)
			if d is None:
				return None
		tempD = d+0
		#print(d,tempD,str(d) == str(tempD))

		while(str(d) == str(tempD)):
			# print(".",d)
			d = self.load(self.dir+channel+self.extChannel)
			time.sleep(wait)
		self.printF("!!!!!!!!!!!!!!!!!")
		return self.load(self.dir+channel+self.extData)

	def pub(self, channel, data, untilTrue = True):
		if self.lowerCase:
			channel = channel.lower()
		if self.printPub:
			print("PUB: ", channel,"\n:::", data)
		return self.save(data, channel, untilTrue = untilTrue)

	# def pubZZ(self, channel, data):
	# 	#if channel+self.extChannel not in self.__Channels:
	# 	#	self.addChannel(channel)
	# 	#else:
	# 	#	self.channelUpdate(channel+self.extChannel)
	# 	#	self.save(data,self.dir+channel+self.extData)
	#
	# 	#self.printF("########")
	# 	self.addChannel(channel)
	# 	#self.printF("########")
	# 	self.channelUpdate(channel+self.extChannel)
	# 	self.savePath(data,self.dir+channel+self.extData)

	def sub(self, channel, func=None, autoPub = None, block = True, once= False, echo=True, debug = False):
		if func is None:
			func = self.defFunc
		if self.lowerCase:
			channel = channel.lower()
		#if channel+self.extChannel not in self.__Channels:
		#self.printF("########")
		self.addChannel(channel)
		#self.printF("########")

		if echo:
			print("Subscribing to", channel)
		if block:
			self.waitAndExe(channel, func, once, autoPub = autoPub, debug = debug)
		else:
			uT = Thread(target = self.waitAndExe, args = [channel, func, once, autoPub, debug])
			self.Threads.append(uT)
			uT.start()

	def defFunc(self, data):

		data, channel = data
		print()
		print(":::::::: "+channel+ "- incoming data ::::::::::::::::::::::::::::: "+time.ctime())
		print(data)
		print(":::::::: "+channel+ "- incoming data :::::::::::::::::::::::::::::")
		print()
		return data

	# def subUDP(self, channel, func, autoPub = None, block = True, once= False, echo=True):
	# 	if self.lowerCase:
	# 		channel = channel.lower()
	# 	#if channel+self.extChannel not in self.__Channels:
	# 	#self.printF("########")
	# 	self.addChannel(channel)
	# 	#self.printF("########")
	# 	autoPub = [channel]
	#
	# 	if echo:
	# 		print("Subscribing to UDP", channel, "IP:", ip ,"PORT",port)
	# 	if block:
	# 		self.waitAndExe(channel, func, once, autoPub = autoPub)
	# 	else:
	# 		uT = Thread(target = self.waitAndExe, args = [channel, func, once, autoPub])
	# 		uT.start()
	def bind(self, channel, default = None, var = None):
		if var is None or len(var)<1:
			var = [None]

		curr = self.GetX(channel)

		if curr is None:
			self.channelUpdate(channel)
		else:
			# self.SaveX(channel,curr)
			var = [curr]
		if default is not None and var[0] is None:
			var[0] = default
			self.SaveX(channel,default)
		# var[0] = curr

		t = Thread(target = self.__bindT, args = [[channel,var],])
		self.Threads.append(t)
		t.start()
		return var


	def __bindT(self, data):
		channel, var = data
		while(True):
			time.sleep(0.01)
			var[0] = self.awaitChannelUpdate(channel)
			print("@@@@@@@@@@@@@@@@@", "updated bind for ",channel, ":::",var)

	def ReRun(self, channel, params = None):
		return self.SaveFuncX(channel, self.GetFuncX(channel), params = params)

	def Run(self, channel, params = None, newFunc = None, untilRes = False):
		func = self.GetFuncX(channel)
		if func is None and newFunc is None:
			print("No Function! for",channel,"- First SaveFuncX !!!!!!!")
			return None
		else:
			self.SaveX(channel+"_done", None)
			if newFunc is None:
				self.ReRun(channel, params = params)
			else:
				self.SaveFuncX(channel,newFunc,params = params)
			res = self.GetX(channel+"_done")
			stop = False
			while res is None and not stop:
				if not untilRes:
					stop = True
				res = self.GetX(channel+"_done")

			# print("!!!!!!!!!!!!!!!","res")
			# print(res)
			# print("!!!!!!!!!!!!!!!")
			return res


	def bindFunc(self, channel, params = None, autoRun = False, preRun = None, ofunc = None):
		var = [None]
		if ofunc is None:
			# if var is None or len(var)<1:
				# var = [(lambda:print("___"))]
			curr = self.GetX(channel)
			if curr is None:
				self.channelUpdate(channel)
			# var[0] = d.loads(curr)
			try:
				var[0] = d.loads(curr)
			except Exception as e:
				print("Exception:",e)
				var[0] = None

			if var[0] is None:
				var[0] = non
		else:
			var = [ofunc]

		if preRun is None:
			# print("TTTTTTTTTTTTT")
			# preRun = self.defPreRun
			pass

		t = Thread(target = self.__bindFuncT, args = [[channel,var, autoRun, preRun],])
		self.Threads.append(t)
		t.start()
		print("binding func to",channel)
		return var

	def defPreRun(self):
		print("preRun")
		return None

	def timeAsTT(self):
		# print("")
		return None
		import time as tt


	def __bindFuncT(self, data):
		channel, var, autoRun, preRun = data
		stop = False
		while(not stop):
			time.sleep(0.01)
			if not self.Debug[0]:
				try:
					data = self.__bindLogic(data)
					channel, var, autoRun, preRun, res, params = data

				except Exception as e:
					print()
					print()
					print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEe")
					print("Exception: ",e)
					print()
					print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEe")
					print()

					self.SaveX(channel+"_done", False)
					# print(e.message)
					# print(e.args)
					if "keyboard" in str(e).lower():
						print("0000000000000000000000000000")
						stop = True
			else:
				data = self.__bindLogic(data)
				channel, var, autoRun, preRun, res, params = data

	def __bindLogic(self, data):
		# print()
		# print("..............")
		res, params = None, None
		if len(data) == 6:
			# print(len(data))
			res, params = data[4], data[5]


		# print(1111111)
		channel, var, autoRun, preRun = data[:4]
		print(channel, var, autoRun, preRun)
		var[0] = d.loads(self.awaitChannelUpdate(channel))
		# print("fffffffff")
		if var[0] is None:
			var[0] = non
		print("\n@@@@@@@@@@@@@@@@@", "updated bind for ",channel)
		# print(1111111)
		if autoRun:
			# print(222222)
			params = [None]
			tparams = self.GetX(channel+"_params")
			if tparams is not None:
				params[0] = tparams

			# print("func:",var, "params",params)
			if preRun is not None:
				preRun()

			# print("PPPPPPPPPPPPPPPPPPPPPP")
			# print("Params :::",params)
			if params is not None:
				if "list" in str(type(params)) and len(params) > 0:
					res = var[0](params[0])
				else:
					res = var[0](params)
			else:
				res = var[0](None)
			# print(222222)
			# print("source res",res)
			self.SaveX(channel+"_done", [True,res])
			# print("xx","...f")
		# print("..............f")
		return channel, var, autoRun, preRun, res, params

	def SubFunc(self, channel):
		return self.bindFunc(channel, autoRun=True)

	def Func(self, channel, func):
		self.SaveFuncX(channel,func)
		return self.bindFunc(channel, autoRun=True, ofunc = func)

	def waitAndExe(self, channel, func, once= False, autoPub = None, debug = False):
		if self.lowerCase:
			channel = channel.lower()
		run = True
		newdata = None
		while run:
			run = not once
			data = self.awaitChannelUpdate(channel)
			self.printF("@@@@@@@@@@@@")
			if not debug:
				try:
					newdata = func([data,channel])
				except:
					pass
			else:
				newdata = func([data,channel])
			self.printF("############")
			if autoPub is not None:
				if type(autoPub) is list:
					for pb in autoPub:
						print("autoPub is ",pb)
						self.pub(pb,newdata)
				else:
					print("autoPub is ",autoPub)
					self.pub(autoPub,newdata)
			else:
				pass
				#print("autoPub is None")




	def addChannel(self, channel):
		if self.lowerCase:
			channel = channel.lower()
		#for l in self.__Channels:
			#self.printF("CHANNEL:",l)
		#	pass
		if channel not in self.__Channels and channel+self.extChannel not in self.__Channels:
			#self.__Channels.append(channel+self.extData)
			#self.__Channels.append(channel+self.extChannel)
			self.savePath(0, self.dir+channel+self.extChannel)
			self.savePath(-1, self.dir+channel+self.extData)
		else:
			self.printF("Already Have Channel",channel)

	def save(self, data, channel, untilTrue = True):
		if self.lowerCase:
			channel = channel.lower()
		### ???
		self.channelUpdate(channel)
		return self.savePath(data,self.dir+channel+self.extData,untilTrue=untilTrue)

	def savePath(self, data, filename, untilTrue = True):
	#    with open(filename,"wb") as file:
	#        pk.dump(data,file)
	#        self.printF("saved",data)
		self.printF("data to be saved:",data)
		self.printF("path:",filename)
		run = True
		while(run):
			run = untilTrue
			try:
				with open(filename,"wb") as file:
					pk.dump(data,file)
					self.printF("saved",str(data), "@",filename)
					run = False
				# del(data)
				### ???
				# print("//////////////////////////")
				return True
			except:
				self.printF("XXXXXXX failed saving")
				time.sleep(0.01)
		return False

	def get(self, filename, untilTrue = True):
		return self.getData(filename,untilTrue)

	def getData(self, filename, untilTrue = True):
		filename = self.dir+str(filename)+self.extData
		return self.load(filename,untilTrue)

	def getChannelData(self, channel):
		return self.get(str(channel),untilTrue=False )

	def load(self, filename, untilTrue = True):
		run = True
		untilTrue = False
		try:
			data = None
			with open(filename,"rb") as file:
				return pk.load(file)
				#self.printF("loaded",data, "from",filename)
			return data
		except:
			if untilTrue:
				self.printF("ERR - Try again, loading",filename)
				time.sleep(0.1)
				self.load(filename)
		return None

	def SaveX(self, channel, data, echo = False):
		time.sleep(0.01)
		if echo:
			print("Saving ",data,"to channel", channel)
		# gd = GlobalData()
		return self.pub(str(channel), data, untilTrue = True)

	def GetX(self, channel, echo = False):
		time.sleep(0.01)
		if echo:
			# print("Loading channel", channel)
			pass
		# gd = GlobalData()
		return self.get(str(channel),untilTrue=False )

	def LoadX(self, channel, echo = False):
		return self.GetX(channel, echo = echo)

	def SaveFuncX(self, channel, func, params = None):
		self.SaveX(channel+"_params", params)
		import dill as d
		return self.pub(channel,d.dumps(func))
		# return SaveX(channel, d.dumps(func))

	def GetFuncX(self, channel):
		import dill as d
		try:
			return d.loads(self.GetX(channel))
		except:
			return None

	def printF(self, data=None, a=None, b=None, c=None, d=None,e=None,f=None,g=None,h=None,i=None,j=None):
		global printX
		s = ""
		ls = [data,a,b,c,d,e,f,g,h,i,j]
		for x in ls:
			if x is not None:
				s = s + str(x)

		if printX:
			print(s)

	def printZ(text, char, thick = 5, length = 70, newline=True, minimal = False):

		#x = list()
		#x.append(text)
		#return x
		TextList = list()
		text = str(text)
		head = char
		for l in range(0,int(length/(len(char)))):
			head += char
		if minimal:
			char = " "
		if newline:
			print()
			TextList.append("")
		extra = length - len(text)
		ntext= ""
		for l in range(0, int(extra/2)+1):
			ntext += char
		ntext+=text
		for l in range(0, int(extra/2)):
			ntext += char
		while (len(ntext)<length+1):
			ntext+=char


		for r in range(0, int(thick)):
			print(head)
			TextList.append(head)
		print(ntext)
		TextList.append(ntext)
		for r in range(0, int(thick)):
			print(head)
			TextList.append(head)
		if newline:
			print()
			TextList.append("")
		return TextList
