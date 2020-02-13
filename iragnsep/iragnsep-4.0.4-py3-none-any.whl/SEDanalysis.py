import numpy as np
import pandas as pd
import os
import emcee

from scipy.special import erf
from emcee import EnsembleSampler
from astropy import constants as const
from scipy import integrate, optimize, signal
from .func import *
from .classes import *
from scipy import special as sp
from numba import jit, njit

c = const.c.value

#########################################################
#														#
#		PHOTOMETRIC + SPEC VERSION OF THE FITTING		#
#														#
#########################################################

@njit()
def lnpostfn_spec_wAGN(theta, P, modelBG, modelSG, fluxFit, efluxFit, UL, wei, z, dlambda, wavFit):
	logl = 0

	# Normal prior on the norm of the dust
	logl += np.log(1./np.sqrt(2.*np.pi*P[0][1]**2.) * np.exp(-0.5*(theta[0])**2./P[0][1]**2.))

	if np.sum(modelSG) > 0.:
		# Add normal prior on the norm of the PAH
		logl += np.log(1./np.sqrt(2.*np.pi*P[1][1]**2.) * np.exp(-0.5*(theta[1])**2./P[1][1]**2.))
	else:
		theta[1] = -10.

	# Normal prior on the AGN power law
	logl += np.log(1./np.sqrt(2.*np.pi*P[2][1]**2.) * np.exp(-0.5*(theta[2])**2./P[2][1]**2.))

	# Flat prior on alpha1
	logl += np.log(1./np.sqrt(2.*np.pi*P[3][1]**2.) * np.exp(-0.5*(theta[3])**2./P[3][1]**2.))
	if (theta[3] < -2.) | (theta[3] > 2.) == True:
			return -np.inf

	# Flat prior on alpha2
	logl += np.log(1./np.sqrt(2.*np.pi*P[4][1]**2.) * np.exp(-0.5*(theta[4])**2./P[4][1]**2.))
	if (theta[4] < -2.) | (theta[4] > 2.) == True:
			return -np.inf

	# Normal prior on the position of the break
	logl += np.log(1./np.sqrt(2.*np.pi*P[5][1]**2.) * np.exp(-0.5*(theta[5])**2./P[5][1]**2.))
	if (theta[5] < -20.) | (theta[5] > 60.) == True:
			return -np.inf

	# Normal Prior on the normalisation of the Si emission at 11 microns
	logl += np.log(1./np.sqrt(2.*np.pi*P[6][1]**2.) * np.exp(-0.5*(theta[6])**2./P[6][1]**2.))

	# Normal Prior on the normalisation of the Si emission at 19 microns
	logl += np.log(1./np.sqrt(2.*np.pi*P[7][1]**2.) * np.exp(-0.5*(theta[7])**2./P[7][1]**2.))

	#model
	modelPL = 10**(theta[2] + P[2][0]) * AGNmodel_jit(wavFit, 15.*(1.+z), (theta[5]+P[5][0])*(1.+z), theta[3]+P[3][0], theta[4]+P[4][0], -3.5)
	modelSi11 = 10**(theta[6] + P[6][0]) * Gauss_jit(wavFit, np.log10(11.*(1.+z)), 0.05)
	modelSi19 = 10**(theta[7] + P[7][0]) * Gauss_jit(wavFit, np.log10(19.*(1.+z)), 0.1)

	# ymodel = modelPL + modelSi11 + modelSi19 + 10**(theta[0] + P[0][0]) * modelBG + 10**(theta[1] + P[1][0]) * modelSG
	ymodel = modelPL + modelSi11 + modelSi19 + 10**(theta[0] + P[0][0]) * modelBG + 10**(theta[1] + P[1][0]) * modelSG

	# UPPER LMITS
	o = np.where(UL == 1)[0]
	if len(o) > 0:
		x = (ymodel[o] - 3.*fluxFit[o])/np.sqrt(2.)/fluxFit[o]
		t_erf = 1./(1. + 0.5*np.abs(x))
		tau_erf = t_erf*np.exp(-x**2. - 1.26551223 + 1.00002368*t_erf + 0.37409196*t_erf**2. + 0.09678418*t_erf**3.\
									  - 0.18628806*t_erf**4., + 0.27886807*t_erf**5. - 1.13520398*t_erf**6. + 1.48851587*t_erf**7. \
									  - 0.82215223*t_erf**8. + 0.17087277*t_erf**9.)
		for i, xnden in np.ndenumerate(x):
			if xnden >= 0:
				erf_approx = 1. - tau_erf
				logl += np.sum(np.log(1. - (0.5 * (1. + erf_approx))))
			else:
				erf_approx = tau_erf - 1.
				logl += np.sum(np.log(1. - (0.5 * (1. + erf_approx))))

	o = np.where((dlambda > 5.) & (UL == 0))[0]
	logl += np.sum(np.log(1./np.sqrt(2.*np.pi)/efluxFit[o][1:]) - 0.5*(fluxFit[o][1:] - ymodel[o][1:])**2./efluxFit[o][1:]*2.)*wei[1]

	o = np.where((dlambda < 5.) & (UL == 0))[0]
	logl += np.sum(np.log(1./np.sqrt(2.*np.pi)/efluxFit[o]) - 0.5*(fluxFit[o] - ymodel[o])**2./efluxFit[o]**2.)*wei[0]

	if np.sum(modelSG) > 0.:
		logprob_model = np.log(1./np.sqrt(2.*np.pi)/0.1) - 0.5*(theta[1] + P[1][0] - (0.24 + 0.86 * (theta[0] + P[0][0])))**2./0.1**2.
		return logl + logprob_model
	else:
		return logl


