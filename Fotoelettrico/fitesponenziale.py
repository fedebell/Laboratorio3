import numpy
import pylab 
from scipy.optimize import curve_fit
#apro il file
f, V, I, dV, dI = pylab.loadtxt('', unpack = True)

def ff(x, a, I, V):
    return I*(numpy.exp(a(V-x))-1)
    
#faccio il fit (parametri in V*s ma verosimil,mente ho le frequenze in 10**13 Hz...)
popt = (, , ) #V è il valore di azzeramento della corrente (circa h/e*f? vedi a occhio cmq), I è la corrente asinotitica(la vedi a occhio), a??
pars, cov = curve_fit(ff, V, I, popt, dI)
print ('a', pars[0],'\pm', cov[0][0]**0.5)
print('Corrente asintotica', pars[1], '\pm', cov[1][1]**0.5)
print ('V azzeramento', pars[2],'\pm', cov[2][2]**0.5)

#chi2(per ora implemento solo errore sulle y)
w=1/dI**2
chi2 = (w*(ff(V, pars[0], pars[1], pars[2]) - I)**2).sum()
ndof = len(f)-3
print('chi2  =',chi2)
print('ndof = ',ndof)

#calcolo Potenziale di frenamento; errore messo a caso in pratica: bella discussione da fare
V0=pars[2]+1/pars[0]*numpy.log(pars[1]/cov[1][1]**0.5)
print('V_0=', v0, '\pm', cov[2][2]*0.5)
#plot
pylab.title('Potenziale vs corrente')
pylab.xlabel('V (V))')
pylab.ylabel('I (nA)')
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '')
pylab.plot(V, ff(V, pars[0], pars[1], pars[2]), linestyle = '-', color = 'black')

pylab.grid()
pylab.show()