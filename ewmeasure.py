#version current as of 24/10/15

#import necessary modules
#import pyfits as pyf
from astropy.io import fits as pyf
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.integrate import simps
from scipy.interpolate import interp1d


#generate list of spectra in a given directory into an array
def gen_speclist(path):
	speclist = []
	for file in os.listdir(path):
		if file.endswith(".fits"):
			speclist.append(file)
	return speclist

#make a text list of the spectra in a given directory, be careful not to include other
#fits files in the same directory!
def makespeclist(path):
	speclist = []
	for file in os.listdir(path):
		if file.endswith(".fits"):
			speclist.append(file)
	outfile = open('speclist.txt','w')
	for name in speclist:
		outfile.write(path+name+'\n')
	outfile.close()

#method to find nearest pixel (x_vals) to a given wavelength value (value)
def find_nearest_pixel(x_vals, value):
	idx = (np.abs(x_vals-value)).argmin()
	return x_vals[idx]

#Wavelength dispersion correction function for APOGEE log-linear spectra
def Dispersion_Correct(spectrum, extension = 1):
	data_x = []
	fit_x = []
	full = pyf.open(spectrum)
	data = full[extension].data
	datahead = full[extension].header
	data_w1 = float(datahead['CRVAL1'])
	data_dw = float(datahead['CDELT1'])
	data_N = int(datahead['NAXIS1'])
	for i in range(1,data_N+1):
		data_w =10 ** (data_w1 + data_dw * (i-1))
		data_x.append(data_w)
	return np.vstack((data_x,data))

#dispersion correction for APOGEE synthetic spectra
def Synth_Dispersion_Correct(spectrum):
	data_x = []
	fit_x = []
	full = pyf.open(spectrum)
	data = full[0].data
	datahead = full[0].header
	data_w1 = float(datahead['CRVAL1'])
	data_dw = float(datahead['CDELT1'])
	data_N = int(datahead['NAXIS1'])
	for i in range(1,data_N+1):
		data_w =10**(data_w1 + data_dw * (i-1))
		data_x.append(data_w)
	return np.vstack((data_x,data))

#define simple EW measurement function using simpsons rule
#(add interpolation of line and continuum??)
def simpEWmeasurement(spectrum, integration, windows, synthetic=False, sigmaclip= True, sigma=2):
	if synthetic == False:
	   spec = Dispersion_Correct(spectrum)
	   errspec = Dispersion_Correct(spectrum, extension = 2)
	   errspec_x = errspec[0]
	   errspec_y = errspec[1]
	elif synthetic == True:
	   spec = Synth_Dispersion_Correct(spectrum)
	spec_x = spec[0]									#create arrays for spectra
	spec_y = spec[1]
	norm_pix = []
	norm_lambda = []
	for i in windows:
		region = (spec_x > i[0]) & (spec_x < i[1])
		pix = spec_y[region]
		lambd = spec_x[region]
		norm_pix.extend(pix)
		norm_lambda.extend(lambd) 
	norm_pix = np.array(norm_pix)
	norm_lambda = np.array(norm_lambda)
	cont_fit = np.polyfit(norm_lambda,norm_pix, 1)
	cont_poly = np.poly1d(cont_fit)
	if sigmaclip == True:
		std = sigma*np.std(norm_pix)
		residual = np.abs(norm_pix - cont_poly(norm_lambda))
		clip = residual < std
		norm_lambda = norm_lambda[clip]
		norm_pix = norm_pix[clip]
		cont_fit = np.polyfit(norm_lambda,norm_pix, 1)
		cont_poly = np.poly1d(cont_fit)
	int_reg = [(spec_x >= integration[0]) & (spec_x <= integration[1])]
	interpol = interp1d(spec_x, spec_y, kind='linear')
	line_x = spec_x[int_reg]
	line_y = spec_y[int_reg]
	bfrac_x=np.array([integration[0], line_x[0]])
	rfrac_x=np.array([line_x[-1], integration[1]])
	cont_y = cont_poly(line_x)
	norm_y = line_y/cont_y
	bfrac_y=np.array([interpol(integration[0])/cont_poly(integration[0]), norm_y[0]])
	rfrac_y=np.array([norm_y[-1], interpol(integration[1])/cont_poly(integration[1])])
	contarea = max(line_x)-min(line_x)
	linearea = simps((1-norm_y), line_x)
	bfrac_area = simps((1-bfrac_y), bfrac_x)
	rfrac_area = simps((1-rfrac_y), rfrac_x)
	if synthetic == False:
		err_interpol = interp1d(errspec_x, errspec_y, kind='linear')
		err_x = errspec_x[int_reg]
		err_y = errspec_y[int_reg]
		errbfrac_x = np.array([integration[0], err_x[0]])
		errrfrac_x = np.array([err_x[-1], integration[1]])
		errbfrac_y = np.array([err_interpol(integration[0]), err_y[0]])
		errrfrac_y = norm_lambda.extend(lambd)
		err_line = simps(err_y, err_x)+ simps(errbfrac_y, errbfrac_x)+ simps(errrfrac_y, errrfrac_x)	
		EW = linearea+bfrac_area+rfrac_area
		return [EW, err_line]
	else:
		EW = linearea+bfrac_area+rfrac_area
		return [EW, 0]
	


#append the parameters of APOGEE synthetic spectra to their existing EW measurements
def appendparams(table, namecol='names'):
	tablefile = pyf.open(table)
	table = tablefile[1].data
	names = table.field(namecol)
	temps = []
	mets = []
	loggs = []
	alphas = []
	carbs = []
	nitros = []
	for name in names:
	    temp = name[18:22]
	    table = tablefile[1].data
	    names = table.field(namecol)
	    temps = []
	    mets = []
	    loggs = []
	    alphas = []
	    temp = float(temp)
	    if name[27] =='p':
		met = name[28:30]
	    else:
		met = '-' + name[28:30]
	    met = float(met)/10
	    if name[1] =='p':
		alpha = name[2:4]
	    else:
		alpha = '-' + name[2:4]
	    alpha = float(alpha)/10
	    if name[5] =='p':
		carb = name[6:8]
	    else:
		carb = '-' + name[6:8]
	    carb = float(carb)/10
	    if name[9] =='p':
		nitro = name[10:12]
	    else:
		nitro = '-' + name[10:12]
	    nitro = float(nitro)/10
	    logg = name[24:26]
	    logg = float(logg)/10
	    mets.append(met)
	    loggs.append(logg)
	    temps.append(temp)
	    alphas.append(alpha)
	    carbs.append(carb)
	    nitros.append(nitro)

	tablefilecols = table.columns
	paramcol = pyf.ColDefs([
							pyf.Column(name='A/M', format='D', array=alphas),
							pyf.Column(name='C/M', format='D', array=carbs),
							pyf.Column(name='N/M', format='D', array=nitros),
							pyf.Column(name='TEMP', format='D', array=temps),
							pyf.Column(name='LOGG', format='D', array=loggs),
							pyf.Column(name='MET', format='D', array=mets)])
	newhdu = pyf.new_table(tablefilecols + paramcol)
	newhdu.writeto('ews_params.fits')