@njit
def lnpostfn_spec_noAGN(theta, P, modelBG, modelSG, fluxFit, efluxFit, UL, wei, z, dlambda):
	logl = 0

	# Normal prior on the norm of the dust
	logl += np.log(1./np.sqrt(2.*np.pi*P[0][1]**2.) * np.exp(-0.5*(theta[0])**2./P[0][1]**2.))

	if np.sum(modelSG) > 0.:
		# Add normal prior on the norm of the PAH
		logl += np.log(1./np.sqrt(2.*np.pi*P[1][1]**2.) * np.exp(-0.5*(theta[1])**2./P[1][1]**2.))
	else:
		theta[1] = -10.

	ymodel = 10**(theta[0] + P[0][0]) * modelBG + 10**(theta[1] + P[1][0]) * modelSG
	
	# UPPER LMITS
	o = np.where(UL == 1)[0]
	if len(o) > 0:
		# x = (ymodel[o] - fluxFit[o])/np.sqrt(2.)/efluxFit[o]
		x = (ymodel[o] - 3.*fluxFit[o])/np.sqrt(2.)/fluxFit[o]
		t_erf = 1./(1. + 0.5*np.abs(x))
		tau_erf = t_erf*np.exp(-x**2. - 1.26551223 + 1.00002368*t_erf + 0.37409196*t_erf**2. + 0.09678418*t_erf**3.\
									  - 0.18628806*t_erf**4., + 0.27886807*t_erf**5. - 1.13520398*t_erf**6. + 1.48851587*t_erf**7. \
									  - 0.82215223*t_erf**8. + 0.17087277*t_erf**9.)
		for i, xnden in np.ndenumerate(x):
			if xnden >= 0:
				erf_approx = 1. - tau_erf
				logl += np.sum(np.log(1. - (0.5 * (1. + erf_approx))))
			else:
				erf_approx = tau_erf - 1.
				logl += np.sum(np.log(1. - (0.5 * (1. + erf_approx))))

	# Herschel loglikelihood aside from upper limits
	o = np.where((dlambda > 5.) & (UL == 0))[0]
	logl += np.sum(np.log(1./np.sqrt(2.*np.pi)/efluxFit[o][1:]) - 0.5*(fluxFit[o][1:] - ymodel[o][1:])**2./efluxFit[o][1:]*2.)*wei[1]

	o = np.where((dlambda < 5.) & (UL == 0))[0]
	logl += np.sum(np.log(1./np.sqrt(2.*np.pi)/efluxFit[o]) - 0.5*(fluxFit[o] - ymodel[o])**2./efluxFit[o]**2.)*wei[0]

	if np.sum(modelSG) > 0.:
		logprob_model = np.log(1./np.sqrt(2.*np.pi)/0.1) - 0.5*(theta[1] + P[1][0] - (0.24 + 0.86 * (theta[0] + P[0][0])))**2./0.1**2.
		return logl + logprob_model
	else:
		return logl

