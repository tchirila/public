# /home/asttchir/Dropbox/Python/ewviewobs.py
import matplotlib.pyplot as plt
from astropy.io import fits
from operator import itemgetter
import numpy as np

pick = 0 # pick a number from 0 to 5, correspoding to the item in plist
plist = ['PARAM_M_H', 'C_H', 'PARAM_ALPHA_M', 'TEFF', 'LOGG', 'AL_H']
perrlist = ['PARAM_M_H_ERR', 'C_H_ERR', 'PARAM_ALPHA_M_ERR', 'TEFF_ERR', 'LOGG_ERR', 'AL_H_ERR']
choice = plist[pick]
plist.remove(plist[pick])
M_H, C_H, ALPHA_M, TEFF, LOGG, AL_H = 0.0, 0.25, 0.25, 4500.0, 2.0, 0.3
M_H_min = M_H-0.1
M_H_max = M_H+0.1
C_H_min = C_H-0.1
C_H_max = C_H+0.1
ALPHA_M_min = ALPHA_M-0.1
ALPHA_M_max = ALPHA_M+0.1
M_H_min = M_H-0.1
M_H_max = M_H+0.1
TEFF_min = TEFF-100.0
TEFF_max = TEFF+100.0
LOGG_min = LOGG-0.2
LOGG_max = LOGG+0.2
AL_H_min = AL_H-0.1
AL_H_max = AL_H+0.1
constlist = [M_H, C_H, ALPHA_M, TEFF, LOGG, AL_H]
constlist_min = [M_H_min, C_H_min, ALPHA_M_min, TEFF_min, LOGG_min, AL_H_min]
constlist_max = [M_H_max, C_H_max, ALPHA_M_max, TEFF_max, LOGG_max, AL_H_max]
arrow = constlist[pick]
constlist.remove(constlist[pick])
constlist_min.remove(constlist_min[pick])
constlist_max.remove(constlist_max[pick])
title = ['[M/H]', '[C/M]', r'[$\alpha$/M]', '$T_eff$', 'log(g)', '[Al/M]']
xlabel = title[pick]
title.remove(title[pick])
rows = 0
count = 0
xlist = []
AL_16723_ew =[]
AL_16755_ew =[]
AL_16767_ew =[]

paramtable = fits.open('allStar-v603.fits')
tbdata = paramtable[1].data
ID = np.array(tbdata['APOGEE_ID'])
ewtable = fits.open('allStar_ews150416_v603.fits')
ewdata = ewtable[1].data
ID_ew = ewdata['names']

for i in tbdata.field(choice):
    rows = rows+1

for i in range(0, rows, 1):
    if constlist_min[0] <= tbdata.field(plist[0])[i] <= constlist_max[0]:
        if constlist_min[1] <= tbdata.field(plist[1])[i] <= constlist_max[1]:
            if constlist_min[2] <= tbdata.field(plist[2])[i] <= constlist_max[2]:
                if constlist_min[3] <= tbdata.field(plist[3])[i] <= constlist_max[3]:
                    if constlist_min[4] <= tbdata.field(plist[4])[i] <= constlist_max[4]:
                        match = np.in1d(ID[i], ID_ew)
                        if match == True:
                            ID_name = ID[i]
                            xlist.append(tbdata.field(choice)[i])
                            AL_16723_ew.append(ewdata.field('AL16723_EW')[ID_name])
                            AL_16755_ew.append(ewdata.field('AL16755_EW')[ID_name])
                            AL_16767_ew.append(ewdata.field('AL16767_EW')[ID_name])
                            count = count+1                        

xlist, AL_16723_ew, AL_16755_ew, AL_16767_ew = [list(x) for x in zip(*sorted(zip(xlist, AL_16723_ew, AL_16755_ew, AL_16767_ew), key=itemgetter(0)))]
plt.figure(figsize=(7,5))
plt.plot(xlist, AL_16723_ew,'b-^')
plt.plot(xlist, AL_16755_ew,'g-D')
plt.plot(xlist, AL_16767_ew,'r-o')
plt.grid()
plt.xlabel(xlabel, fontsize=16)
plt.ylabel('EW ('r'$\AA$)', fontsize=16)
plt.ylim(0.0, 0.6)
plt.title(title[0]+'='+str(constlist[0])+', '+title[1]+'='+str(constlist[1])+', '+title[2]+'='+str(constlist[2])+'\n'+title[3]+'='+str(constlist[3])+', '+title[4]+'='+str(constlist[4])+', [N/M]=0.0, '+str(count)+' spectra', fontsize=14)
plt.legend(['Al16723', 'Al16755', 'Al16767'], loc='best')
plt.annotate('', xy=(arrow, 0.1), xytext=(arrow, 0.05), arrowprops=dict(facecolor='black', shrink=0.1))
plt.show()
'''
table = fits.open('allStar-v603.fits')
data = table[1].data
IDs = data['APOGEE_ID']
match = np.in1d(IDs, measured_IDs)
'''
