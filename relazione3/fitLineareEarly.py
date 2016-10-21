import uncertainties
from uncertainties import ufloat
import math
import numpy
import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

def linear(x, a, b):
	return a*x+b




Vl, Vce, dVl, dVce = pylab.loadtxt('/home/federico/Laboratorio3/relazione3/dati2.txt', unpack=True)

Rb = 46700 
dRb = 400
Rl = 977
dRl = 8

Ic = (Vl)/Rl
dIc = Ic*((dVl/Vl)**2+(dRl/Rl)**2)**0.5

pylab.figure(2)
pylab.title('I_c vs V_ce')
pylab.xlabel('V_ce (V)')
pylab.ylabel('I_c (mA)')
pylab.grid(color = "gray")



#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
error = pylab.sqrt(dIc**2)
init = numpy.array([0.005, 0.005])
par, cov = curve_fit(linear, Vce, Ic, init, error, "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo co capisco il chi quadro, non cambia nulla se cambio da true a false
a = par[0]
b = par[1]
print("Early = ", -b/a)
chisq = ((Ic-linear(Vce, a, b))/error)**2
somma = sum(chisq)
ndof = len(Vce) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (Vce.max()-Vce.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + Vce.min()
        retta[i] = linear(bucket[i], par[0], par[1])

Ic = 1000*Ic
dIc = 1000*dIc
retta = 1000*retta
pylab.errorbar(Vce, Ic, dIc, dVce, "o", color="black")

pylab.plot(bucket, retta, color = "red")

pylab.show()

