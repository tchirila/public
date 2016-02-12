# make a text list of files, not good for indendation using iphyton
import os
import os.path

atmlist = []
path = "/scratch/asttchir/modelatm"
for path, dirnames, filenames in os.walk(path):
    for file in [f for f in filenames if f.endswith(".moog")]:
        file = os.path.join(path, file)
        atmlist.append(file)        
outfile = open('atmlist.txt','w')
for name in atmlist:    
    outfile.write(name+'\n')    
outfile.close()

# /home/asttchir/Dropbox/Python/atmlist.py
