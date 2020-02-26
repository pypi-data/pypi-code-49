import pandas as pd
import os

from .func import *
from .SEDanalysis import *
from .toolplot import *

def fitSpec(wav, flux, eflux,\
			z = -0.01,\
			filters = ['PACS70', 'PACS100', 'PACS160', 'SPIRE250ps', 'SPIRE350ps', 'SPIRE500ps'], \
			wavToFit = [70., 100., 160., 250., 350., 500.],\
			UL = [0., 0., 0., 0., 0., 0.], \
			IRSobsCorr = True,\
			Nmc = 10000, pgrbar = 1, \
			Pdust = [10, 1.], PPAH = [9., 1.], Ppl = [-1., 1.], Pbreak = [40., 3.], Pslope1 = [1., 0.1], Pslope2 = [1., 0.1], \
			Plsg = [-1., 1.], Pllg = [-1., 1.],\
			sourceName = 'NoName', pathTable = './', pathFig = './', \
			redoFit = True, saveRes = True):
 
	#test if the path works for the tables
	if pathTable.endswith('/') == False:
		pathTable = pathTable+'/'
	if os.path.isdir(pathTable) == False:
		raise ValueError('The path specified to save the tables does not exist. Please create it.')

	#test if the path works for the figures
	if pathFig.endswith('/') == False:
		pathFig = pathFig+'/'	
	if os.path.isdir(pathFig) == False:
		raise ValueError('The path specified to save the figures does not exist. Please create it.')

	basictests(wav, flux, eflux, filters, wavToFit, UL, z, specOn = True)
	z = abs(z)

	# Upload the templates.
	path = os.path.dirname(iragnsep.__file__)
	templ = pd.read_csv(path+'/B18_full.csv')

	if redoFit == True:
		res_fit = runSEDspecFit(wav, flux, eflux,\
								z = z,\
								filters = filters, \
								wavToFit = wavToFit,\
								UL = UL, \
								IRSobsCorr = IRSobsCorr,\
								Nmc = Nmc, pgrbar = pgrbar, \
								Pdust = Pdust, PPAH = PPAH, Ppl = Ppl, Pbreak = Pbreak, Pslope1 = Pslope1, Pslope2 = Pslope2, Plsg = Plsg, Pllg = Pllg,\
								templ = templ)
	else:
		try:
			res_fit = pd.read_csv(pathTable+sourceName+'_fitRes_spec.csv')
		except:
			raise ValueError('Cannot find the table. Check the name or redo the fit.')

	UL_temp = UL
	UL = np.zeros(len(wav))
	UL[-len(UL_temp)::] = UL_temp

	# Add the params of the host and AGN to the table
	loglum_hostIR, eloglum_hostIR, \
	loglum_hostMIR, eloglum_hostMIR, \
	loglum_hostFIR, eloglum_hostFIR, \
	loglum_AGNIR, loglum_AGNMIR, loglum_AGNFIR, \
	AGNfrac_IR, AGNfrac_MIR, AGNfrac_FIR, SFR, eSFR, wSFR, ewSFR = get_prop(res_fit, templ = templ, z = z)

	try:
		res_fit['logLumIR_host'] = loglum_hostIR
		res_fit['elogLumIR_host'] = eloglum_hostIR
		res_fit['logLumMIR_host'] = loglum_hostMIR
		res_fit['elogLumMIR_host'] = eloglum_hostMIR
		res_fit['logLumFIR_host'] = loglum_hostFIR
		res_fit['elogLumFIR_host'] = eloglum_hostFIR
		res_fit['logLumIR_AGN'] = loglum_AGNIR
		res_fit['logLumMIR_AGN'] = loglum_AGNMIR
		res_fit['logLumFIR_AGN'] = loglum_AGNFIR
		res_fit['AGNfrac_IR'] = AGNfrac_IR
		res_fit['AGNfrac_MIR'] = AGNfrac_MIR
		res_fit['AGNfrac_FIR'] = AGNfrac_FIR
		res_fit['SFR'] = SFR
		res_fit['eSFR'] = eSFR
		res_fit['wSFR'] = wSFR
		res_fit['ewSFR'] = ewSFR
		# res_fit['QF'] = QF
	except:
		res_fit['logLumIR_host'] = pd.Series(loglum_hostIR, index=res_fit.index)
		res_fit['elogLumIR_host'] = pd.Series(eloglum_hostIR, index=res_fit.index)
		res_fit['logLumMIR_host'] = pd.Series(loglum_hostMIR, index=res_fit.index)
		res_fit['elogLumMIR_host'] = pd.Series(eloglum_hostMIR, index=res_fit.index)
		res_fit['logLumFIR_host'] = pd.Series(loglum_hostFIR, index=res_fit.index)
		res_fit['elogLumFIR_host'] = pd.Series(eloglum_hostFIR, index=res_fit.index)
		res_fit['logLumIR_AGN'] = pd.Series(loglum_AGNIR, index=res_fit.index)
		res_fit['logLumMIR_AGN'] = pd.Series(loglum_AGNMIR, index=res_fit.index)
		res_fit['logLumFIR_AGN'] = pd.Series(loglum_AGNFIR, index=res_fit.index)
		res_fit['AGNfrac_IR'] = pd.Series(AGNfrac_IR, index=res_fit.index)
		res_fit['AGNfrac_MIR'] = pd.Series(AGNfrac_MIR, index=res_fit.index)
		res_fit['AGNfrac_FIR'] = pd.Series(AGNfrac_FIR, index=res_fit.index)
		res_fit['SFR'] = pd.Series(SFR, index=res_fit.index)
		res_fit['eSFR'] = pd.Series(eSFR, index=res_fit.index)
		res_fit['wSFR'] = pd.Series(wSFR, index=res_fit.index)
		res_fit['ewSFR'] = pd.Series(ewSFR, index=res_fit.index)
		# res_fit['QF'] = pd.Series(QF, index=res_fit.index)

	if saveRes == True:
		order = ['tplName', 'AGNon', 'logNormGal_dust', 'elogNormGal_dust', 'logNormGal_PAH','elogNormGal_PAH', 'logNormAGN_PL', 'elogNormAGN_PL', 'lBreak_PL',\
				 'elBreak_PL', 'alpha1_PL', 'ealpha1_PL', 'alpha2_PL', 'ealpha2_PL', 'logNorm_Si11', 'elogNorm_Si11', 'logNorm_Si19', 'elogNorm_Si19',\
				 'logLumIR_host', 'elogLumIR_host', 'logLumMIR_host', 'elogLumMIR_host', 'logLumFIR_host', 'elogLumFIR_host', 'logLumIR_AGN', \
				 'logLumMIR_AGN', 'logLumFIR_AGN', 'AGNfrac_IR', 'AGNfrac_MIR', 'AGNfrac_FIR', 'SFR','eSFR', 'wSFR', 'ewSFR', 'logl', \
				 'Aw', 'tau9p7', 'bestModelFlag']

		res_fit.to_csv(pathTable+sourceName+'_fitRes_spec.csv', index = False, columns = order)

	o = np.where(res_fit['bestModelFlag'] == 1)[0]
	res_fitBM = res_fit.iloc[o]

	print('#########################')
	print('# Generating the plots. #')
	print('#########################')
	# Plot all the fits
	plotFitSpec(res_fit, [wav, flux, eflux], UL = UL, pathFig = pathFig, sourceName = sourceName, templ = templ, z = z, saveRes = saveRes)

	return res_fit, res_fitBM


