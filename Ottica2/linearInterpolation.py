from uncertainties import umath
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

n, l, dl = pylab.loadtxt('/home/federico/Laboratorio3/Ottica2/interferenza.txt', unpack=True)
dn = numpy.array([0.0 for i in range(len(n))])

medio = ufloat(6.5, 0.1)
L = unumpy.uarray(l, dl) - medio
print(L)
N = unumpy.uarray(n, dn)
d = ufloat(1.00, 0.005)


#FIXME: Inserire la lunghezza del tubo
D = ufloat(201, 1)

ipotenuse = (L*L + D*D)**0.5
print(ipotenuse)
seni = D/ipotenuse
print(seni)

pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)
#FIXME: Fix the title

pylab.title('Massimi dell\'interefenza su reticolo', fontsize = "16")
#How to determine the unity of measure
pylab.xlabel('Ordine $m$', size = "14")
#FIXME Unita' di misura
pylab.ylabel('Seno angolo di incidenza', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(n, unumpy.nominal_values(seni), unumpy.std_devs(seni), 0, "o", color="black")


#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
a = 1.0
b = 1.0
#Contollare unit di misura
error = unumpy.std_devs(seni)
init = numpy.array([a, b])
#FIXME: Controllare che l'ordine sia giusto'
par, cov = curve_fit(linear, n, unumpy.nominal_values(seni), init, error, "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo non capisco il chi quadro, non cambia nulla se cambio da true a false
a = par[0]
b = par[1]
chisq = (((unumpy.nominal_values(seni)-linear(n, a, b))/error)**2)
somma = sum(chisq)
ndof = len(N) - 2 #Tolgo due parametri estratti dal fit
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

lunghezza = -a*d*10**6

print("La lunghezza d'onda risulta essere: " + str(lunghezza))
pylab.show()

