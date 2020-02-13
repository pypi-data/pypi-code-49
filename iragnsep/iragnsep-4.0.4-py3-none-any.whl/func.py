import numpy as np
import matplotlib.pyplot  as plt
import os
import iragnsep
import glob

from astropy.cosmology import WMAP9 as cosmo
from astropy import units as u
from astropy import constants as const
from astropy.modeling import models
from scipy import integrate
from scipy.interpolate import UnivariateSpline
from scipy.constants import h,k,c
from numba import jit, njit

c = const.c.value
Lsun = const.L_sun.value

def get_prop(df, templ = '', z = 0.01, specOn = True):

	if len(templ) == 0:
		path = os.path.dirname(iragnsep.__file__)
		templ = pd.read_csv(path+'/B18_full.csv')

	# Extract the name of the templates
	keys = templ.keys().values
	nameTempl_gal = []
	nameTempl_AGN = []
	nameTempl_PAH = []
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
	if len(nameTempl_AGN) == 0:
		print('Warning: The template for AGN is empty. The name of the column defining nuLnu for the AGN templates needs to start with "AGN".')

	# define the wavelengths
	try:
		wavTempl = templ['lambda_mic'].values
	except:
		raise ValueError('Rename the wavelengths column of the template "lambda_mic".')

	nu = c/wavTempl/1e-6 #Hz
	o_IR = np.where((nu > c/1000./1e-6) & (nu < c/8./1e-6))[0][::-1]
	o_MIR = np.where((nu > c/35./1e-6) & (nu < c/5./1e-6))[0][::-1]
	o_FIR = np.where((nu > c/1000./1e-6) & (nu < c/40./1e-6))[0][::-1]
	dMpc = cosmo.luminosity_distance(z).value
	dmeter = dMpc*u.Mpc.to(u.m)
	d2z = dmeter**2./(1.+z) # K correction=>https://ned.ipac.caltech.edu/level5/Sept02/Hogg/Hogg2.html
	JyToLsun = 1e-26 * 4. * np.pi * d2z/Lsun

	loglum_hostIR = []
	eloglum_hostIR = []
	loglum_hostMIR = []
	eloglum_hostMIR = []
	loglum_hostFIR = []
	eloglum_hostFIR = []
	loglum_AGNIR = []
	loglum_AGNMIR = []
	loglum_AGNFIR = []

	if specOn == True:

		for i in range(0, len(df)):

			obj = df.iloc[i]

			#host IR luminosity
			normDust = 10**obj['logNormGal_dust']
			enormDust = obj['elogNormGal_dust'] * np.log(10)
			nuLnuDust = normDust * templ[obj['tplName']].values
			enuLnuDust = enormDust * nuLnuDust

			normPAH = 10**obj['logNormGal_PAH']
			enormPAH = obj['elogNormGal_PAH'] * np.log(10)
			nuLnuPAH = normPAH * templ['gal_PAH'].values
			enuLnuPAH = enormPAH * nuLnuPAH

			nuLnuGal = nuLnuDust + nuLnuPAH
			enuLnuGal = np.sqrt(enuLnuDust ** 2. + enuLnuPAH ** 2.)
			LnuGal = nuLnuGal/nu
			eLnuGal = enuLnuGal/nu

			loglum_hostIR.append(round(np.log10(np.trapz(LnuGal[o_IR], nu[o_IR], dx = np.gradient(nu[o_IR]))),3)) #Lsun
			elum_hostIR_i = 0
			for nu_i, nu_j, nu_k, eLnuGal_j, eLnuGal_k in zip(nu[o_IR[1:-2]], nu[o_IR[2:-1]], nu[o_IR[3:]], eLnuGal[o_IR[2:-1]], eLnuGal[o_IR[3:]]):
				elum_hostIR_i += 1./4. * (nu_j - nu_i)**2. * eLnuGal_j ** 2. + 1./4. * (nu_k - nu_j)**2. * eLnuGal_k ** 2.
			elum_hostIR = np.sqrt(elum_hostIR_i)
			eloglum_hostIR.append(round(0.434 * elum_hostIR/10**np.array(loglum_hostIR[-1]),3))
			
			loglum_hostMIR.append(round(np.log10(np.trapz(LnuGal[o_MIR], nu[o_MIR], dx = np.gradient(nu[o_MIR]))),3)) #Lsun
			elum_hostMIR_i = 0
			for nu_i, nu_j, nu_k, eLnuGal_j, eLnuGal_k in zip(nu[o_MIR[1:-2]], nu[o_MIR[2:-1]], nu[o_MIR[3:]], eLnuGal[o_MIR[2:-1]], eLnuGal[o_MIR[3:]]):
				elum_hostMIR_i += 1./4. * (nu_j - nu_i)**2. * eLnuGal_j ** 2. + 1./4. * (nu_k - nu_j)**2. * eLnuGal_k ** 2.
			elum_hostMIR = np.sqrt(elum_hostMIR_i)
			eloglum_hostMIR.append(round(0.434 * elum_hostMIR/10**np.array(loglum_hostMIR[-1]),3))
			
			loglum_hostFIR.append(round(np.log10(np.trapz(LnuGal[o_FIR], nu[o_FIR], dx = np.gradient(nu[o_FIR]))),3)) #Lsun
			elum_hostFIR_i = 0
			for nu_i, nu_j, nu_k, eLnuGal_j, eLnuGal_k in zip(nu[o_FIR[1:-2]], nu[o_FIR[2:-1]], nu[o_FIR[3:]], eLnuGal[o_FIR[2:-1]], eLnuGal[o_FIR[3:]]):
				elum_hostFIR_i += 1./4. * (nu_j - nu_i)**2. * eLnuGal_j ** 2. + 1./4. * (nu_k - nu_j)**2. * eLnuGal_k ** 2.
			elum_hostFIR = np.sqrt(elum_hostFIR_i)
			eloglum_hostFIR.append(round(0.434 * elum_hostFIR/10**np.array(loglum_hostFIR[-1]),3))
			
			if obj['AGNon'] == 1:
				modelAGN1 = 10**obj['logNorm_Si11'] * Gauss(wavTempl*(1.+z), np.log10(11.*(1.+z)), 0.05)
				modelAGN2 = 10**obj['logNorm_Si19'] * Gauss(wavTempl*(1.+z), np.log10(19.*(1.+z)), 0.1)
				modelAGN3 = 10**obj['logNormAGN_PL'] * AGNmodel(wavTempl*(1.+z), 15.*(1.+z), obj['lBreak_PL']*(1.+z), obj['alpha1_PL'], obj['alpha2_PL'], -3.5)

				LnuAGN = (modelAGN1 + modelAGN2 + modelAGN3) * JyToLsun
				
				loglum_AGNIR.append(round(np.log10(np.trapz(LnuAGN[o_IR], nu[o_IR], dx = np.gradient(nu[o_IR]))),3)) #Lsun
				loglum_AGNMIR.append(round(np.log10(np.trapz(LnuAGN[o_MIR], nu[o_MIR], dx = np.gradient(nu[o_MIR]))),3)) #Lsun
				loglum_AGNFIR.append(round(np.log10(np.trapz(LnuAGN[o_FIR], nu[o_FIR], dx = np.gradient(nu[o_FIR]))),3)) #Lsun
			else:
				loglum_AGNIR.append(0.0)
				loglum_AGNMIR.append(0.0)
				loglum_AGNFIR.append(0.0)
	else:
		for i in range(0, len(df)):

			obj = df.iloc[i]

			#host IR luminosity
			normDust = 10**obj['logNormGal_dust']
			enormDust = obj['elogNormGal_dust'] * np.log(10)
			nuLnuDust = normDust * templ[obj['tplName_gal']].values
			enuLnuDust = enormDust * nuLnuDust

			normPAH = 10**obj['logNormGal_PAH']
			enormPAH = obj['elogNormGal_PAH'] * np.log(10)
			nuLnuPAH = normPAH * templ['gal_PAH'].values
			enuLnuPAH = enormPAH * nuLnuPAH

			nuLnuGal = nuLnuDust + nuLnuPAH
			enuLnuGal = np.sqrt(enuLnuDust ** 2. + enuLnuPAH ** 2.)
			LnuGal = nuLnuGal/nu
			eLnuGal = enuLnuGal/nu

			loglum_hostIR.append(round(np.log10(np.trapz(LnuGal[o_IR], nu[o_IR], dx = np.gradient(nu[o_IR]))),3)) #Lsun
			elum_hostIR_i = 0
			for nu_i, nu_j, nu_k, eLnuGal_j, eLnuGal_k in zip(nu[o_IR[1:-2]], nu[o_IR[2:-1]], nu[o_IR[3:]], eLnuGal[o_IR[2:-1]], eLnuGal[o_IR[3:]]):
				elum_hostIR_i += 1./4. * (nu_j - nu_i)**2. * eLnuGal_j ** 2. + 1./4. * (nu_k - nu_j)**2. * eLnuGal_k ** 2.
			elum_hostIR = np.sqrt(elum_hostIR_i)
			eloglum_hostIR.append(round(0.434 * elum_hostIR/10**np.array(loglum_hostIR[-1]),3))
			
			loglum_hostMIR.append(round(np.log10(np.trapz(LnuGal[o_MIR], nu[o_MIR], dx = np.gradient(nu[o_MIR]))),3)) #Lsun
			elum_hostMIR_i = 0
			for nu_i, nu_j, nu_k, eLnuGal_j, eLnuGal_k in zip(nu[o_MIR[1:-2]], nu[o_MIR[2:-1]], nu[o_MIR[3:]], eLnuGal[o_MIR[2:-1]], eLnuGal[o_MIR[3:]]):
				elum_hostMIR_i += 1./4. * (nu_j - nu_i)**2. * eLnuGal_j ** 2. + 1./4. * (nu_k - nu_j)**2. * eLnuGal_k ** 2.
			elum_hostMIR = np.sqrt(elum_hostMIR_i)
			eloglum_hostMIR.append(round(0.434 * elum_hostMIR/10**np.array(loglum_hostMIR[-1]),3))
			
			loglum_hostFIR.append(round(np.log10(np.trapz(LnuGal[o_FIR], nu[o_FIR], dx = np.gradient(nu[o_FIR]))),3)) #Lsun
			elum_hostFIR_i = 0
			for nu_i, nu_j, nu_k, eLnuGal_j, eLnuGal_k in zip(nu[o_FIR[1:-2]], nu[o_FIR[2:-1]], nu[o_FIR[3:]], eLnuGal[o_FIR[2:-1]], eLnuGal[o_FIR[3:]]):
				elum_hostFIR_i += 1./4. * (nu_j - nu_i)**2. * eLnuGal_j ** 2. + 1./4. * (nu_k - nu_j)**2. * eLnuGal_k ** 2.
			elum_hostFIR = np.sqrt(elum_hostFIR_i)
			eloglum_hostFIR.append(round(0.434 * elum_hostFIR/10**np.array(loglum_hostFIR[-1]),3))

			if obj['AGNon'] == 1:
				#AGN IR luminosity
				normAGN = 10**obj['logNormAGN']
				nuLnuAGN = normAGN * templ[obj['tplName_AGN']].values

				normSi = 10**obj['logNormSiem']
				nuLnuSi = normSi * templ[nameTempl_Siem].values.flatten()

				LnuAGN = (nuLnuAGN + nuLnuSi)/nu
				
				loglum_AGNIR.append(round(np.log10(np.trapz(LnuAGN[o_IR], nu[o_IR], dx = np.gradient(nu[o_IR]))),3)) #Lsun
				loglum_AGNMIR.append(round(np.log10(np.trapz(LnuAGN[o_MIR], nu[o_MIR], dx = np.gradient(nu[o_MIR]))),3)) #Lsun
				loglum_AGNFIR.append(round(np.log10(np.trapz(LnuAGN[o_FIR], nu[o_FIR], dx = np.gradient(nu[o_FIR]))),3)) #Lsun
			else:
				loglum_AGNIR.append(0.0)
				loglum_AGNMIR.append(0.0)
				loglum_AGNFIR.append(0.0)

	#Ratio of luminosities
	loglum_hostIR = np.array(loglum_hostIR)
	eloglum_hostIR = np.array(eloglum_hostIR)
	loglum_hostMIR = np.array(loglum_hostMIR)
	eloglum_hostMIR = np.array(eloglum_hostMIR)
	loglum_hostFIR = np.array(loglum_hostFIR)
	eloglum_hostFIR = np.array(eloglum_hostFIR)
	
	loglum_AGNIR = np.array(loglum_AGNIR)
	loglum_AGNMIR = np.array(loglum_AGNMIR)
	loglum_AGNFIR = np.array(loglum_AGNFIR)

	AGNfrac_IR = np.round(10**loglum_AGNIR/(10**loglum_hostIR + 10**loglum_AGNIR),2)
	o = np.where(loglum_AGNIR == 0.)[0]
	AGNfrac_IR[o] = 0.

	AGNfrac_MIR = np.round(10**loglum_AGNMIR/(10**loglum_hostMIR + 10**loglum_AGNMIR),2)
	o = np.where(loglum_AGNMIR == 0.)[0]
	AGNfrac_MIR[o] = 0.

	AGNfrac_FIR = np.round(10**loglum_AGNFIR/(10**loglum_hostFIR + 10**loglum_AGNFIR),2)
	o = np.where(loglum_AGNFIR == 0.)[0]
	AGNfrac_FIR[o] = 0.

	SFR = np.round(1.09e-10 * 10**loglum_hostIR,3) #Chabrier
	eSFR = np.round(1.09e-10 * 10**loglum_hostIR * np.log(10) * eloglum_hostIR,3)
	wSFR = np.round(1.09e-10 * 10**loglum_hostIR * df['Aw'].values,3)
	ewSFR = np.round(1.09e-10 * 10**loglum_hostIR * df['Aw'].values * np.log(10) * eloglum_hostIR,3)

	return loglum_hostIR, eloglum_hostIR, \
		   loglum_hostMIR, eloglum_hostMIR, \
		   loglum_hostFIR, eloglum_hostFIR, \
		   loglum_AGNIR, loglum_AGNMIR, loglum_AGNFIR, \
		   AGNfrac_IR, AGNfrac_MIR, AGNfrac_FIR, SFR, eSFR, wSFR, ewSFR

