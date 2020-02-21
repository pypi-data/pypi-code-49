import h5py as hp
import pandas as pd
from .datatools import _HistogramList, options, Histogram
 
######################
# \class Hdf5Data
#
# 	The main datatool object in mreddata, providing data manipulation and plotting methods. 
class Hdf5Data(_HistogramList):

	def __init__(self):

		self.__nameMap = {}
		self.__attrs = {} 
		self.__stringData = {}
		self.__strings = {}
		self.__histograms = {}

		for filename in options.files:
			if '.hdf5' in filename:
				try:
					with hp.File(filename, 'r') as f:
						tables = [f['runs'][k] for k in f['runs'].keys()][0]['tables']
						self.__stringData[filename] = [x[0] for x in tables['string_data'][()]] #TODO: Allow for many runs in one hdf5? low priority
						self.__strings[filename] = tables['strings'][()]
						self.__histograms[filename] = tables['histograms'][()]
						self.__attrs[filename] = {}
						for key in f.attrs.keys():	# populate the attributes dict
							self.__attrs[filename][key] = f.attrs[key]
					self.__constructNameMap(filename)

				except Exception as e:
					print("ERROR creating Hdf5Data object for {}".format(filename))
					print(e)

		#  this is a 1-D dictionary as opposed to the other private attributes
		try:
			super().__init__(list(self.__nameMap.keys()))
		except:
			print("ERROR: Couldn't load histgrams...check the path to make sure it's where the Hdf5 files are located.")
		self.__loadAllHistograms()

	def __getHistogramName(self, strings, filename):
		return ''.join([chr(self.__stringData[filename][strings[0]+x]) for x in range(strings[1]-1)])
	def __constructNameMap(self, filename):
		for i in self.__histograms[filename]:
			histogramName = self.__getHistogramName(self.__strings[filename][i[0]], filename)
			self.__nameMap[filename + " - " + histogramName] = (i[1], i[1]+i[2])


	def attributes(self, *args):
		''' Displays the file attributes for all files in the current Histogram object list. Shows all file attributes by default, 
		with the options to pass strings as arguments to view only those attribuetes. '''
		filenames  = set([h.filename for h in self.histograms])
		for filename in filenames:
			print("--------------------------------")
			print(f"{filename}")
			print("  |")
			for k, a in self.__attrs[filename].items():
				#for filename, attrs in self.__attrs.items():
					#if filename in [x.fullpath for x in self.histograms]:
				if args:
					for arg in args:
						if arg in k:
							print("  ├-- {:<15}\t{:<15}".format(str(k), str(a)))
				else:
					print("  ├-- {:<15}\t{:<15}".format(str(k), str(a)))

#TODO: Add attributes dict
	
	def _getHistogram(self, filename,  histogramName=None, diff=None):
		''' Loads a histogram from the given @filename. Defaults to the first histgoram in the file, but can select 
		which histogram to load with @histogramName'''
		try:
			displaystate = options.fullpath
			options.fullpath = True
			histogramName = histogramName if histogramName else self._histNames[0]
			options.fullpath = displaystate
			try:
				if self.histogramsDict[filename + " - " + histogramName].df:
					return self.histogramsDict[filename + " - " + histogramName]
			except:
				pass

			with hp.File(filename, 'r') as f:
				tables = [f['runs'][k] for k in f['runs'].keys()][0]['tables']
				df = pd.DataFrame(tables['histogram_data'][self.__nameMap[filename + " - " + histogramName][0] : self.__nameMap[filename + " - " + histogramName][1]])
				#df = pd.DataFrame(tables['histogram_data'][()][self.__nameMap[filename + " - " + histogramName][0] : self.__nameMap[filename + " - " + histogramName][1]])
			df.name = filename + " - " + histogramName
			try:
				gfu = self.__attrs[filename]['gfu'][0]  	#TODO: Think about generalizing this to any naming convention for nIons/gfu
				nIons = self.__attrs[filename]['nIons'][0]
			except:
				print("ERROR: Can't set gfu or nIons attribute from hdf5 file.")
				gfu = 1
				nIons = 1
			histogram = self.histogramsDict[df.name]#Histogram(filename = filename, histname = histogramName, df = df, gfu = gfu, nIons=nIons)
			histogram.setDF(df)
			#self.histogramsDict[df.name] = histogram

			return histogram
		except Exception as e:
			print("ERROR in _getHistogram method: {}".format(e))
			
	def getHistograms(self, filename=None, histogramNames=None):
		''' Load and return all of the histograms in the current Histogram object list.'''
		output=[]
		filenames = [x.filename for x in self.histograms]
		try:
			displaystate = options.fullpath
			options.fullpath = True
			for filename in filenames:
				histogramNames = [x for x in self._histNames if filename in x]
				for histName, histBounds in self.__nameMap.items():
					if filename in histName:
						if histName in histogramNames: #TODO: CLean this spaghetti bullshit up
							if " - " in histName:
								histName = histName.split(" - ")[1]
							histogram = self._getHistogram(filename = filename, histogramName=histName)
							output.append(histogram)
			options.fullpath = displaystate
			return output
		except Exception as e:
			options.fullpath = displaystate
			print("ERROR in getHistograms method: {}".format(e))
	
	def __loadAllHistograms(self):
		if not options.no_load: #	--no-load is usefull for large files with many histograms; allows exploration of available options without loading into memory
			for filename in options.files:
				with hp.File(filename, 'r') as f:
					try:
						gfu = self.__attrs[filename]['gfu'][0]  	#TODO: Think about generalizing this to any naming convention for nIons/gfu
						nIons = self.__attrs[filename]['nIons'][0]
					except:
						print("ERROR: Can't set gfu or nIons attribute from hdf5 file.")
						gfu = 1
						nIons = 1
					tables = [f['runs'][k] for k in f['runs'].keys()][0]['tables']
					file_df = pd.DataFrame(tables['histogram_data'][()])
					for key, bounds in self.__nameMap.items():
						if filename in key:
							#df= copy.deepcopy(file_df)
							df = file_df.loc[bounds[0]:bounds[1]-1].reset_index(drop=True)
							histogram = self.histogramsDict[key] #Histogram(filename = filename, histname = key.split(" - ")[1], df=df, gfu = gfu, nIons=nIons)
							histogram.gfu = gfu
							histogram.nIons = nIons
							histogram.setDF(df)
							#self.histogramsDict[key] = histogram
							del df
				del tables, file_df
