import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

def fit_function(x, a, b):
	return a*x+b

V, I, dI, dV = pylab.loadtxt("/home/federico/Documenti/Laboratorio2/diodo/dati_arduino/datiInMezzo.txt", unpack="True")

A = numpy.log(I/(3.0455537949880908e-09)+1)
dA = dI/(I+3.0455537949880908e-09)

pylab.title("Dati 'reverse' linearizzati")
pylab.ylabel("V (V)")
pylab.xlabel("log(I/I_0+1))") #modificare gradi
pylab.rc('font',size=16)
pylab.grid(color = "gray")
pylab.grid(color = "gray")
pylab.errorbar(A, V, dV, dA, "o", color="black")

init = numpy.array([0.0, 0.0])
popt, pcov = curve_fit(fit_function, A, V, init, dV) 
a, b = popt
vara, varb = pylab.sqrt(pcov.diagonal())

covarab = pcov[0,1]

print(covarab/math.sqrt(vara*varb))
print("Parametri del fit")
print("a ", a, "dR = ", vara)
print("I_0", b, "dI_0", varb)

#Cambio errore per ogni file dove aver fatto il calcolo su fitNumerico.py
chisq = (((V - fit_function(A, a, b))/(dV))).sum() 
ndof = len(A) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(chisq, ndof)
print("Chisquare/ndof 2 = %f/%d" % (chisq, ndof))
print("p = ", p)

div = 100000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (A.max()-A.min())/div 
for i in range(len(bucket)):
        
        bucket[i]=float(i)*inc + A.min()
        retta[i] = fit_function(bucket[i], a, b)

pylab.plot(bucket, retta, color = "red")

pylab.show()
