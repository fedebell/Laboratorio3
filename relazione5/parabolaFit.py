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

def quadratic(x, a, b):
	return a*(x-b)**2

INPUT = "/home/federico/Laboratorio3/relazione5/datiParabola.txt"

Vd, dVd, Vgs, dVgs = pylab.loadtxt(INPUT, unpack=True)

R_1 = ufloat(0.994*1000, 0.008*1000)
R_2 = ufloat(1.954*1000, 0.016*1000)
V_1 = ufloat(15.01, 0.08)
V_2 = ufloat(-15.11, 0.08)

#Nelle visualizzazioni devo introdurre gli errori

V_GS = unumpy.uarray(Vgs, dVgs)
V_D = unumpy.uarray(Vd, dVd)

I_D = V_D/R_1
I_D = I_D*1000

pylab.rc('font',size=13)
pylab.title('I_D vs V_GS', fontsize = "16")
pylab.xlabel('V_GS (V)', size = "14")
pylab.ylabel('I_D (mA)', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(unumpy.nominal_values(V_GS), unumpy.nominal_values(I_D), 
	unumpy.std_devs(I_D), unumpy.std_devs(V_GS), "o", color="black")

#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
error = ((unumpy.std_devs(I_D))**2.0+(2*1.4*(unumpy.nominal_values(V_GS)+3.40100977e+00)*unumpy.std_devs(V_GS))**2.0)**0.5
#error = unumpy.std_devs(I_D)
init = numpy.array([1.27153396, -3.40100977e+00])
#Errori tutti statistici
par, cov = curve_fit(quadratic, unumpy.nominal_values(V_GS), unumpy.nominal_values(I_D), init, error, absolute_sigma = "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo co capisco il chi quadro, non cambia nulla se cambio da true a false
a = par[0]
b = par[1]

chisq = ((unumpy.nominal_values(I_D)-quadratic(unumpy.nominal_values(V_GS), a, b))/error)**2
somma = sum(chisq)
ndof = len(unumpy.nominal_values(I_D)) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (unumpy.nominal_values(V_GS).max()-unumpy.nominal_values(V_GS).min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + unumpy.nominal_values(V_GS).min()
        retta[i] = quadratic(bucket[i], par[0], par[1])


pylab.plot(bucket, retta, color = "red")

pylab.show()