def runSEDspecFit(lambdaObs, fluxObs, efluxObs,\
				  z = 0.01,\
				  filters = ['PACS70', 'PACS100', 'PACS160', 'SPIRE250ps', 'SPIRE350ps', 'SPIRE500ps'], \
				  wavToFit = [70., 100., 160., 250., 350., 500.],\
			  	  UL = [0., 0., 0., 0., 0., 0.], \
				  IRSobsCorr = True,\
				  Nmc = 10000, pgrbar = 1, \
				  Pdust = [10, 1.], PPAH = [9., 1.], Ppl = [-1., 1.], Pbreak = [40.,3.], Pslope1 = [1., 0.1], Pslope2 = [1., 0.1], \
				  Plsg = [-1., 1.], Pllg = [-1., 1.],\
				  templ = ''):

	if len(templ) == 0:
		path = os.path.dirname(iragnsep.__file__)
		templ = pd.read_csv(path+'/B18_full.csv')

	# Extract the name of the templates
	keys = templ.keys().values
	nameTempl_gal = []
	nameTempl_PAH = []
	for key in keys:
		if str(key).startswith('gal'):
			if str(key).endswith('PAH') == False:
				nameTempl_gal.append(key)
			else:
				nameTempl_PAH.append(key)

	# Test that we have template for everything (if no galaxy then it crashes)
	if len(nameTempl_gal) == 0:
		raise ValueError('The galaxy template does not exist. The name of the column defining nuLnu for the galaxy template needs to start with "gal".')

	# define the wavelengths
	try:
		wavTempl = templ['lambda_mic']
	except:
		raise ValueError('Rename the wavelengths column of the template "lambda_mic".')

	# Throughout we assume the flux in Jansky and wavelength in micron
	dlambda = np.gradient(lambdaObs)
	IRSwav = np.concatenate([lambdaObs[dlambda<5.], [lambdaObs[dlambda>5.][0]]])
	IRSflux = np.concatenate([fluxObs[dlambda<5.], [fluxObs[dlambda>5.][0]]])
	eIRSflux = np.concatenate([efluxObs[dlambda<5.], [efluxObs[dlambda>5.][0]]])
	IRSwavRest = IRSwav/(1. + z)

	# We attempt to correct for obscuration if possible and if set by the User
	# for this we measure the tau9p7 (Sirocky2008 + Spoon2007 for the anchor wavelengths)
	if IRSobsCorr == True:
		try:
			IRSflux_corr, eIRSflux_corr, _tau9p7 = corrIRSobs(IRSwavRest, IRSflux, eIRSflux)
			_tau9p7 = round(_tau9p7,3)
		except:
			IRSflux_corr = IRSflux
			eIRSflux_corr = eIRSflux
			_tau9p7 = -99.
			print('*******************')
			print('It has failed to correct the IRS spectrum for obscuration. The most likely explanation is redshift since it needs the restframe anchor ' + \
				   'wavelengths to measure the strength of the silicate absorption. The fit is continued without correcting for obscuration.')
			print('*******************')
			pass
	else:
		IRSflux_corr = IRSflux
		eIRSflux_corr = eIRSflux
		_tau9p7 = -99.

	# Put all together for the fit
	wavFit = np.concatenate([IRSwav, lambdaObs[dlambda>5.][1::]])
	fluxFit = np.concatenate([IRSflux_corr, fluxObs[dlambda>5.][1::]])
	efluxFit = np.concatenate([eIRSflux_corr, efluxObs[dlambda>5.][1::]])

	#Derive the weights that should be allocated to the IRS spectrum
	Npoints = float(len(fluxFit))
	Herwei = 1./((Npoints-len(IRSwav))/Npoints)
	IRSwei = 1./((len(IRSwav))/Npoints)

	Npoints_IRS_wei = round(Herwei * IRSwei / (Npoints-len(IRSwav))*2.)
	wavFit_IRS_wei = 10**(np.linspace(np.log10(min(IRSwav)), np.log10(max(IRSwav)), num = Npoints_IRS_wei))
	fluxFit_IRS_wei = np.interp(wavFit_IRS_wei, IRSwav, IRSflux_corr)
	efluxFit_IRS_wei = np.interp(wavFit_IRS_wei, IRSwav, eIRSflux_corr)

	wavFit_wei = np.concatenate([wavFit_IRS_wei, lambdaObs[dlambda>5.][1::]])
	fluxFit_wei = np.concatenate([fluxFit_IRS_wei, fluxObs[dlambda>5.][1::]])
	efluxFit_wei = np.concatenate([efluxFit_IRS_wei, efluxObs[dlambda>5.][1::]])

	# Prepare a vector for the Upper Lmits
	ULIRS = np.zeros(len(wavFit_IRS_wei))
	ULall = np.concatenate([ULIRS, UL])

	dlambda = np.gradient(wavFit_wei)

	# Define the free parameters
	lsg_perTempl = []
	elsg_perTempl = []
	llg_perTempl = []
	ellg_perTempl = []
	lnAGN_perTempl = []
	elnAGN_perTempl = []
	coff_perTempl = []
	ecoff_perTempl = []
	alpha1_perTempl = []
	ealpha1_perTempl = []
	alpha2_perTempl = []
	ealpha2_perTempl = []
	
	lnDust_perTempl = []
	elnDust_perTempl = []
	lnPAH_perTempl = []
	elnPAH_perTempl = []
	
	logl_perTempl = []
	tplName_perTempl = []
	tau9p7_save = []
	AGNon = []
	nParms = []

	# We loop over the templates
	for name_i in nameTempl_gal:
		assert isinstance(name_i, str), "The list nameTempl requests strings as it corresponds to the names" + \
										" given to the various templates of galaxies to use for the fit."

		if pgrbar == 1:
			print("****************************************")
			print("  Fit of "+name_i+" as galaxy template  ")
			print("****************************************")

		# We prepare the templates by matching the IRS wavelengths
		# and the broad band fluxes now that we know the redshift.

		# Because the B18 contains Big Grains and PAHs, even if it's a single template
		# we put it in the big grains and test later to shut the PAH component
		nuLnuBGTempl = templ[name_i].values

		# Herschel Fluxes
		SEDgen = modelToSED(wavTempl, nuLnuBGTempl, z)
		fluxHerschel = []
		for filt in filters:
		 	fluxHerschel.append(getattr(SEDgen, filt)())

		# IRS fluxes
		Fnu = nuLnuToFnu(wavTempl, nuLnuBGTempl, z)
		IRSmodelFlux = np.interp(wavFit_IRS_wei/(1.+z), wavTempl, Fnu)

		modelBG = np.concatenate([IRSmodelFlux, fluxHerschel])

		if name_i.endswith('dust') == False:
			modelSG = np.zeros(len(modelBG))
		else:
			nuLnuSGTempl = templ[nameTempl_PAH[0]].values

			# Herschel flux
			SEDgen = modelToSED(wavTempl, nuLnuSGTempl, z)
			fluxHerschel = []
			for filt in filters:
				fluxHerschel.append(getattr(SEDgen, filt)())

			#IRS spec
			Fnu = nuLnuToFnu(wavTempl, nuLnuSGTempl, z)
			IRSmodelFlux = np.interp(wavFit_IRS_wei/(1.+z), wavTempl, Fnu)
		
			modelSG = np.concatenate([IRSmodelFlux, fluxHerschel])
		
		# FIT WITHOUT THE AGN
		ndim = 2
		nwalkers = int(2. * ndim)

		parms = np.zeros(shape=(nwalkers, ndim))
		parms[:,0] = np.random.normal(0., Pdust[1], size=nwalkers) # norm Dust
		parms[:,1] = np.random.normal(0., PPAH[1], size=nwalkers) # norm PAH

		sampler = EnsembleSampler(nwalkers, ndim, lnpostfn_spec_noAGN, args = (np.array([Pdust, PPAH]), modelBG, modelSG, fluxFit_wei, efluxFit_wei, \
								  ULall, np.array([IRSwei, Herwei]), z, dlambda))
		sampler.run_mcmc(parms, Nmc, progress=bool(pgrbar))

		# Build the flat chain
		NburnIn = int(0.2 * Nmc)
		chain = sampler.get_chain(discard=NburnIn, thin=10, flat=True)

		lnDust_perTempl.append(round(np.median(chain[:,0]),3))
		elnDust_perTempl.append(round(np.std(chain[:,0]),3))

		if np.sum(modelSG) > 0.:
			lnPAH_perTempl.append(round(np.median(chain[:,1]),3))
			elnPAH_perTempl.append(round(np.std(chain[:,1]),3))
		else:
			lnPAH_perTempl.append(-20.)
			elnPAH_perTempl.append(0.0)

		logl_perTempl.append(round(lnpostfn_spec_noAGN(np.array([lnDust_perTempl[-1], lnPAH_perTempl[-1]]), np.array([Pdust, PPAH]), modelBG, modelSG, \
								   fluxFit_wei, efluxFit_wei, ULall, np.array([IRSwei, Herwei]), z, dlambda),3))

		lnAGN_perTempl.append(-99.)
		elnAGN_perTempl.append(-99.)

		alpha1_perTempl.append(-99.)
		ealpha1_perTempl.append(-99.)

		alpha2_perTempl.append(-99.)
		ealpha2_perTempl.append(-99.)

		coff_perTempl.append(-99.)
		ecoff_perTempl.append(-99.)

		lsg_perTempl.append(-99.)
		elsg_perTempl.append(-99.)

		llg_perTempl.append(-99.)
		ellg_perTempl.append(-99.)

		AGNon.append(0.)
		if np.sum(modelSG) > 0.:
			nParms.append(ndim)
		else:
			nParms.append(ndim-1)
		tplName_perTempl.append(name_i)

		tau9p7_save.append(_tau9p7)


		# INCLUDING THE AGN
		# MCMC fit
		ndim = 8
		nwalkers = int(2. * ndim)

		parms = np.zeros(shape=(nwalkers, ndim))

		parms = np.zeros(shape=(nwalkers, ndim))
		parms[:,0] = np.random.normal(0., Pdust[1], size=nwalkers) # norm Dust
		parms[:,1] = np.random.normal(0., PPAH[1], size=nwalkers) # norm PAH
		parms[:,2] = np.random.normal(0., Ppl[1], size=nwalkers) # norm PL AGN
		# parms[:,3] = np.random.normal(0., Pslope1[1]/10000., size=nwalkers) # norm PL AGN
		parms[:,3] = np.random.uniform(low = -1., high = 1., size=nwalkers) # alpha1
		# parms[:,4] = np.random.normal(0., Pslope2[1]/10000., size=nwalkers) # norm PL AGN
		parms[:,4] = np.random.uniform(low = -1., high = 1., size=nwalkers) # alpha2
		# parms[:,5] = np.random.normal(0., Pbreak[1], size=nwalkers) # Break
		parms[:,5] = np.random.uniform(low = -10., high = 10., size=nwalkers) # Break
		parms[:,6] = np.random.normal(0., Plsg[1], size=nwalkers) # 10micron
		parms[:,7] = np.random.normal(0., Pllg[1], size=nwalkers) # 18micron

		sampler = EnsembleSampler(nwalkers, ndim, lnpostfn_spec_wAGN, args = (np.array([Pdust, PPAH, Ppl, Pslope1, Pslope2, Pbreak, Plsg, Pllg]), \
								  modelBG, modelSG, fluxFit_wei, efluxFit_wei, ULall, np.array([IRSwei, Herwei]), z, dlambda, wavFit_wei))
		sampler.run_mcmc(parms, Nmc, progress=bool(pgrbar))

		# Build the flat chain
		chain = sampler.get_chain(discard=NburnIn, thin=10, flat=True)

		# Save the results
		lnDust_perTempl.append(round(np.median(chain[:,0]),3))
		elnDust_perTempl.append(round(np.std(chain[:,0]),3))

		if np.sum(modelSG) > 0.:
			lnPAH_perTempl.append(round(np.median(chain[:,1]),3))
			elnPAH_perTempl.append(round(np.std(chain[:,1]),3))
		else:
			lnPAH_perTempl.append(-20.)
			elnPAH_perTempl.append(0.0)

		lnAGN_perTempl.append(round(np.median(chain[:,2]),3))
		elnAGN_perTempl.append(round(np.std(chain[:,2]),3))

		alpha1_perTempl.append(round(np.median(chain[:,3]),3))
		ealpha1_perTempl.append(round(np.std(chain[:,3]),3))

		alpha2_perTempl.append(round(np.median(chain[:,4]),3))
		ealpha2_perTempl.append(round(np.std(chain[:,4]),3))

		coff_perTempl.append(round(np.median(chain[:,5]),3))
		ecoff_perTempl.append(round(np.std(chain[:,5]),3))

		lsg_perTempl.append(round(np.median(chain[:,6]),3))
		elsg_perTempl.append(round(np.std(chain[:,6]),3))

		llg_perTempl.append(round(np.median(chain[:,7]),3))
		ellg_perTempl.append(round(np.std(chain[:,7]),3))

		theta = np.array([lnDust_perTempl[-1], lnPAH_perTempl[-1], lnAGN_perTempl[-1], alpha1_perTempl[-1], \
				 		  alpha2_perTempl[-1], coff_perTempl[-1], lsg_perTempl[-1], llg_perTempl[-1]])
		logl_perTempl.append(round(lnpostfn_spec_wAGN(theta, np.array([Pdust, PPAH, Ppl, Pslope1, Pslope2, Pbreak, Plsg, Pllg]), modelBG, modelSG, fluxFit_wei, efluxFit_wei, ULall, np.array([IRSwei, Herwei]), z, dlambda, wavFit_wei),3))

		AGNon.append(1.)
		tau9p7_save.append(round(_tau9p7,3))

		tplName_perTempl.append(name_i)
		if np.sum(modelSG) > 0.:
			nParms.append(ndim)
		else:
			nParms.append(ndim-1)

	# Find the best model and the Akaike weight
	bestModelInd, Awi = exctractBestModel(logl_perTempl, nParms, len(wavFit_wei), corrected = False)
	bestModelFlag = np.zeros(len(AGNon))
	bestModelFlag[bestModelInd] = 1


	# Save the results in a table
	resDict = {'logNormGal_dust': np.array(lnDust_perTempl) + Pdust[0], 'elogNormGal_dust': np.array(elnDust_perTempl), \
			   'logNormGal_PAH': np.array(lnPAH_perTempl) + PPAH[0], 'elogNormGal_PAH': np.array(elnPAH_perTempl), \
			   'logNormAGN_PL': np.array(lnAGN_perTempl) + Ppl[0], 'elogNormAGN_PL': np.array(elnAGN_perTempl), \
			   'lBreak_PL': np.array(coff_perTempl) + Pbreak[0], 'elBreak_PL': np.array(ecoff_perTempl), \
			   'alpha1_PL': np.array(alpha1_perTempl) + Pslope1[0], 'ealpha1_PL': np.array(ealpha1_perTempl), \
			   'alpha2_PL': np.array(alpha2_perTempl) + Pslope2[0], 'ealpha2_PL': np.array(ealpha2_perTempl), \
			   'logNorm_Si11': np.array(lsg_perTempl) + Plsg[0], 'elogNorm_Si11': np.array(elsg_perTempl), \
			   'logNorm_Si19': np.array(llg_perTempl) + Pllg[0], 'elogNorm_Si19': np.array(ellg_perTempl), \
			   'logl': logl_perTempl, 'AGNon': AGNon, 'tplName': tplName_perTempl,\
			   'bestModelFlag': bestModelFlag, 'Aw': Awi, 'tau9p7': tau9p7_save}

	dfRes = pd.DataFrame(resDict)

	return dfRes


