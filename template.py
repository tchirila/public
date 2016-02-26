# Writes the template parameter file
with open('/home/asttchir/specwork/template_Al.par', 'w') as par:            
    par.write('synth\n'
              'terminal       xterm\n'
              'plot           0\n'
              'standard_out   out1_standard\n'
              'summary_out    out1_synthraw\n'
              'iraf_out       iraf.txt\n'
              'damping        0\n'
              'strong         1\n'
              "stronglines_in   '/home/asttchir/specwork/stronglines.vac'\n"
              "model_in      'model.mod'\n"
              "lines_in      '/home/asttchir/specwork/moog.201312161124.vac'\n"
              'atmosphere     1\n'
              'molecules      1\n'
              'lines          0\n'
              'iraf           1\n'
              'flux/int       0\n'
              'isotopes   17     1\n'
              'abundances     1     1\n'
              '  13       -1.20\n'
              'synlimits\n'
              '16700.0     16800.0     0.10     0.30\n'
              'obspectrum     0\n'
              'plotpars      1\n'
              '  16700.0  16800.0   0.40    1.02\n'
              '   0       0.000   0.000    1.0000\n'
              '   g       0.800    0.0     0.0     0.0     0.0\n')
    par.close()

# /home/asttchir/Dropbox/Python/template.py
