# writes the filename into a parameter file
path = "D:\\Program Files\\Dropbox\\Python\\atmlist.txt"
path2 = "D:\\Program Files\\Dropbox\\Python\\m4500m075_Si+025.par"

with open(path) as atmfile:
    atmdata = atmfile.read()
    atmlist = atmdata.split() # each .mod name has 28 characters including the '.mod' part
    n = int(len(atmlist)) # calculates nr. of elements and converts string to integer

    for i in range(0, n, 1): # iterates for each element(.mod file) of the list
        atmpath = atmlist[i]
        modelatm = atmpath[-28:]
        param = modelatm[0:24]
        t = modelatm[14:18]
        g = 'g'+modelatm[19:21]
        m = 'm'+modelatm[2:5]

        with open(path2, 'r') as template, open(param+'_Al.par', 'w') as paramfile:
            for line in template:
                if line.strip() == 'standard_out   out1_s4500g20m075_sip025': 
                    paramfile.write('standard_out   out1_s'+t+g+m+'_al'+'\n')
                elif line.strip() == 'summary_out    out2_s4500g20m075_sip025': 
                    paramfile.write('summary_out    out2_s'+t+g+m+'_al'+'\n') 
                elif line.strip() == 'iraf_out       s4500g20m075_sip025.txt': 
                    paramfile.write('iraf_out       s'+t+g+m+'_al.txt'+'\n')
                elif line.strip() == "model_in      'amm08cp00op00t4500g20v20.moog'":
                    paramfile.write('model_in      '+"'"+atmpath+"'"+'\n')
                else:
                    paramfile.write(line)
