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

def linear(x, a, b):
	return a*x+b


Vrb, dVrb, Vce, dVce, Vbe, dVbe = pylab.loadtxt('/home/federico/Laboratorio3/relazione3/datiFit.txt', unpack=True)

Vrb = unumpy.uarray(Vrb, dVrb)
Vrb = unumpy.uarray(Vce, dVce)
Vrb = unumpy.uarray(Vbe, dVbe)
Rb = ufloat(46700, 400) 
Rl = ufloat(977, 8)
V1 = ufloat(10.06, 0.06)
Isat = ufloat(10.03, 0.03)
Isat = Isat/1000
Vcesat = V1 - Rl* Isat  
print(Vcesat)


Ib = Vrb/Rb 

Ic = (V1 - Vce)/Rl


pylab.title('I_c vs I_b')
pylab.xlabel('I_b (uA)')
pylab.ylabel('I_c (mA)')
pylab.grid(color = "gray")

pylab.errorbar(unumpy.nominal_values(Ib), unumpy.nominal_values(Ic), 
	unumpy.std_devs(Ic), unumpy.std_devs(Ib), "o", color="black")



#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
#Paramatro da cambiare per considerare gli errori su tutti e due gli assi
error = pylab.sqrt(unumpy.std_devs(Ic)**2+0.25/1000*unumpy.std_devs(Ib)**2)
init = numpy.array([0.0, 0.0])
par, cov = curve_fit(linear, unumpy.nominal_values(Ib), unumpy.nominal_values(Ic), init, error, "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo co capisco il chi quadro, non cambia nulla se cambio da true a false
a = par[0]
b = par[1]
chisq = (((unumpy.nominal_values(Ic)-linear(unumpy.nominal_values(Ib), a, b))/error)**2)
somma = sum(chisq)
ndof = len(Ib) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (unumpy.nominal_values(Ib).max()-unumpy.nominal_values(Ib).min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + unumpy.nominal_values(Ib).min()
        retta[i] = linear(bucket[i], par[0], par[1])
pylab.plot(bucket, retta, color = "red")

pylab.show()

