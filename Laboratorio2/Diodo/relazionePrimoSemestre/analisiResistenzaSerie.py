import numpy
import math
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
import lab

def fit_function(x, a, b, c, d):
	return a*(numpy.log(x/b + 1)) + c*I + d

FileName='/home/federico/Documenti/Laboratorio2/diodo/dati_arduino/datiResistenza.txt'
V, I, dV, dI = pylab.loadtxt(FileName, unpack="True")


pylab.title("Curva corrente tensione")
pylab.xlabel("I (A)")
pylab.ylabel("V (V)") 
pylab.grid(color = "gray")
pylab.grid(color = "gray")
pylab.errorbar(I, V, dV, dI, "o", color="black")


initial = numpy.array([0.048, 30e-10, 250, 0.0])
error = dV+dI/10
popt, pcov = curve_fit(fit_function, I, V, initial, error)
#a, b, c, d = popt
a, b, c, d = initial
print(a, b, c, d)


div = 249
bucket = numpy.array([0.0 for i in range(div)])
funzione = numpy.array([0.0 for i in range(div)])
inc = (0.40-I.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + I.min()

pylab.plot(bucket, fit_function(bucket, a, b, c, d), color = "red")

#calcolo il chi quadro
chisq = (((I - fit_function(I, a, b, c, d))/error)**2).sum()
ndof = len(I) - 2
p=1.0-scipy.stats.chi2.cdf(chisq, len(I)-4)
print("Carica Chisquare/ndof = %f/%d" % (chisq, ndof))
print("p = ", p)


pylab.show()

#da finire insomma visualizzare correttamente.
#cmq questo è il modello che funziona, cioè il modello corretto come detto è quello di una resistenza in serie l'altro modello invece non fitta assolutamente
#bene ed è quello di resistenza in parallelo




