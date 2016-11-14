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

deltaV = ufloat(1.00, 0.02)
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



