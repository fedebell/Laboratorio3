import uncertainties
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

#Angolo di riferimento
a = ufloat(169.0 + 45.0/60, 1.0/60.0)
#Misure angoli per ordine 0 e ordine 1:
#$\alpha_V^{0} = 227 \degree 53 ' \pm 1'$ e $\alpha_V^{1} = 275 \degree 6' \pm 1'$
a_0 = ufloat(227.0+53.0/60.0, 1.0/60.0)
a_1 = ufloat(275.0+52.0/60.0, 1.0/60.0)
#Misure riscalando lo zero
t_0 = a_0 - a
t_1 = a_1 - a

t_i = (180.0-t_0)/2
t_d = 180.0-t_i-t_1
t_i = (t_i/180.0)*3.1415
t_d = (t_d/180.0)*3.1415
lambdaHg = ufloat(546.074, 0.001)
d = lambdaHg/(sin(t_i)-sin(t_d))
N = 1000000/d
print("d =" + str(d))
print("N =" + str(N))
d= ufloat(840.0, 3.0)

#theta incidente e uguale per tutti

viola = ufloat(267.0+47/60, 1/60)
azzurro = ufloat(271+38/60, 1/60)
verde = ufloat(274+50/60, 5/60)
rossa = ufloat(283+20/60, 1/60)

viola = viola - a
azzurro = azzurro - a
verde = verde - a
rossa = rossa -a

violaD = 180.0-(t_i/3.1415)*180.0-viola
azzurroD = 180.0-(t_i/3.1415)*180.0-azzurro
verdeD = 180.0-(t_i/3.1415)*180.0-verde
rossaD = 180.0-(t_i/3.1415)*180.0-rossa

violaD = (violaD/180.0)*3.1415
azzurroD = (azzurroD/180.0)*3.1415
verdeD = (verdeD/180.0)*3.1415
rossaD = (rossaD/180.0)*3.1415
 
lambdaVioletto = d*(sin(t_i)-sin(violaD))
lambdaAzzurro = d*(sin(t_i)-sin(azzurroD))
lambdaVerde = d*(sin(t_i)-sin(verdeD))
lambdaRossa = d*(sin(t_i)-sin(rossaD))

lung = [lambdaVioletto.nominal_value(), lambdaAzzurro.nominal_value(), lambdaVerde.nominal_value(), lambdaRossa.nominal_value()]
menouno = 1/lung


#%n_1=2 Balmer  violetto (n_2=5) azzurro (n_2=4) rosso (n_2=3)


print("Lunghezze d'onda:")
print("Violetto = ", lambdaVioletto)
print("Azzurro = ", lambdaAzzurro)
print("Verde = ", lambdaVerde)
print("Rossa = ", lambdaRossa)

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









