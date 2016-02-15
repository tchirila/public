# writes the filename into a parameter file, run in paramfiles
path = "/scratch/asttchir/specwork/atmlist.txt"
temppath = "/scratch/asttchir/specwork/template_Al.par"
alabun = ['_Al_m00', '_Al_p15']
parampath = '/scratch/asttchir/paramfiles/'

with open(path) as atmfile:
    atmdata = atmfile.read()
    atmlist = atmdata.split() # each .moog name has 29 characters including the '.moog' part
    n = int(len(atmlist)) # calculates nr. of elements and converts string to integer
 
    for i in range(0, n, 1): # iterates for each element(.moog file) of the list    
        atmpath = atmlist[i]
        modelatm = atmpath[-29:]
        param = modelatm[0:24]
        t = modelatm[14:18]
        g = 'g'+modelatm[19:21]
        m = 'm'+modelatm[2:5]

        for j in range(0, 2, 1): #iterates twice so it creates 2 seperate param files
            with open(temppath, 'r') as template:
                with open(parampath+param+alabun[j]+'.par', 'w') as paramfile:
                    for line in template:                
                        if line.strip() == 'iraf_out       iraf.txt': 
                            paramfile.write('iraf_out       s'+t+g+m+alabun[j]+'.txt\n')
                        elif line.strip() == "model_in      'model.mod'":
                            paramfile.write('model_in      '+"'"+atmpath+"'"+'\n')
                        elif line.strip() == 'isotopes   17     1':
                            if float(modelatm[19:21]) <= 3.5: # for Arcturus values
                                paramfile.write('isotopes   17     5\n'
                                                '  108.00116       1.001 1.001 1.001 1.001 1.001\n'
                                                '  606.01212       1.01  1.01  1.01  1.01  1.01\n'
                                                '  606.01213       90    90    90    90    90\n'
                                                '  606.01313       180   180   180   180   180\n'
                                                '  607.01214       1.01  1.01  1.01  1.01  1.01\n'
                                                '  607.01314       90    90    90    90    90\n'
                                                '  607.01215       273   273   273   273   273\n'
                                                '  608.01216       1.01  1.01  1.01  1.01  1.01\n'
                                                '  608.01316       90    90    90    90    90\n'
                                                '  608.01217       1101  1101  1101  1101  1101\n'
                                                '  608.01218       551   551   551   551   551\n'
                                                '  114.00128       1.011 1.011 1.011 1.011 1.011\n'
                                                '  114.00129       20    20    20    20    20\n'
                                                '  114.00130       30    30    30    30    30\n'
                                                '  101.00101       1.001 1.001 1.001 1.001 1.001\n'
                                                '  101.00102       1000  1000  1000  1000  1000\n'
                                                '  126.00156       1.00  1.00  1.00  1.00  1.00\n')
                            elif float(modelatm[19:21]) >= 4.0: # for Solar values
                                paramfile.write('isotopes   17     5     5     5     5     5\n'
                                                '  108.00116       1.001 1.001 1.001 1.001 1.001\n'
                                                '  606.01212       0.91  0.91  0.91  0.91  0.91\n'
                                                '  606.01213       8     8     8     8     8\n'
                                                '  606.01313       81    81    81    81    81\n'
                                                '  607.01214       0.91  0.91  0.91  0.91  0.91\n'
                                                '  607.01314       8     8     8     8     8\n'
                                                '  607.01215       273   273   273   273   273\n'
                                                '  608.01216       0.91  0.91  0.91  0.91  0.91\n'
                                                '  608.01316       8     8     8     8     8\n'
                                                '  608.01217       1101  1101  1101  1101  1101\n'
                                                '  608.01218       551   551   551   551   551\n'
                                                '  114.00128       1.011 1.011 1.011 1.011 1.011\n'
                                                '  114.00129       20    20    20    20    20\n'
                                                '  114.00130       30    30    30    30    30\n'
                                                '  101.00101       1.001 1.001 1.001 1.001 1.001\n'
                                                '  101.00102       1000  1000  1000  1000  1000\n'
                                                '  126.00156       1.00  1.00  1.00  1.00  1.00\n')
                        elif line.strip() == '13       -1.20   -0.90   -0.60   -0.30   0.00':
                            if j == 0:
                                paramfile.write('  13       -1.20   -0.90   -0.60   -0.30   0.00\n')
                            elif j == 1:
                                paramfile.write('  13       0.30   0.60   0.90   1.20   1.50\n')
                        else:
                            paramfile.write(line)
                paramfile.close()

# /home/asttchir/Dropbox/Python/param.py
