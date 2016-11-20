import uncertainties
from uncertainties import ufloat
import math
import numpy
import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats
import uncertainties 
from uncertainties import unumpy

Vmeno = ufloat(-15.00, 15.00*0.005)
Vpiu = ufloat(14.99, 14.99*0.005)
R1 = ufloat(2.18, 2.18*0.008)*1000
R2 = ufloat(21.5, 21.5*0.008)*1000

print("Vmeno = ", Vmeno)
print("Vpiu = ", Vpiu)
print("R1 = ", R1)
print("R2 = ", R2)
A = -R2/R1
print("A_atteso = ", A) 


#Resistenze ingresso
V1 = ufloat(9.68, 0.08)
V2 = ufloat(4.88, 0.04)
RS = ufloat(2.19, ((2.19*0.008)**2+0.01**2)**0.5)
R_in_att = RS*1/(V1/V2 -1)
print("V1 = ", V1)
print("V2 = ", V2)
print("RS = ", RS)
print("R_in_attesa = ", R_in_att)

deltaV = ufloat(1.00, 0.04)
deltat = ufloat(90, 1)*10**(-3)
s = deltaV/deltat
print("s = ", s)

#Amplificatore invertente
R1 = ufloat(218, ((0.008*218)**2+1)**0.5)
P1 = ufloat(97.8, ((0.008*97.8)**2+0.1**2)**0.5)*1000
VIN = ufloat(0.340, 0.002)

print("R1 = ", R1)
print("P1 = ", P1)
print("VIN = ", VIN)

#Integratore
R1 = ufloat(984, 984*0.008)
R2 = ufloat(11.77, 11.77*0.008)*1000
C = ufloat(45.2, 45.2*0.04)
print("R1 = ", R1)
print("R2 = ", R2)
print("C = ", C)
#Derivatore

deltaV = ufloat(1.00, 0.03)
deltat = ufloat(0.088, 0.004)
slew = deltaV/deltat
print("slew rate", slew)

V_I = ufloat(4.68, 0.02)
V_OUT = ufloat(1.02, 0.02)
A = V_OUT/V_I
print("Amplificazione derivatore a 100\,Hz:", A)

f = 0.100
f_t = 3.42515
Amax = 11.597690
A = Amax/(1+(f_t/f)**2)**0.5
print("Amplificazione derivatore a 100\,Hz attesa:", A)
