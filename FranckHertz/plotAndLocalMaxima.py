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
import numpy as np
from scipy.signal import argrelextrema

INPUT = "/home/federico/Laboratorio3/FrankHertz/data1.txt"

t, V = pylab.loadtxt(INPUT, unpack=True)

dt = numpy.array[0.0 for i in len(t)]
dV = numpy.array[0.0 for i in len(V)]

T = unumpy.urray(t, dt)
V = unumpy.uarray(V, dV)

#FIXME You should convolve and smooth here!

pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)
pylab.title('I_C vs U_A at U_E = ', fontsize = "16")
#How to determine the unity of measure
pylab.xlabel('U_A (V)', size = "14")
#FIXME UNità di misura
pylab.ylabel('I_C (mA)', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(unumpy.nominal_values(U_A), unumpy.nominal_values(I_C), 
	unumpy.std_devs(I_C), unumpy.std_devs(U_A), "o", color="black")


# for local maxima
posmax =argrelextrema(x, np.greater)
for i in len(posmax):
	print("Maximum number" & i & ": " & T[posmax[i]] & V[posmax[i]] & "\n")


# for local minima
posmin = argrelextrema(x, np.less)
for i in len(posmin):
	print("Minumum number" & i & ": " & T[posmin[i]] & V[posmin[i]] & "\n")

pylab.savefig("plot.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)

pylab.show()




