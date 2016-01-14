import apogee.modelspec.moog
from apogee.modelatm import atlas9
import apogee.spec.plot as splot
 
atm= atlas9.Atlas9Atmosphere(teff=5000,logg=2.0,metals=0.0,am=0.3,cm=0.3)
synspec= apogee.modelspec.moog.synth([13,-0.05,0.25],modelatm=atm,\
         linelist='moog.201312161124.vac',lsf='all',cont='aspcap',vmacro=6.,isotopes='solar')
 
splot.waveregions(synspec[0])
splot.waveregions(synspec[1],overplot=True)