def basictests(wav, flux, eflux, filters, wavToFit, UL, z, specOn = True):

	#test that the length of wavelength is the same as the data
	if (len(wav) != len(flux)) or (len(wav) != len(eflux)):
		raise ValueError("Wavelengths, fluxes and uncertainties on the fluxes have different lengths.")
		
	#test that there are no negative values
	if (any(flux<0) == True) or (any(eflux<0) == True) or (any(wav<0) == True):
		raise ValueError("Any of the vectors wavelengths, fluxes or uncertainties on the fluxes contain negative values.")

	#test that there are NAN
	if (any(flux != flux) == True) or (any(eflux != eflux) == True) or (any(wav != wav) == True):
		raise ValueError("Any of the vectors wavelengths, fluxes or uncertainties on the fluxes contain non-numerical values.")

	#test if the lenght of photometry vectors are consistent
	if (len(filters) != len(wavToFit)) or (len(filters) != len(UL)):
		raise ValueError("The broadband filters [keyword: filters], the wavelength of the FIR photometry or the upper limits [keyword: UL] have different lengths.")

	#test if the filter vector contains strings for the name of the broadband filters
	if all(isinstance(item, str) for item in filters) == False:
		raise TypeError("The vector filters should only contain strings with the name of the broadband filters that need to be used for the fit.")		

	#test if the filter exists
	path = os.path.dirname(iragnsep.__file__) + '/Filters/'
	files = [f for f in glob.glob(path + "*.csv")]
	count = -1
	for f in [path+f+"Filter.csv" for f in filters]:
		count += 1
		if (f in files) == False:
			raise ValueError("The filter "+ str(filters[count]) + " does not exist. This version does not allow you to add some filters." + \
							 " Please get in touch with us to add the required filters (e.p.bernhard@sheffield.ac.uk).")

	#Test if the redshift has been given by the user
	if z<0:
		try:
			zdefault = input('Warning: The redshift is set to the default value of 0.01. The keyword "z" allows you to indicate the redshift of the source.\n '+\
							 ' Press enter to continue, or press ctr+c to abort.')
		except:
			pass

	#Test that if the IRS spectra is included, no broadband photometry are overlapping
	if (specOn == True):
		dlambda = np.gradient(wav)
		o = np.where(dlambda < 0.)[0]
		if len(o) > 0.:
			raise ValueError('Make sure that all the wavelengths are in ascending order.')
		wavIRS = np.concatenate([wav[dlambda<5.], [wav[dlambda>5.][0]]])
		if any(wavIRS>min(wavToFit)) == True:
			raise ValueError('The IRS spectra is included. Any broadband photometry overlapping with the IRS spectra are useless.'+\
							 ' Please remove the filters that are not necessary.')
		wavHer = wav[dlambda>5.][1::]
		if len(wavHer) != len(wavToFit):
			raise ValueError('There is a missmatch between the numbers of wavelengths with detected Herschel fluxes and the '+\
							 'number of wavelengths to fit. Most common fix: The default FIR wavelengths are '+\
							 '[70., 100., 160., 250., 350., 500.]. If you do not have all the fluxes (or have different bands), change the keyword '+\
							 'wavToFit accordingly.')

	# Break as not enough data points anyway,
	if len(wav) < 4:
		raise ValueError('There are not enough data points to fit the model when compared to the number of degrees of freedom. It needs a minimum of' + \
						 ' 5 data points (including upper-limits).')
	# if len(wav) == 4:
	# 	print('There are not enough data points. The Si emission template is removed and only the continuum will be fit.')
	# 	QF -= 2.

	# #Test for the quality flag
	# QF = 0.0
	

	# o = np.where(wav <= 70.)[0]
	# if len(o) <=2.:
	# 	QF -= 0.5 #The Lir and SFR should be OK.

	# if len(wav) == 5:
	# 	QF -= 1. # The Lir and SFR shoud be OK

	# if specOn == False:
	# 	return QF