#################################################
#												#
#		PHOTOMETRIC VERSION OF THE FITTING		#
#												#
#################################################
@njit
def lnpostfn_photo_noAGN(theta, P, modelBG, modelSG, UL, fluxFit, efluxFit, wei):
	logl = 0

	# Normal prior on the norm of the dust
	logl += np.log(1./np.sqrt(2.*np.pi*P[0][1]**2.) * np.exp(-0.5*(theta[0])**2./P[0][1]**2.))

	if np.sum(modelSG) > 0.:
		# Add normal prior on the norm of the PAH
		logl += np.log(1./np.sqrt(2.*np.pi*P[1][1]**2.) * np.exp(-0.5*(theta[1])**2./P[1][1]**2.))
	else:
		theta[1] = -10.

	ymodel = 10**(theta[0] + P[0][0]) * modelBG + 10**(theta[1] + P[1][0]) * modelSG
	
	# UPPER LMITS
	o = np.where(UL == 1)[0]
	if len(o) > 0:
		# x = (ymodel[o] - fluxFit[o])/np.sqrt(2.)/efluxFit[o]
		x = (ymodel[o] - 3.*fluxFit[o])/np.sqrt(2.)/fluxFit[o]
		t_erf = 1./(1. + 0.5*np.abs(x))
		tau_erf = t_erf*np.exp(-x**2. - 1.26551223 + 1.00002368*t_erf + 0.37409196*t_erf**2. + 0.09678418*t_erf**3.\
									  - 0.18628806*t_erf**4., + 0.27886807*t_erf**5. - 1.13520398*t_erf**6. + 1.48851587*t_erf**7. \
									  - 0.82215223*t_erf**8. + 0.17087277*t_erf**9.)
		for i, xnden in np.ndenumerate(x):
			if xnden >= 0:
				erf_approx = 1. - tau_erf
				logl += np.sum(np.log(1. - (0.5 * (1. + erf_approx))))
			else:
				erf_approx = tau_erf - 1.
				logl += np.sum(np.log(1. - (0.5 * (1. + erf_approx))))

	# DETECTED VALUES
	o = np.where(UL == 0)[0]
	logl += np.sum((np.log(1./np.sqrt(2.*np.pi)/efluxFit[o]) - 0.5*(fluxFit[o] - ymodel[o])**2./efluxFit[o]**2.)*wei[o])

	if np.sum(modelSG) > 0.:
		logprob_model = np.log(1./np.sqrt(2.*np.pi)/0.1) - 0.5*(theta[1] + P[1][0] - (0.24 + 0.86 * (theta[0] + P[0][0])))**2./0.1**2.
		return logl + logprob_model
	else:
		return logl

