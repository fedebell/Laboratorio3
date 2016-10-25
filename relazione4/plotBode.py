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

INPUT = "/home/federico/Laboratorio3/relazione4/datiBode.txt"
OUTPUT = "/home/federico/Laboratorio3/relazione4/datiBode.txt"

Vout, dVout, f, df = pylab.loadtxt(INPUT, unpack=True)

#Nelle visualizzazioni devo introdurre gli errori

F = unumpy.uarray(f, df)
VOUT = unumpy.uarray(Vout, dVout)
VOUT3 = unumpy.uarray(Vout, (dVout**2 + (0.03*Vout)**2))
VIN = ufloat(1.02, 0.02) 
VIN3 = ufloat(1.02, ((0.02)**2+(0.03*1.02)**2)**0.5)
#Per la visualizzazione inserisco il 3%
A = VOUT3/VIN3
dB = 20*unumpy.log10(A)
logF = unumpy.log10(F)

pylab.title('A vs logf')
pylab.xlabel('I_b (uA)')
pylab.ylabel('I_c (mA)')
pylab.grid(color = "gray")

pylab.errorbar(unumpy.nominal_values(logF), unumpy.nominal_values(dB), 
	unumpy.std_devs(dB), unumpy.std_devs(logF), "o", color="black")

pylab.show()


