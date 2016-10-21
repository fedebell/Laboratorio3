import numpy
import math
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
import lab

def fit_function(x, a, b):
	return a*(numpy.log(I/b + 1))

FileName='/home/federico/Documenti/Laboratorio2/diodo/dati_arduino/dati.txt'
N1, N2 = pylab.loadtxt(FileName, unpack="True")

errN2 = numpy.array([1.0 for i in range(len(N2))])
errN1 = numpy.array([1.0 for i in range(len(N1))])

Rd = 3280.0
errRd = 30.0

eta = 4.89/1000
erreta = 0.02/1000

V1 = eta*N1
V2 = eta*N2

I = (V1-V2)/Rd

print(numpy.log(I/1e-09 + 1))

#Inserire errori per i i V
errV2 = (erreta/eta + errN2/N2)*V2
errV1 = (erreta/eta + errN1/N1)*V1

errI = (errRd/Rd)*I

for i in range(len(I)):
        errI[i] = 50e-06

for i in range(len(I)):
        if(I[i]==0.0): I[i] = 1.0e-11*i

for i in range(len(V2)):
        if(V2[i]==0.0): V2[i] = 1.0e-11*i

pylab.title("Best fit equazione di Shockley")
pylab.xlabel("V (V)")
pylab.ylabel("I (A)") 
pylab.grid(color = "gray")
pylab.grid(color = "gray")
pylab.errorbar(I, V2, errV2, errI, "o", color="black")

pylab.show()

initial = numpy.array([0.0481547, 3.2e-09])
error = errI #NON posso prendere errore squadrato perchè mescolerei le unità di misura
popt, pcov = curve_fit(fit_function, I, V2, initial, error)
a, b = popt
print(popt)
print(pcov)

div = 1000 
bucket = numpy.array([0.0 for i in range(div)])
funzione = numpy.array([0.0 for i in range(div)])
inc = (V2.max()-V2.min())/div
print(len(bucket))
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + V2.min()
        funzione[i] = fit_function(bucket[i], a, b)
        
print(len(bucket))
print(len(function))
pylab.plot(bucket, funzione, color = "red")

#calcolo il chi quadro
chisq = (((I - fit_function(V2, a, b))/error)**2).sum()
ndof = len(V2) - 2
p=1.0-scipy.stats.chi2.cdf(chisq, len(V2)-3)
print("Carica Chisquare/ndof = %f/%d" % (chisq, ndof))
print("p = ", p)


pylab.show()
