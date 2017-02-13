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

INPUT = "/home/federico/Laboratorio3/FranckHertz/data2.txt"

ua, ic = pylab.loadtxt(INPUT, unpack=True)

dic = numpy.array([0.0 for i in range(len(ic))])
dua = numpy.array([0.0 for i in range(len(ua))])

U_A = unumpy.uarray(ua, dua)
I_C = unumpy.uarray(ic, dic)

#FIXME You should convolve and smooth here!

pylab.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
pylab.rc('font',size=13)
#FIXME: Fix the title
pylab.title('$I_C$ vs $U_A$ at $U_E = 2,0$', fontsize = "16")
#How to determine the unity of measure
pylab.xlabel('$U_A$ (V)', size = "14")
#FIXME Unita' di misura
pylab.ylabel('$I_C$ (mA)', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(unumpy.nominal_values(U_A), unumpy.nominal_values(I_C), 
	unumpy.std_devs(I_C), unumpy.std_devs(U_A), "o", color="black")

#Per prendere il massimo locale dovrei eseguire una interpolazione con delle parabole, ma non ne ho troppa voglia.

pylab.savefig("plot.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None)

pylab.show()

