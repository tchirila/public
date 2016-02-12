# converts kurucz model atmospheres using the awk script
import os
import os.path

atmlist = []
path = "/scratch/asttchir/modelatm_kurucz"

for i in range(0, 1, 1):
    for path, dirnames, filenames in os.walk(path):
        for file in [f for f in filenames if f.endswith(".mod")]:
            file = os.path.join(path, file)
            atmlist.append(file)        
    outfile = open('atmlist_kurucz.txt','w')

    for name in atmlist:    
        outfile.write(name+'\n')    
    outfile.close()

listpath = "/scratch/asttchir/specwork/atmlist_kurucz.txt"

with open(listpath) as atmfile:
    atmdata = atmfile.read()
    atmlist = atmdata.split() # each .mod name has 28 characters including the '.mod' part
    n = int(len(atmlist)) # calculates nr. of elements and converts string to integer
    
    for i in range(0, n, 1): # iterates for each element(.mod file) of the list    
        oldpath = atmlist[i]
        fullatmname = oldpath[-28:]
        name = fullatmname[0:24]
        newpath = '/scratch/asttchir/modelatm/'
    
    input = ('awk -f mod2moog '+str(oldpath)+' > '+newpath+str(name)+'.moog')
    input = (' ')

# /home/asttchir/Dropbox/Python/converter.py
# /home/asttchir/Dropbox/Python/trigger.py
