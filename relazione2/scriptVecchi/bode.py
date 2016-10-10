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

def fitPassaBasso(x, f_0):
	return 1/pylab.sqrt(1/(1+(x/f_0)^2))

Vout_o, dVout_o, f_o, df_o = pylab.loadtxt('/home/federico/Laboratorio3/relazione2/datiPassaBasso.txt', unpack=True)

#Trascuriamo la resistenza in in uscita del generatore di funzioni cosi che V_in sia circa costante. 
Vin = 5.0 #Misurata una volta per tutte l'ampiezza massima
dVin = 0.15
A_o = Vout_o/Vin

dA_o = A_o *pow(((dVout_o/Vout_o)**2 + (dVin/Vin)**2), 0.5)

B_o = 20 * pylab.log10(A_o)
dB_o = 8.7*dA_o/A_o

logf_o = pylab.log10(f_o)

dlogf_o = (1/pylab.log(10))*df_o/f_o

print(dlogf_o)
print(dB_o)

pylab.figure(1)
pylab.title('Bode diagram of low-pass RC filter')
pylab.xlabel('frequency [kHz]')
pylab.ylabel('gain [dB]')
pylab.ylim(-50, 2)
pylab.xlim(1, 7)
pylab.grid(color = "gray")
pylab.grid(color = "gray")

pylab.errorbar(logf_o, B_o, dB_o, dlogf_o, "o", color="black")

init = numpy.array([0.0, 0.0])
par_o, cov_o = curve_fit(linear, logf_o, B_o, init, pylab.sqrt(dB_o*dB_o+20.0*dlogf_o*dlogf_o))
print(par_o, cov_o)

chisq = (((dB_o - linear(logf_o, par_o[0], par_o[1]))/(pylab.sqrt(dB_o*dB_o+20.0*dlogf_o*dlogf_o)))**2).sum()
ndof = len(logf_o) - 2 #Tolgo due parametri estratti dal fit
p=1.0-scipy.stats.chi2.cdf(chisq, ndof)
print("Chisquare/ndof = %f/%d" % (chisq, ndof))
print("p = ", p)

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = 6/div 
for i in range(len(bucket)):
        
        bucket[i]=float(i)*inc
        retta[i] = linear(bucket[i], par_o[0], par_o[1])

pylab.plot(bucket, retta, color = "red")

pylab.show()
