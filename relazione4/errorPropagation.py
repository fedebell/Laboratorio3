import pylab
import scipy
import uncertainties
import uncertainties.umath
from uncertainties import ufloat

#Inserire a mano i risultati del fit

#IMPORTANTE: Formalismo per trattare variabili con associata una covarianza, non 
#ho mai implementato per ora una analoga funzione sui vettori

print("Intersezione tra due rette.")
#Inserire la matrice di covarianza
matrix = [[1.0, 1.0, 0.0, 0.0],
	[1.0, 1.0, 0.0, 0.0],
	[0.0, 0.0, 1.0, 1.0],
	[0.0, 0.0, 1.0, 1.0]]
#Definisco le variabili correlate
(a1, b1, a2, b2) = uncertainties.correlated_values((1,2,3,4), matrix)
x = (b1-b2)/(a2-a2)
print("Frequenza di taglio = ", x)

	





