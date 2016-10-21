import numpy
import math
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
import lab

def fit_function(x, a, b, c, d):
	return b*(numpy.exp((x+d)/a)-1) + (V+d)/c
    
FileName='/home/federico/Documenti/Laboratorio2/diodo/dati_arduino/datiResistenza.txt'
V, I, dV, dI = pylab.loadtxt(FileName, unpack="True")


pylab.title("Curva corrente tensione")
pylab.xlabel("V (V)")
pylab.ylabel("I (A)") 
pylab.grid(color = "gray")
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, "o", color="black")


initial = numpy.array([0.048, 30e-10, 0.98, 1.5])
error = dI+dV/100 
popt, pcov = curve_fit(fit_function, V, I, initial, error)
a, b, c, d = popt
print(a, b, c, d)
print(pcov)

div = 249
bucket = numpy.array([0.0 for i in range(div)])
funzione = numpy.array([0.0 for i in range(div)])
inc = (V.max()-V.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + V.min()

pylab.plot(bucket, fit_function(bucket, a, b, c, d), color = "red")

#calcolo il chi quadro
chisq = (((I - fit_function(V, a, b, c, d))/error)**2).sum()
ndof = len(V) - 2
p=1.0-scipy.stats.chi2.cdf(chisq, len(V)-3)
print("Carica Chisquare/ndof = %f/%d" % (chisq, ndof))
print("p = ", p)


pylab.show()

