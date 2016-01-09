# make a text list of files, not good for indendation using iphyton, does not work in python2.7
import os
import os.path

atmlist = []
path = "/scratch/asttchir/apogee/apogeework/apogee/spectro/redux/speclib/kurucz_filled"
for path, dirnames, filenames in os.walk(path):
    for file in [f for f in filenames if f.endswith(".mod")]:
        file = os.path.join(path, file)
        atmlist.append(file)        
outfile = open('atmlist.txt','w')
for name in atmlist:    
    outfile.write(name+'\n')    
outfile.close()


# it's the same code but formatted for correct indentation in ipython when copy+pasting it there
import os
import os.path

atmlist = []
path = "/scratch/asttchir/apogee/apogeework/apogee/spectro/redux/speclib/kurucz_filled"
for path, dirnames, filenames in os.walk(path):
    
    for file in [f for f in filenames if f.endswith(".mod")]:
        
        file = os.path.join(path, file)
        atmlist.append(file)        

outfile = open('atmlist.txt','w')
for name in atmlist:    

    outfile.write(name+'\n')    

outfile.close()
