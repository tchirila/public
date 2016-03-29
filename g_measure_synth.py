from ewmeasure import simpEWmeasurement as EW_measure
import ewmeasure
import numpy as np
import astropy.io.fits as pyf
import glob
import os

dspecpath = '/home/asttchir/synthfits'
linelistpath = '/home/asttchir/specwork/linelist.txt'
speclist = [file for file in glob.glob(os.path.join(dspecpath, '*/*.fits'))]

linelist =np.genfromtxt(linelistpath, dtype=None, names=True)
int_reg = []
cont_reg = []
for i in range(0,len(linelist)):
	int_tuple = (linelist['i_b'][i], linelist['i_r'][i])
	cont_tuples = eval(linelist['cont'][i])
	int_reg.append(int_tuple)
	cont_reg.append(cont_tuples)

AL_16723_ews = []
AL_16723_errs = []
AL_16755_ews = []
AL_16755_errs = []
AL_16767_ews = []
AL_16767_errs = []
TEMPS = []
METS= []
LOGGS = []
A_MS = []
C_MS = []
N_MS = []
names = []

numspec = len(speclist)
bins = numspec/100
print 'measuring '+str(numspec)+' spectra...'
counter = 0
bincount = 0
sigma_clip = False
sigma = 2
synthetic = True
for file in speclist:
	AL_16723_ew = EW_measure(file,int_reg[0],cont_reg[0], synthetic=synthetic,  sigmaclip=sigma_clip, sigma=sigma)
	AL_16755_ew = EW_measure(file,int_reg[1],cont_reg[1], synthetic=synthetic,  sigmaclip=sigma_clip, sigma=sigma)
	AL_16767_ew = EW_measure(file,int_reg[2],cont_reg[2], synthetic=synthetic,  sigmaclip=sigma_clip, sigma=sigma)
    #name=str(file[-23:-5])
	name=str(file[6:-5])
	counter = counter + 1
	if counter == bins:
		bincount = bincount + 1
		print "Process is " + str(int(bincount)) + "% complete"
		counter = 0
	names.append(name)
        AL_16723_ews.append(AL_16723_ew[0])
        AL_16723_errs.append(AL_16723_ew[1])
        AL_16755_ews.append(AL_16755_ew[0])
        AL_16755_errs.append(AL_16755_ew[1])
        AL_16767_ews.append(AL_16767_ew[0])
        AL_16767_errs.append(AL_16767_ew[1])
	dat= pyf.open(file)
	head = dat[0].header
	A_MS.append(head['A_M'])
	C_MS.append(head['C_M'])
	N_MS.append(head['N_M'])
	TEMPS.append(float(head['TEFF']))
	METS.append(head['M_H'])
	LOGGS.append(head['LOGG'])

	
speclist = speclist
tbhdu = tbhdu = pyf.new_table(pyf.ColDefs(
                                  [pyf.Column(name='names', format='40A', array=names), \
                                   pyf.Column(name='AL16723_EW', format='D', array=AL_16723_ews), \
                                   pyf.Column(name='AL16723_ERR', format='D', array=AL_16723_errs), \
                                   pyf.Column(name='AL16755_EW', format='D', array=AL_16755_ews), \
                                   pyf.Column(name='AL16755_ERR', format='D', array=AL_16755_errs), \
                                   pyf.Column(name='AL16767_EW', format='D', array=AL_16767_ews), \
                                   pyf.Column(name='AL16767_ERR', format='D', array=AL_16767_errs), \
                                   pyf.Column(name='A/M', format='D', array=A_MS), \
                                   pyf.Column(name='C/M', format='D', array=C_MS), \
                                   pyf.Column(name='N/M', format='D', array=N_MS), \
                                   pyf.Column(name='TEMP', format='D', array=TEMPS), \
                                   pyf.Column(name='LOGG', format='D', array=LOGGS), \
                                   pyf.Column(name='MET', format='D', array=METS)]))
tbhdu.writeto('/home/asttchir/synthfits/test.fits')
# /home/asttchir/Dropbox/Python/g_measure_synth.py
