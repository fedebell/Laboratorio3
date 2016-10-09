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

Vout_o, dVout_o, f_o, df_o = pylab.loadtxt('/home/federico/Scrivania/lab3/relazione2/orizzontale.txt', unpack=True)
Vout_a, dVout_a, f_a, df_a = pylab.loadtxt('/home/federico/Scrivania/lab3/relazione2/attenuato.txt', unpack=True)

logf_o = pylab.log10(f_o)
dlogf_o = (1/pylab.log(10))*df_o/f_o

logf_a = pylab.log10(f_a)
dlogf_a = (1/pylab.log(10))*df_a/f_a

def linear(x, a, b):
	return a*x+b

def fitPassaBasso(x, f_0):
	return 1/pylab.sqrt(1/(1+(x/f_0)^2))

#Trascuriamo la resistenza in in uscita del generatore di funzioni cosi che V_in sia circa costante. 
Vin = 5 #Misurata una volta per tutte l'ampiezza massima
dVin = 0.05
A_o = Vout_o/Vin
dA_o = A_o *(dVout_o/Vout_o + dVin/Vin) 
B_o = 20 * pylab.log10(A_o)
dB_o = 8.7*dA_o/A_o


par_o, cov_o = curve_fit(linear, logf_o, B_o)

#Trascuriamo la resistenza in in uscita del generatore di funzioni cosi che V_in sia circa costante. 
Vin = 5 #Misurata una volta per tutte l'ampiezza massima
dVin = 0.05
A_a = Vout_a/Vin
dA_a = A_a *(dVout_a/Vout_a + dVin/Vin) 
B_a = 20 * pylab.log10(A_a)
dB_a = 8.7*dA_a/A_a

par_a, cov_a = curve_fit(linear, logf_a, B_a)


B = numpy.concatenate((B_o, B_a))
dB = numpy.concatenate((dB_o, dB_a))
f = numpy.concatenate((f_o, f_a))
df = numpy.concatenate((df_o, df_a))


#Ricordarsi che il grafico di Bode logaritmico su entrambi gli assi

pylab.figure(1)
pylab.title('Bode diagram of low-pass RC filter')
pylab.xlabel('frequency [kHz]')
pylab.ylabel('gain [dB]')
pylab.errorbar(f, B, dB, df, "o", color="black")

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (logf_o.max()-logf_o.min())/div 
for i in range(len(bucket)):
        
        bucket[i]=float(i)*inc
        retta[i] = linear(bucket[i], par_o[0], par_o[1])

pylab.plot(bucket, retta, color = "red")

#Routine per stampare due rette:
div = 1000
bucket = numpy.array([0.0 for i in range(div)])
retta = numpy.array([0.0 for i in range(div)])
inc = (logf_a.max()-logf_a.min())/div 
for i in range(len(bucket)):
        
        bucket[i]=float(i)*inc
        retta[i] = linear(bucket[i], par_a[0], par_a[1])

pylab.plot(bucket, retta, color = "blue")

pylab.show()

