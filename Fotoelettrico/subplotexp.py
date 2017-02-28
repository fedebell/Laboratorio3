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
import matplotlib.pyplot as plt

def ff(x, a, I, V):
    return I*(numpy.exp(a*(V-x))-1)

bucket = numpy.linspace(0,2700, 1000)

#ARANCIO
f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiArancio.txt", unpack = True)

popt = (.1, -2.0, 300.0)  
pars, cov = curve_fit(ff, V, I, popt, dI,  absolute_sigma = "true")

#plot
x1 = plt.subplot(321)

pylab.xlabel("V (mV)", size = "14")
pylab.ylabel("I (nA)", size = "14")
pylab.xlim(0, 2700)
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '', label = "Arancio")
pylab.legend(loc = "upper-right")
pylab.plot(bucket, ff(bucket, pars[0], pars[1], pars[2]), color = "red")

#GIALLO
f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiGialli.txt", unpack = True)

popt = (.1, -2.0, 300.0)  
pars, cov = curve_fit(ff, V, I, popt, dI,  absolute_sigma = "true")

#plot
x2 = plt.subplot(322)

pylab.xlabel("V (mV)", size = "14")
pylab.ylabel("I (nA)", size = "14")
pylab.xlim(0, 2700)
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '', label = "Giallo")
pylab.legend(loc = "upper-right")
pylab.plot(bucket, ff(bucket, pars[0], pars[1], pars[2]), color = "red")

#VERDE
f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiVerdi.txt", unpack = True)

popt = (.1, -2.0, 300.0)  
pars, cov = curve_fit(ff, V, I, popt, dI,  absolute_sigma = "true")

#plot
x3 = plt.subplot(323)

pylab.xlabel("V (mV)", size = "14")
pylab.ylabel("I (nA)", size = "14")
pylab.xlim(0, 2700)
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '', label = "Verde")
pylab.legend(loc = "upper-right")
pylab.plot(bucket, ff(bucket, pars[0], pars[1], pars[2]), color = "red")

#VERDE-AZZURRO
f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiVerdeAzzurro.txt", unpack = True)

popt = (.1, -2.0, 300.0)  
pars, cov = curve_fit(ff, V, I, popt, dI,  absolute_sigma = "true")

#plot
x4 = plt.subplot(324)

pylab.xlabel("V (mV)", size = "14")
pylab.ylabel("I (nA)", size = "14")
pylab.xlim(0, 2700)
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '', label = "Verde-Azzurro")
pylab.plot(bucket, ff(bucket, pars[0], pars[1], pars[2]), color = "red")
pylab.legend(loc = "upper-right")
#AZZURRO

f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiAzzurro.txt", unpack = True)

popt = (.1, -2.0, 300.0)  
pars, cov = curve_fit(ff, V, I, popt, dI,  absolute_sigma = "true")

#plot
x5 = plt.subplot(325)

pylab.xlabel("V (mV)", size = "14")
pylab.ylabel("I (nA)", size = "14")
pylab.xlim(0, 2700)
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '', label = "Azzurro")
pylab.legend(loc = "upper-right")
pylab.plot(bucket, ff(bucket, pars[0], pars[1], pars[2]), color = "red")

#BLU
f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiBlu.txt", unpack = True)

popt = (.1, -2.0, 300.0)  
pars, cov = curve_fit(ff, V, I, popt, dI,  absolute_sigma = "true")

#plot
x6 = plt.subplot(326)

pylab.xlabel("V (mV)", size = "14")
pylab.ylabel("I (nA)", size = "14")
pylab.xlim(0, 2700)
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '', label = "Blu")
pylab.legend(loc = "upper-right")
pylab.plot(bucket, ff(bucket, pars[0], pars[1], pars[2]), color = "red")

plt.suptitle('Corrente vs Potenziale di frenamento: fit esponenziale', size = 18)


pylab.show()