def exctractBestModel(logl, k, n, corrected = True):

	nkdif = np.array(n)-np.array(k)
	o = np.where(nkdif == 1)[0]
	if len(o) > 0:
		corrected = False

	if corrected == True:
		AIC = 2*np.array(k) - 2.*np.array(logl) + (2.*np.array(k)**2. + 2.*np.array(k))/(np.array(n)-np.array(k)-1.)
	else:
		AIC = 2*np.array(k) - 2.*np.array(logl)

	bestModelInd = np.where(AIC == np.min(AIC))[0]
	AICmin = AIC[bestModelInd]
	AwiNorm = np.sum(np.exp(-0.5 * (AIC-AICmin)))

	Awi = np.exp(-0.5 * (AIC-AICmin))/AwiNorm

	return bestModelInd, Awi

def nuLnuToFnu(spec_wav, nuLnu, z):

	dMpc = cosmo.luminosity_distance(z).value #Mpc
	dmeter = dMpc*u.Mpc.to(u.m)
	d2z = dmeter**2./(1.+z) # K correction=>https://ned.ipac.caltech.edu/level5/Sept02/Hogg/Hogg2.html

	# Derive the observed flux
	nu = c/spec_wav/1e-6 #Hz
	Lnu = nuLnu/nu*Lsun #W/Hz
	Fnu = Lnu/4./np.pi/d2z #W/Hz/m2

	return Fnu * 1e26 # Jy

