from uncertainties import umath
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
import numpy as np
from scipy.signal import argrelextrema

deltas = ufloat(11.5, 0.5)*10
N = ufloat(85.0, 2.0)
hene = ufloat(632.8, 0.1)/1000

eta = 1/(N*hene/(2*deltas))

#Inserire qui la truffa
#eta = ufloat(5.3, 0.1)

print(eta)

#Inserire qui la truffa
ds = numpy.array([8.0, 8.0, 17.0, 23.0, 20.0])*10
dds = numpy.array([0.5, 0.5, 0.5, 0.5, 0.5])
N = numpy.array([50, 50, 100, 150, 150])
dN = numpy.array([0, 0, 0, 0, 0])

ds = unumpy.uarray(ds, dds)
N = unumpy.uarray(N, dN)

dX = ds/eta

l = (2*ds/(N*eta))*1000

print(l)
