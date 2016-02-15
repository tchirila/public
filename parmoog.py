# 1st half creates a file with the full list of parameter files
# 2nd half uses the file from the 1st half to feed the parameter files into MOOGSILENT
import os
import os.path

parlist = []
path = "/scratch/asttchir/paramfiles"

for i in range(0, 1, 1):
    for path, dirnames, filenames in os.walk(path):
        for file in [f for f in filenames if f.endswith(".par")]:
            file = os.path.join(path, file)
            parlist.append(file)        
    outfile = open('/scratch/asttchir/specwork/parlist.txt','w')

    for name in parlist:    
        outfile.write(name+'\n')    
    outfile.close()

listpath = "/scratch/asttchir/specwork/parlist.txt"

with open(listpath) as parfile:
    pardata = parfile.read()
    parlist = pardata.split() # each .par name has 28 characters including the '.par' part
    n = int(len(parlist)) # calculates nr. of elements and converts string to integer
    
    for i in range(0, n, 1): # iterates for each element(.par file) of the list    
        parpath = parlist[i]
        os.system("gnome-terminal -e 'bash -c \"MOOGSILENT ; %s\"'" % (parpath))

# /home/asttchir/Dropbox/Python/parmoog.py
