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

#slew rate

VCC = ufloat(14.96, 0.005*14.96)
VEE = ufloat(14.96, 0.005*14.96)
dV = ufloat(4.00, (0.02**2+0.12**2)**0.5)
dt = ufloat(336, 4)/1000
s = dV/dt
print("Slew rate = ", s)
print("VCC = ", VCC)
print("VEE = ", VEE)

#aplificatore di carica
Vmeno = ufloat(200, 4)/1000
CT = ufloat(1.01, 1.01*0.04)
CF = ufloat(1.02, 1.02*0.04)
C1 = ufloat(21.9, 21.9*0.04)
R3 = ufloat(97.8, ((0.008*97.8)**2+0.1**2)**0.5)
R2 = ufloat(99.9, ((0.008*99.9)**2+0.1**2)**0.5)
R1 = ufloat(98.3, ((0.008*98.3)**2+0.1**2)**0.5)
VIN = unumpy.uarray([6.00, 4.00, 2.02], [0.06, 0.04, 0.01])
deltaT = unumpy.uarray([336, 293, 220], [4, 4, 4])

a = R1*CF
b = -R1*CF*unumpy.log(Vmeno*CF/CT)

print(a, b)

print("C1 = ", C1)
print("CT = ", CT)
print("CF = ", CF)
print("R3 = ", R3)
print("R2 = ", R2)
print("R1 = ", R1)

VSHMAXATT = VIN[0]*CT/CF

print("V SH ATT MAX = ", VSHMAXATT)

dtatteso = -R1*CF*unumpy.log(Vmeno*CF/(VIN*CT))
print(dtatteso)

#trigger smith

R1 = ufloat(9.92, ((9.92*0.008)**2+0.03**2)**0.5)
R2 = ufloat(2.14, ((2.14*0.008)**2+0.03**2)**0.5)

print("R1 smit = ", R1)
print("R2 smit = ", R2)


VOH = ufloat(14.5, 0.2)
VOL = ufloat(14.0, 0.2)

print("Threshold inferiore = ", -VOH/(1+R1/R2))

print("Threshold superiore = ", VOL/(1+R1/R2))

#oscilatore

R = ufloat(3.87, ((3.87*0.008)**2+0.03**2)**0.5)*1000
C = ufloat(229, 0.04*229)*10**(-9)
T = 2*R*C*math.log(3)

print("R = ", R)
print("C = ", C)
print("T = ", T)

R1 = ufloat(9.78, ((9.78*0.008)**2+0.03**2)**0.5)
R2 = ufloat(9.80, ((9.80*0.008)**2+0.03**2)**0.5)
R3 = ufloat(0.961, ((0.961*0.008)**2+0.003**2)**0.5)


print("R1 = ", R1)
print("R2 = ", R2)
print("R3 = ", R3)
Vd = ufloat(6.9, 0.1)
V_th = Vd/(1+R1/R2)
print("Vth = ", V_th)

dV = ufloat(2.00, 0.04)
dt = ufloat(194, 4)*10**(-3)
print("slew rate = ", dV/dt)

