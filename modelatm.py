# downloads all files within parameter range (all combinations), use python2.7
from apogee.modelatm import atlas9
import sys

for t in range(3500, 6750, 250):
    for x in range(0, 55, 5):
        g = x/10.0 
        for y in range(-25, 10, 5):
            m = y/10.0
            try:
                atm= atlas9.Atlas9Atmosphere(teff=t,logg=g,metals=m,am=0.25,cm=0.25)
            except KeyError:
                sys.exc_clear()

# new version, not tested yet

from apogee.modelatm import atlas9
import sys

for t in range(3500, 6750, 250):
    
    for x in range(0, 55, 5):
        g = x/10.0 
        
        for y in range(-25, 10, 5):
            m = y/10.0
            
            try:
                atm= atlas9.Atlas9Atmosphere(teff=t,logg=g,metals=m,am=0.25,cm=0.25)
            
            except KeyError:
                sys.exc_clear()
