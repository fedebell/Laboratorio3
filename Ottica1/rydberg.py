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

n1, n2, alpha0, dalpha0, alpha1, dalpha1 = pylab.loadtxt('Users\Lisa\Desktop\Lab3\rydberg.txt', unpack=True)

thetai=(180-alpha0)*0.5
dthetai= (dalpha0/alpha0)*thetai
thetad = 180-alpha1-thetai
dthetad = dalpha1+dthetai
#inserire passo reticolare
d=
dd=

lamb= (1/n1)*d*(pylab.sin(thetai)-pylab.sin(thetad))
dlamb = lamb*((dd/d)+(dthetai/thetai)+(dthetad/thetad))

l=1/lamb
dl = l*dlamb/lamb
n= (1/(n1)**2)-(1/(n2)**2)
dn = ?

L = unumpy.uarray(l, dl)

pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)

pylab.xlim([1, 4.5])
pylab.ylim([10, 90])
pylab.title('Lampada al cadmio', fontsize = "16")

pylab.ylabel('$1/\lambda [microm^-1]$', size = "14")

pylab.xlabel('$(1/(n1)**2)-(1/(n2)**2)$', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(l, alpha, dalpha, dl, "o", color="black")


#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
a = 1.0
b = 1.0
#Contollare unit di misura
error = pylab.sqrt(dl**2+(a*dn)**2)
init = numpy.array([a, b])
par, cov = curve_fit(linear, n, l, init, error, "true")
#trattazione statistica degli errori
print(par, cov)

a = par[0]
b = par[1]
chisq = (((alpha-linear(n, a, b))/error)**2)
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

print("Si ricavano dai parametti i seguenti due valori di a = ", a, "e di b =",  b)

pylab.show()
