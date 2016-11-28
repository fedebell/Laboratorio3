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

C1 = ufloat(9.90, 0.04*9.85)/10**9
C2 = ufloat(10.03, 0.04*10.19)/10**9
R2 = ufloat(9.81, ((0.008*9.81)**2+0.03**2)**0.5)*1000
R1 = ufloat(9.95, ((0.008*9.95)**2+0.03**2)**0.5)*1000

R3 = ufloat(9.82, ((0.008*9.82)**2+0.03**2)**0.5)*1000
R4 = ufloat(9.89, ((0.008*9.89)**2+0.03**2)**0.5)*1000
R5 = ufloat(9.88, ((0.008*9.88)**2+0.03**2)**0.5)*1000
POTmin = ufloat(0.3, ((0.008*0.3)**2+0.1**2)**0.5)
POTmax = ufloat(10.47, ((0.008*10.47)**2+0.03**2)**0.5)*1000

f1 = 1/(2*3.1415*C1*R1)
f2 = 1/(2*3.1415*C2*R2)
#Frequenze di taglio
print("C1 = ", C1)
print("C2 = ", C2)
print("R1 = ", R1)
print("R2 = ", R2)
print("R3 = ", R3)
print("R4 = ", R4)
print("R5 = ", R5)
print("POTmax = ", POTmax)
print("f1 =", f1)
print("f2 =", f2)
