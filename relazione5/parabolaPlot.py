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

def linear(x, a, b):
	return a*(x-b)**2

INPUT = "/home/federico/Laboratorio3/relazione5/datiParabola.txt"

Vd, dVd, Vgs, dVgs = pylab.loadtxt(INPUT, unpack=True)

Vd, dVd, Vgs, dVgs = pylab.loadtxt(INPUT, unpack=True)

R_1 = ufloat(0.994*1000, 0.008*1000)
R_2 = ufloat(1.954*1000, 0.016*1000)
V_1 = ufloat(15.01, 0.08)
V_2 = ufloat(-15.11, 0.08)

#Nelle visualizzazioni devo introdurre gli errori

V_GS = unumpy.uarray(Vgs, dVgs)
V_D = unumpy.uarray(Vd, dVd)

I_D = V_D/R_1
I_D = 1000*I_D

pylab.rc('font',size=13)
pylab.title('I_D vs V_GS', fontsize = "16")
pylab.xlabel('V_GS (V)', size = "14")
pylab.ylabel('I_D (mA)', size = "14")
pylab.grid(color = "gray")
pylab.errorbar(unumpy.nominal_values(V_GS), unumpy.nominal_values(I_D), 
	unumpy.std_devs(I_D), unumpy.std_devs(V_GS), "o", color="black")


pylab.show()


