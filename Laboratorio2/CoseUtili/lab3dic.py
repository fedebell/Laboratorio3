import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

def fit_function(x, a, b):
	return a*x+b

f, Vin, Vout, deltaPhi = pylab.loadtxt("data.txt", unpack=True)
ef, eVin, eVout, edeltaPhi = pylab.loadtxt("errori.txt", unpack=True)
Z = Vout/Vin
print(Z)
eZ = Z*(eVin/Vin+eVout/Vout)
A = -20*numpy.log(Z)
dA = -20*eZ/Z

print(f)
print(A)

pylab.figure(1)
pylab.subplot(211)
# Format the plot.
pylab.rc("font", size = 18)
pylab.title("Diagramma di bode", y = 1.02)
pylab.xlabel("Frequenza (kHz)")
pylab.ylabel("Attenuazione (dB)", labelpad = -5)
#pylab.ylim(0, 600)
pylab.grid(color = "gray")
# Create the histogram.
pylab.errorbar(f, A, dA, df, "o", color="black")
#pylab.plot(dati, color = "black")

partenza = 1 #definisco qua
#eseguo fit lineare, devo cancellae a meno i dati iniziali che no hanno andamento lineare
#nf = f[partenza:len(f):1]
#nA = A[partenza:len(A):1]

nf = f
nA = A

print(nf)
print(nA)

errFit = 0.1
init = numpy.array([0.0, 0.0])
popt, pcov = curve_fit(linear_fit, nf, nA, init, errFit) #definire errFit
a, b = popt
da, db = pylab.sqrt(pcov.diagonal())

covarab = pcov[0,1]

print(covarab)
print("Parametri del fit")
print("a = ", a, "da = ", da)
print("b = ", b, "", db)

chisq = (((nA - fit_function(nf, a, b))/dI)**2).sum()
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

pylab.subplot(212)
pylab.title("Residui normalizzati")
pylab.xlabel("Delta V (V)")
pylab.ylabel("Sigma") #modificare gradi
pylab.grid(color = "gray")
pylab.grid(color = "gray")
pylab.ylim(1.2*min((I-fit_function(V, a, b))/(dI)), 1.2*max((I-fit_function(V, a, b))/(dI)))
pylab.plot(V, (I-fit_function(V, a, b))/(dI), "o", color="black")

pylab.show()
