import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

def fit_function(x, a, b):
	return a*x+b

V, dV, I, dI = pylab.loadtxt("data00.txt", unpack="True")


pylab.title("Best fit numerico")
pylab.xlabel("V (V)")
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

covarab = pcov[1,0]

print(pcov)
print("Parametri del fit")
print("a = ", a, "da = ", da)
print("b", b, "db", db)

chisq = (((I - fit_function(V, a, b))/dI)**2).sum()
ndof = len(V) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(chisq, ndof)
print("Chisquare/ndof = %f/%d" % (chisq, ndof))
print("p = ", p)

div = 100000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (V.max())/div 
for i in range(len(bucket)):
        
        bucket[i]=float(i)*inc
        retta[i] = fit_function(bucket[i], a, b)

pylab.plot(bucket, retta, color = "red")