def getFluxInFilt(filt_wav, filt_QE, spec_wav, nuLnu, z):

	norm = integrate.trapz(filt_QE, x=c/filt_wav/1e-6)

	Fnu_0 = nuLnuToFnu(spec_wav, nuLnu, z) #Flux received on Earth
	lambda_0 = spec_wav * (1. + z) # Wavelenght of emission
	Fnu_0filt = np.interp(filt_wav, lambda_0, Fnu_0) # Move the template to grab the redshifted flux
	flux_Obs = integrate.trapz(Fnu_0filt*filt_QE, x = c/filt_wav/1e-6)/norm # This is the flux received on Earth

	return flux_Obs

@njit
def Gauss_jit(x, mu, sigma):

	Bnu = np.exp(-(np.log10(x)-mu)**2./2./sigma/sigma)

	return Bnu/np.max(Bnu)

@njit()
def AGNmodel_jit(x, lambdab1, lambdab2, alpha1, alpha2, alpha3):

	Bnu0 = x**alpha1*(1. + (x/lambdab1)**(abs(alpha2-alpha1)))**np.sign(alpha2)
	Bnu1 = x**alpha2*(1. + (x/lambdab2)**(abs(alpha3-alpha2)))**np.sign(alpha3)

	# o = np.where(np.gradient(np.log10(Bnu1)) < np.gradient(np.log10(Bnu0)))[0]
	o = np.where(np.diff(np.log10(Bnu1)) < np.diff(np.log10(Bnu0)))[0]
	xJoint = x[o][0]
	Bnu0Norm = xJoint**alpha1*(1. + (xJoint/lambdab1)**(abs(alpha2-alpha1)))**np.sign(alpha2)
	Bnu1Norm = xJoint**alpha2*(1. + (xJoint/lambdab2)**(abs(alpha3-alpha2)))**np.sign(alpha3)

	Bnu = x*0.
	o = np.where(x<xJoint)[0]
	Bnu[o] = Bnu0[o]/Bnu0Norm
	o = np.where((x>=xJoint))[0]
	Bnu[o] = Bnu1[o]/Bnu1Norm

	o = np.where((x>14.) & (x<16.))[0]
	BnuNorm = np.mean(Bnu[o])

	return Bnu/BnuNorm