@njit
def lnpostfn_photo_wAGN(theta, P, modelBG, modelSG, modelAGN, modelSi, UL, fluxFit, efluxFit, wei):
	logl = 0

	# Normal prior on the norm of the dust
	logl += np.log(1./np.sqrt(2.*np.pi*P[0][1]**2.) * np.exp(-0.5*(theta[0])**2./P[0][1]**2.))
	
	# Add normal prior on the norm of the PAH
	if np.sum(modelSG) > 0.:
		logl += np.log(1./np.sqrt(2.*np.pi*P[1][1]**2.) * np.exp(-0.5*(theta[1])**2./P[1][1]**2.))
	else:
		theta[1] = -10.

	# Add normal prior on the norm of the AGN continuum
	logl += np.log(1./np.sqrt(2.*np.pi*P[2][1]**2.) * np.exp(-0.5*(theta[2])**2./P[2][1]**2.))

	# Add normal prior on the norm of the Si emission
	if np.sum(modelSi) > 0.:
		logl += np.log(1./np.sqrt(2.*np.pi*P[3][1]**2.) * np.exp(-0.5*(theta[3])**2./P[3][1]**2.))
	else:
		theta[3] = -10.

	ymodel = 10**(theta[0] + P[0][0]) * modelBG + 10**(theta[1] + P[1][0]) * modelSG + 10**(theta[2] + P[2][0]) * modelAGN + 10**(theta[3] + P[3][0]) * modelSi

	# UPPER LMITS
	o = np.where(UL == 1)[0]
	if len(o) > 0:
		x = (ymodel[o] - 3.*fluxFit[o])/np.sqrt(2.)/fluxFit[o]
		t_erf = 1./(1. + 0.5*np.abs(x))
		tau_erf = t_erf*np.exp(-x**2. - 1.26551223 + 1.00002368*t_erf + 0.37409196*t_erf**2. + 0.09678418*t_erf**3.\
									  - 0.18628806*t_erf**4., + 0.27886807*t_erf**5. - 1.13520398*t_erf**6. + 1.48851587*t_erf**7. \
									  - 0.82215223*t_erf**8. + 0.17087277*t_erf**9.)
		for i, xnden in np.ndenumerate(x):
			if xnden >= 0:
				erf_approx = 1. - tau_erf
				logl += np.sum(np.log(1. - (0.5 * (1. + erf_approx))))
			else:
				erf_approx = tau_erf - 1.
				logl += np.sum(np.log(1. - (0.5 * (1. + erf_approx))))

	# DETECTED VALUES
	o = np.where(UL == 0)[0]
	logl += np.sum((np.log(1./np.sqrt(2.*np.pi)/efluxFit[o]) - 0.5*(fluxFit[o] - ymodel[o])**2./efluxFit[o]**2.)*wei[o])

	if np.sum(modelSG) > 0.:
		logprob_model = np.log(1./np.sqrt(2.*np.pi)/0.1) - 0.5*(theta[1] + P[1][0] - (0.24 + 0.86 * (theta[0] + P[0][0])))**2./0.1**2.
		return logl + logprob_model
	else:
		return logl

