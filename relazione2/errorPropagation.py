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

print("Intersezione tra due rette. Passa basso")

#Inserire la matrice di covarianza
matrix = [[0.00948684, 0.0, 0.0, 0.0],
	[0.0, 0.0, 0.0, 0.0],
	[0.0, 0.0, 0.12345903, -0.46197214],
	[0.0, 0.0, -0.46197214, 1.73409314]]
#Definisco le variabili correlate
(a1, b1, a2, b2) = uncertainties.correlated_values((0.0,0.21637946,-18.05254106,57.60008368), matrix)
x = pow(10, (b1-b2)/(a2-a1))
print("Frequenza di taglio _ Passa Basso = ", x)

print("Intersezione tra due rette. Passa banda. Salita")



#Inserire la matrice di covarianza
matrix = [[0.00349517, 0.0, 0.0, 0.0],
	[0.0, 0.0, 0.0, 0.0],
	[0.0, 0.0, 2.28013502, -5.48270144],
	[0.0, 0.0, -5.48270144, 13.26307781]]
#Definisco le variabili correlate
(a1, b1, a2, b2) = uncertainties.correlated_values((0.0,-6.23598879, 11.12716648, -35.97594446), matrix)
x = pow(10, (b1-b2)/(a2-a1))
print("Frequenza di taglio _ Passa Banda Salita = ", x)



print("Intersezione tra due rette. Passa banda. Discesa")

#Inserire la matrice di covarianza
matrix = [[0.00349517, 0.0, 0.0, 0.0],
	[0.0, 0.0, 0.0, 0.0],
	[0.0, 0.0, 1.50457078, -6.41584978],
	[0.0, 0.0, -6.41584978, 27.61611408]]
#Definisco le variabili correlate
(a1, b1, a2, b2) = uncertainties.correlated_values((0.0,-6.23598879,-12.7853335,40.61842064), matrix)
x = pow(10, (b1-b2)/(a2-a1))
print("Frequenza di taglio _ Passa Banda Salita = ", x)







	





