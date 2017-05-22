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

A1 = ufloat(754.929577, 12.0331)
A2 = ufloat(234.61388927953405, 1.2427815)
df = ufloat(0.63809213546403709, 0.006032255878)*1000
cov_matrix = [[ 12.37042596,  12.33819617],
       [ 12.33819617,  14.4071076 ]]
(V0, Rt) = uncertainties.correlated_values([79.964038454691433, 23.103687379322871], cov_matrix)
T = ufloat(25.0+273.15, 2)
A = A1*A2
print(A)
print(T)
k = (V0/1000)**2/(4*(Rt*1000)*(T)*(df)*(A**2))
print(k)
