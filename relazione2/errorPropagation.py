import pylab
import scipy
import uncertainties
import uncertainties.umath
from uncertainties import ufloat

print("Filro passa basso")
r = ufloat(0.98*1000, 0.8*1000) #Ohm
R = ufloat(1200, 10) #Ohm
C = ufloat(70*pow(10, -9), 3*pow(10, -9)) #F
#In tutto cio ho bellamente trascurato la resistenza da 100 kOhm
f0 = 1/(R*C*2*3.14)
print(f0)

A_2 = pow(1/(1+(2000/f0)**2), 0.5)
print("Attenuzone segnale = ", A_2)

A = pow((f0*f0+(20000**2))/(f0*f0+(2000**2)), 0.5)
print("Rapporto segnale rumore = ", A)

print("Passa-Banda")

R = ufloat(3.3*1000, 0.03*1000)
C = ufloat(100.0*pow(10, -9), 4*pow(10, -9))
f0 = 1/(R*C*2*3.14)
print("Frequenza di taglio", f0)


#Inserire a mano i risultati del fit

print("Intersezione tra due rette.")
#Inserire la matrice di covarianza
matrix = [[1.0, 1.0, 0.0, 0.0],
	[1.0, 1.0, 0.0, 0.0],
	[0.0, 0.0, 1.0, 1.0],
	[0.0, 0.0, 1.0, 1.0]]
#Definisco le variabili correlate
(a1, b1, a2, b2) = uncertainties.correlated_values((1,2,3,4), matrix)
x = (b1-b2)/(a1-a2)
print("Frequenza di taglio = ", x)

	