def AGNmodel(x, lambdab1, lambdab2, alpha1, alpha2, alpha3):

	Bnu0 = x**alpha1*(1. + (x/lambdab1)**(abs(alpha2-alpha1)))**np.sign(alpha2)
	Bnu1 = x**alpha2*(1. + (x/lambdab2)**(abs(alpha3-alpha2)))**np.sign(alpha3)

	# o = np.where(np.gradient(np.log10(Bnu1)) < np.gradient(np.log10(Bnu0)))[0]
	o = np.where(np.diff(np.log10(Bnu1)) < np.diff(np.log10(Bnu0)))[0]
	xJoint = x[o][0]
	Bnu0Norm = xJoint**alpha1*(1. + (xJoint/lambdab1)**(abs(alpha2-alpha1)))**np.sign(alpha2)
	Bnu1Norm = xJoint**alpha2*(1. + (xJoint/lambdab2)**(abs(alpha3-alpha2)))**np.sign(alpha3)

	Bnu = x*0.
	o = np.where(x<xJoint)[0]
	Bnu[o] = Bnu0[o]/Bnu0Norm
	o = np.where((x>=xJoint))[0]
	Bnu[o] = Bnu1[o]/Bnu1Norm

	o = np.where((x>14.) & (x<16.))[0]
	BnuNorm = np.mean(Bnu[o])

	return Bnu/BnuNorm

