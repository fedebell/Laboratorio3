import pylab
import scipy
import uncertainties
import uncertainties.umath
from uncertainties import ufloat

R = ufloat(0.900, 0.001) #kOhm
C = ufloat(80, 20) #nF
f0 = 1/(R*C*2*3.14)
print(f0)

A = pow((f0*f0+400)/(f0*f0+4), 0.5)

print(A)

A2 = pow(1/(1+(2.0/f0)*(2.0/f0)), 0.5)

print(A2)

#In tuto cio ho bellamente trascurato la resistenza da 100 kOhm

#Inserire a mano i risultati del fit

matrix = [[1.0, 1.0, 0.0, 0.0],
	[1.0, 1.0, 0.0, 0.0],
	[0.0, 0.0, 1.0, 1.0],
	[0.0, 0.0, 1.0, 1.0]]

(a1, b1, a2, b2) = uncertainties.correlated_values((1,2,3,4), matrix)

x = (b1-b2)/(a1-a2)

print(x)
	





