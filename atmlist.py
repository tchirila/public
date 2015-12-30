#make a text list of files
import os

atmlist = []
path = "scratch//asttchir//apogee//apogeework//apogee//spectro//redux//speclib//kurucz_filled"
for file in os.listdir(path):
    if file.endswith(".mod"):
        atmlist.append(file)
outfile = open('atmlist.txt','w')
for name in atmlist:
    outfile.write(name+'\n')
outfile.close()