def fitPhoto(wav, flux, eflux,\
			 z = -0.01,\
			 filters = ['MIPS24', 'PACS70', 'PACS100', 'PACS160', 'SPIRE250ps', 'SPIRE350ps', 'SPIRE500ps'], \
			 wavToFit = [24., 70., 100., 160., 250., 350., 500.],\
			 UL = [0., 0., 0., 0., 0., 0., 0.], \
			 Nmc = 10000, pgrbar = 1, \
			 NoSiem = False, \
			 Pdust = [10., 1.], PPAH = [9., 1.], PnormAGN = [10., 1.], PSiEm = [10., 1.], \
			 sourceName = 'NoName', pathTable = './', pathFig = './', \
			 redoFit = True, saveRes = True):

	#test if the path works for the tables
	if pathTable.endswith('/') == False:
		pathTable = pathTable+'/'	
	if os.path.isdir(pathTable) == False:
		raise ValueError('The path specified to save the tables does not exist. Please create it.')

	#test if the path works for the figures
	if pathFig.endswith('/') == False:
		pathFig = pathFig+'/'	
	if os.path.isdir(pathFig) == False:
		raise ValueError('The path specified to save the figures does not exist. Please create it.')

	QF = basictests(wav, flux, eflux, filters, wavToFit, UL, z, specOn = False)
	z = abs(z)

	# Test if there are data points
	if NoSiem == True:
		pass
	else:
		SiRange = [int(9.*(1.+z)), int(20.*(1.+z))]
		o = np.where((wav>SiRange[0]) & (wav<SiRange[1]))[0]
		if len(o) == 0.:
			NoSiem = True
			print('No silicate emission are fit due to the lack of data points around the silicate emission features.')
			pass

		o = np.where(wav < 70.)[0]
		if len(o) < 4:
			NoSiem = True
			print('No silicate emission are fit due to the lack of data points at shorter wavelengths.')
			pass

	# Upload the templates.
	path = os.path.dirname(iragnsep.__file__)
	templ = pd.read_csv(path+'/B18_full.csv')

	if redoFit == True:
		res_fit = runSEDphotFit(wav, flux, eflux,\
								z = z,\
								filters = filters, \
								wavToFit = wavToFit,\
								UL = UL, \
								Nmc = Nmc, pgrbar = pgrbar, \
								NoSiem = NoSiem, \
								Pdust = Pdust, PPAH = PPAH, PnormAGN = PnormAGN, PSiEm = PSiEm,\
								templ = templ)
	else:
		try:
			res_fit = pd.read_csv(pathTable+sourceName+'_fitRes_photo.csv')
		except:
			raise ValueError('Cannot find the table. Check the name or redo the fit.')

	# Add the params of the host and AGN to the table
	loglum_hostIR, eloglum_hostIR, \
	loglum_hostMIR, eloglum_hostMIR, \
	loglum_hostFIR, eloglum_hostFIR, \
	loglum_AGNIR, loglum_AGNMIR, loglum_AGNFIR, \
	AGNfrac_IR, AGNfrac_MIR, AGNfrac_FIR, SFR, eSFR, wSFR, ewSFR = get_prop(res_fit, templ = templ, z = z, specOn = False)

	try:
		res_fit['logLumIR_host'] = loglum_hostIR
		res_fit['elogLumIR_host'] = eloglum_hostIR
		res_fit['logLumMIR_host'] = loglum_hostMIR
		res_fit['elogLumMIR_host'] = eloglum_hostMIR
		res_fit['logLumFIR_host'] = loglum_hostFIR
		res_fit['elogLumFIR_host'] = eloglum_hostFIR
		res_fit['logLumIR_AGN'] = loglum_AGNIR
		res_fit['logLumMIR_AGN'] = loglum_AGNMIR
		res_fit['logLumFIR_AGN'] = loglum_AGNFIR
		res_fit['AGNfrac_IR'] = AGNfrac_IR
		res_fit['AGNfrac_MIR'] = AGNfrac_MIR
		res_fit['AGNfrac_FIR'] = AGNfrac_FIR
		res_fit['SFR'] = SFR
		res_fit['eSFR'] = eSFR
		res_fit['wSFR'] = wSFR
		res_fit['ewSFR'] = ewSFR
		# res_fit['QF'] = QF
	except:
		res_fit['logLumIR_host'] = pd.Series(loglum_hostIR, index=res_fit.index)
		res_fit['elogLumIR_host'] = pd.Series(eloglum_hostIR, index=res_fit.index)
		res_fit['logLumMIR_host'] = pd.Series(loglum_hostMIR, index=res_fit.index)
		res_fit['elogLumMIR_host'] = pd.Series(eloglum_hostMIR, index=res_fit.index)
		res_fit['logLumFIR_host'] = pd.Series(loglum_hostFIR, index=res_fit.index)
		res_fit['elogLumFIR_host'] = pd.Series(eloglum_hostFIR, index=res_fit.index)
		res_fit['logLumIR_AGN'] = pd.Series(loglum_AGNIR, index=res_fit.index)
		res_fit['logLumMIR_AGN'] = pd.Series(loglum_AGNMIR, index=res_fit.index)
		res_fit['logLumFIR_AGN'] = pd.Series(loglum_AGNFIR, index=res_fit.index)
		res_fit['AGNfrac_IR'] = pd.Series(AGNfrac_IR, index=res_fit.index)
		res_fit['AGNfrac_MIR'] = pd.Series(AGNfrac_MIR, index=res_fit.index)
		res_fit['AGNfrac_FIR'] = pd.Series(AGNfrac_FIR, index=res_fit.index)
		res_fit['SFR'] = pd.Series(SFR, index=res_fit.index)
		res_fit['eSFR'] = pd.Series(eSFR, index=res_fit.index)
		res_fit['wSFR'] = pd.Series(wSFR, index=res_fit.index)
		res_fit['ewSFR'] = pd.Series(ewSFR, index=res_fit.index)
		# res_fit['QF'] = pd.Series(QF, index=res_fit.index)


	if saveRes == True:
		order = ['tplName_gal', 'AGNon', 'tplName_AGN', 'logNormGal_dust', 'elogNormGal_dust', 'logNormGal_PAH','elogNormGal_PAH', 'logNormAGN', 'elogNormAGN',\
				 'logNormSiem', 'elogNormSiem', 'logLumIR_host', 'elogLumIR_host', 'logLumMIR_host', 'elogLumMIR_host', 'logLumFIR_host', \
				 'elogLumFIR_host', 'logLumIR_AGN', 'logLumMIR_AGN', 'logLumFIR_AGN', 'AGNfrac_IR', 'AGNfrac_MIR', 'AGNfrac_FIR', 'SFR','eSFR', \
				 'wSFR', 'ewSFR', 'logl', 'Aw', 'bestModelFlag']
		res_fit.to_csv(pathTable+sourceName+'_fitRes_photo.csv', index = False, columns = order)

	o = np.where(res_fit['bestModelFlag'] == 1)[0]
	res_fitBM = res_fit.iloc[o]

	print('#########################')
	print('# Generating the plots. #')
	print('#########################')
	# Plot all the fits
	plotFitPhoto(res_fit, [wav, flux, eflux], UL = UL, pathFig = pathFig, sourceName = sourceName, templ = templ, z = z, saveRes = saveRes)

	return res_fit, res_fitBM