def Gauss(x, mu, sigma):

	Bnu = np.exp(-(np.log10(x)-mu)**2./2./sigma/sigma)

	return Bnu/np.max(Bnu)

def KVTextinctCurve(lambda_obs):

	lambda_mic = np.arange(1., 40., 0.01)
	kvt_wav = 8.0, 8.2, 8.4,  8.6,  8.8,  9.0,  9.2,  9.4, 9.6, 9.7, 9.75, 9.8, 10.0, 10.2,\
			  10.4, 10.6, 10.8, 11.0, 11.2, 11.4,11.6, 11.8, 12.0, 12.2, 12.4, 12.6, 12.7
	kvt_prof= .06, .09, .16, .275, .415, .575, .755, .895, .98, .99, 1.00, .99, .94 ,  .83,\
			  .745, .655,  .58, .525,  .43,  .35, .27,  .20,  .13,  .09,  .06, .045, .04314 

	PSIlambda = np.zeros(len(lambda_mic))

	o = np.where((lambda_mic > 8) & (lambda_mic < 12.7))[0]
	if len(o) > 0:
		PSIlambda[o] = np.interp(lambda_mic[o], kvt_wav, kvt_prof)

	PSI8 = 0.06
	o = np.where(lambda_mic <= 8)[0]
	if len(o) > 0:
		PSIlambda[o] = PSI8*np.exp(2.03*(lambda_mic[o]-8.))

	o = np.where(lambda_mic >= 12.7)[0]
	if len(o) > 0:
		PSIlambda[o] = 0.247 * drude(lambda_mic[o], 0.4, 18.)

	PSI9p7 = np.interp(9.7, lambda_mic, PSIlambda)
	tau = (0.9*PSIlambda + 0.1*(9.7/lambda_mic)**1.7)/PSI9p7

	return np.interp(lambda_obs, lambda_mic, tau)

