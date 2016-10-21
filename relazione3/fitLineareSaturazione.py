import uncertainties
from uncertainties import ufloat
import math
import numpy
import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

def linear(x, a):
	return a


Vrb, dVrb, Vce, dVce, Vbe, dVbe = pylab.loadtxt('/home/federico/Laboratorio3/relazione3/datiFitSaturazione.txt', unpack=True)

Rb = 46700 
dRb = 400
Rl = 977
dRl = 8

V1 = 10.06
dV1 = 0.06

Ib = Vrb/Rb 
dIb = Ib*((dVrb/Vrb)**2 + (dRb/Rb)**2)**0.5

Ic = (V1 - Vce)/Rl
dIc = Ic*((dV1**2 + dVce**2)/((V1-Vce)**2) + (dRl/Rl)**2)**0.5


pylab.title('I_c vs I_b')
pylab.xlabel('I_b (uA)')
pylab.ylabel('I_c (mA)')
pylab.grid(color = "gray")
Ib = 1000000*Ib
Ic = 1000*Ic
dIb = 1000000*dIb
dIc = 1000*dIc
pylab.errorbar(Ib, Ic, dIc, dIb, "o", color="black")


#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
error = pylab.sqrt(dIc**2)
init = numpy.array([0.0])
par, cov = curve_fit(linear, Ib, Ic, init, error, "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo co capisco il chi quadro, non cambia nulla se cambio da true a false
a = par[0]
chisq = (((Ic-linear(Ib, a))/error)**2)
somma = sum(chisq)
ndof = len(Ib) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (Ib.max()-Ib.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + Ib.min()
        retta[i] = linear(bucket[i], par[0])
pylab.plot(bucket, retta, color = "red")

pylab.show()

