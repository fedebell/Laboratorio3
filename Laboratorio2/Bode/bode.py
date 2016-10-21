from pylab import curve_fit
import uncertainties
from uncertainties import ufloat
import math
import numpy

#Misuro a mano con il tester i valori che poi vado a mettere nel file, posso anche lasciare lo sfasamento vuoto

Vout_o, dVout_o, f_o, df_o = loadtxt('orizzontale.txt', unpack=True)
Vout_a, dVout_a, f_a, df_a = loadtxt('attenuato.txt', unpack=True)

def linear(x, a, b):
	return a*x+b

def fitPassaBasso(x, f_0):
	return 1/pylab.sqrt(1/(1+(x/f_0)^2))

#Trascuriamo la resistenza in in uscita del generatore di funzioni così che V_in sia circa costante. 
Vin = 5 #Misurata una volta per tutte l'ampiezza massima
dVin = 0.05
A_o = Vout_o/Vin_o
dA_o = A_o *(dVout_o/Vout_o + dVin/Vin) 
B_o = 20 * log10(A_o)
dB_o = 8.7*dA_o/A_o


par_o, cov_o = pylab.curve_fit(linear, f_o, B_o, pylab.sqrt((dB_o)^2 + (df_o)^2))

#Trascuriamo la resistenza in in uscita del generatore di funzioni così che V_in sia circa costante. 
Vin = 5 #Misurata una volta per tutte l'ampiezza massima
dVin = 0.05
A_a = Vout_a/Vin_a
dA_a = A_a *(dVout_a/Vout_a + dVin/Vin) 
B_a = 20 * log10(A_a)
dB_a = 8.7*dA_a/A_a

par_a, cov_a = pylab.curve_fit(linear, f_a, B_a, pylab.sqrt((dB_a)^2 + (df_a)^2))


Vout = numpy.concatenate(Vout_o, Vout_a)
dVout = numpy.concatenate(dVout_o, dVout_a)
f = numpy.concatenate(f_o, f_a)
df = numpy.concatenate(df_o, df_a)

#Ricordarsi che il grafico di Bode logaritmico su entrambi gli assi

title('Bode diagram of low-pass RC filter')
subplot(211)
xlabel('frequency [Hz]')
ylabel('gain [dB]')
xscale('log')
plot(f, dB)
subplot(212)
xlabel('frequency [Hz]')
ylabel('phase [pi rad]')
xscale('log')
plot(, -phi)
savefig('plot.png')

print("\ncut frequency: %s Hz" % util_format(fT, dfT))
print("\ncut frequency (from phase): %s Hz\n" % util_format(fTp, dfTp))

show()

