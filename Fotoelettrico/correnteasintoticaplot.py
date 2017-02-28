import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

l = numpy.array([602, 577, 546, 499, 449, 405])
dl = numpy.array([12, 11, 546*2/100, 11, 449*2/100, 11])
f = 1/l * 3*10**5
df = f*dl/l
I = numpy.array([1.759, 2.27, 2.11, 1.488, 2.30, 0.265])
dI = numpy.array([0.1, 0.1, 0.1, 0.05, 0.1, 0.01])/2
 
pylab.errorbar(f, I, dI, df, linestyle = "", color = "blue", marker = "o")
pylab.xlabel("f (THz)", size = 16)
pylab.ylabel("$I_A$ (nA)", size = 16)
pylab.title("Corrente anodica vs frequenza", size = 16)
pylab.grid()
pylab.show()