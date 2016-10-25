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

INPUT = "/home/federico/Laboratorio3/relazione4/datiBodeToFit.txt"
OUTPUT = "/home/federico/Laboratorio3/relazione4/datiBodeToFit.txt"

Vout, dVout, f, df = pylab.loadtxt(INPUT, unpack=True)

#Nelle visualizzazioni devo introdurre gli errori

F = unumpy.uarray(f, df)
VOUT = unumpy.uarray(Vout, dVout)
VOUT3 = unumpy.uarray(Vout, (dVout**2 + (0.03*Vout)**2))
VIN = ufloat(1.02, 0.02) 
VIN3 = ufloat(1.02, ((0.02)**2+(0.03*1.02)**2)**0.5)
#Per la visualizzazione inserisco il 3%
A = VOUT3/VIN3
dB = 20*unumpy.log10(A)
#Attento a unità di misura della frequenza
logF = unumpy.log10(F)

pylab.title('A vs logf')
pylab.xlabel('I_b (uA)')
pylab.ylabel('I_c (mA)')
pylab.grid(color = "gray")

pylab.errorbar(unumpy.nominal_values(logF), unumpy.nominal_values(dB), 
	unumpy.std_devs(dB), unumpy.std_devs(logF), "o", color="black")


#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
error = pylab.sqrt((unumpy.std_devs(dB))**2 + 20.0*(unumpy.std_devs(logF))**2)
init = numpy.array([0.0, 0.0])
par, cov = curve_fit(linear, unumpy.nominal_value(logF), unumpy.nominal_value(dB), init, error, "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo co capisco il chi quadro, non cambia nulla se cambio da true a false
a = par[0]
b = par[1]

chisq = ((dB-linear(logF, a, b))/error)**2
somma = sum(chisq)
ndof = len(logF) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (unumpy.nominal_value(logF).max()-unumpy.nominal_value(logF).min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + unumpy.nominal_value(logF).min()
        retta[i] = linear(bucket[i], par[0], par[1])


pylab.plot(bucket, retta, color = "red")

pylab.show()


