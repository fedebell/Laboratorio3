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

def linear(x, a, b):
	return a*x+b


VCC = ufloat(14.96, 0.005*14.96)
VEE = ufloat(14.96, 0.005*14.96)

#amplificatore di carica
Vmeno = ufloat(200, 4)/1000
CT = ufloat(1.01, 1.01*0.04)
CF = ufloat(1.02, 1.02*0.04)
C1 = ufloat(21.9, 21.9*0.04)
R3 = ufloat(97.8, ((0.008*97.8)**2+0.1**2)**0.5)
R2 = ufloat(99.9, ((0.008*99.9)**2+0.1**2)**0.5)
R1 = ufloat(98.3, ((0.008*98.3)**2+0.1**2)**0.5)

INPUT = "/home/federico/Laboratorio3/relazione7/datiTruccati.txt"


n, Vs, dVs, Tatt, dTatt, Tmis, dTmis = pylab.loadtxt(INPUT, unpack=True)


#Nelle visualizzazioni devo introdurre gli errori
print(dVs, 0.03*Vs)
VS = unumpy.uarray(Vs, dVs)
TMIS = unumpy.uarray(Tmis, dTmis)
deltaT = TMIS
logVS = unumpy.log(VS)

pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)
pylab.title('$\Delta t$ vs $log(V_{S})$', fontsize = "16")
pylab.ylabel('$\Delta t$ ($\mu s$)', size = "14")
pylab.xlabel('$ log(V_S/1V)$', size = "14")
pylab.xlim(0.0, 2.5)
pylab.ylim(130, 450)
pylab.grid(color = "gray")
pylab.errorbar(unumpy.nominal_values(logVS), unumpy.nominal_values(deltaT), 
	unumpy.std_devs(deltaT), unumpy.std_devs(logVS), "o", color="black")


#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
error = ((unumpy.std_devs(logVS))**2.0+(1.0*unumpy.std_devs(deltaT))**2.0)**0.5
#error = unumpy.std_devs(I_D)
init = numpy.array([2.0, 0.0])
#Errori tutti statistici
par, cov = curve_fit(linear, unumpy.nominal_values(logVS), unumpy.nominal_values(deltaT), init, error, absolute_sigma = "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo co capisco il chi quadro, non cambia nulla se cambio da true a false
a = par[0]
b = par[1]

chisq = ((unumpy.nominal_values(deltaT)-linear(unumpy.nominal_values(logVS), a, b))/error)**2
somma = sum(chisq)
ndof = len(unumpy.nominal_values(deltaT)) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (3.00)/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + 0.0
        retta[i] = linear(bucket[i], par[0], par[1])


pylab.plot(bucket, retta, color = "red")

pylab.savefig("plot.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)

pylab.show()

