import pylab
import scipy
import uncertainties
import uncertainties.umath
from uncertainties import ufloat
from uncertainties import unumpy
import numpy

#Inserire a mano i risultati del fit

#IMPORTANTE: Formalismo per trattare variabili con associata una covarianza, non 
#ho mai implementato per ora una analoga funzione sui vettori


print("Frequenza di taglio bassa:\n")
#Inserire la matrice di covarianza
matrix = [[0.0, 1.0, 0.0, 0.0],
	[1.0, 0.01645, 0.0, 0.0],
	[0.0, 0.0, 0.50193422, 2.35784653],
	[0.0, 0.0, 2.35784653, 11.09527365]]
#Definisco le variabili correlate
(a1, b1, a2, b2) = uncertainties.correlated_values((0.0, 19.58726298, 17.71086057, 94.51293025), matrix)
x = (b1-b2)/(a2-a1)
print("Frequenza di taglio bassa = ", unumpy.pow(10.0, x))



print("Frequenza di taglio alta:\n")
#Inserire la matrice di covarianza
matrix = [[0.0, 1.0, 0.0, 0.0],
	[1.0, 0.01645, 0.0, 0.0],
	[0.0, 0.0, 0.24498001,  0.08087699],
	[0.0, 0.0, 0.08087699,  0.03940115]]
#Definisco le variabili correlate
(a1, b1, a2, b2) = uncertainties.correlated_values((0.0, 19.58726298, -19.61622398, -1.45953847), matrix)
x = (b1-b2)/(a2-a1)
print("Frequenza di taglio alta = ", unumpy.pow(10.0, x))

	









