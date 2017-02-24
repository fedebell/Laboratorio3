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
#Con tre punti si fa una interpolazione lineare?

e, de, n = pylab.loadtxt('/home/federico/Laboratorio3/FranckHertz/FranckHertzFit.txt', unpack=True)
dn = numpy.array([0.0 for i in range(len(n))])

E = unumpy.uarray(e, de)
N = unumpy.uarray(n, dn)

#FIXME: Inserire la lunghezza del tubo
L = ufloat(10.0, 0.1)

pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)
#FIXME: Fix the title
pylab.xlim([1, 4.5])
pylab.ylim([10, 90])
pylab.title('$U_A$ vs $n$', fontsize = "16")
#How to determine the unity of measure
pylab.xlabel('$n$', size = "14")
#FIXME Unita' di misura
pylab.ylabel('$U_A (V)$', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(n, e, de, dn, "o", color="black")


#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
a = 1.0
b = 1.0
#Contollare unit di misura
error = pylab.sqrt(de**2+(a*dn)**2)
init = numpy.array([a, b])
#FIXME: Controllare che l'ordine sia giusto'
par, cov = curve_fit(linear, n, e, init, error, "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo non capisco il chi quadro, non cambia nulla se cambio da true a false
a = par[0]
b = par[1]
chisq = (((e-linear(n, a, b))/error)**2)
somma = sum(chisq)
ndof = len(n) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (n.max()-n.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + n.min()
        retta[i] = linear(bucket[i], par[0], par[1])
pylab.plot(bucket, retta, color = "red")

a = ufloat(a, cov[0][0]**0.5)
b = ufloat(b, cov[1][1]**0.5)

#FIXME: To finish E(N) = (1+ l/L (2n+1))Ea
E_a = L*a/2
libmedio = 4*b/(L*a)-2
print("Si ricavano dai parametti i seguenti due valori di a = ", a, "e di b =",  b)

pylab.show()

