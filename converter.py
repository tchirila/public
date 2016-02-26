# First half creates a list of modelatm paths, run in specwork (where the awk script file is)
# Second half uses the list from the 1st half to convert kurucz model atmospheres using the awk script
import os
import os.path

atmlist = []
path = "/home/asttchir/modelatm_kurucz"

for i in range(0, 1, 1):
    for path, dirnames, filenames in os.walk(path):
        for file in [f for f in filenames if f.endswith(".mod")]:
            file = os.path.join(path, file)
            atmlist.append(file)        
    outfile = open('/home/asttchir/specwork/atmlist_kurucz.txt','w')

    for name in atmlist:    
        outfile.write(name+'\n')    
    outfile.close()

listpath = "/home/asttchir/specwork/atmlist_kurucz.txt"

with open(listpath) as atmfile:
    atmdata = atmfile.read()
    atmlist = atmdata.split() # each .mod name has 28 characters including the '.mod' part
    n = int(len(atmlist)) # calculates nr. of elements and converts string to integer
    
    for i in range(0, n, 1): # iterates for each element(.mod file) of the list    
        oldpath = atmlist[i]
        fullatmname = oldpath[-28:]
        name = fullatmname[0:24]
        newpath = '/home/asttchir/modelatm/'+str(name)+'.moog'
        os.system("gnome-terminal -e 'bash -c \"awk -f mod2moog %s > %s\"'" % (oldpath, newpath))

# /home/asttchir/Dropbox/Python/converter.py
