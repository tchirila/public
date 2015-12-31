# downloads all files within parameter range (all combinations), use python2.7
from apogee.modelatm import atlas9
for t in range(3500, 6250, 250):
    for x in range(0, 55, 5):
        g = x/10.0 
        for y in range(-2, 5, 1):
            m = y/10.0
            atm= atlas9.Atlas9Atmosphere(teff=t,logg=g,metals=m,am=0.25,cm=0.25)
