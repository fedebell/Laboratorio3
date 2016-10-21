import numpy
import math
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
import lab

def fit_function(x, a, b, c):
    return a + b*pylab.sin(c*x)

FileName='/home/federico/Documenti/Laboratorio2/diodo/dati_arduino/datiRelazione.txt'
N1, N2 = pylab.loadtxt(FileName, unpack="True")

L1 = numpy.array([i for i in range(len(N2))])
L2 = numpy.array([i for i in range(len(N1))])

pylab.title("Curva corrente tensione")
pylab.xlabel("t (V)")
pylab.ylabel("V (A)") 
pylab.grid(color = "gray")
pylab.grid(color = "gray")

pylab.errorbar(L2, N2, 0, 0, "o", color="black")

print(N2)

initial = numpy.array([500.0, 500.0, 160.0])
popt, pcov = curve_fit(fit_function, L2, N2, initial)
a, b, c = popt
print(a, b, c)
print(pcov)

div = 1000
bucket = numpy.array([0.0 for i in range(div)])
inc = (L1.max()-L1.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + L1.min()

pylab.plot(bucket, fit_function(bucket, a, b, c), color = "red")


pylab.show()


