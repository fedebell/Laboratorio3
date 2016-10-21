import pylab
import numpy
import scipy
from scipy.optimize import curve_fit
from scipy import stats
import math


#come errore sui tempi dovrei mettere la deviazione statdard della dimensione degli intervalli di tempo

t, x = pylab.loadtxt("data2.txt", unpack=True)

dt = pylab.array([2.0/1000 for i in range(len(t))])
dx = pylab.array([5.0 for i in range(len(x))])

error = (dt**2+dx**2)**(0.5)

t = t/1.0e3

pylab.figure(1)
pylab.subplot(211)

pylab.title("Oscillatore RLC 0,10 uF")
pylab.xlabel("Tempo (ms)")
pylab.ylabel("V (UA)")
pylab.grid(color = "gray")

pylab.grid(color = "gray")

pylab.errorbar(t, x, dx, dt, "o", color="black") #aggiungere eventuali errori

def fit_function(t, tau, a, omega, phi, k):
    return a*(math.e)**(-t/tau)*pylab.sin(omega*t+phi)+k

init = numpy.array([15, 450, 0.4, -3.14/2, 400]) #variare i parametri iniziali per ottenere diverse omega.

popt, pcov = curve_fit(fit_function, t, x, init, error, "true") #aggiungere l'errore
tau, a, omega, phi, k = popt
#dtau = 0
#da = 0
#domega = 0
#dphi = 0
#dk 
dtau, da, domega, dphi, dk = pylab.sqrt(((pcov.diagonal())))

print(tau, a, omega, phi, k)
print(dtau, da, domega, dphi, dk)

div = 100000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (t.max())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc
        retta[i] = fit_function(bucket[i], tau, a, omega, phi, k)

N = len(x)
chi2 = (( (fit_function(t, tau, a , omega, phi, k)-x)/error )**2).sum()
print("chiquadro =",chi2)
#(C.L. del valore x per un chi^2 a N-2 gradi di libertà)
print("C.L. = %.2f percento " % (scipy.stats.chi2.cdf( chi2, N-2)*100) )
        
pylab.plot(bucket, retta, color = "black")

pylab.subplot(212)
pylab.title("Grafico dei residui")
pylab.xlabel("Tempo (ms)")
pylab.ylabel("Residui")
pylab.grid(color = "gray")
pylab.plot(t, fit_function(t, tau, a , omega, phi, k) - x)


pylab.show()
