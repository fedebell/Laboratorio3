import uncertainties
from uncertainties import ufloat
import math
import numpy
import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

#Misuro a mano con il tester i valori che poi vado a mettere nel file, posso anche lasciare lo sfasamento vuoto

def linear(x, a, b):
	return a*x+b

#def fitPassaBasso(x, f_0):
#	return 1/pylab.sqrt(1/(1+(x/f_0)^2))

Vout, dVout, f, df = pylab.loadtxt('/home/federico/Laboratorio3/relazione2/datiFit.txt', unpack=True)

#Trascuriamo la resistenza in in uscita del generatore di funzioni cosi che V_in sia circa costante. 
Vin = 5.0 #Misurata una volta per tutte l'ampiezza massima
dVin = 0.15
A = Vout/Vin

dA = A*pylab.sqrt(((dVout/Vout)**2 + (dVin/Vin)**2))

B = 20 * pylab.log10(A)
dB = 8.7*dA/A

logf = pylab.log10(f)

dlogf = (1/pylab.log(10))*df/f

pylab.title('Bode diagram of low-pass RC filter')
pylab.xlabel('frequency [kHz]')
pylab.ylabel('gain [dB]')
#pylab.ylim(-50, 2)
#pylab.xlim(1, 7)
pylab.grid(color = "gray")

pylab.errorbar(logf, B, dB, dlogf, "o", color="black")

error = pylab.sqrt(dB**2+20.0*dlogf**2)
print(error)
init = numpy.array([0.0, 0.0])
par, cov = curve_fit(linear, logf, B, init, error, "true")
#trattazione statistica degli errori
print(par, cov)

a = par[0]
b = par[1]
chisq = (((B-linear(logf, a, b))/error)**2).sum()
somma = sum(chisq)
ndof = len(logf) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(somma, ndof)
print("Chisquare/ndof = %f/%d" % (somma, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (logf.max()-logf.min())/div 
for i in range(len(bucket)):
        bucket[i]=float(i)*inc + logf.min()
        retta[i] = linear(bucket[i], par[0], par[1])
pylab.plot(bucket, retta, color = "red")

pylab.show()


