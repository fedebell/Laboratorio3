import uncertainties
from uncertainties import ufloat
import math
import numpy
import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
import uncertainties 
from uncertainties import unumpy

#apro il file
f, V, df, dV = pylab.loadtxt('', unpack = True)

def ff(x, a ,b):
    return a*x + b

#faccio il fit (parametri in V*s ma verosimil,mente ho le frequenze in 10**13 Hz...)
popt = (3.73*10**(-15), 0)
pars, cov = curve_fit(ff, f, V, popt, dV)
print ('h/e', pars[0],'\pm', cov[0][0]**0.5)
print ('Lavoro estrazione', pars[1],'\pm', cov[1][1]**0.5)
print('covarianza', cov[0][1])

#chi2(per ora implemento solo errore sulle y)
w=1/dV**2
chi2 = (w*(ff(f, pars[0], pars[1]) - V)**2).sum()
ndof = len(f)-2
print('chi2  =',chi2)
print('ndof = ',ndof)

#plot
pylab.title('Frequenza vs potenziale di frenamento')
pylab.xlabel('Frequenza (Hz)')
pylab.ylabel('$V_0$ (V)')
pylab.errorbar(f, V, dV, df, color = 'blue', marker = 'o', linestyle = '')
pylab.plot(f, ff(f, pars[0], pars[1]), linestyle = '-', color = 'black')

pylab.grid()
pylab.show()

