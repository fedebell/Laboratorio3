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
K_P = ufloat( 1.40488015e-03, 7.12938032e-07**0.5)
V_P = ufloat(-3.36702552, 4.51107590e-03**0.5)
I_DSS = K_P*V_P**2
C = ufloat(99.3/10**6, 0.04*99.3/10**6)
f = ufloat(10000, 10)
R_INatt = ((R_3)**2+(1/(2*3.1415*C*f))**2)**0.5

print("K_P = ", K_P)
print("V_P = ", V_P)
print("I_DSS = ", I_DSS)
print("R_INatt = ", R_INatt)





