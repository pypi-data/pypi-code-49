import h5py as hp
import numpy as np
import pandas as pd
import argparse, sys, os
import matplotlib.pyplot as plt 
 
class PlotOptions:
	def __init__(self, dictIn=None):
		if dictIn:
			self.__dict__.update(dictIn)	
		else:
			self.resetDefaults()
	
	def resetDefaults(self):
		self.fontsize = 10
		self.xlim = (1e-3, 1e2)
		self.ylim = 'auto'#(1e-20, 1e-5)
		self.dpi = 100
		self.title = ""
		self.xlabel = "Energy Deposited [MeV]"
		self.ylabel = ""
		self.logx = True
		self.logy = True
		self.size = (6.4, 4.8)
		self.dashes = (None, None)
		self.dashesOn = True
		self.drawstyle = 'steps' # or default
		self.legendPadding = 0.8
		self.save = False
		self.saveOnly = False 				# Don't plot, just save 
		self.saveFormat = 'png'
		self.saveName = ''
		self.bbox_inches = 'tight'			# fits legend when saving plot 
		self.legend = None 					# default to file/histogram names
		self.loc = 'center left'			# legend location
		self.bbox_to_anchor = (1.05, 0.5) 	# legend anchor 

plot_options = PlotOptions()

def resetOptions():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--files' , type=str, nargs="+", default=[], help='Only load data from the HDF5 files listed after this flag (rather than every HDF5 in the directory)')
	parser.add_argument('--fullpath', '--includeFilenames', action='store_true', default=False, help='include the full filename')
	parser.add_argument('--no-load', action='store_true', default=False, help='Only load the file/histogram names into memory, not the histogram data. Usefull for files with a large number of histograms')
	parser.add_argument('--no-norm', action='store_true', default=False, help='for pkl/txt files; selecting this flag disables the interactive setting of the gfu and nIons for the run/file.')
	parser.add_argument('-m', '--manual-load', action='store_true', default=False, help='default behavior for mreddata is to autodetect what kind of file is being opened. Use the manual flag to select the data type class (Hdf5Data(), PklData(), TxtData()) manually. The default selection is based on the file extensions of whichever file is first in options.files, and renders the appropriate class as Data() (e.g. using "import Hdf5Data as Data")')
	#parser.add_argument('-e', '--include-error', action='store_true', default=False, help='include error bars in the plot')TODO
	options, __remaining = parser.parse_known_args(sys.argv[1:])
	if not options.files:
		from glob import glob
		options.files = glob("*.hdf5")
		if not options.files:
			options.files = glob("*.pkl")
			if not options.files:
				options.files = glob("*.txt")
	return options

options = resetOptions()


### TODO: write class
colors = {
	'cu' : [(252./255,13./255,27./255)],
	'copper' : [(252./255,13./255,27./255)],
	'w' : [(41./255,253./255,47./255)],
	'tungsten' : [(41./255,253./255,47./255)],
	'au' : [(1,127./255,0)],
	'ru' : [(153./255,102./255,51./255)],
	'co' : [(0, 0, 1)],
	'cobalt' : [(0, 0, 1)]}

