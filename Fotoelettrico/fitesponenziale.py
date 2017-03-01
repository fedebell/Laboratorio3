#import uncertainties
#from uncertainties import ufloat
import math
import numpy
import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
import uncertainties 
from uncertainties import ufloat, unumpy

f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiArancio.txt", unpack = True)

def ff(x, a, I, V):
    return I*(numpy.exp(a*(V-x))-1)


#faccio il fit (parametri in V*s ma verosimil, mente ho le frequenze in 10**13 Hz...)
popt = (.1, -2.0, 300.0) #V e il valore di azzeramento della corrente (circa h/e*f? vedi a occhio cmq), I e la corrente asinotitica(la vedi a occhio), a??
pars, cov = curve_fit(ff, V, I, popt, dI,)
print ('a', pars[0], '\pm', cov[0][0]**0.5)
print('Corrente asintotica', pars[1], '\pm', cov[1][1]**0.5)
print ('V azzeramento', pars[2],'\pm', cov[2][2]**0.5)
print("covarianza=", cov[0][1])
print("covarianza=", cov[0][2])
print("covarianza=", cov[1][2])

#ua = ufloat(pars[0], cov[0][0]**0.5)
#uI = ufloat(pars[1], cov[1][1]**0.5)
#uV = ufloat(pars[2], cov[2][2]**0.5)
(ua, uI, uV) = uncertainties.correlated_values(pars, cov)

#Marco
#chi2(per ora implemento solo errore sulle y)
w=1/dI**2
chi2 = (w*(ff(V, pars[0], pars[1], pars[2]) - I)**2).sum()
ndof = len(f)-3
print('chi2  =', chi2)
print('ndof = ', ndof)

#Marco
#calcolo Potenziale di frenamento; errore messo a caso in pratica: bella discussione da fare
#print("deltaI = ", cov[1][1]**0.5)
deltaI = 0.02
v0 = uV+(1/ua)*unumpy.log(uI/deltaI)

print('V_0=', v0)

div = 1000
bucket = numpy.array([0.0 for i in range(div)])
linea = numpy.array([0.0 for i in range(div)])
inc = (V.max()-V.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + V.min()
        linea[i] = ff(bucket[i], pars[0], pars[1], pars[2])


#plot
pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)
pylab.title("Corrente vs Tensione")
pylab.xlabel("V (mV)", size = "14")
pylab.ylabel("I (nA)", size = "14")
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '')
pylab.plot(bucket, linea, color = "red")

pylab.show()
