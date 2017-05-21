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

def quadratic(x, V0, Rt):
	return V0*(1+(x/Rt))**0.5

INPUT = "/home/federico/Laboratorio3/relazione15/datiBoltzmann.txt"

R, dR, V, dV= pylab.loadtxt(INPUT, unpack=True)

pylab.rc('font',size=13)
pylab.title('$ V_{rms} \, \, vs \, \,R$', fontsize = "16")
pylab.ylabel('$V_{rms}\,(mV)$', size = "14")
pylab.xlabel('$R\,(k\Omega)$', size = "14")
pylab.grid(color = "gray")
#Controllare ordine
pylab.errorbar(R, V, dV, dR, ".", color="black")


#V = unumpy.uarray(V, dV)
#R = unumpy.uarray(R, dR)

#Fare attenzione che gli errori devono essere sempre sommati con le stesse unita di misura, 
#quindi nel coeffiente ci cade anche il fattore per passare da una unita di misura all'altra
#TODO: Make it better
error = dV
init = numpy.array([80, 40])
#Errori tutti statistici
par, cov = curve_fit(quadratic, R, V, init, error, absolute_sigma = "true")
#trattazione statistica degli errori
print(par, cov)

#Di nuovo co capisco il chi quadro, non cambia nulla se cambio da true a false
V0 = par[0]
Rt = par[1]

dV0 = (cov[0][0])**0.5
dRt = (cov[1][1])**0.5

print("V0 =", V0, "+/-", dV0)
print("Rt =", Rt, "+/-", dRt)

chisq = ((V-quadratic(R, V0, Rt))/error)**2
somma = sum(chisq)
ndof = len(unumpy.nominal_values(V)) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (R.max()-R.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + R.min()
        retta[i] = quadratic(bucket[i], par[0], par[1])

pylab.plot(bucket, retta, color = "red")


pylab.show()




