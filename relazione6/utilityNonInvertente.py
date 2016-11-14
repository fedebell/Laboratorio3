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

V_IN = ufloat(0.340, 0.002)
V_OUT = ufloat(13.00, 0.2)
A = 20.0*unumpy.log10(V_OUT/V_IN)
Amis = A-3.0
V_OUT_mis = V_IN*10**(Amis/20)
print(V_OUT_mis)

