import pylab
import numpy
import scipy
from scipy.optimize import curve_fit
from scipy import stats
import math

#come errore sui tempi dovrei mettere la deviazione statdard della dimensione degli intervalli di tempo

f, x, dx = pylab.loadtxt("data.txt", unpack=True)
n = len(x)

df = numpy.array([1.0 for i in range(n)])
Vin = numpy.array([5.92 for i in range(n)]) #mettere valori corretti
dVin = numpy.array([0.1 for i in range(n)])

A = x/Vin
dA = A*(dx/x)

error = dA #Aggiungere l'errore sulla f facendo la propagazione

#Devo inserire manualmente la frequenza di risonanza che misuro all'oscilloscopio
def fit_function(f, c1, c2):
    return (c1*f)/((c2*f)**2+(1-(f/718)**2)**2)**(0.5)

init = numpy.array([4e-4, 4e-4]) #variare i parametri iniziali per ottenere diverse omega.

popt, pcov = curve_fit(fit_function, f, A, init, error, "false") #aggiungere l'errore
c1, c2 = popt
dc1, dc2 = pylab.sqrt(((pcov.diagonal())))

print(c1, c2)
print(dc1, dc2)
print("Covarianza normalizzata = ", pcov[1][0]/(dc1*dc2))

div = 100000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (f.max()+200-f.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + f.min()
        retta[i] = fit_function(bucket[i], c1, c2)

N = len(x)
chi2 = (((fit_function(f, c1, c2)-A)/error)**2).sum()
print("chiquadro =",chi2)
#(C.L. del valore x per un chi^2 a N-3 gradi di libertà)
print("C.L. = %.2f percento " % (scipy.stats.chi2.cdf( chi2, N-3)*100) )

pylab.figure(1)
pylab.subplot(211)
pylab.title("Curva di Risonanza")
pylab.xlabel("Frequenza (Hz)")
pylab.ylabel("Attuazione")
pylab.grid(color = "gray")
pylab.errorbar(f, A, dA, df, ".", color="black") #aggiungere eventuali errori
pylab.plot(bucket, retta, color = "black")

#punti aggiungivi valore a metà altezza
R = numpy.array([556.0, 930.0])
T = numpy.array([fit_function(556.0, c1, c2), fit_function(930.0, c1, c2)])

pylab.plot(R, T, "o", color = "red",)

pylab.subplot(212)
pylab.title("Grafico dei residui")
pylab.xlabel("Frequenza (Hz)")
pylab.ylabel("Residui")
pylab.grid(color = "gray")
pylab.plot(f, fit_function(f, c1, c2) - A)


pylab.show()
