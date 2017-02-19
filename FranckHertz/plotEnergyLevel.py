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

def linear(x, b):
	return b

#Prendo in due file ognuno contenenti i valori di U_E e quelli dei relativi massimi e minimi.

INPUTMIN = "/home/federico/Laboratorio3/FranckHertz/MIN.txt"
INPUTMAX = "/home/federico/Laboratorio3/FranckHertz/MAX.txt"

#Continuare a inserire gli errori e plottare i grafici e i fit con uan costante
#Indicare sul grafico il miglior valore da cui si sceglie di eseguire il fit succesivo

#L'errore su ue si prende dalle manopoline

ue, due, min1, dmin1, min2, dmin2, min3, dmin3 = pylab.loadtxt(INPUTMIN, unpack=True)
ue, due, max1, dmax1, max2, dmax2, max3, dmax3 = pylab.loadtxt(INPUTMAX, unpack=True)

UE = unumpy.uarray(ue, due)
MIN1 = unumpy.uarray(min1, dmin1)
MIN2 = unumpy.uarray(min2, dmin2)
MIN3 = unumpy.uarray(min3, dmin3)

MAX1 = unumpy.uarray(max1, dmax1)
MAX2 = unumpy.uarray(max2, dmax2)
MAX3 = unumpy.uarray(max3, dmax3)


pylab.figure(num=1, figsize=(8, 5), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)
pylab.title('Minimi', fontsize = "16")
#How to determine the unity of measure
pylab.xlabel('$U_E$ (V)', size = "14")
pylab.ylabel('$U_A$ (V)', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(unumpy.nominal_values(UE), unumpy.nominal_values(MIN1), 
	unumpy.std_devs(MIN1), unumpy.std_devs(UE), "o", color="black")
pylab.errorbar(unumpy.nominal_values(UE), unumpy.nominal_values(MIN2), 
	unumpy.std_devs(MIN2), unumpy.std_devs(UE), "o", color="black")
pylab.errorbar(unumpy.nominal_values(UE), unumpy.nominal_values(MIN3), 
	unumpy.std_devs(MIN3), unumpy.std_devs(UE), "o", color="black")

#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
b = 1.0
#Contollare unita'' di misura
error = dmin1
init = numpy.array([b])
#FIXME ordine
par, cov = curve_fit(linear, ue, min1, init, error, "true")
#trattazione statistica degli errori
print(par, cov)


#Di nuovo non capisco il chi quadro, non cambia nulla se cambio da true a false
b = par[0]
chisq = (((min1-linear(ue, b))/error)**2)
somma = sum(chisq)
ndof = len(min1) - 1 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (ue.max()-ue.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + ue.min()
        retta[i] = linear(bucket[i], par[0])
pylab.plot(bucket, retta, color = "red")

#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
b = 1.0
#Contollare unita'' di misura
error = dmin2
init = numpy.array([b])
#FIXME ordine
par, cov = curve_fit(linear, ue, min2, init, error, "true")
#trattazione statistica degli errori
print(par, cov)


#Di nuovo non capisco il chi quadro, non cambia nulla se cambio da true a false
b = par[0]
chisq = (((min2-linear(ue, b))/error)**2)
somma = sum(chisq)
ndof = len(min2) - 1 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (ue.max()-ue.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + ue.min()
        retta[i] = linear(bucket[i], par[0])
pylab.plot(bucket, retta, color = "green")

b = 1.0
#Contollare unita'' di misura
error = dmin3
init = numpy.array([b])
#FIXME ordine
par, cov = curve_fit(linear, ue, min3, init, error, "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo non capisco il chi quadro, non cambia nulla se cambio da true a false
b = par[0]
chisq = (((min3-linear(ue, b))/error)**2)
somma = sum(chisq)
ndof = len(min3) - 1 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (ue.max()-ue.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + ue.min()
        retta[i] = linear(bucket[i], par[0])
pylab.plot(bucket, retta, color = "blue")

pylab.savefig("min.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)


pylab.figure(num=2, figsize=(8, 5), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)
pylab.title('Massimi', fontsize = "16")
#How to determine the unity of measure
pylab.xlabel('$U_E$ (V)', size = "14")
pylab.ylabel('$U_A$ (V)', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(unumpy.nominal_values(UE), unumpy.nominal_values(MAX1), 
	unumpy.std_devs(MAX1), unumpy.std_devs(UE), "o", color="black")
pylab.errorbar(unumpy.nominal_values(UE), unumpy.nominal_values(MAX2), 
	unumpy.std_devs(MAX2), unumpy.std_devs(UE), "o", color="black")
pylab.errorbar(unumpy.nominal_values(UE), unumpy.nominal_values(MAX3), 
	unumpy.std_devs(MAX3), unumpy.std_devs(UE), "o", color="black")

#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
b = 1.0
#Contollare unita'' di misura
error = dmax1
init = numpy.array([b])
#FIXME ordine
par, cov = curve_fit(linear, ue, max1, init, error, "true")
#trattazione statistica degli errori
print(par, cov)


#Di nuovo non capisco il chi quadro, non cambia nulla se cambio da true a false
b = par[0]
chisq = (((max1-linear(ue, b))/error)**2)
somma = sum(chisq)
ndof = len(max1) - 1 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (ue.max()-ue.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + ue.min()
        retta[i] = linear(bucket[i], par[0])
pylab.plot(bucket, retta, color = "red")

#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
b = 1.0
#Contollare unita'' di misura
error = dmax2
init = numpy.array([b])
#FIXME ordine
par, cov = curve_fit(linear, ue, max2, init, error, "true")
#trattazione statistica degli errori
print(par, cov)


#Di nuovo non capisco il chi quadro, non cambia nulla se cambio da true a false
b = par[0]
chisq = (((max2-linear(ue, b))/error)**2)
somma = sum(chisq)
ndof = len(max2) - 1 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (ue.max()-ue.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + ue.min()
        retta[i] = linear(bucket[i], par[0])
pylab.plot(bucket, retta, color = "green")

b = 1.0
#Contollare unita'' di misura
error = dmax3
init = numpy.array([b])
#FIXME ordine
par, cov = curve_fit(linear, ue, max3, init, error, "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo non capisco il chi quadro, non cambia nulla se cambio da true a false
b = par[0]
chisq = (((max3-linear(ue, b))/error)**2)
somma = sum(chisq)
ndof = len(max3) - 1 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (ue.max()-ue.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + ue.min()
        retta[i] = linear(bucket[i], par[0])
pylab.plot(bucket, retta, color = "blue")

pylab.savefig("max.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)

pylab.show()