def runSEDphotFit(lambdaObs, fluxObs, efluxObs, \
				  z = 0.01, \
				  filters = ['MIPS24', 'PACS70', 'PACS100', 'PACS160', 'SPIRE250', 'SPIRE350', 'SPIRE500'], \
				  wavToFit = [24., 70., 100., 160., 250., 350., 500.], \
				  UL = [0., 0., 0., 0., 0., 0., 0.], \
				  Nmc = 10000, pgrbar = 1, \
				  NoSiem = False, \
				  Pdust = [10., 1.], PPAH = [9., 1.], PnormAGN = [10., 1.], PSiEm = [10., 1.], \
				  templ = ''):

	if len(templ) == 0:
		path = os.path.dirname(iragnsep.__file__)
		templ = pd.read_csv(path+'/B18_full.csv')

	# Extract the name of the templates
	keys = templ.keys().values
	nameTempl_gal = []
	nameTempl_PAH = []
	nameTempl_AGN = []
	nameTempl_Siem = []
	for key in keys:
		if str(key).startswith('gal'):
			if str(key).endswith('PAH') == False:
				nameTempl_gal.append(key)
			else:
				nameTempl_PAH.append(key)
		if str(key).startswith('AGN'):
			if str(key).endswith('Siem'):
				nameTempl_Siem.append(key)
			else:
				nameTempl_AGN.append(key)

	# Test that we have template for everything (if no galaxy then it crashes)
	if len(nameTempl_gal) == 0:
		raise ValueError('The galaxy template does not exist. The name of the column defining nuLnu for the galaxy template needs to start with "gal".')

	# define the wavelengths
	try:
		wavTempl = templ['lambda_mic']
	except:
		raise ValueError('Rename the wavelengths column of the template "lambda_mic".')

	# wavelength for the templates
	try:
		wavTempl = templ.lambda_mic.values
	except:
		raise Exception('Rename the wavelength column in the template file to "lambda_mic".')

	# Define the free parameters
	lnAGN_perTempl = []
	elnAGN_perTempl= []

	lnSi_perTempl = []
	elnSi_perTempl = []

	lnDust_perTempl = []
	elnDust_perTempl = []

	lnPAH_perTempl = []
	elnPAH_perTempl = []

	logl_perTempl = []
	tplNameGal_perTempl = []
	tplNameAGN_perTempl = []
	AGNon = []
	nParms = []

	#Derive the weights that should be allocated to the IRS spectrum
	totUnc = np.sum(efluxObs)
	wei = efluxObs/totUnc

	# We loop over the templates
	for name_i in nameTempl_gal:
		assert isinstance(name_i, str), "The list nameTempl requests strings as it corresponds to the names" + \
										" given to the various templates of galaxies to use for the fit."

		if pgrbar == 1:
			print("****************************************")
			print("  Fit of "+name_i+" as galaxy template  ")
			print("****************************************")

		# Because the B18 contains Big Grains and Small grains, even if it's a single template
		# we put it in the BG grains and test later to shut the small grain component
		
		nuLnuBGTempl = templ[name_i].values
		# Convert to photometric flux
		SEDgen = modelToSED(wavTempl, nuLnuBGTempl, z)
		modelBG = []
		for filt in filters:
			modelBG.append(getattr(SEDgen, filt)())

		modelBG = np.array(modelBG)

		if name_i.endswith('dust') == False:
			modelSG = modelBG * 0.
			emodelSG = modelBG * 0.
		else:
			nuLnuSGTempl = templ['gal_PAH'].values
			SEDgen = modelToSED(wavTempl, nuLnuSGTempl, z)
			modelSG = []
			for filt in filters:
				modelSG.append(getattr(SEDgen, filt)())

			modelSG = np.array(modelSG)

		# FIT WITHOUT THE AGN
		ndim = 2
		nwalkers = int(2. * ndim)

		parms = np.zeros(shape=(nwalkers, ndim))
		parms[:,0] = np.random.normal(0., Pdust[1], size=nwalkers) # norm Dust
		parms[:,1] = np.random.normal(0., PPAH[1], size=nwalkers) # norm PAH

		sampler = EnsembleSampler(nwalkers, ndim, lnpostfn_photo_noAGN, args = (np.array([Pdust, PPAH]), modelBG, modelSG, UL, fluxObs, efluxObs, wei))
		sampler.run_mcmc(parms, Nmc, progress=bool(pgrbar))

		# Build the flat chain
		NburnIn = int(0.2 * Nmc)
		chain = sampler.get_chain(discard=NburnIn, thin=10, flat=True)

		lnDust_perTempl.append(round(np.median(chain[:,0]),3))
		elnDust_perTempl.append(round(np.std(chain[:,0]),3))

		if np.sum(modelSG) > 0.:
			lnPAH_perTempl.append(round(np.median(chain[:,1]),3))
			elnPAH_perTempl.append(round(np.std(chain[:,1]),3))
		else:
			lnPAH_perTempl.append(-20.)
			elnPAH_perTempl.append(0.0)

		logl_perTempl.append(round(lnpostfn_photo_noAGN(np.array([lnDust_perTempl[-1], lnPAH_perTempl[-1]]), np.array([Pdust, PPAH]), \
								   modelBG, modelSG, UL, fluxObs, efluxObs, wei),3))
		
		lnSi_perTempl.append(-99.)
		elnSi_perTempl.append(-99.)

		lnAGN_perTempl.append(-99.)
		elnAGN_perTempl.append(-99.)

		AGNon.append(0.)
		if np.sum(modelSG) > 0.:
			nParms.append(ndim)
		else:
			nParms.append(ndim-1)
		tplNameGal_perTempl.append(name_i)
		tplNameAGN_perTempl.append(str('N/A'))


		# INCLUDE THE AGN
		for AGN_i in nameTempl_AGN:

			nuLnu_AGN = templ[AGN_i].values
			SEDgen = modelToSED(wavTempl, nuLnu_AGN, z)
			modelAGN = []
			for filt in filters:
				modelAGN.append(getattr(SEDgen, filt)())

			modelAGN = np.array(modelAGN)

			modelSiem = []
			if NoSiem == False:
				nuLnu_Siem = templ[nameTempl_Siem].values.flatten()
				SEDgen = modelToSED(wavTempl, nuLnu_Siem, z)
				for filt in filters:
					modelSiem.append(getattr(SEDgen, filt)())

				modelSiem = np.array(modelSiem)
			else:
				modelSiem = modelAGN * 0.

			ndim = 4
			nwalkers = int(2. * ndim)

			parms = np.zeros(shape=(nwalkers, ndim))
			parms[:,0] = np.random.normal(0., Pdust[1], size=nwalkers) # norm Dust
			parms[:,1] = np.random.normal(0., PPAH[1], size=nwalkers) # norm PAH
			parms[:,2] = np.random.normal(0., PnormAGN[1], size=nwalkers) # NormAGN
			parms[:,3] = np.random.normal(0., PSiEm[1], size=nwalkers) # NormSi

			sampler = EnsembleSampler(nwalkers, ndim, lnpostfn_photo_wAGN, args = (np.array([Pdust, PPAH, PnormAGN, PSiEm]), \
									  modelBG, modelSG, modelAGN, modelSiem, UL, fluxObs, efluxObs, wei))
			sampler.run_mcmc(parms, Nmc, progress=bool(pgrbar))

			# Build the flat chain
			chain = sampler.get_chain(discard=NburnIn, thin=10, flat=True)

			lnDust_perTempl.append(round(np.median(chain[:,0]),3))
			elnDust_perTempl.append(round(np.std(chain[:,0]),3))

			if np.sum(modelSG) > 0.:
				lnPAH_perTempl.append(round(np.median(chain[:,1]),3))
				elnPAH_perTempl.append(round(np.std(chain[:,1]),3))
			else:
				lnPAH_perTempl.append(-20.)
				elnPAH_perTempl.append(0.0)

			lnAGN_perTempl.append(round(np.median(chain[:,2]),3))
			elnAGN_perTempl.append(round(np.std(chain[:,2]),3))

			if NoSiem == True:
				lnSi_perTempl.append(-20.)
				elnSi_perTempl.append(0.0)
			else:
				lnSi_perTempl.append(round(np.median(chain[:,3]),3))
				elnSi_perTempl.append(round(np.std(chain[:,3]),3))

			AGNon.append(1.)
			if len(modelSG) > 0.:
				nParms.append(ndim)
			else:
				nParms.append(ndim-1)
			tplNameGal_perTempl.append(name_i)
			tplNameAGN_perTempl.append(AGN_i)

			logl_perTempl.append(round(lnpostfn_photo_wAGN(np.array([lnDust_perTempl[-1], lnPAH_perTempl[-1], lnAGN_perTempl[-1], \
									   lnSi_perTempl[-1]]), np.array([Pdust, PPAH, PnormAGN, PSiEm]), modelBG, modelSG, modelAGN, \
									   modelSiem, UL, fluxObs, efluxObs, wei),3))

	# Find the best model and the Akaike weight
	bestModelInd, Awi = exctractBestModel(logl_perTempl, nParms, len(lambdaObs), corrected = True)
	bestModelFlag = np.zeros(len(AGNon))
	bestModelFlag[bestModelInd] = 1

	# Save the results in a table
	resDict = {'logNormGal_dust': np.array(lnDust_perTempl) + Pdust[0], 'elogNormGal_dust': np.array(elnDust_perTempl), \
			   'logNormGal_PAH': np.array(lnPAH_perTempl) + PPAH[0], 'elogNormGal_PAH': np.array(elnPAH_perTempl), \
			   'logNormAGN': np.array(lnAGN_perTempl) + PnormAGN[0], 'elogNormAGN': np.array(elnAGN_perTempl), \
			   'logNormSiem': np.array(lnSi_perTempl) + PSiEm[0], 'elogNormSiem': np.array(elnSi_perTempl), \
			   'logl': logl_perTempl, 'AGNon': AGNon, 'tplName_gal': tplNameGal_perTempl, 'tplName_AGN': tplNameAGN_perTempl,\
			   'bestModelFlag': bestModelFlag, 'Aw': Awi}

	dfRes = pd.DataFrame(resDict)

	return dfRes