######################
# \class Histogram
#### TODO: (maybe) -- write export functions (csv, pickle etc.)
class Histogram:
	'''
	@df 	: pandas DataFrame object, optional for partially loaded large files.
	@label 	: label to display in the plot legend; defaults to the full path (filename + histogram name)
	@color 	: rbg tuple or matplotlib keyword; used for plotting
	@gfu 	: gun fluence unit attribute from the root directory of the .hdf5 file. In units of cm2. May also be set manually using the device radius (include 4pi solid angle factor for isotropic gun direction)
	@nIons 	: nIons attribute from the root directory of the .hdf5 file. Total number of ions associated with the simulation output file. 
	@custom : boolean flag allowing pandas DataFrames of non-standard format. #TODO: implement this functionality by default type checking 
	'''
	def __init__(self, histname, filename, df = None, label=None, color=None, dashes = (None, None), sortOrder=None, gfu=1, nIons=0, custom=False):
		self.filename = filename
		self.name = histname
		self.color = color
		self.fullpath = self.filename + " - " + self.name
		self.label = label if label else self.fullpath 
		self.sortOrder = sortOrder
		self.gfu = gfu
		self.nIons = nIons
		self.dashes = dashes
		self.setDF(df, custom = custom)

	def __repr__(self):
		if options.fullpath:
			return self.filename + " - " + self.name
		else:
			return self.name
	
	def setDF(self, df, yOnly =True, custom=False):
		if custom:
			self.df = df
			return df#There has to be a better way of doing this. TODO
		if type(df) != type(None):
			if yOnly:
				#columnsToNormalize = ['y']#TODO: Procedurally generate the other columns based on this rather than explicitly, expand for all columns (xy, x2y etc.)
				df = df[['x', 'y', 'y2', 'n', 'w']].copy()
				df.columns = ['x', 'y_raw', 'y2_raw', 'n', 'w']
				if int(sum(df['n'])) > self.nIons:
					self.nIons = int(sum(df['n'])) ###This should never happen...
				df.loc[:, ('y_norm')] = df['y_raw']/(self.gfu * self.nIons)
				df.loc[:, ('yerr_norm')] = np.sqrt(df['y2_raw'])/(self.gfu * self.nIons)
				df.loc[:, ('y_int')] =  df.loc[:,('y_norm')][::-1].cumsum()[::-1]
				df.loc[:, ('yerr_int')] =  df.loc[:,('yerr_norm')][::-1].cumsum()[::-1]
				df.loc[:, ('y_diff')] = df['y_norm'] / df['w']
				df.loc[:, ('yerr_diff')] = df['yerr_norm'] / df['w']
				df['y_diff'][0] = 0
				df['yerr_diff'][0] = 0
				df = df.replace(np.inf, 0)
				df = df.fillna(0)
				self.df = df
				self._getTotalDose()
			else:
					##TODO
				columnsToNormalize = ['y', 'y2', 'xy', 'x2y']
	
	def getHistAtE(self, energy, column = None):
		idx = np.abs(self.df['x'] - energy).idxmin()		
		if column:
			return list(self.df[idx:idx + 1][column])[0]
		else:
			return self.df[idx:idx + 1]

	def _getTotalDose(self):####Need way of converting from revInt back to diff/raw for calculating total dose. 
		''' Returns the total dose accumulated in a sensitive region's histogram. Does not include the under/overflow bins. 
		Default MRED units assumed -- MeV '''# TODO: Include conversion to useful units ( rad (SiO2) )
		try:
			self.totalDose =  np.sum(list(self.df['x'] * self.df['y_norm'])[1:-1])
			self.totalDoseN =  np.sum(list(self.df['x'] * self.df['n'])[1:-1])
		except:
			print("ERROR -- no data in Histogram object")
	
	#def setColor(element):

	

