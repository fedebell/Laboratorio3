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

R_1 = ufloat(0.994*1000, 0.008*1000)
R_2 = ufloat(1.954*1000, 0.016*1000)
R_3 = ufloat(4.66*10**(6), 4.66*10**(6)*0.008) 
V_1 = ufloat(15.01, 0.08)
V_2 = ufloat(-15.11, 0.08)
K_P = ufloat( 1.3046e-03, 0.0003456**0.5*10**(-3))
V_P = ufloat(-3.3863, 0.00026868**0.5)
I_DSS = K_P*V_P**2
C = ufloat(99.3/10**9, 0.04*99.3/10**9)

print("R_1 = ", R_1)
print("R_2 = ", R_2)
print("R_3 = ", R_3)
print("C = ", C)

print("K_P = ", K_P)
print("V_P = ", V_P)
print("I_DSS = ", I_DSS)


#Dati a 1kHz
f = ufloat(1000, 10)
R_INatt = ((R_3)**2+(1/(2*3.1415*C*f))**2)**0.5
R_S = ufloat(5.20*10**6, ((0.01*5.20)**2 + 0.01**2)**0.5 * 10**6)
V_OUT1 = ufloat(1.43, 0.01)
V_OUT2 = ufloat(0.648, 0.004)
#V_OUT1 = ufloat(2.64, (0.02**2+(0.03*2.64)**2)**0.5)
#V_OUT2 = ufloat(1.16, (0.01**2+(0.03*1.16)**2)**0.5)
R_IN = R_S * 1/(V_OUT1/V_OUT2-1)
print("R_S = ", R_S)
print("V_OUT1 = ", V_OUT1)
print("V_OUT2 = ", V_OUT2)
print("R_INatt = ", R_INatt)
print("R_IN misurata = ", R_IN)

#Dati a 10 kHz
f = ufloat(10000, 10)
R_INatt = ((R_3)**2+(1/(2*3.1415*C*f))**2)**0.5
V_OUT1 = ufloat(1.43, 0.01)
V_OUT2 = ufloat(0.206, 0.002)
R_IN = R_S * 1/(V_OUT1/V_OUT2-1)
print("R_S = ", R_S)
print("V_OUT1 = ", V_OUT1)
print("V_OUT2 = ", V_OUT2)
print("R_INatt = ", R_INatt)
print("R_IN misurata = ", R_IN)

V_D = ufloat(4.49, ((0.005*4.49)**2+0.01**2)**0.5)
I_D = V_D/R_1*1000
I_DSS = ufloat(9.5, 0.2)
print("I_D - meta:", I_D)
V_GS = (0.972, 0.005*0.972)
V_GS_Att = (1-(I_D/I_DSS)**0.5)*V_P
print("V_GS_Attesa = ", V_GS_Att)
g_m = -2*(I_DSS/V_P)*(I_D/I_DSS)**0.5
g_m = g_m/1000
print("g_m = ", g_m)

R_part = ufloat(237, 0.008*237)
print("R_part = ", R_part)

A_V_att = - R_1*g_m/(1+R_part*g_m)
print("A_V_att = ", A_V_att)

A_V_att = R_part*g_m/(1+R_part*g_m)
print("A_V_att = ", A_V_att)






