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

def ff(x, a, b):
    return (a*x+b)**2

bucket = numpy.linspace(0,2700, 1000)

#ARANCIO
f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiAranciocut.txt", unpack = True)

#stimo a occhio la corrente anodica dal grafico
I_a = -1.8
#faccio il fit (parametri in V*s ma verosimil, mente ho le frequenze in 10**13 Hz...)
popt = (5, 20)
pars, cov = curve_fit(ff, V, I-I_a, popt, dI,  absolute_sigma = "true")

#plot
x1 = plt.subplot(321)

pylab.xlabel("V (mV)", size = "14")
pylab.ylabel("I (nA)", size = "14")
pylab.xlim(0, 1000)
pylab.ylim(min(I-10),max(I)+10)
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '', label = "Arancio")
pylab.legend(loc = "upper-right")
pylab.plot(bucket, ff(bucket, pars[0], pars[1])+I_a, color = "red")

#GIALLO
f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiGiallicut.txt", unpack = True)

#stimo a occhio la corrente anodica dal grafico
I_a = -2.27
#faccio il fit (parametri in V*s ma verosimil, mente ho le frequenze in 10**13 Hz...)
popt = (5, 20)
pars, cov = curve_fit(ff, V, I-I_a, popt, dI,  absolute_sigma = "true")

#plot
x2 = plt.subplot(322)

pylab.xlabel("V (mV)", size = "14")
pylab.ylabel("I (nA)", size = "14")
pylab.xlim(0, 1000)
pylab.ylim(min(I-10),max(I)+10)
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '', label = "Giallo")
pylab.legend(loc = "upper-right")
pylab.plot(bucket, ff(bucket, pars[0], pars[1])+I_a, color = "red")

#VERDE
f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiVerdicut.txt", unpack = True)

#stimo a occhio la corrente anodica dal grafico
I_a = -2.11
#faccio il fit (parametri in V*s ma verosimil, mente ho le frequenze in 10**13 Hz...)
popt = (5, 20)
pars, cov = curve_fit(ff, V, I-I_a, popt, dI,  absolute_sigma = "true")
#plot
x3 = plt.subplot(323)

pylab.xlabel("V (mV)", size = "14")
pylab.ylabel("I (nA)", size = "14")
pylab.xlim(0, 1000)
pylab.ylim(min(I-10),max(I)+10)
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '', label = "Verde")
pylab.legend(loc = "upper-right")
pylab.plot(bucket, ff(bucket, pars[0], pars[1])+I_a, color = "red")

#VERDE-AZZURRO
f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiVerdeAzzurrocut.txt", unpack = True)

#stimo a occhio la corrente anodica dal grafico
I_a = -1.488
#faccio il fit (parametri in V*s ma verosimil, mente ho le frequenze in 10**13 Hz...)
popt = (5, 20)
pars, cov = curve_fit(ff, V, I-I_a, popt, dI,  absolute_sigma = "true")

#plot
x4 = plt.subplot(324)

pylab.xlabel("V (mV)", size = "14")
pylab.ylabel("I (nA)", size = "14")
pylab.xlim(0, 1000)
pylab.ylim(min(I-10),max(I)+10)
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '', label = "Verde-Azzurro")
pylab.plot(bucket, ff(bucket, pars[0], pars[1])+I_a, color = "red")
pylab.legend(loc = "upper-right")
#AZZURRO

f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiAzzurrocut.txt", unpack = True)

#stimo a occhio la corrente anodica dal grafico
I_a = -2.30
#faccio il fit (parametri in V*s ma verosimil, mente ho le frequenze in 10**13 Hz...)
popt = (5, 20)
pars, cov = curve_fit(ff, V, I-I_a, popt, dI,  absolute_sigma = "true")

#plot
x5 = plt.subplot(325)

pylab.xlabel("V (mV)", size = "14")
pylab.ylabel("I (nA)", size = "14")
pylab.xlim(0, 1000)
pylab.ylim(min(I-10),max(I)+10)
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '', label = "Azzurro")
pylab.legend(loc = "upper-right")
pylab.plot(bucket, ff(bucket, pars[0], pars[1])+I_a, color = "red")

#BLU
f, V, dV, I, dI = pylab.loadtxt("C:\\Users\\marco\\Desktop\\Laboratorio3\\Fotoelettrico\\datiBlucut.txt", unpack = True)

#stimo a occhio la corrente anodica dal grafico
I_a = -0.265
#faccio il fit (parametri in V*s ma verosimil, mente ho le frequenze in 10**13 Hz...)
popt = (5, 20)
pars, cov = curve_fit(ff, V, I-I_a, popt, dI,  absolute_sigma = "true")

#plot
x6 = plt.subplot(326)

pylab.xlabel("V (mV)", size = "14")
pylab.ylabel("I (nA)", size = "14")
pylab.xlim(0, 1000)
pylab.ylim(min(I-10),max(I)+10)
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, color = 'blue', marker = 'o', linestyle = '', label = "Blu")
pylab.legend(loc = "upper-right")
pylab.plot(bucket, ff(bucket, pars[0], pars[1])+I_a, color = "red")

plt.suptitle('Corrente vs Potenziale di frenamento: fit parabolico', size = 18)


pylab.show()