######################
# \class _HistogramListMgr
#	
#	This private class provides utilities for managing the histogram object list such as sorting, selecting, filtering
class _HistogramList:
	def __init__(self, listIn = []):
		self.histograms = []
		if type(listIn[0]) == str:
			for item in listIn:
				if " - " not in item:
					print("\n\n\n***********************\nERROR in setting Histogram object list. If only entering names and not Histogram objects, these should be in the format of '/path/to/filename.hdf5 - histogramName' (i.e. with a space-slash-space separating the filename and histogram name).\n\nBreaking from this entry. {}\n\n".format(item))
					break
				else:
					filename, histname = item.split(" - ")
					self.histograms.append(Histogram(histname=histname, filename=filename))
		else:
			self.histograms = listIn
		self._reset = self.histograms
		self.histogramsDict ={} 
		for item in self.histograms:
			self.histogramsDict[item.fullpath] = item
		self.customHistograms = []

	_histNames = property(lambda self: [x.fullpath if options.fullpath else x.name for x in self.histograms if type(x) == Histogram], None, None, "")

	filenames = property(lambda self: list(set([x.filename for x in self.histograms])), None, None, "")

	def __repr__(self):
		self.displayHistograms()
		return ""

	def __len__(self):
		return len(self.histograms)

	def __getitem__(self, item):
		return self.histograms[item]

	def dropHistograms(self, *args, exact=False, dropFilter=None):
		''' Removes histograms from the list based on any number of matching strings passed as arguments. '''
		if args:
			for item in args:
				if type(item) == list:
					for i in item:
						self.dropHistograms(exact=exact, dropFilter=i)
				else:
					self.dropHistograms(exact=exact, dropFilter=item)
		else:
			if exact:
				selected = [f for f in self.histograms if dropFilter != f.name]
			else:
				selected = [f for f in self.histograms if dropFilter not in f.fullpath]
			self.histograms = selected

	def selectHistograms(self, *args, exact=False, selectFilter=None):
		''' Updates the histogram object list to only include those histograms which match the patterns passed as string arguments'''
		if args:
			for item in args:
				if type(item) == list:
					for i in item:
						self.selectHistograms(exact=exact, selectFilter=i)
				else:
					self.selectHistograms(exact=exact, selectFilter=item)
		else:
			if exact:
				selected = [f for f in self.histograms if selectFilter == f.name]
			else:
				selected = [f for f in self.histograms if selectFilter in f.fullpath]
			self.histograms = selected

	def resetHistograms(self):
		''' update the histogram list to its original (complete) state'''
		self.histograms = self._reset
	
	def displayHistograms(self):
		''' Displays the directory tree of histograms/files in the histogram object list'''
		dirs = set([x.filename for x in self.histograms])
		for parent in dirs:
			print("---------------------------------------")
			print(parent)
			print("  |")
			for hist in self.histograms:
				if parent in hist.filename:
					print("  ├── {}".format(hist.name))

