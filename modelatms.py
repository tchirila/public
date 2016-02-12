# downloads all files within parameter range (all combinations), use python2.7
from apogee.modelatm import atlas9
import sys

logfile = open('DownloaderLogs.txt', 'w')
count = 0 # number of downloaded atmospheres

for t in range(3500, 6750, 250):
    for x in range(0, 55, 5):
        g = x/10.0 
        for y in range(-25, 10, 5):
            m = y/10.0
            try:
                atm= atlas9.Atlas9Atmosphere(teff=t,logg=g,metals=m,am=0.25,cm=0.25)
                count = count+1
            except IOError as errIO:
                logfile.write('Error encountered: '+str(errIO)+'/n')
                sys.exc_clear()
            except IndexError as errIdx:
                logfile.write('Error encountered: '+str(errIdx)+'/n')
                sys.exc_clear()

logfile.write('Number of downloaded atmospheres is: '+str(count))
logfile.close()

# /home/asttchir/Dropbox/Python/modelatms.py
