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

INPUT = "/home/federico/Laboratorio3/relazione6/datiGuadagno.txt"
OUTPUT = "/home/federico/Laboratorio3/relazione6/datiGuadagnoEstesi.txt"

file = open(OUTPUT,"w")

Vin, dVin, Vout, dVout = pylab.loadtxt(INPUT, unpack=True)

#Nelle visualizzazioni devo introdurre gli errori

V_IN = unumpy.uarray(Vin, dVin)
V_OUT = unumpy.uarray(Vout, dVout)

A_V = -V_OUT/V_IN

pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)
pylab.title('V_OUT vs V_IN', fontsize = "16")
pylab.xlabel('V_IN (V)', size = "14")
pylab.ylabel('V_OUT (V)', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(unumpy.nominal_values(V_IN), unumpy.nominal_values(V_OUT), 
	unumpy.std_devs(V_OUT), unumpy.std_devs(V_IN), "o", color="black")


for i in range(len(V_IN)):
	file.write(str(Vin[i]))
	file.write("\t")
	file.write(str(dVin[i]))
	file.write("\t")
	file.write(str(Vout[i]))
	file.write("\t")
	file.write(str(dVout[i]))
	file.write("\t")
	file.write(str(unumpy.nominal_values(A_V)[i]))
	file.write("\t")
	file.write(str(unumpy.std_devs(A_V)[i]))
	file.write("\n")

file.close()

#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
error = ((unumpy.std_devs(V_OUT))**2.0+(1.0*unumpy.std_devs(V_IN))**2.0)**0.5
#error = unumpy.std_devs(I_D)
init = numpy.array([2.0, 0.0])
#Errori tutti statistici
par, cov = curve_fit(linear, unumpy.nominal_values(V_IN), unumpy.nominal_values(V_OUT), init, error, absolute_sigma = "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo co capisco il chi quadro, non cambia nulla se cambio da true a false
a = par[0]
b = par[1]

chisq = ((unumpy.nominal_values(V_OUT)-linear(unumpy.nominal_values(V_IN), a, b))/error)**2
somma = sum(chisq)
ndof = len(unumpy.nominal_values(V_OUT)) - 2 #Tolgo due parametri estratti dal fit
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

pylab.savefig("plotGuadagno.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)

pylab.show()
