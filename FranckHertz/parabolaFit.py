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

def quadratic(x, a, b, c):
	return a**2+b*x+c

INPUT = "/home/federico/Laboratorio3/FranckHertz/datiParabolaFit.txt"

ua, ic = pylab.loadtxt(INPUT, unpack=True)

dic = numpy.array([0.1 for i in range(len(ic))])
dua = numpy.array([0.1 for i in range(len(ua))])

U_A = unumpy.uarray(ua, dua)
I_C = unumpy.uarray(ic, dic)

#Nelle visualizzazioni devo introdurre gli errori

pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)
#FIXME: Fix the title
pylab.title('$I_C$ vs $U_A$ at $U_E = 2.0$', fontsize = "16")
#How to determine the unity of measure
pylab.xlabel('$U_A$ (V)', size = "14")
#FIXME Unita' di misura
pylab.ylabel('$I_C$ (mA)', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(unumpy.nominal_values(U_A), unumpy.nominal_values(I_C), 
	unumpy.std_devs(I_C), unumpy.std_devs(U_A), "o", color="black")

#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
#Valori di inizializzazione:
a = 1.0
b = 2.0
c = 3.0
error = ((unumpy.std_devs(I_C))**2.0+(2*a*(unumpy.nominal_values(U_A)+b)*unumpy.std_devs(U_A))**2.0)**0.5
print(error)
#error = unumpy.std_devs(I_D)
init = numpy.array([a, b, c])
#Errori tutti statistici
par, cov = curve_fit(quadratic, unumpy.nominal_values(U_A), unumpy.nominal_values(I_C), init, error, absolute_sigma = "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo co capisco il chi quadro, non cambia nulla se cambio da true a false
a = par[0]
b = par[1]
c = par[2]

chisq = ((unumpy.nominal_values(I_C)-quadratic(unumpy.nominal_values(U_A), a, b, c))/error)**2
somma = sum(chisq)
ndof = len(unumpy.nominal_values(I_C)) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

div = 1000
bucket = numpy.array([0.0 for i in range(div)])
parabola = numpy.array([0.0 for i in range(div)])
inc = (unumpy.nominal_values(U_A).max()-unumpy.nominal_values(U_A).min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + unumpy.nominal_values(U_A).min()
        parabola[i] = quadratic(bucket[i], par[0], par[1], par[2])


#Print del valor a cui si trova il minimo
print("Minimo:", -b/(2*a))

pylab.plot(bucket, parabola, color = "red")

pylab.show()


