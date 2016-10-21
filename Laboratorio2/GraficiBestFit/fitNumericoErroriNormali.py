import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

def fit_function(x, a, b):
	return a*x+b

V, dV, I, dI = pylab.loadtxt("data05.txt", unpack="True")

pylab.figure(1)
pylab.subplot(211)
pylab.title("Best fit numerico")
pylab.xlabel("Delta V (V)")
pylab.ylabel("I (mA)") #modificare gradi
pylab.grid(color = "gray")
pylab.xlim(0, 1.1*max(V)) 
pylab.ylim(0, 1.1*max(I))
pylab.grid(color = "gray")
pylab.errorbar(V, I, dI, dV, "o", color="black")

init = numpy.array([0.0, 0.0])
popt, pcov = curve_fit(fit_function, V, I, init, dI) 
a, b = popt
vara, varb = pylab.sqrt(pcov.diagonal())

covarab = pcov[0,1]

print(covarab)
print("Parametri del fit")
print("R = ", 1/a, "dR = ", vara/(a*a))
print("I_0", b, "dI_0", varb)

chisq = (((I - fit_function(V, a, b))/dI)**2).sum()
ndof = len(V) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(chisq, ndof)
print("Chisquare/ndof 2 = %f/%d" % (chisq, ndof))
print("p = ", p)

div = 100000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (V.max())/div 
for i in range(len(bucket)):
        
        bucket[i]=float(i)*inc
        retta[i] = fit_function(bucket[i], a, b)
        
pylab.subplot(211)
pylab.plot(bucket, retta, color = "red")

#Calcolo di un valore di I e della sua incertezza
Vingresso = 2
Iteorico = a + b*Vingresso
dIteorico = (vara**2 + (Vingresso * varb)**2 + 2*(Vingresso)*covarab)**0.5

print("I' = ", Iteorico)

#Rifaccio il fit considerando anche l'errore sulla V

pylab.subplot(212)
pylab.title("Residui normalizzati")
pylab.xlabel("Delta V (V)")
pylab.ylabel("Sigma") #modificare gradi
pylab.grid(color = "gray")
pylab.grid(color = "gray")
pylab.ylim(1.2*min((I-fit_function(V, a, b))/(dI)), 1.2*max((I-fit_function(V, a, b))/(dI)))
pylab.plot(V, (I-fit_function(V, a, b))/(dI), "o", color="black")

pylab.show()