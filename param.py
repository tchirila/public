# writes the filename into a parameter file, run in paramfiles
path = "/scratch/asttchir/specwork/atmlist.txt"
path2 = "/scratch/asttchir/specwork/template_Al.par"

with open(path) as atmfile:
    atmdata = atmfile.read()
    atmlist = atmdata.split() # each .moog name has 29 characters including the '.mod' part
    n = int(len(atmlist)) # calculates nr. of elements and converts string to integer
 
    for i in range(0, n, 1): # iterates for each element(.moog file) of the list    
        atmpath = atmlist[i]
        modelatm = atmpath[-29:]
        param = modelatm[0:24]
        t = modelatm[14:18]
        g = 'g'+modelatm[19:21]
        m = 'm'+modelatm[2:5]

        with open(path2, 'r') as template:
            with open(param+'_Al.par', 'w') as paramfile:
                for line in template:                
                    if line.strip() == 'iraf_out       iraf.txt': 
                        paramfile.write('iraf_out       s'+t+g+m+'_al.txt'+'\n')
                    elif line.strip() == "model_in      'model.mod'":
                        paramfile.write('model_in      '+"'"+atmpath+"'"+'\n')
                    elif line.strip() == 'isotopes   17     1':
                        if float(modelatm[19:21]) <= 3.5: # for Arcturus values
                            paramfile.write('isotopes   17     1\n'
                                            '  108.00116       1.001\n'
                                            '  606.01212       1.01\n'
                                            '  606.01213       90\n'
                                            '  606.01313       180\n'
                                            '  607.01214       1.01\n'
                                            '  607.01314       90\n'
                                            '  607.01215       273\n'
                                            '  608.01216       1.01\n'
                                            '  608.01316       90\n'
                                            '  608.01217       1101\n'
                                            '  608.01218       551\n'
                                            '  114.00128       1.011\n'
                                            '  114.00129       20\n'
                                            '  114.00130       30\n'
                                            '  101.00101       1.001\n'
                                            '  101.00102       1000\n'
                                            '  126.00156       1.00\n')
                        elif float(modelatm[19:21]) >= 4.0: # for Solar values
                            paramfile.write('isotopes   17     1\n'
                                            '  108.00116       1.001\n'
                                            '  606.01212       0.91\n'
                                            '  606.01213       8\n'
                                            '  606.01313       81\n'
                                            '  607.01214       0.91\n'
                                            '  607.01314       8\n'
                                            '  607.01215       273\n'
                                            '  608.01216       0.91\n'
                                            '  608.01316       8\n'
                                            '  608.01217       1101\n'
                                            '  608.01218       551\n'
                                            '  114.00128       1.011\n'
                                            '  114.00129       20\n'
                                            '  114.00130       30\n'
                                            '  101.00101       1.001\n'
                                            '  101.00102       1000\n'
                                            '  126.00156       1.00\n')
                    else:
                        paramfile.write(line)
            paramfile.close()

# /home/asttchir/Dropbox/Python/param.py
