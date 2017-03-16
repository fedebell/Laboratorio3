from uncertainties import *
from uncertainties import ufloat
from uncertainties.umath import * 
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

#Angolo di riferimento
a = ufloat(169.0 + 45.0/60.0, 1.0/60.0)
#Misure angoli per ordine 0 e ordine 1:
#$\alpha_V^{0} = 227 \degree 53 ' \pm 1'$ e $\alpha_V^{1} = 275 \degree 6' \pm 1'$
a_0 = ufloat(227.0+53.0/60.0, 1.0/60.0)
a_1 = ufloat(275.0+52.0/60.0, 1.0/60.0)
#Misure riscalando lo zero
t_0 = a_0 - a
t_1 = a_1 - a

t_i = (180.0-t_0)/2
t_d = 180.0-t_i-t_1
print("ti" + str(t_i))
t_i = (t_i/180.0)*3.1415
t_d = (t_d/180.0)*3.1415
lambdaHg = ufloat(546.074, 0.001)
d = lambdaHg/(sin(t_i)-sin(t_d))
N = 1000000/d
print("d =" + str(d))
print("N =" + str(N))
d= ufloat(840.0, 3.0)

#theta incidente e uguale per tutti

viola = ufloat(267.0+47.0/60.0, 1.0/60.0)
azzurro = ufloat(271.0+38.0/60.0, 1.0/60.0)
arancio = ufloat(280.0 + 33.0/60.0, 1.0/60.0)
verde = ufloat(274.0+50.0/60.0, 5.0/60.0)
rossa = ufloat(283.0+20.0/60.0, 1.0/60.0)

viola = viola - a
azzurro = azzurro - a
arancio = arancio -a
verde = verde - a
rossa = rossa -a

violaD = 180.0-(t_i/3.1415)*180.0-viola
azzurroD = 180.0-(t_i/3.1415)*180.0-azzurro
arancioD = 180.0 -(t_i/3.1415)*180.0-arancio
verdeD = 180.0-(t_i/3.1415)*180.0-verde
rossaD = 180.0-(t_i/3.1415)*180.0-rossa

violaD = (violaD/180.0)*3.1415
azzurroD = (azzurroD/180.0)*3.1415
verdeD = (verdeD/180.0)*3.1415
rossaD = (rossaD/180.0)*3.1415
arancioD = (arancioD/180.0)*3.1415
 
lambdaArancio = d*(sin(t_i)-sin(arancioD))
lambdaVioletto = d*(sin(t_i)-sin(violaD))
lambdaAzzurro = d*(sin(t_i)-sin(azzurroD))
lambdaVerde = d*(sin(t_i)-sin(verdeD))
lambdaRossa = d*(sin(t_i)-sin(rossaD))

lung = [uncertainties.nominal_value(lambdaVioletto), uncertainties.nominal_value(lambdaAzzurro), uncertainties.nominal_value(lambdaRossa)]
lungErr = [uncertainties.std_dev(lambdaVioletto), uncertainties.std_dev(lambdaAzzurro), uncertainties.std_dev(lambdaRossa)]

lungh = unumpy.uarray(lung, lungErr)

y = 1/lungh

#violetto 1: n 2 = 5; azzurro: n 2 = 4; rosso 2: n 2 = 3

numeri1 = [5.0, 4.0, 3.0]
errNum1 = [0, 0, 0]
numeri2 = [2.0, 2.0, 2.0]
errNum2 = [0, 0, 0]


n1 = unumpy.uarray(numeri1, errNum1)
n2 = unumpy.uarray(numeri2, errNum2)

x = (1/n2**2-1/n1**2)

y = 1000*y

print("Lunghezze d'onda:")
print("Arancio = ", lambdaArancio)
print("Violetto = ", lambdaVioletto)
print("Azzurro = ", lambdaAzzurro)
print("Verde = ", lambdaVerde)
print("Rossa = ", lambdaRossa)

pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)

pylab.xlim(0.138, 0.211)

pylab.title('Determinazione della costante di Rydberg', fontsize = "16")

pylab.ylabel(r'$ \Lambda $ (1/um)', size = "14")

pylab.xlabel('1/n_1^2-1/n_2^2', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(unumpy.nominal_values(x), unumpy.nominal_values(y), unumpy.std_devs(y), unumpy.std_devs(x), "o", color="black")

#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
a = 1.0
b = 1.0
#Contollare unit di misura
error = unumpy.std_devs(y)
init = numpy.array([a, b])
par, cov = curve_fit(linear, unumpy.nominal_values(x), unumpy.nominal_values(y), init, error, "true")
#trattazione statistica degli errori
print(par, cov)

a = par[0]
b = par[1]
chisq = (((unumpy.nominal_values(y)-linear(unumpy.nominal_values(x), a, b))/error)**2)
somma = sum(chisq)
ndof = len(x) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (unumpy.nominal_values(x).max()-unumpy.nominal_values(x).min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + (unumpy.nominal_values(x)).min()
        retta[i] = linear(bucket[i], par[0], par[1])
pylab.plot(bucket, retta, color = "red")

a = ufloat(a, cov[0][0]**0.5)
b = ufloat(b, cov[1][1]**0.5)

print("Si ricavano dai parametti i seguenti due valori di a = ", a, "e di b =",  b)

alpha_1 = ufloat(108.0+42.0/60.0, 1.0/60.0)
alpha_2 = ufloat(108.0+45.0/60.0, 1.0/60.0)

alpha_1 = 180.00-(t_i/3.1415)*180.00-alpha_1
alpha_2 = 180.00-(t_i/3.1415)*180.00-alpha_2

theta_1 = (alpha_1/180)*3.1415
theta_2 = (alpha_2/180)*3.1415

print(theta_1, theta_2)

lambda1 = d*(sin(t_i)-sin(theta_1))
lambda2 = d*(sin(t_i)-sin(theta_2))

print("lambda1 = " + str(lambda1))
print("lambda2 = " + str(lambda2))


pylab.show()









