import uncertainties
from uncertainties import ufloat
import math
import numpy
import numpy
import pylab
from scipy.optimize import curve_fit
import math
import scipy.stats

def linear(x, a, b):
	return a*x+b


Vrb, dVrb, Vce, dVce, Vbe, dVbe = pylab.loadtxt('/home/federico/Laboratorio3/relazione3/dati1.txt', unpack=True)

Rb = 46700 
dRb = 400
Rl = 977
dRl = 8

V1 = 10.06
dV1 = 0.06

Ib = Vrb/Rb 
dIb = Ib*((dVrb/Vrb)**2 + (dRb/Rb)**2)**0.5

Ic = (V1 - Vce)/Rl
dIc = Ic*((dV1**2 + dVce**2)/((V1-dVce)**2) + (dRl/Rl)**2)**0.5



pylab.figure(1)
pylab.title('I_c vs I_b')
pylab.xlabel('I_b (uA)')
pylab.ylabel('I_c (mA)')
pylab.grid(color = "gray")
Ib = 1000000*Ib
Ic = 1000*Ic
dIb = 1000000*dIb
dIc = 1000*dIc
pylab.errorbar(Ib, Ic, dIc, dIb, "o", color="black")
Ib = Ib/1000000
Ic = Ic/1000
dIb = dIb/1000000
dIc = dIc/1000

pylab.figure(2)
pylab.title('I_c vs V_be')
pylab.xlabel('V_be (V)')
pylab.ylabel('I_c (mA)')
pylab.grid(color = "gray")
Ic = 1000*Ic
pylab.errorbar(Vbe, Ic, dIc, dVbe, "o", color="black")
Ic = Ic/1000

pylab.show()