# Drude profile
def drude(x, gamma_r, lambda_r, normed = True):
	numerateur = gamma_r**2.
	denominateur = (x/lambda_r - lambda_r/x)**2. + gamma_r**2.
	drudeVal = numerateur/denominateur

	if normed == True:
		return drudeVal/np.max(drudeVal)
	else:
		return np.max(drudeVal), drudeVal


# Correct from obscuration
def corrIRSobs(IRSwavRest, IRSflux, eIRSflux):

	loc1 = np.where((IRSwavRest >= 5.) & (IRSwavRest<=7.))[0]
	loc2 = np.where((IRSwavRest >= 14.) & (IRSwavRest<=14.5))[0]
	loc3 = np.where((IRSwavRest >= 25.) & (IRSwavRest<=31.5))[0]

	if (len(loc1) <1) & (len(loc2) < 1):
	 	raise Exception()

	if len(loc3) > 0:
		k = 4
		# Get the flux in the anchored wavelengths
		IRSwavAbs = np.concatenate((IRSwavRest[loc1], IRSwavRest[loc2], IRSwavRest[loc3]))
		IRSfluxAbs = np.concatenate((IRSflux[loc1], IRSflux[loc2], IRSflux[loc3]))
	
		Npoints = float(len(loc1) + len(loc2) + len(loc3))

		wei = np.zeros(len(IRSwavAbs))
		wei[0:len(loc1)] = 1./(len(loc1)/Npoints)
		wei[len(loc1):len(loc1)+len(loc2)] = 1./(len(loc2)/Npoints)
		wei[len(loc1)+len(loc2):] = 1./(len(loc3)/Npoints)

	else:
		k = 1

		# Get the flux in the anchored wavelengths
		IRSwavAbs = np.concatenate((IRSwavRest[loc1], IRSwavRest[loc2]))
		IRSfluxAbs = np.concatenate((IRSflux[loc1], IRSflux[loc2]))
		
		Npoints = float(len(loc1) + len(loc2))

		wei = np.zeros(len(IRSwavAbs))
		wei[0:len(loc1)] = 1./(len(loc1)/Npoints)
		wei[len(loc1):len(loc1)+len(loc2)] = 1./(len(loc2)/Npoints)

	# Fit a k-order spline
	spl = UnivariateSpline(np.log10(IRSwavAbs), np.log10(IRSfluxAbs), k=k, w = wei)
	contFlux = 10**spl(np.log10(IRSwavRest))

	# Measure the ratio between the true and the obsverbed flux
	fluxTrue9p7 = np.interp(9.7, IRSwavRest, contFlux)
	locDeep = np.where((IRSwavRest >= 9.4) & (IRSwavRest <= 10.0))[0]
	fluxObs9p7 = np.mean(IRSflux[locDeep])
	f9p7ratio = fluxObs9p7/fluxTrue9p7

	# Use the definition of tau9p7 and measure absorption(lambda)
	_tau9p7 = -np.log(f9p7ratio)
	tau = KVTextinctCurve(IRSwavRest) * _tau9p7

	# Exctintion corrected flux
	IRSflux_corr = IRSflux/((1. - np.exp(-tau))/tau) # Exctinction corrected flux
	eIRSflux_corr = eIRSflux/((1. - np.exp(-tau))/tau) # Exctinction corrected flux

	if _tau9p7 > 5.:
		print('The correction for obscuration is abnormally high (tau9p7 > 5). Please check carefully.')

	return IRSflux_corr, eIRSflux_corr, _tau9p7

def mod_black_body_norm(x, T, beta):
	
	nu = 3e8/x/1e-6

	expo = np.exp(h*nu/k/T)
	term1 = 2.*h*nu**3/c**2.
	term2 = 1./(expo-1.0)

	Bnu = nu**beta * term1 * term2

	nu = 3e8/10./1e-6

	expo = np.exp(h*nu/k/T)
	term1 = 2.*h*nu**3/c**2.
	term2 = 1./(expo-1.0)

	BnuNorm = np.max(Bnu)#nu**beta * term1 * term2

	return Bnu/BnuNorm # W/m2/Hz/sr

	