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

A1 = ufloat(770.35408428197263, 12.93)
A2 = ufloat(235.2198112656061, 1.158273259)


df = ufloat(0.63809213546403709, 0.006032255878)*1000
V0 = ufloat(79.964038454691433, 3.5171616346795327)
Rt = ufloat(23.103687379322871,  3.79566958464680182)
T = ufloat(28.0+217.15, 1)
A = A1*A2

k = (V0/1000)**2/(4*(Rt*1000)*(T)*(df)*(A**2))
print(k)
