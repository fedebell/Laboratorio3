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
import numpy as np
from scipy.signal import argrelextrema

def linear(x, a, b):
    return a*x+b


lamb, dlamb, alpha, dalpha = pylab.loadtxt('/home/federico/Laboratorio3/Ottica1/cadmio.txt', unpack=True)


l=1/lamb
dl = l*dlamb/lamb

L = unumpy.uarray(l, dl)
A = unumpy.uarray(alpha, dalpha)

pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)

#pylab.xlim([1, 4.5])
#pylab.ylim([10, 90])
pylab.title('Lampada al cadmio', fontsize = "16")

pylab.xlabel("1/lambda (1/nm)", size = "14")
pylab.ylabel("alpha (gradi)", size = "14")
pylab.grid(color = "gray")
pylab.errorbar(l, alpha, dalpha, dl, "o", color="black")


#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
a = 1.0
b = 1.0
#Contollare unit di misura
error = pylab.sqrt(dalpha**2+(a*dl)**2)
init = numpy.array([a, b])
par, cov = curve_fit(linear, l, alpha, init, error, "true")
#trattazione statistica degli errori
print(par, cov)

a = par[0]
b = par[1]

chisq = (((alpha-linear(l, a, b))/error)**2)
somma = sum(chisq)
ndof = len(l) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (l.max()-l.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + l.min()
        retta[i] = linear(bucket[i], par[0], par[1])
pylab.plot(bucket, retta, color = "red")

a = ufloat(a, cov[0][0]**0.5)
b = ufloat(b, cov[1][1]**0.5)

print("Si ricavano dai parametti i seguenti due valori di a = ", a, "e di b =",  b)

sodio = 142.5+0.0833
sodiol = (sodio-b)/a
print("sodio = " + str(1/sodiol))

pylab.show()
