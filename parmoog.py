# 1st half creates a file with the full list of parameter files
# 2nd half uses the file from the 1st half to feed the parameter files into MOOGSILENT
# run in iraffiles folder
import os
import os.path
import time

parlist = []
path = "/home/asttchir/paramfiles"
batchpath = "/home/asttchir/iraffiles"
start=time.time()

for i in range(0, 1, 1):
    for path, dirnames, filenames in os.walk(path):
        for file in [f for f in filenames if f.endswith(".par")]:
            file = os.path.join(path, file)
            parlist.append(file)        
    outfile = open('/home/asttchir/specwork/parlist.txt','w')

    for name in parlist:    
        outfile.write(name+'\n')    
    outfile.close()

listpath = "/home/asttchir/specwork/parlist.txt"

with open(listpath) as parfile:
    pardata = parfile.read()
    parlist = pardata.split() # each .par name has 28 characters including the '.par' part
    n = int(len(parlist)) # calculates nr. of elements and converts string to integer
    
    for i in range(0, n, 1): # iterates for each element(.par file) of the list    
        parpath = parlist[i]
        
        with open(parpath, 'r') as partemplate: # saves .par file as batch.par for MOOGSILENT to use
                with open('batch.par', 'w') as paramfile:
                    for line in partemplate:
                        paramfile.write(line)
                paramfile.close()
        partemplate.close()
        os.system("MOOGSILENT")
	
end=time.time()-start
print str(end)+' seconds'        

# /home/asttchir/Dropbox/Python/parmoog.py