### TODO: Change name to stupidCombineAll

	def stupidCombineAllHistograms(self):
		### Takes all of the histograms in the current histogram object list 
		## 	and attempts to combine them based on the histogram names. This is 
		## 	called stupid on purpose -- it should only be done AFTER the list is 
		##  filtered to only include histograms from those files which should be 
		##  combined. (e.g. filter to all of the copies from a specific run [using
		##  my standard naming scheme of 00X_Y.hdf5, 00X_Y.hdf5...], and then call 
		##  this function to return a list of custom histograms that are combined
		##  based on the names of the histograms)

		pathState = options.fullpath
		options.fullpath = False
		pathCheck = set(['/'.join(x.split("/")[:-1]) +"/" +  x.split("/")[-1].split("_")[0][:-3] for x in self.filenames])
		uniquePath = list(pathCheck)[0]
		if len(pathCheck) > 1:
			print("{}".format(data.filenames))
			cont = input("\n\nWARNING: the filenames do not match. \n\nAre you __SURE__ you want to name-combine all of the histograms in the current list? [y/Any]: ")
			if cont != 'y':
				return False
			else:
				print("Continuing...combining based of the first path name: {}".format(uniquePath) )

		histogramNames = list(set([h.name for h in self.histograms]))
		for hName in histogramNames:
			self.resetHistograms()
			self.selectHistograms(uniquePath, hName)
			self.combineHistograms(newHistName = hName, filename = uniquePath )

		options.fullpath = pathState
         


	def combineHistograms(self, newHistName, label="", color="", histograms=[], filename = 'combined histograms'):
		#TODO: add method for saving to file, extend the custoHistograms list
		''' Combines all of the histgorams in the current Histogram object list''' 
		if not histograms:
			histograms = self.histograms

		if len(set([h.gfu for h in histograms])) > 1:
			print("ERROR: gun fluence units do not match -- cannot combine histograms." )
			return False

		#if sum([h.df['w'] for h in histograms]) / len(histograms) != h.df['w']:
			#print("ERROR: bin widths do not match")
		#TODO: Fix this...don't need it for right now though (NSREC)
		
		if len(histograms) > 0:
			gfu = histograms[0].gfu 
		else:
			print("ERROR: No histograms passed to combineHistograms()")
			return False
		nTotal = sum([h.nIons for h in histograms])
		cDF = histograms[0].df.loc[:,('x', 'w')]
		cDF[['y','y2','n']] = sum([h.df[['y_raw','y2_raw', 'n']] for h in histograms])
		newHist = Histogram(histname = newHistName , filename=filename, label=label, color=color, df = cDF, gfu = gfu, nIons=nTotal)
		self.customHistograms.append(newHist)
		return newHist

	#TODO: Think about how to make this more efficient, allow for pltoting different types aside from just y_int for example
	def plot(self, histograms = [], y='y_int',**kwargs):
		# override global plot_options in this instance with kwargs passed as function parameters; set kwargs specific to df.plot()
		allOptions = PlotOptions(plot_options.__dict__)
		allOptions.__dict__.update(kwargs)

		# load histograms
		if not histograms:
			histograms = self.histograms
		# automatically find the best y limit
		if allOptions.ylim == 'auto':
			yMin = 1e300
			yMax = 1e-300
			for h in histograms:
				tmin = h.df[h.df[y] > 0][y].min()
				tmax = h.df[h.df[y] > 0][y].max()
				yMin = tmin if tmin < yMin else yMin
				yMax = tmax if tmax > yMax else yMax
			yMax *= 10
			allOptions.ylim = (yMin, yMax)

		plotKwargs = {k:v for k, v in allOptions.__dict__.items() if k in ['kind', 'figsize', 'use_index', 'title', 'grid', 'legend', 'style', 'logx', 'logy', 'loglog', 'xticks', 'yticks', 'xlim', 'ylim', 'rot', 'fontsize', 'colormap', 'colorbar', 'position', 'table', 'yerr', 'xerr','capsize', 'dahses', 'drawstyle']}

		plt.figure()
		ax = plt.subplot()

		for histogram in histograms:
			df = histogram.df
			if allOptions.dashesOn:
				if histogram.color:
					df.plot(x='x', y=y, label = histogram.label, dashes = histogram.dashes, color=histogram.color, ax = ax, **plotKwargs)
				else:
					df.plot(x='x', y=y, label = histogram.label, dashes = histogram.dashes, ax = ax, **plotKwargs)
			else:
				if histogram.color:
					df.plot(x='x', y=y, label = histogram.label, color=histogram.color, ax = ax, **plotKwargs)
				else:
					df.plot(x='x', y=y, label = histogram.label, ax = ax, **plotKwargs)

		if allOptions.legend:
			ax.legend(allOptions.legend, loc=allOptions.loc, bbox_to_anchor = allOptions.bbox_to_anchor)
		else:
			ax.legend(loc=allOptions.loc, bbox_to_anchor = allOptions.bbox_to_anchor)
		ax.set_xlabel(allOptions.xlabel)
		ax.set_ylabel(allOptions.ylabel)
		ax.set_title(allOptions.title)
		plt.subplots_adjust(right=allOptions.legendPadding)

		# Saves based on saveName option setting, or title if none, or defaultSaveName if no title.
		if allOptions.save:
			if not allOptions.saveName:
				if not allOptions.title:
					allOptions.saveName = 'defaultSaveName'
				else:
					allOptions.saveName = allOptions.title
			plt.savefig(allOptions.saveName+"."+allOptions.saveFormat, format=allOptions.saveFormat, dpi=allOptions.dpi, bbox_inches=allOptions.bbox_inches)

		if not allOptions.saveOnly:
			plt.show()
