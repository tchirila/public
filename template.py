# Writes the template parameter file
with open('template_Al.par', 'w') as par:            
    par.write('synth\n'
              'terminal       xterm\n'
              'plot           0\n'
              'standard_out   out1_standard\n'
              'summary_out    out1_synthraw\n'
              'iraf_out       iraf.txt\n'
              'damping        0\n'
              'strong         1\n'
              "stronglines_in   '../stronglines.vac'\n" # change
              "model_in      'model.mod'\n"
              "lines_in      '../linelist.201306191000.vac.moog'\n" # change
              'atmosphere     1\n'
              'molecules      1\n'
              'lines          0\n'
              'iraf           1\n'
              'flux/int       0\n'
              'isotopes   17     1\n'
              'abundances     1     2\n' # change to nr. of abundances
              '  13       -1.20   -0.90\n' # add Al abundances
              'synlimits\n'
              '15000.0     17000.0     0.10     0.30\n'
              'obspectrum     0\n'
              'plotpars      1\n'
              '  15100.0  17000.0   0.40    1.02\n'
              '   0       0.000   0.000    1.0000\n'
              '   g       0.800    0.0     0.0     0.0     0.0\n')
    par.close()

# /home/asttchir/Dropbox/Python/template.py
