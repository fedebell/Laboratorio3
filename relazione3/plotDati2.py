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

def linear(x, a, b):
	return a*x+b


Vl, Vce, dVl, dVce = pylab.loadtxt('/home/federico/Laboratorio3/relazione3/dati2.txt', unpack=True)


Rb = 46700 
dRb = 400
Rl = 977
dRl = 8

Ic = (Vl)/Rl
dIc = Ic*((dVl/Vl)**2+(dRl/Rl)**2)**0.5


pylab.figure(2)
pylab.title('I_c vs V_be')
pylab.xlabel('V_ce (V)')
pylab.ylabel('I_c (mA)')
pylab.grid(color = "gray")
Ic = 1000*Ic
dIc = 1000*dIc
pylab.errorbar(Vce, Ic, dIc, dVce, "o", color="black")
Ic = Ic/1000
dIc = dIc/1000

pylab.show()
